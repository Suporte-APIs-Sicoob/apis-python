import requests
from requisicao_token import token

client_id = '9b5e603e428cc477a2841e2683c92d21'
dt_inicio = '2023-04-01T00:00:00Z'
dt_fim = '2020-04-01T17:00:00Z'
cpf = 'string'
cnpj = 'string'
locationPresent = 'true'
status = 'string'


# url_cpf = f"https://api.sicoob.com.br/pix/api/v2/cob?inicio={dt_inicio}&fim={dt_fim}&cpf={cpf}&locationPresent=true&status={status}&paginacao.paginaAtual=0&paginacao.itensPorPagina=100"
url_cnpj = f"https://api.sicoob.com.br/pix/api/v2/cob?inicio={dt_inicio}&fim={dt_fim}&&cnpj={cnpj}&locationPresent=true&status={status}&paginacao.paginaAtual=0&paginacao.itensPorPagina=100"

payload = {}
headers = {
  'Authorization': f'Bearer {token(client_id)}',
  'client_id': f'{client_id}',
  'Accept': 'application/json',
}

response = requests.request("GET", url_cnpj, headers=headers, data=payload)
# response = requests.request("GET", url_cpf, headers=headers, data=payload)
