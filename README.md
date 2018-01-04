# kirara-slack

まんがタイムきらら系列誌の発売日を Slack に通知します。きらら以外の月刊誌での使えるはずです。

`python 3.5.4`

## 導入方法

```
$ git clone --recursive https://github.com/joisino/kirara-slack.git
$ pip install -r requirements.txt
```

`pip` が python2 用のものを参照している場合は、適宜 `pip3` 等を利用してください。

## 使い方

`config.py` に slack の Webhook URL を記入してください。これは、 https://slack.com/services/new/incoming-webhook 等から得ることができます。

また、お好みで `config.py` 内の通知する雑誌、通知するメッセージ内容を設定してください。

発売日に `notify.py` を実行すると、Slack に通知が飛びます。

例えば crobtab に以下のように設定すると、発売日の朝 9 時 5 分頃に通知されます。

```
5 9 * * * /path/to/kirara-slack/notify.py
```
