

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency_code import CurrencyCode


class InsurancePensionMinValue(UniversalBaseModel):
    """
    Listagem do valor mínimo de cobertura (Capital Segurado), diária ou parcela aceito pela sociedade para cada combinação de modalidade/cobertura do produto.<br>Conforme moeda.
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
