#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RootResource:
    def on_get(self, _, response):
        response.media = {'hello': 'world'}
