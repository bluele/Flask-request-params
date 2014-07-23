#-*- coding:utf-8 -*-
from .base import TestCase
import json


class TestRequestCase(TestCase):

    def test_get_parameters(self):
        response = self.client.get('/?one=1&two=2')
        data = json.loads(response.data.decode('utf8'))
        assert 'one' in data and 'two' in data
        assert data['one'] == '1' and data['two'] == '2'

    def test_hash_parameters(self):
        response = self.client.post('/', data={'one': '1', 'two': '2'})
        data = json.loads(response.data.decode('utf8'))
        assert 'one' in data and 'two' in data
        assert data['one'] == '1' and data['two'] == '2'

    def test_json_parameters(self):
        response = self.client.post(
            '/',
            headers=[('Content-Type', 'application/json')],
            data=json.dumps({'one': '1', 'two': '2'})
        )
        data = json.loads(response.data.decode('utf8'))
        assert 'one' in data and 'two' in data
        assert data['one'] == '1' and data['two'] == '2'
