

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .running_state import RunningState


class ComputationCollectionRunRestGet(UniversalBaseModel):
    collection_run_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="collectionRunId"), pydantic.Field(alias="collectionRunId")
    ]
    project_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="projectIds"), pydantic.Field(alias="projectIds")
    ]
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
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
