from zabbix_utils import Getter

agent = Getter(host='127.0.0.1', port=22222)
resp = agent.get('''
{
  "request": "passive checks",
  "data": [
    {
      "key": "system.uname;agent.version",
      "timeout": 3
    }
  ]
}
                 ''')

print(resp.value)