

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DepositSwitchAddressData(UniversalBaseModel):
    """
    The user's address.
    """

    city: str = pydantic.Field()
    """
    The full city name
    """

    country: str = pydantic.Field()
    """
    The ISO 3166-1 alpha-2 country code
    """

    postal_code: str = pydantic.Field()
    """
    The postal code
    """

    region: str = pydantic.Field()
    """
    The region or state
    Example: `"NC"`
    """

    street: str = pydantic.Field()
    """
    The full street address
    Example: `"564 Main Street, APT 15"`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
