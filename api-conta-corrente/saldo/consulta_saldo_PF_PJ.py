import requests
from requisicao_token import token

client_id = "1234567a-1ab2-12ab-12a3-12abcd71234a"
numeroContaCorrente = "123456"

payload = {}
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {token(client_id)}',
    'client_id': f'{client_id}'
}

response = requests.request("GET", f"https://api.sicoob.com.br/conta-corrente/saldo?numeroContaCorrente={numeroContaCorrente}", headers=headers, data=payload)
