# fiscal_agent.py  - Agente fiscal

from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from agent_tools import extrair_dados_xml_tool, validar_dados_fiscais_tool

load_dotenv()

def criar_agente_fiscal(verbose=False):
    model = ChatGroq(model_name="mixtral-8x7b-32768") # chave lida do .env automaticamente

    tools = [extrair_dados_xml_tool, validar_dados_fiscais_tool]

    prompt = PromptTemplate.from_template(
        """
        Você é um assistente fiscal inteligente. Seu objetivo é analisar arquivos XML de nota fiscal eletrônica,
        extrair os dados fiscais e verificar se os campos CFOP e ICMS estão corretos com base nas regras fornecidas.
        Utilize as ferramentas disponíveis para obter e validar os dados, fornecendo uma resposta clara ao usuário.

        {input}
        """
    )

    agent = create_react_agent(
        llm=model,
        tools=tools,
        prompt=prompt
    )

    executor = AgentExecutor(agent=agent, tools=tools, verbose=verbose)
    
    return executor
