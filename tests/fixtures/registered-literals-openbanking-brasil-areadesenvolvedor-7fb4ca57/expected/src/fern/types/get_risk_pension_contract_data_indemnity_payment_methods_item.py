

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRiskPensionContractDataIndemnityPaymentMethodsItem(enum.StrEnum):
    """
    Modalidade de pagamento da indenização, a considerar os domínios abaixo:
      1. Único
      2. Sob a forma de renda
    """

    UNICO = "UNICO"
    SOB_FORMA_RENDA = "SOB_FORMA_RENDA"

    def visit(self, unico: typing.Callable[[], T_Result], sob_forma_renda: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRiskPensionContractDataIndemnityPaymentMethodsItem.UNICO:
            return unico()
        if self is GetRiskPensionContractDataIndemnityPaymentMethodsItem.SOB_FORMA_RENDA:
            return sob_forma_renda()
