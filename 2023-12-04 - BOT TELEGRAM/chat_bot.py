import requests

API_KEY = 'YOUT_API_KEY_HERE'

strURL = f'https://api.telegram.org/bot{API_KEY}'

reqURL = requests.get(url_req + '/getUpdates')

print(reqURL.status_code)

retorno = reqURL.json()
print(f'\n{retorno}')

id_chat = retorno['result'][0]['message']['chat']['id']

mensagem = input('Digite Algo: ')

dados = {'chat_id':id_chat, 'text':mensagem}

post = requests.post(url_req + '/sendMessage',data=dados)

