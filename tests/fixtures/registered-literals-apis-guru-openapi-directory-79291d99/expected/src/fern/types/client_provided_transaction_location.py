

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClientProvidedTransactionLocation(UniversalBaseModel):
    """
    A representation of where a transaction took place.

    Use this field to pass in structured location information you may have about your transactions. Providing location data is optional but can increase result quality. If you have unstructured location information, it may be appended to the `description` field.
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
    The country where the transaction occurred.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code where the transaction occurred.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region or state where the transaction occurred.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
