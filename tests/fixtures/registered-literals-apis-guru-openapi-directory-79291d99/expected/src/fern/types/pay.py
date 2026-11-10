

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Pay(UniversalBaseModel):
    """
    An object representing a monetary amount.
    """

    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    A numerical amount of a specific currency.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency code, e.g. USD
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
