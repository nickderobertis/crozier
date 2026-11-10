

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaystubAddress(UniversalBaseModel):
    """
    Address on the paystub
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full city name.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO 3166-1 alpha-2 country code.
    """

    line1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Street address line 1.
    """

    line2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Street address line 2.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code of the address.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region or state
    Example: `"NC"`
    """

    state_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region or state
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
