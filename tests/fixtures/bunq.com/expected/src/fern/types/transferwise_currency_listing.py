

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferwiseCurrencyListing(UniversalBaseModel):
    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country code associated with the currency.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency code.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
