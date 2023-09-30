# 概要

MQTT ブローカーの EMQX とラズベリーパイを接続するためのソースコード
使用機器：ラズベリーパイ 4, ラズベリーパイ 3model B+

# 準備

```
$ python3 --version 
　Python 3.9.2
$ pip --version
　pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.9)
```

```
$ sudo apt-get install git-all
$ git clone https://github.com/eclipse/paho.mqtt.python 
$ cd paho.mqtt.python 
$ python3 setup.py install
$ pip install paho-mqtt
```

# 参考

https://qiita.com/taiyyytai/items/e63259542407758afd44
