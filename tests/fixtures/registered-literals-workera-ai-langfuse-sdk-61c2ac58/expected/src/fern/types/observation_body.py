

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_value import MapValue
from .observation_level import ObservationLevel
from .observation_type import ObservationType
from .usage import Usage


class ObservationBody(UniversalBaseModel):
    id: typing.Optional[str] = None
    trace_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="traceId"), pydantic.Field(alias="traceId")
    ] = None
    type: ObservationType
    name: typing.Optional[str] = None
    start_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startTime"), pydantic.Field(alias="startTime")
    ] = None
    end_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endTime"), pydantic.Field(alias="endTime")
    ] = None
    completion_start_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completionStartTime"),
        pydantic.Field(alias="completionStartTime"),
    ] = None
    model: typing.Optional[str] = None
    model_parameters: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[MapValue]]],
        FieldMetadata(alias="modelParameters"),
        pydantic.Field(alias="modelParameters"),
    ] = None
    input: typing.Optional[typing.Any] = None
    version: typing.Optional[str] = None
    metadata: typing.Optional[typing.Any] = None
    output: typing.Optional[typing.Any] = None
    usage: typing.Optional[Usage] = None
    level: typing.Optional[ObservationLevel] = None
    status_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="statusMessage"), pydantic.Field(alias="statusMessage")
    ] = None
    parent_observation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentObservationId"), pydantic.Field(alias="parentObservationId")
    ] = None
    environment: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
