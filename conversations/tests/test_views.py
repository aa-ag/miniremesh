from django.test import TestCase, Client
from django.urls import reverse
from conversations.models import Thought, Conversation

class TestViews(TestCase):

    def test_project_list_GET(self):
        client = Client()

        response = client.get(reverse('addconversation'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'conversations/addconversation.html')
