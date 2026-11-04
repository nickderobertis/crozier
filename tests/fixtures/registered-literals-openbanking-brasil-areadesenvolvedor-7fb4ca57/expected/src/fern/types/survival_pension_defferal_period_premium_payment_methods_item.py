

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem(enum.StrEnum):
    CARTAO_CREDITO = "CARTAO_CREDITO"
    DEBITO_CONTA = "DEBITO_CONTA"
    DEBITO_CONTA_POUPANCA = "DEBITO_CONTA_POUPANCA"
    BOLETO_BANCARIO = "BOLETO_BANCARIO"
    PIX = "PIX"
    CARTAO_DEBITO = "CARTAO_DEBITO"
    REGRA_PARCEIRO = "REGRA_PARCEIRO"
    CONSIGNACAO_FOLHA_PAGAMENTO = "CONSIGNACAO_FOLHA_PAGAMENTO"
    PONTOS_PROGRAMA_BENEFICIO = "PONTOS_PROGRAMA_BENEFICIO"
    TED_DOC = "TED_DOC"
    OUTROS = "OUTROS"

    def visit(
        self,
        cartao_credito: typing.Callable[[], T_Result],
        debito_conta: typing.Callable[[], T_Result],
        debito_conta_poupanca: typing.Callable[[], T_Result],
        boleto_bancario: typing.Callable[[], T_Result],
        pix: typing.Callable[[], T_Result],
        cartao_debito: typing.Callable[[], T_Result],
        regra_parceiro: typing.Callable[[], T_Result],
        consignacao_folha_pagamento: typing.Callable[[], T_Result],
        pontos_programa_beneficio: typing.Callable[[], T_Result],
        ted_doc: typing.Callable[[], T_Result],
        outros: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.CARTAO_CREDITO:
            return cartao_credito()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.DEBITO_CONTA:
            return debito_conta()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.DEBITO_CONTA_POUPANCA:
            return debito_conta_poupanca()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.BOLETO_BANCARIO:
            return boleto_bancario()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.PIX:
            return pix()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.CARTAO_DEBITO:
            return cartao_debito()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.REGRA_PARCEIRO:
            return regra_parceiro()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.CONSIGNACAO_FOLHA_PAGAMENTO:
            return consignacao_folha_pagamento()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.PONTOS_PROGRAMA_BENEFICIO:
            return pontos_programa_beneficio()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.TED_DOC:
            return ted_doc()
        if self is SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem.OUTROS:
            return outros()
