import requests
import json
from requisicao_token import token

client_id = '9b5e603e428cc477a2841e2683c92d21'
url = "https://api.sicoob.com.br/pix/api/v2/cob"

payload = json.dumps({
  "calendario": {
    "expiracao": 3600
  },
  "devedor": {
    "cnpj": "12345678000195",
    "nome": "Empresa de Serviços SA"
  },
  "valor": {
    "original": "37.00",
    "modalidadeAlteracao": 1
  },
  "chave": "7d9f0335-8dcc-4054-9bf9-0dbd61d36906",
  "solicitacaoPagador": "Serviço realizado.",
  "infoAdicionais": [
    {
      "nome": "Campo 1",
      "valor": "Informação Adicional1 do PSP-Recebedor"
    },
    {
      "nome": "Campo 2",
      "valor": "Informação Adicional2 do PSP-Recebedor"
    }
  ]
})
headers = {
  'Authorization': f'Bearer {token(client_id)}',
  'client_id': f'{client_id}',
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)
