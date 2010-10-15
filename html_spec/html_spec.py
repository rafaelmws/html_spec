#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from lxml.html import fromstring
from lxml.etree import tostring
from lxml.cssselect import CSSSelector
from tag_exceptions import DoesNotHaveTagException, FoundManyTagsException
from tag_exceptions import ExpectedTagsException, DifferentTextException

class HtmlSpec(object):
    html = None
    tree = None
    node = None

    def __init__(self, html, node=None):
        self.html = html
        self.tree = fromstring(str(html))
        self.node = node
        
        if(self.node == None):
            self.node = self.tree

    def __find__(self, tag_name):
        return self.tree.cssselect(tag_name)

    def has(self, tag_name, count=1):
        result = self.__find__(tag_name)

        if len(result) == 0:
            raise DoesNotHaveTagException('Html does not have tag %s' % tag_name)
        elif len(result) != count:
            raise ExpectedTagsException('Expected %s %s, founded %s' % (count ,tag_name ,len(result)))

        self.node = result[0]
        return HtmlSpec(tostring(self.node), node = self.node)
    
    def with_tag(self, tag_name):
        self.__find__(tag_name)

        if self.node != None:
            return HtmlSpec(self.html)
        else:
            raise DoesNotHaveTagException('Html does not have tag %s' % tag_name)
    
    def text(self, value):
    	text = self.node.text
    	if text != value:
    		raise DifferentTextException("Text different %s, %s" % (value, text))
    	
    	return self
    	
