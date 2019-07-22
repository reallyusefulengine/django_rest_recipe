from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'test@test.com',
            password = 'test1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@LONDONAPPDEV.COM',
            password = 'testpass123',
            name = 'Mr Blobby'
        )

    def test_users_listed(self):
        """tests that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        print(f'Response is: {res}')
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
