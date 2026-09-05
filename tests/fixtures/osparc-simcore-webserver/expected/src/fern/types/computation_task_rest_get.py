

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .running_state import RunningState


class ComputationTaskRestGet(UniversalBaseModel):
    project_uuid: typing_extensions.Annotated[
        str, FieldMetadata(alias="projectUuid"), pydantic.Field(alias="projectUuid")
    ]
    node_id: typing_extensions.Annotated[str, FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId")]
    state: RunningState
    progress: float
    image: typing.Dict[str, typing.Any]
    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    ended_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endedAt"), pydantic.Field(alias="endedAt")
    ] = None
    log_download_link: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logDownloadLink"), pydantic.Field(alias="logDownloadLink")
    ] = None
    node_name: typing_extensions.Annotated[str, FieldMetadata(alias="nodeName"), pydantic.Field(alias="nodeName")]
    osparc_credits: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="osparcCredits"), pydantic.Field(alias="osparcCredits")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
