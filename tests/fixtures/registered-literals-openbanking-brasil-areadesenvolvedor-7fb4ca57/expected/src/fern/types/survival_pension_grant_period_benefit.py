

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survival_pension_grant_period_benefit_biometric_table_item import (
    SurvivalPensionGrantPeriodBenefitBiometricTableItem,
)
from .survival_pension_grant_period_benefit_income_modalities_item import (
    SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem,
)
from .survival_pension_investiment_fund import SurvivalPensionInvestimentFund
from .update_index import UpdateIndex


class SurvivalPensionGrantPeriodBenefit(UniversalBaseModel):
    """
    Período de concessão do benefício
    """

    income_modalities: typing_extensions.Annotated[
        typing.List[SurvivalPensionGrantPeriodBenefitIncomeModalitiesItem],
        FieldMetadata(alias="incomeModalities"),
        pydantic.Field(alias="incomeModalities"),
    ]
    biometric_table: typing_extensions.Annotated[
        typing.List[SurvivalPensionGrantPeriodBenefitBiometricTableItem],
        FieldMetadata(alias="biometricTable"),
        pydantic.Field(alias="biometricTable"),
    ]
    interest_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="interestRate"),
        pydantic.Field(
            alias="interestRate", description="Taxa de juros garantida utilizada para conversão em renda. Em %"
        ),
    ] = None
    """
    Taxa de juros garantida utilizada para conversão em renda. Em %
    """

    update_index: typing_extensions.Annotated[
        typing.Optional[UpdateIndex], FieldMetadata(alias="updateIndex"), pydantic.Field(alias="updateIndex")
    ] = None
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
