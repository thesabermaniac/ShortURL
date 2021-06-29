from rest_framework.response import Response

from .models import ShortURL
from rest_framework import viewsets, status
from .serializers import ShortURLSerializer
from django.shortcuts import redirect
from django.urls import reverse


class URLViewSet(viewsets.ModelViewSet):
    """
    Uses a ModelViewSet to minimize code into one location
    """
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        """
        Custom retrieve method increments hit_count by 1 every time its called
        and redirects user to longer url
        """
        instance = self.get_object()
        instance.hit_count = instance.hit_count + 1
        instance.save()
        return redirect(instance.url)

    def create(self, request, *args, **kwargs):
        """
        Custom create method to return the total short url, as per the instructions
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            headers = self.get_success_headers(serializer.data)
            path = request.build_absolute_uri(reverse('short_url-list') + "/" + instance.id)
            return Response(path, status=status.HTTP_201_CREATED, headers=headers)

