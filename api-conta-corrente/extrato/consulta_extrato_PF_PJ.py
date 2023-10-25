import requests
from requisicao_token import token

extrato = "06/2023"
numeroContaCorrente = "12345678"
client_id = "1234567a-1ab2-12ab-12a3-12abcd71234a"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': f'Bearer {token(client_id)}',
  'client_id': f'{client_id}'
}

response = requests.request("GET", f"https://api.sicoob.com.br/conta-corrente/extrato/{extrato}?numeroContaCorrente={numeroContaCorrente}", headers=headers, data=payload)
