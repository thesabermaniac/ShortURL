from django.db import models
import uuid


class ShortURL(models.Model):
    """
    This model stores an id which will be used as part of a short url to
    redirect a user to the longer url, also stored in this model.

    It also keeps track of the number of visits in the hit_count field
    """
    # We create our own pk here called id. This uses a uuid and unique=True to ensure that no 2 ShortURLs are identical
    id = models.SlugField(primary_key=True, max_length=100, unique=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=200)
    hit_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        """
        I've created a custom save method to shorten the uuid to 5 characters.
        I felt having a full UUID defeated the purpose of a short url.
        Additionally, I double check to make sure there are no other ShortURL
        objects with the same id, given the shorter size of the id
        """
        if self._state.adding:
            new_id = str(self.id)[:5]
            while ShortURL.objects.filter(id=new_id).exists():
                new_id = str(uuid.uuid4())[:5]
            self.id = new_id
        super(ShortURL, self).save(*args, **kwargs)

