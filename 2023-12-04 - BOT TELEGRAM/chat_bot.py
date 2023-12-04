import requests

API_KEY = 'YOUR_API_TOKEN_HERE'

strURL = f'https://api.telegram.org/bot{API_KEY}'

reqURL = requests.get(strURL + '/getUpdates')

print(reqURL.status_code)

retorno = reqURL.json()
print(f'\n{retorno}')

id_chat = retorno['result'][0]['message']['chat']['id']

mensagem = input('Digite Algo: ')

dados = {'chat_id':id_chat, 'text':mensagem}

post = requests.post(strURL + '/sendMessage',data=dados)

