#!/usr/bin/env python
# -*- coding:utf-8 -*-

class DoesNotHaveTagException(AssertionError):
    pass

class FoundManyTagsException(AssertionError):
    pass
