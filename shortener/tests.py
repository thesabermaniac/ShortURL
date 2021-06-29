from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import ShortURL


class ShortURLTest(APITestCase):

    def test_create_url(self):
        """
        Tests creation of ShortURL object via post request
        """
        # build post request
        url = reverse('create_url-list')
        data = {'url': 'http://ravkavonline.co.il'}
        response = self.client.post(url, data, format='json')

        # assert 201 status code and ensure correct field data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ShortURL.objects.count(), 1)
        self.assertEqual(ShortURL.objects.get().url, 'http://ravkavonline.co.il')
        self.assertEqual(ShortURL.objects.get().hit_count, 0)

    def test_redirect(self):
        """
        Ensures ShortURL object redirects to proper url upon get request
        """
        # create ShortURL object
        short_url = ShortURL.objects.create(url='http://ravkavonline.co.il')

        # Build get request
        url = reverse('short_url-list') + "/" + short_url.id
        response = self.client.get(url)

        # verify proper redirect
        self.assertRedirects(response, "http://ravkavonline.co.il", status_code=302, target_status_code=200, fetch_redirect_response=False)

    def test_hit_count(self):
        """
        Ensure hit_count is incremented properly
        """
        # create ShortURL object
        short_url = ShortURL.objects.create(url='http://ravkavonline.co.il')

        # build url for get request
        url = reverse('short_url-list') + "/" + short_url.id

        # make get request 10 times, ensuring the hit_count is incremented each time
        for i in range(10):
            self.client.get(url)
            self.assertEqual(ShortURL.objects.get().hit_count, i+1)

    def test_non_existent_url(self):
        """
        Ensure get request with non-existent short_url properly notifies user
        """
        # create ShortURL object
        short_url = ShortURL.objects.create(url='http://ravkavonline.co.il')

        # create get url and add a "1" to form incorrect url
        url = reverse('short_url-list') + "/" + short_url.id + "1"
        response = self.client.get(url)

        # verify that we get a 404 status and return "Not found."
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"detail": "Not found."})

    def test_unique_IDs(self):
        """
        Ensure that 10,000 unique ShortURL objects can be made without conflicting id values
        """
        # create 10,000 ShortURL objects without throwing an error
        for i in range(10_000):
            ShortURL.objects.create(url="http://abc.com")
        # verify that there are 10,000 objects in the database
        self.assertEqual(ShortURL.objects.count(), 10_000)

    def test_invalid_url(self):
        """
        Ensure that an invalid url in a post request is flagged as such, and prevents the user from
        creating a ShortURL object
        """
        # create post request with invalid url
        url = reverse('create_url-list')
        data = {'url': 'ravkavonline'}
        response = self.client.post(url, data, format='json')

        # verify that we get a 400 error and that we return the proper reason
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"url": ["Enter a valid URL."]})

    def test_update(self):
        """
        Test patch request to ensure we can properly update a ShortURL object
        """
        # create ShortURL object
        short_url = ShortURL.objects.create(url='http://ravkavonline.co.il')

        # build patch request
        url = reverse('short_url-list') + '/' + short_url.id
        data = {'url': 'http://abc.com'}
        response = self.client.patch(url, data, format='json')

        # verify that the status code is 200 and the object has been updated
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ShortURL.objects.get().url, 'http://abc.com')
