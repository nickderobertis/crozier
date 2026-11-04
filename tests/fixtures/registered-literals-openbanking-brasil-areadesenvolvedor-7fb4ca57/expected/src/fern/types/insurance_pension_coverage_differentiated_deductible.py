

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency_code import CurrencyCode


class InsurancePensionCoverageDifferentiatedDeductible(UniversalBaseModel):
    """
    Detalhamento da franquia em reais diferentes para cada cobertura que exista alguma especificidade.<br>Caso a seguradora não tenha essa diferenciação, não retornará nada no campo.
    """

    amount: str
    currency: CurrencyCode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
