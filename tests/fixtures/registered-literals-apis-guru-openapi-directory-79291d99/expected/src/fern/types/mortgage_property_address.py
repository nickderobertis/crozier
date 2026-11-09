

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MortgagePropertyAddress(UniversalBaseModel):
    """
    Object containing fields describing property address.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The city name.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO 3166-1 alpha-2 country code.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The five or nine digit postal code.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region or state (example "NC").
    """

    street: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full street address (example "564 Main Street, Apt 15").
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
