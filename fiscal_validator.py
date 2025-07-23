# fiscal_validator.py - Validador de dados fiscais

class FiscalValidator:
    def validar_cfop(self, cfop):
        cfops_validos = {"5101", "6101", "6108"}
        return cfop in cfops_validos

    def validar_icms(self, icms):
        try:
            return float(icms) >= 0.0
        except:
            return False

    def validar_dados(self, dados):
        return {
            "cfop_valido": self.validar_cfop(dados.get("cfop")),
            "icms_valido": self.validar_icms(dados.get("icms"))
        }

