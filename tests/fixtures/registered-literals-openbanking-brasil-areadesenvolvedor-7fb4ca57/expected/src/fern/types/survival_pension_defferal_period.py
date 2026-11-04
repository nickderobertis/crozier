

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survival_pension_defferal_period_premium_payment_methods_item import (
    SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem,
)
from .survival_pension_grace_period import SurvivalPensionGracePeriod
from .survival_pension_investiment_fund import SurvivalPensionInvestimentFund
from .survival_pension_minimum_premium import SurvivalPensionMinimumPremium
from .update_index import UpdateIndex


class SurvivalPensionDefferalPeriod(UniversalBaseModel):
    """
    Período de Diferimento
    """

    interest_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="interestRate"),
        pydantic.Field(
            alias="interestRate",
            description="Taxa de juros mensal garantida que remunera o plano durante a fase de diferimento/acumulação.",
        ),
    ] = None
    """
    Taxa de juros mensal garantida que remunera o plano durante a fase de diferimento/acumulação.
    """

    update_index: typing_extensions.Annotated[
        typing.Optional[UpdateIndex], FieldMetadata(alias="updateIndex"), pydantic.Field(alias="updateIndex")
    ] = None
    other_minimum_performance_garantees: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="otherMinimumPerformanceGarantees"),
        pydantic.Field(
            alias="otherMinimumPerformanceGarantees",
            description="Para produtos do tipo PDR e VDR, indicação do índice de ampla divulgação utilizados como garantia mínima de desempenho.",
        ),
    ] = None
    """
    Para produtos do tipo PDR e VDR, indicação do índice de ampla divulgação utilizados como garantia mínima de desempenho.
    """

    reversal_financial_results: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="reversalFinancialResults"),
        pydantic.Field(
            alias="reversalFinancialResults",
            description="Percentual de reversão de excedente financeiro na concessão. Em %.",
        ),
    ] = None
    """
    Percentual de reversão de excedente financeiro na concessão. Em %.
    """

    minimum_premiums: typing_extensions.Annotated[
        typing.Optional[typing.List[SurvivalPensionMinimumPremium]],
        FieldMetadata(alias="minimumPremiums"),
        pydantic.Field(alias="minimumPremiums"),
    ] = None
    premium_payment_methods: typing_extensions.Annotated[
        typing.List[SurvivalPensionDefferalPeriodPremiumPaymentMethodsItem],
        FieldMetadata(alias="premiumPaymentMethods"),
        pydantic.Field(alias="premiumPaymentMethods"),
    ]
    permission_extraordinary_contributions: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="permissionExtraordinaryContributions"),
        pydantic.Field(
            alias="permissionExtraordinaryContributions",
            description="Se ficam permitidos aportes extraordinários. A considerar os seguintes domínios:\n1. true\n2. false",
        ),
    ] = None
    """
    Se ficam permitidos aportes extraordinários. A considerar os seguintes domínios:
    1. true
    2. false
    """

    permission_scheduled_financial_payments: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="permissionScheduledFinancialPayments"),
        pydantic.Field(
            alias="permissionScheduledFinancialPayments",
            description="Se ficam permitidos pagamentos financeiros programados. A considerar os seguintes domínios:\n1. true\n2. false",
        ),
    ] = None
    """
    Se ficam permitidos pagamentos financeiros programados. A considerar os seguintes domínios:
    1. true
    2. false
    """

    grace_period: typing_extensions.Annotated[
        typing.Optional[SurvivalPensionGracePeriod],
        FieldMetadata(alias="gracePeriod"),
        pydantic.Field(alias="gracePeriod"),
    ] = None
    redemption_payment_term: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="redemptionPaymentTerm"),
        pydantic.Field(alias="redemptionPaymentTerm", description="Prazo em dias para pagamento do resgate"),
    ] = None
    """
    Prazo em dias para pagamento do resgate
    """

    portability_payment_term: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="portabilityPaymentTerm"),
        pydantic.Field(
            alias="portabilityPaymentTerm",
            description="Prazo em dias para pagamento da portabilidade (entre empresas diferentes).",
        ),
    ] = None
    """
    Prazo em dias para pagamento da portabilidade (entre empresas diferentes).
    """

    investment_funds: typing_extensions.Annotated[
        typing.Optional[typing.List[SurvivalPensionInvestimentFund]],
        FieldMetadata(alias="investmentFunds"),
        pydantic.Field(alias="investmentFunds"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
