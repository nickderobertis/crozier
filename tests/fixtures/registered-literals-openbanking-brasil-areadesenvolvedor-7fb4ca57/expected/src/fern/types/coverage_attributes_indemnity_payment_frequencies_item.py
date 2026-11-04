

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CoverageAttributesIndemnityPaymentFrequenciesItem(enum.StrEnum):
    """ """

    INDENIZACAO_UNICA = "INDENIZACAO_UNICA"
    DIARIA_OU_PARCELA = "DIARIA_OU_PARCELA"

    def visit(
        self, indenizacao_unica: typing.Callable[[], T_Result], diaria_ou_parcela: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CoverageAttributesIndemnityPaymentFrequenciesItem.INDENIZACAO_UNICA:
            return indenizacao_unica()
        if self is CoverageAttributesIndemnityPaymentFrequenciesItem.DIARIA_OU_PARCELA:
            return diaria_ou_parcela()
