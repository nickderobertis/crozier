

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CoverageAttributesIndemnityPaymentMethodsItem(enum.StrEnum):
    PAGAMENTO_CAPITAL_SEGURADO_VALOR_MONETARIO = "PAGAMENTO_CAPITAL_SEGURADO_VALOR_MONETARIO"
    REEMBOLSO_DESPESAS = "REEMBOLSO_DESPESAS"
    PRESTACAO_SERVICOS = "PRESTACAO_SERVICOS"

    def visit(
        self,
        pagamento_capital_segurado_valor_monetario: typing.Callable[[], T_Result],
        reembolso_despesas: typing.Callable[[], T_Result],
        prestacao_servicos: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CoverageAttributesIndemnityPaymentMethodsItem.PAGAMENTO_CAPITAL_SEGURADO_VALOR_MONETARIO:
            return pagamento_capital_segurado_valor_monetario()
        if self is CoverageAttributesIndemnityPaymentMethodsItem.REEMBOLSO_DESPESAS:
            return reembolso_despesas()
        if self is CoverageAttributesIndemnityPaymentMethodsItem.PRESTACAO_SERVICOS:
            return prestacao_servicos()
