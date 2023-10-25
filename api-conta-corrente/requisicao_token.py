import json
from requests_pkcs12 import post


def token(client_id):
    data = {
        'grant_type': 'client_credentials',
        'client_id': f'{client_id}',
        'scope': 'cco_extrato cco_saldo'
    }

    cert_path = 'caminho_do_certificao'
    cert_password = 'senha_do_certificado'

    token_url = 'https://auth.sicoob.com.br/auth/realms/cooperado/protocol/openid-connect/token'

    response = post(token_url, data=data, pkcs12_filename=cert_path, pkcs12_password=cert_password)

    return json.loads(response.text)['access_token']