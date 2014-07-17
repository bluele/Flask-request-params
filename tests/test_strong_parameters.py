#-*- coding:utf-8 -*-
from .base import TestCase
import json


class TestStrongParametersCase(TestCase):

    def test_require(self):
        response = self.client.post('/require/user', data={'user[name]': 'bluele'})
        data = json.loads(response.data.decode('utf8'))
        assert 'name' in data and data['name'] == 'bluele'

    def test_permit(self):
        response = self.client.post('/permit/user', data={
            'user[name]': 'bluele',
            'user[age]': 16,
            'user[unused]': 'unused'
        })
        data = json.loads(response.data.decode('utf8'))
        assert 'name' in data and 'age' in data
        assert 'unused' not in data
