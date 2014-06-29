#-*- coding:utf-8 -*-
from .base import TestCase
import json


class TestPostParameters(TestCase):

    def test_hash_parameters(self):
        response = self.client.post('/', data={'one': '1'})
        data = json.loads(response.data.decode('utf8'))
        assert 'one' in data
        assert data['one'] == '1'
