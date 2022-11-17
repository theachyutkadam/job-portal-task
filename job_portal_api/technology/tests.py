from django.test import TestCase
from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
client = APIClient()
client.login(username='admin', password='12345678')

factory = APIRequestFactory()
request = factory.post('/technology/', {'name': 'new idea', 'description': 'this is the testing line', 'is_active': True}, format='json')


client.logout()
