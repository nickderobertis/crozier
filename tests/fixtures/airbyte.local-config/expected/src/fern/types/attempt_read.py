

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attempt_failure_summary import AttemptFailureSummary
from .attempt_stats import AttemptStats
from .attempt_status import AttemptStatus
from .attempt_stream_stats import AttemptStreamStats


class AttemptRead(UniversalBaseModel):
    bytes_synced: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bytesSynced"), pydantic.Field(alias="bytesSynced")
    ] = None
    created_at: typing_extensions.Annotated[int, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    ended_at: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="endedAt"), pydantic.Field(alias="endedAt")
    ] = None
    failure_summary: typing_extensions.Annotated[
        typing.Optional[AttemptFailureSummary],
        FieldMetadata(alias="failureSummary"),
        pydantic.Field(alias="failureSummary"),
    ] = None
    id: int
    records_synced: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="recordsSynced"), pydantic.Field(alias="recordsSynced")
    ] = None
    status: AttemptStatus
    stream_stats: typing_extensions.Annotated[
        typing.Optional[typing.List[AttemptStreamStats]],
        FieldMetadata(alias="streamStats"),
        pydantic.Field(alias="streamStats"),
    ] = None
    total_stats: typing_extensions.Annotated[
        typing.Optional[AttemptStats], FieldMetadata(alias="totalStats"), pydantic.Field(alias="totalStats")
    ] = None
    updated_at: typing_extensions.Annotated[int, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
