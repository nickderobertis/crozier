

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRiskPensionContractDataPremiumPaymentFrequenciesItem(enum.StrEnum):
    """
    Periodicidade de pagamento do prêmio:
      1. Diária
      2. Mensal
      3. Única
      4. Anual
      5. Trimestral
      6. Semestral
      7. Fracionado
      8. Outra
    """

    DIARIA = "DIARIA"
    MENSAL = "MENSAL"
    UNICA = "UNICA"
    ANUAL = "ANUAL"
    TRIMESTRAL = "TRIMESTRAL"
    SEMESTRAL = "SEMESTRAL"
    FRACIONADO = "FRACIONADO"
    OUTRA = "OUTRA"

    def visit(
        self,
        diaria: typing.Callable[[], T_Result],
        mensal: typing.Callable[[], T_Result],
        unica: typing.Callable[[], T_Result],
        anual: typing.Callable[[], T_Result],
        trimestral: typing.Callable[[], T_Result],
        semestral: typing.Callable[[], T_Result],
        fracionado: typing.Callable[[], T_Result],
        outra: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetRiskPensionContractDataPremiumPaymentFrequenciesItem.DIARIA:
            return diaria()
        if self is GetRiskPensionContractDataPremiumPaymentFrequenciesItem.MENSAL:
            return mensal()
        if self is GetRiskPensionContractDataPremiumPaymentFrequenciesItem.UNICA:
            return unica()
        if self is GetRiskPensionContractDataPremiumPaymentFrequenciesItem.ANUAL:
            return anual()
        if self is GetRiskPensionContractDataPremiumPaymentFrequenciesItem.TRIMESTRAL:
            return trimestral()
        if self is GetRiskPensionContractDataPremiumPaymentFrequenciesItem.SEMESTRAL:
            return semestral()
        if self is GetRiskPensionContractDataPremiumPaymentFrequenciesItem.FRACIONADO:
            return fracionado()
        if self is GetRiskPensionContractDataPremiumPaymentFrequenciesItem.OUTRA:
            return outra()
