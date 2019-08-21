import pytest
import time
from io import StringIO

# テストの前後処理
#
# * conftest.pyを用意すると、pytestがテスト実行前に読んでくれる
# * fixture付きの関数を作成し、前後処理を記載(yield前が前処理、後が後処理)
# * scopeで前後処理が適用されるスコープを指定
#    - session .. プログラム全体を対象に前後処理を挟んでくれる
#    - module .. モジュール単位で..
#    - class .. クラス単位で..
#    - function .. 関数単位で..
# * autouseがTrueだと、暗黙的に指定したスコープで前後処理を挟んでくれる
# * yieldで任意型のオブジェクトをテストコードに渡せる
#    - test_app3.py では、test_1, test_2の引数に以下のfixture関数g_sio_aaaを
#      指定しているため、test_1, test_2は引数で以下のsioを受け取ることができる
#
# たとえば、このファイルがある状態で、
# `pytest test_app3.py` を実行すると、test_app3.py内のtest_1, test_2の
# それぞれの前後処理として、以下のyield前後の処理が実行される

@pytest.fixture(scope="module", autouse=True)
def g_sio_aaa():
    sio = StringIO("12345")
    time.sleep(1)
    print("created!")
    yield sio
    time.sleep(1)
    sio.close()
    print("closed!")


# scope, autouseを省略する例

class Client(object):
    def say(self, str):
        print(str)

@pytest.fixture()
def g_client():
    client = Client()
    client.say("before")

    yield client

    client.say("after")

    
