# APIs Disponíveis em Python

Este repositório contém várias APIs úteis para tarefas bancárias e financeiras. As APIs foram desenvolvidas em Python e podem ser utilizadas para facilitar diversas operações, como pagamentos PIX, cobranças bancárias, consultas de conta corrente e poupança.

## APIs Disponíveis

1. **API PIX**

   A API PIX permite que você integre o sistema de pagamento instantâneo brasileiro em suas aplicações. Com esta API, você pode criar e gerenciar pagamentos PIX, consultar transações e muito mais.

2. **API de Cobrança Bancária**

   A API de Cobrança Bancária simplifica o processo de criação e gerenciamento de boletos e cobranças bancárias. Com ela, você pode gerar boletos, verificar o status de cobranças e automatizar tarefas de cobrança.

3. **API de Conta Corrente**

   A API de Conta Corrente permite acessar informações sobre contas correntes em instituições financeiras. Você pode consultar o saldo, extrato, histórico de transações e muito mais.

4. **API Poupança**

   Com a API de Poupança, você pode acessar informações sobre contas poupança, incluindo saldos, rendimentos, depósitos e retiradas.

## Como Usar

Cada API possui sua própria documentação e exemplos de uso. Certifique-se de consultar a documentação específica de cada API para obter informações detalhadas sobre como começar a utilizá-las.

## Exemplos

Nesta seção, serão fornecidos alguns exemplos básicos de como usar cada API:

### Exemplo de Uso da API PIX

```python
# Importe as bibliotecas
import json
from requests_pkcs12 import post

data = {
    'grant_type': 'client_credentials',
    'client_id': f'{client_id}',
    'scope': 'openid cco_extrato cco_saldo'
}

# Caminho para o arquivo de certificado PFX
cert_path = 'caminho_onde_ta_certificado'

cert_password = 'senhadocertificado'

# URL da API para obter o token
token_url = 'https://auth.sicoob.com.br/auth/realms/cooperado/protocol/openid-connect/token'

response = post(token_url, data=data, pkcs12_filename=cert_path, pkcs12_password=cert_password)

token = json.loads(response.text)['access_token']

print(token)
```

Lembre-se de substituir `'client_id'`, `'caminho_onde_ta_certificado'`, `'senhadocertificado'` e outras informações relevantes pelos valores apropriados em seus casos de uso.

## Contribuição

Se você deseja contribuir para este projeto ou relatar problemas, sinta-se à vontade para abrir um problema ou enviar uma solicitação pull. Sua contribuição é bem-vinda!

---

Esperamos que estas APIs em Python sejam úteis para suas necessidades bancárias e financeiras. Se você tiver alguma dúvida ou precisar de suporte adicional, não hesite em entrar em contato conosco.
Atravês do WhatsApp. Basta escrever o termo **#API** e enviar para o número **61 4000-1111**. O time de suporte estará disponível para atendê-lo das **09h** às **18:30** durante os dias úteis.
