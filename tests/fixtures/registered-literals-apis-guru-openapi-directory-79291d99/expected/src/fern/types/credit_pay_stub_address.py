

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreditPayStubAddress(UniversalBaseModel):
    """
    Address on the pay stub.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full city name.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO 3166-1 alpha-2 country code.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code of the address.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region or state.
    Example: `"NC"`
    """

    street: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full street address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
