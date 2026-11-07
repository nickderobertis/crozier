

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CourtLocation(UniversalBaseModel):
    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City
    """

    court_location_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="courtLocationId"), pydantic.Field(alias="courtLocationId")
    ]
    court_service_status_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="courtServiceStatusAPI"),
        pydantic.Field(alias="courtServiceStatusAPI"),
    ] = None
    courts_for_court_location_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="courtsForCourtLocationAPI"), pydantic.Field(alias="courtsForCourtLocationAPI")
    ]
    created_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdDate"),
        pydantic.Field(
            alias="createdDate",
            description="The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.",
        ),
    ]
    """
    The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.
    """

    name: str
    object: str
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
