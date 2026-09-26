

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_job_state_status import V2TableJobStateStatus
from .v2table_job_state_type import V2TableJobStateType


class V2TableJobState(UniversalBaseModel):
    """
    Current background work associated with a table.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Background job identifier, or null when unavailable.
    """

    type: typing.Optional[V2TableJobStateType] = pydantic.Field(default=None)
    """
    Kind of background table work.
    """

    status: V2TableJobStateStatus = pydantic.Field()
    """
    Current background job state.
    """

    rows_processed: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="rowsProcessed"),
        pydantic.Field(alias="rowsProcessed", description="Number of rows processed by the job."),
    ]
    """
    Number of rows processed by the job.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Failure reason, or null when the job has not failed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
