from django.test import SimpleTestCase
from conversations.forms import CreateThought

class TestForms(SimpleTestCase):

    def thought_form_valid_data(self):
        form = CreateThought(data={
            'text': 'ABC123abc123',
        })

        self.assertTrue(form.is_valid())

    def thought_form_no_data(self):
        form = CreateThought(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)