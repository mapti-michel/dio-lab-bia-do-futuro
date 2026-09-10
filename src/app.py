import json
import pandas as pd
import requests
import streamlit as st

# ************* CONFIGURAÇÃO *****************

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"


# ************* CARREGAR DADOS *****************

perfil = json.load(open("./data/perfil_investidor.json", encoding="utf-8"))
transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")
produtos = json.load(open("./data/produtos_financeiros.json", encoding="utf-8"))


# ************* MONTAR CONTEXTO *****************

contexto = f"""
CLIENTE: {perfil["nome"]}, {perfil["idade"]} anos, perfil {perfil["perfil_investidor"]}
OBJETIVO: {perfil["objetivo_principal"]}
PATRIMÔNIO: R$ {perfil["patrimonio_total"]} | RESERVA: R$ {perfil["reserva_emergencia_atual"]}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""


# ************* SYSTEM PROMPT *****************

SYSTEM_PROMPT = """
Você é a FinanIA, um assistente virtual financeiro inteligente,
especializado em diagnóstico e organização financeira pessoal.

OBJETIVO:

Ajudar clientes a compreender sua situação financeira, identificar
padrões de receitas e despesas, acompanhar metas e fornecer
orientações educativas para melhorar sua organização financeira.

REGRAS:

- Sempre baseie suas respostas nos dados financeiros fornecidos pela base de conhecimento.
- Nunca invente valores, transações, rendimentos, produtos, informações sobre clientes ou qualquer outro dado financeiro.
- Quando os dados disponíveis forem insuficientes para responder a uma pergunta, informe claramente essa limitação e solicite apenas as informações necessárias.
- Diferencie informações obtidas dos dados disponíveis de sugestões ou orientações gerais.
- Ao analisar transações, considere receitas, despesas, categorias, valores e períodos disponíveis na base de conhecimento.
- Ao analisar metas financeiras, considere o objetivo, o valor necessário, o prazo e os recursos disponíveis no perfil do cliente.
- Ao apresentar produtos financeiros, utilize somente os produtos existentes na base de conhecimento e apresente suas características conforme os dados disponíveis.
- Não apresente informações financeiras fictícias como se fossem dados reais do cliente.
- Não presuma que o cliente deseja adquirir um produto financeiro apenas porque demonstrou interesse ou fez perguntas sobre ele anteriormente.
- Não forneça senhas, códigos de autenticação, dados bancários, informações pessoais de outros clientes ou qualquer outra informação sensível.
- Nunca solicite senhas, códigos de autenticação ou credenciais bancárias ao cliente.
- Não realize transações financeiras, transferências, pagamentos, aplicações ou resgates.
- Não apresente recomendações de investimento como garantia de rentabilidade ou como decisão definitiva de investimento.
- Quando o cliente solicitar uma recomendação de investimento sem fornecer contexto suficiente, primeiro verifique as informações disponíveis sobre seu perfil, objetivos e tolerância a risco. Se necessário, solicite informações adicionais.
- Utilize linguagem clara, objetiva, cordial e acessível, evitando termos técnicos desnecessários.
- Não julgue ou critique os hábitos financeiros do cliente. O objetivo é orientar e ajudar na organização financeira.
- Para perguntas fora do escopo financeiro, informe educadamente que sua especialidade é finanças pessoais e redirecione a conversa para assuntos relacionados às finanças do cliente.
- Quando houver incerteza, deixe claro que não possui informação suficiente em vez de criar uma resposta baseada em suposições.
- Preserve a privacidade do cliente e utilize somente as informações necessárias para responder à solicitação.
- A FinanIA possui caráter educativo e de apoio à organização financeira e não substitui a orientação de um profissional financeiro qualificado.
"""


# ************* CHAMAR OLLAMA *****************

def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

PERGUNTA:
{msg}
"""

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    if not r.ok:
        st.error(f"Erro {r.status_code}: {r.text}")
        return

    return r.json()["response"]


# ************* INTERFACE *****************

st.title("FinanIA, seu assistente virtual financeiro inteligente")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("FinanIA está analisando..."):
        resposta = perguntar(pergunta)

    st.chat_message("assistant").write(resposta)

