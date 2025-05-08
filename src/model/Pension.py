
# src/model/Pension.py

class Pension:

    def __init__(self, id: int, cedula: str, base_settlement_income: int,
                 current_legal_minimum_wage: int, pension_porcentage: int):
        """Representa un registro de pensión asociado a un usuario"""
      
        self.cedula = cedula
        self.base_settlement_income = base_settlement_income
        self.current_legal_minimum_wage = current_legal_minimum_wage
        self.pension_porcentage = pension_porcentage

    def EsIgual(self, otra):
        """Compara si esta instancia es igual a otra"""
        assert self.id == otra.id
        assert self.cedula == otra.cedula
        assert self.base_settlement_income == otra.base_settlement_income
        assert self.current_legal_minimum_wage == otra.current_legal_minimum_wage
        assert self.pension_porcentage == otra.pension_porcentage
        return True
