

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency_code import CurrencyCode
from .survival_pension_minimum_premium_periodicity import SurvivalPensionMinimumPremiumPeriodicity


class SurvivalPensionMinimumPremium(UniversalBaseModel):
    """
    Valor mínimo de prêmio/contribuição
    """

    currency: typing.Optional[CurrencyCode] = None
    periodicity: typing.Optional[SurvivalPensionMinimumPremiumPeriodicity] = None
    amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    Valor mínimo em R$ de prêmio/ contribuição aceita pela sociedade ao plano (identificar valor mensal e/ou aporte único).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
