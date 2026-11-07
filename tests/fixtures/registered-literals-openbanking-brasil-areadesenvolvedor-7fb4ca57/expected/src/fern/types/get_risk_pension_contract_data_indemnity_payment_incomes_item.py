

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRiskPensionContractDataIndemnityPaymentIncomesItem(enum.StrEnum):
    """
    Tipo de renda ou pensão, caso modalidade de pagamento de indenização seja sob a forma de renda:
      1. Certa
      2. Temporária
      3. Temporária reversível
      4. Temporário com mínimo garantido
      5. Temporária reversível com mínimo garantido
      6. Vitalícia
      7. Vitalícia reversível
      8. Vitalícia com o mínimo garantido
      9. Vitalícia reversível como mínimo garantido
    """

    CERTA = "CERTA"
    TEMPORARIA = "TEMPORARIA"
    TEMPORARIA_REVERSIVEL = "TEMPORARIA_REVERSIVEL"
    TEMPORARIO_MINIMO_GARANTIDO = "TEMPORARIO_MINIMO_GARANTIDO"
    TEMPORARIA_REVERSIVEL_MINIMO_GARANTIDO = "TEMPORARIA_REVERSIVEL_MINIMO_GARANTIDO"
    VITALICIA = "VITALICIA"
    VITALICIA_REVERSIVEL = "VITALICIA_REVERSIVEL"
    VITALICIA_MINIMO_GARANTIDO = "VITALICIA_MINIMO_GARANTIDO"
    VITALICIA_REVERSIVEL_MINIMO_GARANTIDO = "VITALICIA_REVERSIVEL_MINIMO_GARANTIDO"

    def visit(
        self,
        certa: typing.Callable[[], T_Result],
        temporaria: typing.Callable[[], T_Result],
        temporaria_reversivel: typing.Callable[[], T_Result],
        temporario_minimo_garantido: typing.Callable[[], T_Result],
        temporaria_reversivel_minimo_garantido: typing.Callable[[], T_Result],
        vitalicia: typing.Callable[[], T_Result],
        vitalicia_reversivel: typing.Callable[[], T_Result],
        vitalicia_minimo_garantido: typing.Callable[[], T_Result],
        vitalicia_reversivel_minimo_garantido: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetRiskPensionContractDataIndemnityPaymentIncomesItem.CERTA:
            return certa()
        if self is GetRiskPensionContractDataIndemnityPaymentIncomesItem.TEMPORARIA:
            return temporaria()
        if self is GetRiskPensionContractDataIndemnityPaymentIncomesItem.TEMPORARIA_REVERSIVEL:
            return temporaria_reversivel()
        if self is GetRiskPensionContractDataIndemnityPaymentIncomesItem.TEMPORARIO_MINIMO_GARANTIDO:
            return temporario_minimo_garantido()
        if self is GetRiskPensionContractDataIndemnityPaymentIncomesItem.TEMPORARIA_REVERSIVEL_MINIMO_GARANTIDO:
            return temporaria_reversivel_minimo_garantido()
        if self is GetRiskPensionContractDataIndemnityPaymentIncomesItem.VITALICIA:
            return vitalicia()
        if self is GetRiskPensionContractDataIndemnityPaymentIncomesItem.VITALICIA_REVERSIVEL:
            return vitalicia_reversivel()
        if self is GetRiskPensionContractDataIndemnityPaymentIncomesItem.VITALICIA_MINIMO_GARANTIDO:
            return vitalicia_minimo_garantido()
        if self is GetRiskPensionContractDataIndemnityPaymentIncomesItem.VITALICIA_REVERSIVEL_MINIMO_GARANTIDO:
            return vitalicia_reversivel_minimo_garantido()
