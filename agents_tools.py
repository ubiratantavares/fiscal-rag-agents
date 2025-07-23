#  agents_tools.py  - Ferramentas para agentes

from langchain.agents import Tool
from xml_extractor import XMLExtractor
from fiscal_validator import FiscalValidator

extrair_dados_xml_tool = Tool(
    name="Extrator XML",
    func=lambda caminho: XMLExtractor().extrair_dados_xml(caminho),
    description="Extrai dados fiscais de um arquivo XML de nota fiscal."
)

validar_dados_fiscais_tool = Tool(
    name="Validador Fiscal",
    func=lambda dados: FiscalValidator().validar_dados(dados),
    description="Valida CFOP e ICMS dos dados extraídos."
)