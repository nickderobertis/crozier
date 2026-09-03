

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MonetaryAmount(UniversalBaseModel):
    amount: float = pydantic.Field()
    """
    Betrag
    """

    currency: str = pydantic.Field()
    """
    Währung (ISO 4217)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
