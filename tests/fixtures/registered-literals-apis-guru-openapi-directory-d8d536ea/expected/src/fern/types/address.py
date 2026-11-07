

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Address(UniversalBaseModel):
    """
    Address object Data Schema
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City
    """

    country_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="countryCode"),
        pydantic.Field(
            alias="countryCode",
            description="ISO 3166-1 alpha-3 (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#Officially_assigned_code_elements). Code of the country if country name is present.",
        ),
    ] = None
    """
    ISO 3166-1 alpha-3 (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3#Officially_assigned_code_elements). Code of the country if country name is present.
    """

    country_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="countryName"),
        pydantic.Field(alias="countryName", description="Country Name if present else default value."),
    ]
    """
    Country Name if present else default value.
    """

    first_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(alias="firstFetchDate", description="Date at which this record is created in UniCourt."),
    ]
    """
    Date at which this record is created in UniCourt.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(alias="isVisible", description="Boolean indicating if the address is visible or not."),
    ]
    """
    Boolean indicating if the address is visible or not.
    """

    last_fetch_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="Date at which this record was updated in UniCourt."),
    ]
    """
    Date at which this record was updated in UniCourt.
    """

    latitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    Coordinates at geographic coordinate system.
    """

    longitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    Coordinates at geographic coordinate system.
    """

    object: str
    state_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="stateCode"),
        pydantic.Field(alias="stateCode", description="State Code if the state is a US state else contains null."),
    ] = None
    """
    State Code if the state is a US state else contains null.
    """

    state_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="stateName"),
        pydantic.Field(alias="stateName", description="State Name if present else default value."),
    ]
    """
    State Name if present else default value.
    """

    street_address1: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="streetAddress1"),
        pydantic.Field(alias="streetAddress1", description="1st part of the street address."),
    ] = None
    """
    1st part of the street address.
    """

    street_address2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="streetAddress2"),
        pydantic.Field(alias="streetAddress2", description="2nd part of the street address."),
    ] = None
    """
    2nd part of the street address.
    """

    zip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Zip code of the address.
    """

    zip4: typing.Optional[str] = pydantic.Field(default=None)
    """
    4 digit extension of the zip code if the address is a US address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
