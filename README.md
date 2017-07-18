# やり方

## library install

virtualenv上で
pip install slackbot
pip install PyGithub

## ファイル追加

slackbot_settings.py を run.pyと同じ階層に用意
以下のようにつくる

API_TOKEN = 'hogehogehoge'
DEFAULT_REPLY = "repo#issue_id"
PLUGINS = ['plugins']
GITHUB_TOKEN = 'tokentokentoken'

## bot起動

python run.py

