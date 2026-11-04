

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project_parameter_details import ProjectParameterDetails


class ProjectsRow(UniversalBaseModel):
    bbox: typing.Optional[typing.List[float]] = None
    countries: typing.Optional[typing.List[str]] = None
    entity: typing.Optional[str] = None
    first_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="firstUpdated"), pydantic.Field(alias="firstUpdated")
    ]
    id: int
    is_analysis: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isAnalysis"), pydantic.Field(alias="isAnalysis")
    ] = None
    is_mobile: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isMobile"), pydantic.Field(alias="isMobile")
    ] = None
    last_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    location_ids: typing_extensions.Annotated[
        typing.List[int], FieldMetadata(alias="locationIds"), pydantic.Field(alias="locationIds")
    ]
    locations: int
    measurements: int
    name: str
    parameters: typing.List[ProjectParameterDetails]
    sensor_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sensorType"), pydantic.Field(alias="sensorType")
    ] = None
    sources: typing.Optional[typing.List[typing.Any]] = None
    subtitle: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
