

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2TableRowRunState(UniversalBaseModel):
    """
    Run outcome for one workflow group on one row.
    """

    status: str = pydantic.Field()
    """
    Lifecycle state of the most recent run for this cell: `pending`, `queued`, `running`, `completed`, `error`, or `canceled`.
    """

    execution_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="executionId"),
        pydantic.Field(
            alias="executionId", description="Workflow execution identifier, or null before a worker claimed the cell."
        ),
    ] = None
    """
    Workflow execution identifier, or null before a worker claimed the cell.
    """

    workflow_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflowId"),
        pydantic.Field(alias="workflowId", description="Workflow the group runs for this cell."),
    ]
    """
    Workflow the group runs for this cell.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Failure reason, or null when the run did not fail.
    """

    running_block_ids: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="runningBlockIds"),
        pydantic.Field(alias="runningBlockIds", description="Block identifiers currently mid-execution."),
    ]
    """
    Block identifiers currently mid-execution.
    """

    block_errors: typing_extensions.Annotated[
        typing.Dict[str, str],
        FieldMetadata(alias="blockErrors"),
        pydantic.Field(alias="blockErrors", description="Per-block failure messages keyed by block identifier."),
    ]
    """
    Per-block failure messages keyed by block identifier.
    """

    canceled_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="canceledAt"),
        pydantic.Field(alias="canceledAt", description="ISO 8601 timestamp when the cell was canceled, or null."),
    ] = None
    """
    ISO 8601 timestamp when the cell was canceled, or null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
