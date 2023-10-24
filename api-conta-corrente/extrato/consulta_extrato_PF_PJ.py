import requests
from Python.api_conta_corrente.requisicao_token import token

extrato = "06/2022"
numeroContaCorrente = "123456"
client_id = "68d0d27a-3ffa-41bf-93a5-25cbff71500f"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': f'Bearer {token(client_id)}',
  'client_id': f'{client_id}'
}

response = requests.request("GET", f"https://api.sicoob.com.br/conta-corrente/extrato/{extrato}?numeroContaCorrente={numeroContaCorrente}", headers=headers, data=payload)

print(response.text)


