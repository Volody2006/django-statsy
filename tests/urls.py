# coding: utf-8
from django.urls import path

from tests.views import ViewFabric


def get_test_urlpatterns():
    url_list, urlpatterns = [], []
    for idx, (view, _) in enumerate(ViewFabric()):
        url_part = 'test_view_{0}'.format(idx)
        url_name = url_part.strip('^')

        urlpatterns.append(path(url_part, view, name=url_name))

        url_list.append(url_name)

    return urlpatterns, url_list


urlpatterns, test_url_list = get_test_urlpatterns()
