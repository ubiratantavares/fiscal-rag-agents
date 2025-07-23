#v main.py - Organizador principal

from agents_tools import extrair_dados_xml_tool, validar_dados_fiscais_tool

from fiscal_agent import criar_agente_fiscal

def main():
    agente = criar_agente_fiscal(verbose=True)
    pergunta = "O CFOP e o ICMS da nota fiscal em exemplos/exemplo_nfe.xml estão corretos?"
    resposta = agente.invoke({"input": pergunta})
    print(resposta['output'])

if __name__ == "__main__":
    main()

