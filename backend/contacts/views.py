from rest_framework import viewsets
from .models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
