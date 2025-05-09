class Usuario:
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa a un usuario de la pensión en la aplicación
    """
    def __init__(self, cedula:int, nombre:str, base_settlement_income:float, current_legal_minimum_wage:float, pension_porcentage: float):
        self.cedula = cedula
        self.nombre = nombre
        self.base_settlement_income = base_settlement_income
        self.current_legal_minimum_wage = current_legal_minimum_wage
        self.pension_porcentage = pension_porcentage


    def esIgual( self, comparar_con ) :
        """
        Compara el objeto actual, con otra instancia de la clase Usuario
        """
        assert( self.cedula == comparar_con.cedula )
        assert( self.nombre == comparar_con.nombre )
        assert( self.base_settlement_income== comparar_con.base_settlement_income )
        assert( self.current_legal_minimum_wage== comparar_con.current_legal_minimum_wage )
        assert( self.pension_porcentage== comparar_con.pension_porcentage )
        return True