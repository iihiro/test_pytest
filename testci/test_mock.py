#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

# モック
#
# monkypatch.setattr(対象クラス, 対象メソッド, モックメソッド)で
# 対象クラスの対象メソッドをモックメソッドに置き換えることが可能
#
# 参考: https://thinkami.hatenablog.com/entry/2017/03/07/065903

class Target(object):
    CONST_VAL = 'aaa'

    @classmethod
    def clsmethod(cls):
        return "original"
    
    def get(self):
        return self.CONST_VAL

    def get2(self, x):
        return self.CONST_VAL

def test_1(monkeypatch):
    expected = 'bbb'
    monkeypatch.setattr(Target, "get", lambda x: expected)
    t = Target()
    assert t.get() == expected
    
def test_2(monkeypatch):
    expected = 'bbb'
    def func(x, y):
        print(x)
        print(y)
        return expected
    monkeypatch.setattr(Target, "get2", func)
    t = Target()
    assert t.get2('hoge') == expected
    
def test_3(monkeypatch):
    expected = 'mock'
    monkeypatch.setattr(Target, "clsmethod", lambda x: expected)
    t = Target()
    assert t.clsmethod() == expected

@pytest.fixture()
def sample_fixture(monkeypatch):
    expected = 'mock'
    monkeypatch.setattr(Target, "clsmethod", lambda x: expected)
    yield

@pytest.mark.usefixtures('sample_fixture')
def test_4():
    expected = 'mock'
    t = Target()
    assert t.clsmethod() == expected


