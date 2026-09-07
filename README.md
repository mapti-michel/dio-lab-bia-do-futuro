# FinanIA 🤖💰

Assistente virtual financeiro desenvolvido com **Inteligência Artificial**, com foco em **diagnóstico e organização financeira pessoal**.

## 🎯 Objetivo

A FinanIA foi desenvolvida para ajudar clientes a compreender sua situação financeira, identificar padrões de receitas e despesas, acompanhar metas e receber orientações educativas para melhorar sua organização financeira.

## 💡 Como funciona

A aplicação utiliza uma base de conhecimento composta por:

* Perfil do cliente;
* Histórico de transações;
* Histórico de atendimentos;
* Produtos financeiros disponíveis.

Esses dados são combinados com um **System Prompt** que define o comportamento, as regras de segurança e as limitações do agente.

A aplicação utiliza **Python, Pandas, Streamlit e Ollama** para disponibilizar a interação com o modelo de IA.

### Fluxo da aplicação

```text
Cliente
   ↓
Streamlit
   ↓
Python
   ↓
Contexto + System Prompt
   ↓
Ollama / gpt-oss
   ↓
Resposta da FinanIA
```

## 🔐 Segurança e confiabilidade

A FinanIA foi projetada com regras para:

* Não inventar dados financeiros;
* Reconhecer quando as informações são insuficientes;
* Não solicitar senhas, códigos ou credenciais bancárias;
* Não realizar transações financeiras;
* Não apresentar rentabilidade como garantia;
* Utilizar somente produtos existentes na base de conhecimento;
* Diferenciar dados reais do contexto de sugestões gerais.

## 📂 Estrutura do projeto

```text
FinanIA/
├── data/
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   └── produtos_financeiros.json
│
├── src/
│   └── app.py
│
├── 01 - documentacao-agente.md
├── 02 - base-conhecimento.md
├── 03 - prompt.md
├── 04 - metricas.md
├── 05 - pitch.md
└── README.md
```

## 🛠️ Tecnologias

* Python
* Pandas
* Streamlit
* Ollama
* gpt-oss
* JSON
* CSV

## 🚀 Execução

### Instalar dependências

```bash
pip install pandas requests streamlit
```

### Executar a aplicação

```bash
streamlit run src/app.py
```

### Ollama

Instale o [Ollama](https://ollama.com/) e, caso disponha de recursos computacionais adequados, baixe o modelo:

```bash
ollama pull gpt-oss
```

Teste:

```bash
ollama run gpt-oss "Olá!"
```

## 📊 Avaliação

A solução foi planejada para ser avaliada nos seguintes aspectos:

* **Assertividade:** responde de acordo com os dados disponíveis;
* **Segurança:** evita informações inventadas e solicitações indevidas;
* **Coerência:** mantém respostas compatíveis com o perfil e os objetivos do cliente.

Os testes funcionais e suas evidências estão documentados em `04 - metricas.md`.

## 📚 Documentação

| Arquivo                       | Conteúdo                                            |
| ----------------------------- | --------------------------------------------------- |
| `01 - documentacao-agente.md` | Problema, solução, persona, arquitetura e segurança |
| `02 - base-conhecimento.md`   | Dados e estratégia de integração                    |
| `03 - prompt.md`              | System Prompt, exemplos e regras do agente          |
| `04 - metricas.md`            | Avaliação, métricas e cenários de teste             |
| `05 - pitch.md`               | Roteiro de apresentação do projeto                  |

## ⚠️ Observação

A FinanIA utiliza dados fictícios para fins educacionais e de demonstração. A solução não substitui orientação financeira profissional e não executa operações financeiras.

---

**Projeto desenvolvido como parte do desafio de criação de um assistente virtual com Inteligência Artificial.**
