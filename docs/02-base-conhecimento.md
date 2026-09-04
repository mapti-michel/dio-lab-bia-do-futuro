# Base de Conhecimento

## Dados Utilizados

A base de conhecimento utiliza arquivos fictícios para representar informações financeiras e de relacionamento de clientes de uma instituição financeira.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores entre o cliente e o banco |
| `perfil_investidor.json` | JSON | Identificar perfil, objetivos e preferências financeiras do cliente |
| `produtos_financeiros.json` | JSON | Consultar produtos e serviços financeiros disponíveis |
| `transacoes.csv` | CSV | Analisar receitas, despesas, categorias de gastos e padrões financeiros do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram adaptados e expandidos para representar um cenário de diagnóstico financeiro, utilizando informações fictícias e sem dados reais de clientes.

Foram incluídos diferentes tipos de transações, categorias de despesas, receitas, metas financeiras, informações de perfil e históricos de atendimento, permitindo que o agente realize análises relacionadas ao comportamento financeiro do cliente.

Os dados foram estruturados de forma que possam ser relacionados entre si por meio de um identificador de cliente, permitindo que o agente utilize diferentes fontes de informação durante o diagnóstico.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos CSV e JSON da pasta data são carregados pela aplicação e disponibilizados ao agente como contexto para análise.

Os dados são organizados por cliente, permitindo que o agente consulte as informações relevantes de acordo com a solicitação realizada.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

As informações relevantes são incorporadas dinamicamente ao contexto enviado ao modelo de linguagem.

O agente utiliza os dados de transações para analisar receitas, despesas e padrões de consumo; o perfil do cliente para compreender seus objetivos e preferências; o histórico de atendimento para contextualizar interações anteriores; e os produtos financeiros para consultar opções disponíveis.

O agente deve utilizar somente informações presentes na base de conhecimento para realizar afirmações específicas sobre o cliente e deve informar quando não houver dados suficientes para responder.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil de investidor: Moderado
- Renda mensal: R$ 5.500,00
- Meta financeira: Formar uma reserva de emergência de R$ 15.000,00

Resumo financeiro:
- Receitas no mês: R$ 5.500,00
- Despesas no mês: R$ 4.120,00
- Valor disponível: R$ 1.380,00

Principais categorias de despesas:
- Moradia: R$ 1.500,00
- Alimentação: R$ 850,00
- Transporte: R$ 420,00
- Lazer: R$ 380,00
- Assinaturas: R$ 170,00

Últimas transações:
- 01/09: Salário
- R$ 5.500,00
- 02/09: Aluguel
- R$ 1.200,00
- 03/09: Supermercado
- R$ 450,00
- 05/09: Transporte
- R$ 180,00
- 07/09: Streaming
- R$ 55,00

Histórico de atendimento:
- 15/08: Cliente solicitou orientação para organizar seu orçamento mensal.
- 22/08: Cliente informou interesse em formar uma reserva de emergência.

Produtos financeiros disponíveis:
- Conta poupança
- CDB
- Fundo de investimento
- Previdência privada
...
```
