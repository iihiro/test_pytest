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

    def get(self):
        return self.CONST_VAL

def test_1(monkeypatch):
    expected = 'bbb'
    monkeypatch.setattr(Target, "get", lambda x: expected)
    t = Target()
    assert t.get() == expected


