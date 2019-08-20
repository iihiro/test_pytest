#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

# pytestがテスト対象とするルール
# * ファイル名 test_* 
# * 関数名 test_*()
#
# ※クラスのメンバメソッドもtest_*()なら対象となる
#
# ファイルを指定して実行
# * pytest test_app.py
#
# 全テストを実行 (カレントディレクトリのtest_*.pyがすべて実行される)
# * pytest
#
# 処理時間計測 (durationsで処理時間のかかる関数の上位N個を表示)
# * pytest --durations=0 -vv test_app.py
#
# 参考: https://qiita.com/everylittle/items/1a2748e443d8282c94b2

# 判定方法
# * アサート
#   * assert "aaa" == "bbb"
# * 例外
#   * with pytest.raises(例外)
#   * → test_assert_1()参照


def test_1():
    a = 1
    b = 2
    assert a == b

def test_2():
    a = 1
    b = 2
    assert a != b

def test_assert_1():
    def _target():
        raise ValueError
    with pytest.raises(ValueError):
        _target()
