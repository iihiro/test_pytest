#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

# 複数のテストを指定
#
# * @pytest.mark.parametrize()デコレータを使う
# * "x, y"がテスト関数の引数に対応
# * [("aaa", "bbb"), ...]がテストパラメータに対応

@pytest.mark.parametrize(
    "x, y", [
        ("aaa", "bbb"),
        ("aaa", "aaa"),
        ("bbb", "bbb")
    ]
)
def test_1(x, y):
    assert x == y

