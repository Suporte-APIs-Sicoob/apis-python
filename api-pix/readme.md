# API Pix

## Visão Geral

A API Pix é uma ferramenta poderosa que permite aos usuários recebedores automatizar os serviços de pagamento com o Sicoob, facilitando a recepção e gestão de transações Pix. No contexto do arranjo Pix, os usuários recebedores podem gerar cobranças, verificar Pix recebidos, processar devoluções e realizar conciliações. É importante ressaltar que a API Pix está em conformidade com as normas do Banco Central do Brasil (Bacen), seguindo fielmente as orientações estabelecidas pela entidade reguladora.

## Funcionalidades

A API Pix oferece várias funcionalidades que tornam a gestão de pagamentos Pix mais eficiente e prática. As principais funcionalidades incluem:

1. **Gerenciamento de Cobranças com Pagamento Imediato (Cob)**
   - Permite a criação, alteração e consulta de cobranças imediatas.

2. **Gerenciamento de Pix Recebidos (Pix)**
   - Facilita a consulta e gerenciamento de transações Pix recebidas.

3. **Gerenciamento de Cobranças para Pagamento com Vencimento (CobV)**
   - Permite a criação, alteração e consulta de cobranças com data de vencimento.

4. **Gerenciamento de Lote de Cobranças para Pagamento com Vencimento (LoteCobV)**
   - Facilita a gestão de lotes de cobranças com data de vencimento, simplificando o processo.

5. **Gerenciamento de Notificações (Webhook)**
   - Permite a consulta e configuração de webhooks para receber notificações de eventos relacionados a transações Pix.

## Especificação da API

Para obter detalhes técnicos e informações específicas sobre como utilizar a API Pix, acesse a documentação completa em [https://documenter.getpostman.com/view/20565799/2s93kz5QVE](https://documenter.getpostman.com/view/20565799/2s93kz5QVE).

## Lista de Escopos da API

A API Pix utiliza escopos para definir permissões de acesso às diferentes funcionalidades. A seguir, estão os escopos disponíveis:

- `cob.write`: Permissão para alteração de cobranças imediatas.
- `cob.read`: Permissão para consulta de cobranças imediatas.
- `cobv.write`: Permissão para alteração de cobranças com vencimento.
- `cobv.read`: Permissão para consulta de cobranças com vencimento.
- `lotecobv.write`: Permissão para alteração de lotes de cobranças com vencimento.
- `lotecobv.read`: Permissão para consulta de lotes de cobranças com vencimento.
- `pix.write`: Permissão para alteração de transações Pix.
- `pix.read`: Permissão para consulta de transações Pix.
- `webhook.read`: Permissão para consulta de webhooks.
- `webhook.write`: Permissão para alteração de configurações de webhooks.
- `payloadlocation.write`: Permissão para alteração de informações de payloads.
- `payloadlocation.read`: Permissão para consulta de informações de payloads.

## Exemplos de Uso

Aqui estão alguns exemplos de casos de uso com a API Pix:

- Para criar uma cobrança imediata, você pode usar o escopo `cob.write`.
- Para consultar as transações Pix recebidas, utilize o escopo `pix.read`.
- Para configurar um webhook que notificará sobre novas transações, use o escopo `webhook.write`.

A API Pix oferece uma gama de recursos para atender às suas necessidades de gerenciamento de pagamentos Pix de forma eficaz e segura.


**Atenção**: Certifique-se de seguir as diretrizes do Banco Central do Brasil ao utilizar a API Pix para garantir a segurança e conformidade de suas operações financeiras.