# API de Cobrança Bancária

A API de Cobrança Bancária é uma poderosa ferramenta que permite às empresas gerenciar eficazmente o processo de cobrança de boletos bancários, autorizado pelo fluxo de Client Credentials. Com esta API, você pode gerenciar sua carteira de boletos, garantindo um controle completo desde a inclusão de novos boletos até a liquidação ou baixa dos títulos, além de diversas outras funcionalidades essenciais. 

## Visão Geral

A API de Cobrança Bancária é a evolução da API de Cobrança Bancária, projetada para atender às necessidades das empresas na gestão de pagamentos de produtos e serviços. Ela facilita o recebimento de valores através de boletos bancários, oferecendo uma solução eficaz para acompanhar todo o processo de cobrança.

Aqui estão algumas das funcionalidades oferecidas pela API:

## Funcionalidades

1. **Gerenciamento de Boletos**: A inclusão, consulta e controle de boletos é simples e eficiente, permitindo uma gestão completa da sua carteira de títulos.

2. **Alteração de Informações de Pagadores de Boletos**: Você pode atualizar informações de pagadores de boletos, garantindo que os dados estejam sempre corretos.

3. **Negativação de Pagadores**: Indique a negativação de pagadores de boletos não pagos para recuperar seus valores de maneira eficaz.

4. **Protesto de Boletos**: Registre títulos vencidos e não pagos para protesto, protegendo seus direitos financeiros.

5. **Movimentação**: Realize movimentações na sua carteira de cobrança registrada para otimizar o processo de recebimento de pagamentos.

## Especificação da API

Para obter informações técnicas detalhadas e exemplos de uso, acesse a [documentação técnica](https://documenter.getpostman.com/view/20565799/Uzs6yNhe#1bcf3134-afbd-4cf3-ba49-9cdf5ea2c224).

## Lista de Escopos da API

A API de Cobrança Bancária V2 oferece uma variedade de escopos para atender às necessidades específicas do seu negócio. Alguns dos principais escopos incluem:

- **cobranca_boletos_consultar**: Consulta de um boleto bancário.
- **cobranca_boletos_incluir**: Inclusão de boletos informados.
- **cobranca_boletos_pagador**: Listagem de boletos por pagador.
- **cobranca_boletos_segunda_via**: Emissão da segunda via de boleto já registrado.
- **cobranca_boletos_descontos**: Alteração de informações de valor e/ou data de validade do desconto e/ou tipo de desconto de boletos informados.
- **cobranca_boletos_abatimentos**: Alteração do valor de abatimento de boletos informados.
- **cobranca_boletos_valor_nominal**: Alteração do valor nominal de boletos informados.
- **cobranca_boletos_seu_numero**: Alteração do seu número e/ou número de controle da empresa dos boletos informados.
- **cobranca_boletos_especie_documento**: Alteração da informação da espécie de documento dos boletos informados.
- **cobranca_boletos_baixa**: Comando para baixa de boletos informados.
- **cobranca_boletos_rateio_credito**: Comando para rateio de crédito de boletos informados.
- **cobranca_pagadores**: Alteração de informações de pagadores vinculados aos boletos informados.
- **cobranca_boletos_negativacoes_incluir**: Indicação de negativação de pagadores de boletos informados.
- **cobranca_boletos_negativacoes_alterar**: Cancelamento do apontamento da negativação de pagadores de boletos informados.
- **cobranca_boletos_negativacoes_baixar**: Comando para baixa da negativação de pagadores de boletos informados.
- **cobranca_boletos_protestos_incluir**: Registro da indicação a protesto de boletos informados.
- **cobranca_boletos_protestos_alterar**: Indicação de cancelamento de protesto de boletos informados.
- **cobranca_boletos_protestos_desistir**: Pedido de desistência do protesto de boletos informados.
- **cobranca_boletos_solicitacao_movimentacao_incluir**: Solicitação da movimentação da carteira de cobrança registrada para beneficiário informado.
- **cobranca_boletos_solicitacao_movimentacao_consultar**: Consulta da situação da solicitação da movimentação.
- **cobranca_boletos_solicitacao_movimentacao_download**: Obtenção de um arquivo de movimentação.
- **cobranca_boletos_prorrogacoes_data_vencimento**: Prorrogação da data de vencimento de boletos informados.
- **cobranca_boletos_prorrogacoes_data_limite_pagamento**: Prorrogação da data limite de pagamento de boletos informados.
- **cobranca_boletos_encargos_multas**: Alteração do valor de multa de boletos informados.
- **cobranca_boletos_encargos_juros_mora**: Alteração do valor de juros de mora de boletos informados.
- **cobranca_boletos_pix**: Alteração de boletos para utilização de PIX.
- **cobranca_boletos_faixa_nn_disponiveis**: Consulta de dados de faixas de nosso número disponíveis.

A API de Cobrança Bancária oferece uma gama de recursos para otimizar o processo de cobrança de boletos e facilitar a gestão financeira da sua empresa. Se você tem alguma dúvida ou precisa de assistência, consulte a documentação técnica ou entre em contato conosco para obter suporte.

---

*Observação: Certifique-se de revisar a documentação técnica para obter informações detalhadas sobre os endpoints, autenticação e exemplos de uso da API.*