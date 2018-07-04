# coding=utf-8
# create by toonew at 2018/2/26
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
    username='xxx',
    password='yyy',
    version='2017-04-21')

conversation.set_http_config({'timeout': 100})
response = conversation.message(workspace_id=workspace_id, input={
    'text': 'What\'s the weather like?'})
print(json.dumps(response, indent=2))