import requests
from requisicao_token import token

client_id = '9b5e603e428cc477a2841e2683c92d21'
txid = 'digite_o_txid_aqui'

url = f"https://api.sicoob.com.br/pix/api/v2/cob/{txid}?revisao=integer"

payload = {}
headers = {
  'Authorization': f'Bearer {token(client_id)}',
  'client_id': f'{client_id}',
  'Accept': 'application/json',
}

response = requests.request("GET", url, headers=headers, data=payload)
