#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Tuple


class StaticBasicAuthMiddleware:
    def __init__(self, auth_tuples: List[Tuple[str, str]]):
        raise NotImplementedError
