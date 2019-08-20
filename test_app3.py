#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

# fixtureを使った前後処理の挿入
# * fixture関数を作成(この例では、conftest.pyに記載)
# * → conftest.py参照

def test_1(g_sio_aaa):
    assert sio_aaa.getvalue() == "2345"

def test_2(g_sio_aaa):
    assert sio_aaa.getvalue() == "3456"
    
def test_3(g_client):
    client.say("test_3")
    assert True

@pytest.fixture()
def sample_fixture():
    print("before")
    yield
    print("after")

# @pytest.mark.usefixtures('fixture関数名')をクラスにデコレートすると
# クラス中の全メソッドにそのfixutre関数が適用される
# ただし、↓のようにconftest.pyに書いたfixture(グローバルfixture)はダメみたい
#@pytest.mark.usefixtures('g_client')
@pytest.mark.usefixtures('sample_fixture')
class TestSample(object):
    def test_sample_1(self):
        #client.say("test_sample_1")
        assert True
    def test_sample_2(self):
        #client.say("test_sample_2")
        assert True
