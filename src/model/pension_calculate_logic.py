import sys
sys.path.append("src")  # Asegura que el módulo pueda importar desde el directorio 'src'

# Importa las excepciones personalizadas relacionadas al cálculo de pensión
from model.error_pension import (
    ErrorBaseSettlementIncomeNegative,
    ErrorBaseSettlementIncomeLetras,
    ErrorPensionPorcentageNegative,
    ErrorPensionPorcentageLetras,
    ErrorHighPensionPorcentage,
    ErrorCurrentLegalMinimumWageLetras,
    ErrorCurrentLegalMinimumWageNegative
)


def calculate_pension(ingreso_base_de_liquidacion: float, pension_porcentage: float, salario_minimo_legal_vigente: float) -> float:
    """
    Calcula la pensión mensual con base en el ingreso base de liquidación (IBL),
    el porcentaje de pensión y el salario mínimo mensual legal vigente (SMMLV).

    Parámetros:
        ingreso_base_de_liquidacion (float): Salario promedio sobre el cual se liquida la pensión (IBL).
        pension_porcentage (float): Porcentaje de liquidación de pensión (ej: 75%).
        salario_minimo_legal_vigente (float): Monto del SMMLV actual.

    Retorna:
        float: El valor final de la pensión mensual.

    Excepciones:
        Lanza excepciones personalizadas si los valores son inválidos (negativos, no numéricos, etc.).
    """

    # ---------------- VALIDACIONES DEL INGRESO BASE DE LIQUIDACIÓN (IBL) ----------------

    if isinstance(ingreso_base_de_liquidacion, str):
        raise ErrorBaseSettlementIncomeLetras()
    if ingreso_base_de_liquidacion <= 0:
        raise ErrorBaseSettlementIncomeNegative()

    # ---------------- VALIDACIONES DEL PORCENTAJE DE PENSIÓN ----------------

    if isinstance(pension_porcentage, str):
        raise ErrorPensionPorcentageLetras()
    if pension_porcentage <= 0:
        raise ErrorPensionPorcentageNegative()
    if pension_porcentage > 100:
        raise ErrorHighPensionPorcentage()

    # ---------------- VALIDACIONES DEL SALARIO MÍNIMO LEGAL VIGENTE (SMMLV) ----------------

    if isinstance(salario_minimo_legal_vigente, str):
        raise ErrorCurrentLegalMinimumWageLetras()
    if salario_minimo_legal_vigente <= 0:
        raise ErrorCurrentLegalMinimumWageNegative()

    # ---------------- CÁLCULO FINAL ----------------

    resultado = ingreso_base_de_liquidacion * pension_porcentage / 100

    # La pensión no puede ser mayor al ingreso base de liquidación
    if resultado > ingreso_base_de_liquidacion:
        resultado = ingreso_base_de_liquidacion

    resultado = round(resultado, 2)

    return resultado
