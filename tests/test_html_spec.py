#!/usr/bin/env python
# -*- coding:utf-8 -*-

from html_spec.html_spec import HtmlSpec
from html_spec.tag_exceptions import DoesNotHaveTagException

HTML = """
        <body>
        <p>
        <strong>Meu <a href=''>teste</a></strong>
        <span>outro marcador</span>
        </p>
        <h2>Nao</h2>
        </body>
"""

def test_make_xpath():
    html = "<body><p><strong>Meu teste</strong></p></body>"
    tag = "p"
    
    html_func = HtmlSpec(html)
    resp = html_func.make_xpath(tag)
    
    assert resp == ".//p"

def test_should_be_instance_html_functional():
    v = HtmlSpec(html='<teste />')
    assert isinstance(v, HtmlSpec) == True

def test_should_raise_exception_when_not_have_tag():
    html = '<body><h1>Titulo</h1></body>'
    html_func = HtmlSpec(html)
    try:
        html_func.has('h3')
        assert False
    except DoesNotHaveTagException, e:
        got = e.message
        expected = 'Html does not have tag h3'
        assert expected == got, "\nexpected: %s \ngot: %s" % (expected, got)

# Deve retornar uma nova instancia da classe HtmlSpec contendo como
# parent o xpath usado anteriormente para buscar a tag html
def test_should_be_return_new_instance_in_have_tag():
    html = "<body><p>testando</p></body>"
    html_func = HtmlSpec(html)
    resp = html_func.has('p')

    assert isinstance(resp, HtmlSpec) == True
    assert resp.node.text == "testando"

def test_should_be_return_new_instance_in_have_tag_with_find_child():
    html = "<body><p><strong>Meu teste</strong></p><strong>Nao</strong></body>"
    html_func = HtmlSpec(html)
    resp = html_func.has('p').has('strong')
		
    assert isinstance(resp, HtmlSpec) == True
    assert resp.node.text != "Nao"
    assert resp.node.text == "Meu teste"

def test_should_be_return_new_instance_in_have_tag_with_find_some_level():
    html_func = HtmlSpec(HTML)
    resp = html_func.with_tag('p').with_tag('h2')
    
    html_func.has('p').with_tag('strong').with_tag('span')
		
    assert isinstance(resp, HtmlSpec) == True
    assert True

def test_should_be_find_tag_with_attributes():
    html = """
        <body><div>Nao pode peguar esse</div><div id='test_id'><strong>test with attr</strong></div></body>
    """
    spec = HtmlSpec(html)
    resp = spec.has('div', id='test_id').has('strong')
    assert resp.node.text == 'test with attr'

def test_make_xpath_with_kwargs():
    spec = HtmlSpec(HTML)
    xpath = spec.make_xpath('div',id='tag_id')
    assert xpath == ".//div[@id='tag_id']"
