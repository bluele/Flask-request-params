#-*- coding:utf-8 -*-
from __future__ import with_statement
from functools import reduce

from flask import request


class Params(dict):

    def __init__(self, base_params=None, is_parse=True):
        self._params = base_params or {}
        if is_parse:
            self.__assign_get_args(request.args)
            if request.view_args is not None:
                self.__assign_args(request.view_args)
            if request.json:
                self.__assign_args(request.json)
            else:
                if request.files:
                    self.__assign_args(request.files)
                self.__assign_body(request.form.items(multi=True))

    def __assign_args(self, args):
        self._params.update(args)

    def __assign_get_args(self, args):
        for k, v in args._iter_hashitems():
            if isinstance(v, list) and len(v) == 1:
                self._params[k] = v[0]
            else:
                self._params[k] = v

    def __assign_body(self, items):
        queries = []
        for k, v in items:
            keys = self._parse_keys(k)
            queries.append(reduce(lambda res, key: {key: res} if key != '' else [res], reversed(keys), v))
        [self.__assign_params(params) for params in queries]

    @classmethod
    def _parse_keys(cls, keys):
        if '[' in keys or ']' in keys:
            return keys.replace(']', '').split('[')
        else:
            return [keys]

    def __assign_params(self, other):
        def deep_merge(a, b):
            for k, v in b.items():
                if isinstance(v, dict) and k in a:
                    deep_merge(a[k], v)
                elif isinstance(v, list) and k in a and isinstance(a[k], list):
                    a[k].extend(v)
                else:
                    a[k] = v
        deep_merge(self._params, other)

    def require(self, key):
        if key not in self._params:
            raise ValueError(key)
        return Params(self._params[key], is_parse=False)

    def permit(self, *args):
        params = dict()
        for k in args:
            if k in self._params:
                params[k] = self._params[k]
        return Params(params, is_parse=False)

    def __getattr__(self, item):
        return getattr(self._params, item)

    def __getitem__(self, item):
        return self._params[item]

    def __setitem__(self, k, v):
        raise NotImplementedError

    def __len__(self):
        return len(self._params)

    def __iter__(self):
        return self._params.__iter__()

    def keys(self):
        return self._params.keys()

    def values(self):
        return self._params.values()

    def items(self):
        return self._params.items()

    def iterkeys(self):
        return self._params.iterkeys()

    def itervalues(self):
        return self._params.itervalues()

    def iteritems(self):
        return self._params.iteritems()


def get_request_params(base_params=None):
    if not hasattr(request, '_request_params'):
        setattr(request, '_request_params', Params(base_params))
    return getattr(request, '_request_params')


def bind_request_params(attr_name='params'):
    setattr(request, attr_name, get_request_params())
