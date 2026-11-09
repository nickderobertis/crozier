

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Location(UniversalBaseModel):
    """
    A representation of where a transaction took place
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The street address where the transaction occurred.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The city where the transaction occurred.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO 3166-1 alpha-2 country code where the transaction occurred.
    """

    lat: typing.Optional[float] = pydantic.Field(default=None)
    """
    The latitude where the transaction occurred.
    """

    lon: typing.Optional[float] = pydantic.Field(default=None)
    """
    The longitude where the transaction occurred.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code where the transaction occurred. In API versions 2018-05-22 and earlier, this field is called `zip`.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region or state where the transaction occurred. In API versions 2018-05-22 and earlier, this field is called `state`.
    """

    store_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant defined store number where the transaction occurred.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
