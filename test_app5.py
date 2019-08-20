#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import time

# テストにマークをつける
#
# * @pytest.mark.xxxx でマークをつける(xxxxは任意)
# * xxxx は `pytest.ini` ファイルを作って登録しておく(やらないとPytestUnknownMarkWarningが出る)
#   ```
#    [pytest]
#    markers =
#      small
#      large
#   ```
# * `pytest -m xxxx test_app5.py` で任意のマークだけ実行可能
# * `-m`を付けないと通常通り、全テストが実行される
#
# 特殊マーク
# * @pytest.mark.skip をつけるとそのテストはスキップされる

@pytest.mark.small
def test_1():
    time.sleep(0.1)
    assert "aaa" == "bbb"

@pytest.mark.small
def test_2():
    time.sleep(0.1)
    assert "bbb" == "bbb"

@pytest.mark.large
def test_3():
    time.sleep(5)
    assert "aaa" == "bbb"

