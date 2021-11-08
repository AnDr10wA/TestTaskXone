from django.test import TestCase
from .models import Link
from .form import LinkForm
from django.contrib.auth.models import User
from django.test import Client


class LinkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        link = Link.objects.create(input_link='https://ru.tradingview.com/chart/wILTczrN/',
                                   output_link='b2r4ed4',
                                   user=None)

    def test_link(self):
        link = Link.objects.first()
        self.assertEqual(link.output_link, 'b2r4ed4')
        self.assertEqual(link.input_link,'https://ru.tradingview.com/chart/wILTczrN/' )

    def test_links_max_length(self):
        link = Link.objects.first()
        max_length = link._meta.get_field('input_link').max_length
        self.assertEqual(max_length, 255)


class LinkFormTest(TestCase):

    def test_link_input(self):
        form_data = {'input_link': 'https://www.youtube.com/'}
        form = LinkForm(form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('input_link'), 'https://www.youtube.com/')


class ShorterViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        link = Link.objects.create(input_link='https://ru.tradingview.com/chart/wILTczrN/',
                                   output_link='b2r4ed4',
                                   user=user)

    def test_dedirect_if_not_logged_in(self):
        resp = self.client.get('/links')
        self.assertEqual(resp.status_code, 302)


    def test_user_login(self):
        c = Client()
        logged_in = c.login(username = 'testuser', password = '12345')
        resp = c.get('/links')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(str(resp.context['user']), 'testuser')






