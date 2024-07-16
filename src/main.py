#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon
import yaml

from resources.root import RootResource

# from auth.basic import StaticBasicAuthMiddleware
# from auth.token import StaticTokenAuthMiddleware

with open('../config.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

app = falcon.App(
    middleware=[],
    cors_enable=True,
)

app.add_route('/', RootResource())
