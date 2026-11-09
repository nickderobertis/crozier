

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .additional_levels import AdditionalLevels


class Court(UniversalBaseModel):
    additional_levels: typing_extensions.Annotated[
        typing.Optional[AdditionalLevels],
        FieldMetadata(alias="additionalLevels"),
        pydantic.Field(alias="additionalLevels"),
    ] = None
    appeal_courts_for_court_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="appealCourtsForCourtAPI"),
        pydantic.Field(alias="appealCourtsForCourtAPI"),
    ] = None
    container: typing.Optional[str] = None
    container_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="containerType"), pydantic.Field(alias="containerType")
    ] = None
    court_id: typing_extensions.Annotated[str, FieldMetadata(alias="courtId"), pydantic.Field(alias="courtId")]
    court_locations_for_court_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="courtLocationsForCourtAPI"),
        pydantic.Field(alias="courtLocationsForCourtAPI"),
    ] = None
    court_service_status_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="courtServiceStatusAPI"),
        pydantic.Field(alias="courtServiceStatusAPI"),
    ] = None
    court_system_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="courtSystemId"), pydantic.Field(alias="courtSystemId")
    ]
    court_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="courtTypeId"), pydantic.Field(alias="courtTypeId")
    ]
    created_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdDate"),
        pydantic.Field(
            alias="createdDate",
            description="The date and time when the Court was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.",
        ),
    ]
    """
    The date and time when the Court was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.
    """

    jurisdiction_geo_for_court_api: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jurisdictionGeoForCourtAPI"),
        pydantic.Field(alias="jurisdictionGeoForCourtAPI"),
    ] = None
    name: str
    name_aka: typing_extensions.Annotated[str, FieldMetadata(alias="nameAka"), pydantic.Field(alias="nameAka")]
    object: str
    system: str
    type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
