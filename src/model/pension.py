<<<<<<< HEAD:src/model/Pension.py

# src/model/Pension.py

class Pension:

    def __init__(self, cedula: int, base_settlement_income: float,
                current_legal_minimum_wage: float, pension_porcentage: float):
        """Representa un registro de pensión asociado a un usuario"""
        self.cedula = cedula
        self.base_settlement_income = base_settlement_income
        self.current_legal_minimum_wage = current_legal_minimum_wage
        self.pension_porcentage = pension_porcentage

    def EsIgual(self, otra):
        """Compara si esta instancia es igual a otra"""
        assert self.cedula == otra.cedula
        assert self.base_settlement_income == otra.base_settlement_income
        assert self.current_legal_minimum_wage == otra.current_legal_minimum_wage
        assert self.pension_porcentage == otra.pension_porcentage
        return True
=======

# src/model/Pension.py

class Pension:

    def __init__(self, cedula: int, base_settlement_income: float,
                current_legal_minimum_wage: float, pension_porcentage: float):
        """Representa un registro de pensión asociado a un usuario"""
        self.cedula = cedula
        self.base_settlement_income = base_settlement_income
        self.current_legal_minimum_wage = current_legal_minimum_wage
        self.pension_porcentage = pension_porcentage

    def EsIgual(self, otra):
        """Compara si esta instancia es igual a otra"""
      
        assert self.cedula == otra.cedula
        assert self.base_settlement_income == otra.base_settlement_income
        assert self.current_legal_minimum_wage == otra.current_legal_minimum_wage
        assert self.pension_porcentage == otra.pension_porcentage
        return True
>>>>>>> a43afe1d20d40cd9a90d55b9c4659cfa8716d34b:src/model/pension.py
