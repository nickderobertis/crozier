

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address_type import AddressType
from .row_version import RowVersion


class Address(UniversalBaseModel):
    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of city.
    """

    contact_name: typing.Optional[str] = None
    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    country code according to ISO 3166-1 alpha-2.
    """

    county: typing.Optional[str] = pydantic.Field(default=None)
    """
    Address field that holds a sublocality, such as a county
    """

    email: typing.Optional[str] = None
    fax: typing.Optional[str] = None
    id: typing.Optional[str] = None
    latitude: typing.Optional[str] = None
    line1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Line 1 of the address e.g. number, street, suite, apt #, etc.
    """

    line2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Line 2 of the address
    """

    line3: typing.Optional[str] = pydantic.Field(default=None)
    """
    Line 3 of the address
    """

    line4: typing.Optional[str] = pydantic.Field(default=None)
    """
    Line 4 of the address
    """

    longitude: typing.Optional[str] = None
    name: typing.Optional[str] = None
    phone_number: typing.Optional[str] = None
    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Zip code or equivalent.
    """

    row_version: typing.Optional[RowVersion] = None
    salutation: typing.Optional[str] = None
    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of state
    """

    street_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Street number
    """

    string: typing.Optional[str] = None
    type: typing.Optional[AddressType] = None
    website: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
