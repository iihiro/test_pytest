#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

# fixtureを使ったオブジェクトの提供
#
# @pytest.fixture()でデコレートした関数を用意しておくと、
# test_*()関数の引数にその関数を渡すことができる

class Client(object):
    def __init__(self, str):
        self._msg = str
        
    def hello(self):
        return self._msg

@pytest.fixture()
def client():
    return Client("hoge")

def test_1(client):
    assert client.hello() == "hoge"

