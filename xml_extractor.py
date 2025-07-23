# xml_extractor.py

import xml.etree.ElementTree as ET

class XMLExtractor:

    def extrair_dados_xml(self, caminho_arquivo):
        try:
            tree = ET.parse(caminho_arquivo)

            root = tree.getroot()

            dados = {'emitente': root.findtext('.//emit/CNPJ'),
                     'destinatario': root.findtext('.//dest/CNPJ'), 
                     'cfop': root.findtext('.//det/prod/CFOP'),
                     'cst': root.findtext('.//imposto/ICMS/*/CST'),
                     'ncm': root.findtext('.//det/prod/NCM'),
                     'icms': root.findtext('.//imposto/ICMS/*/vICMS')
            }

            return dados
        except ET.ParseError as e:
            raise ValueError(f"Erro ao analisar o XML: {e}")
        except Exception as e:
            raise ValueError(f"Erro ao extrair dados do XML: {e}")
