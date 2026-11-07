

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem(enum.StrEnum):
    """
    Meio de pagamento escolhido pelo segurado. A considerar os domínios abaixo:
      1. Cartão de Crédito
      2. Cartão de Débito
      3. Débito em conta corrente
      4. Débito em conta poupança
      5. Boleto bancário
      6. PIX
      7. Consignação em Folha de Pagamento
      8. Pontos de Programa de Benefício
      9. Outros
    """

    CARTAO_CREDITO = "CARTAO_CREDITO"
    CARTAO_DEBITO = "CARTAO_DEBITO"
    DEBITO_CONTA_CORRENTE = "DEBITO_CONTA_CORRENTE"
    DEBITO_CONTA_POUPANCA = "DEBITO_CONTA_POUPANCA"
    BOLETO_BANCARIO = "BOLETO_BANCARIO"
    PIX = "PIX"
    CONSIGNACAO_FOLHA_PAGAMENTO = "CONSIGNACAO_FOLHA_PAGAMENTO"
    PONTOS_PROGRAMA_BENEFICIO = "PONTOS_PROGRAMA_BENEFÍCIO"
    OUTROS = "OUTROS"

    def visit(
        self,
        cartao_credito: typing.Callable[[], T_Result],
        cartao_debito: typing.Callable[[], T_Result],
        debito_conta_corrente: typing.Callable[[], T_Result],
        debito_conta_poupanca: typing.Callable[[], T_Result],
        boleto_bancario: typing.Callable[[], T_Result],
        pix: typing.Callable[[], T_Result],
        consignacao_folha_pagamento: typing.Callable[[], T_Result],
        pontos_programa_beneficio: typing.Callable[[], T_Result],
        outros: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem.CARTAO_CREDITO:
            return cartao_credito()
        if self is GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem.CARTAO_DEBITO:
            return cartao_debito()
        if self is GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem.DEBITO_CONTA_CORRENTE:
            return debito_conta_corrente()
        if self is GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem.DEBITO_CONTA_POUPANCA:
            return debito_conta_poupanca()
        if self is GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem.BOLETO_BANCARIO:
            return boleto_bancario()
        if self is GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem.PIX:
            return pix()
        if self is GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem.CONSIGNACAO_FOLHA_PAGAMENTO:
            return consignacao_folha_pagamento()
        if self is GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem.PONTOS_PROGRAMA_BENEFICIO:
            return pontos_programa_beneficio()
        if self is GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem.OUTROS:
            return outros()
