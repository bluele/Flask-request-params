#-*- coding:utf-8 -*-
from .base import TestCase
import json


class TestRequestCase(TestCase):

    def test_get_parameters(self):
        response = self.client.get('/?one=1')
        data = json.loads(response.data.decode('utf8'))
        raise Exception(data)
        assert 'one' in data
        assert data['one'] == '1'

    def test_hash_parameters(self):
        response = self.client.post('/', data={'one': '1'})
        data = json.loads(response.data.decode('utf8'))
        assert 'one' in data
        assert data['one'] == '1'
