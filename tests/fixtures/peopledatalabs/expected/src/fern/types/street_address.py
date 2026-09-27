

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .street_address_continent import StreetAddressContinent
from .street_address_metro import StreetAddressMetro


class StreetAddress(UniversalBaseModel):
    street_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The street address associated with the location object
    """

    address_line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="address_line_2"),
        pydantic.Field(
            alias="address_line_2", description="The secondary street address associated with the location object"
        ),
    ] = None
    """
    The secondary street address associated with the location object
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string that appends location fields together to create a standard location field
    """

    locality: typing.Optional[str] = pydantic.Field(default=None)
    """
    The administrative locality associated with the location object
    """

    metro: typing.Optional[StreetAddressMetro] = pydantic.Field(default=None)
    """
    The metro area associated with the location object
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The administrative region associated with the location object
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code associated with the location object
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country associated with the location object
    """

    geo: typing.Optional[str] = pydantic.Field(default=None)
    """
    The geolocation associated with the location object in latitude, longitude format
    """

    continent: typing.Optional[StreetAddressContinent] = pydantic.Field(default=None)
    """
    The continent associated with the country in the location object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
