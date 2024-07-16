#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

import falcon


class StaticTokenAuthMiddleware:
    def __init__(self, tokens: List[str]):
        self._tokens = set(tokens)

    def process_request(self, request, _):
        if request.method == 'OPTIONS':
            return

        if request.path == '/':
            return

        token = request.get_header('Authorization')
        if token is None or token.split(' ')[-1] not in self._tokens:
            raise falcon.HTTPUnauthorized
