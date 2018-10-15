# coding: utf-8

from django.test import Client, TestCase
from django.urls import reverse

from tests.urls import test_url_list

import statsy


class TestWatch(TestCase):
    def setUp(self):
        self.client = Client()
        self.statsy = statsy.Statsy(cache=False)

    def test_views(self):
        for url in test_url_list:
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, 200)

        self.assertEqual(len(test_url_list), self.statsy.objects.count())
