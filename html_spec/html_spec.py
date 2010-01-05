#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from lxml import etree
from tag_exceptions import DoesNotHaveTagException

class HtmlSpec(object):
    html = None
    tree = None
    node = None

    def __init__(self, html, node=None):
        self.html = html
        self.tree = etree.fromstring(str(html))
        self.node = node
        
        if(self.node == None):
            self.node = self.tree

    def __find__(self, tag_name, **kwargs):
        xpath = self.make_xpath(tag_name, **kwargs)
        return self.tree.find(xpath)

    def has(self, tag_name, **kwargs):
        self.node = self.__find__(tag_name, **kwargs)
        
        if self.node != None:
            return HtmlSpec(etree.tostring(self.node),
                                    node = self.node)
        else:
            raise DoesNotHaveTagException('Html does not have tag %s' % tag_name)
    
    def with_tag(self, tag_name):
        self.__find__(tag_name)

        if self.node != None:
            return HtmlSpec(self.html)
        else:
            raise DoesNotHaveTagException('Html does not have tag %s' % tag_name)

    def make_xpath(self, tag, **kwargs):
        if kwargs == {}:
            return ".//%s" % tag
        else:
            attrs = ""
            for key in kwargs.keys():
                attr = "@%s='%s'," % (key, kwargs[key])
                attrs = "%s%s" % (attrs, attr)
        
            return ".//%s[%s]" % (tag, attrs[:-1])
