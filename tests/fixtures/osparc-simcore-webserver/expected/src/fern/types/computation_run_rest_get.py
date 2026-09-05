

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .running_state import RunningState


class ComputationRunRestGet(UniversalBaseModel):
    project_uuid: typing_extensions.Annotated[
        str, FieldMetadata(alias="projectUuid"), pydantic.Field(alias="projectUuid")
    ]
    iteration: int
    state: RunningState
    info: typing.Dict[str, typing.Any]
    submitted_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="submittedAt"), pydantic.Field(alias="submittedAt")
    ]
    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    ended_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endedAt"), pydantic.Field(alias="endedAt")
    ] = None
    root_project_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="rootProjectName"), pydantic.Field(alias="rootProjectName")
    ]
    project_custom_metadata: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="projectCustomMetadata"),
        pydantic.Field(alias="projectCustomMetadata"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
