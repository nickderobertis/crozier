

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_run_dispatch_limit import V2TableRunDispatchLimit
from .v2table_run_dispatch_mode import V2TableRunDispatchMode
from .v2table_run_dispatch_scope import V2TableRunDispatchScope
from .v2table_run_dispatch_status import V2TableRunDispatchStatus


class V2TableRunDispatch(UniversalBaseModel):
    """
    Lifecycle state of one table workflow-column run dispatch.
    """

    id: str = pydantic.Field()
    """
    Unique dispatch identifier.
    """

    table_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tableId"),
        pydantic.Field(alias="tableId", description="Table the dispatch runs against."),
    ]
    """
    Table the dispatch runs against.
    """

    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="Workspace that owns the dispatch."),
    ]
    """
    Workspace that owns the dispatch.
    """

    status: V2TableRunDispatchStatus = pydantic.Field()
    """
    Current dispatch lifecycle state.
    """

    mode: V2TableRunDispatchMode = pydantic.Field()
    """
    Which cells the dispatch targets: `all` re-runs settled cells, `incomplete` skips them, `new` covers only cells that have never run.
    """

    scope: V2TableRunDispatchScope = pydantic.Field()
    """
    What the dispatch was asked to run.
    """

    limit: typing.Optional[V2TableRunDispatchLimit] = pydantic.Field(default=None)
    """
    Cap on how much work the dispatch does, or null when unbounded.
    """

    processed_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="processedCount"),
        pydantic.Field(alias="processedCount", description="Units of `limit.type` consumed so far."),
    ]
    """
    Units of `limit.type` consumed so far.
    """

    is_manual_run: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isManualRun"),
        pydantic.Field(
            alias="isManualRun", description="True when a caller started the run, false for an automatic re-fire."
        ),
    ]
    """
    True when a caller started the run, false for an automatic re-fire.
    """

    requested_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="requestedAt"),
        pydantic.Field(alias="requestedAt", description="ISO 8601 timestamp when the dispatch was created."),
    ]
    """
    ISO 8601 timestamp when the dispatch was created.
    """

    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completedAt"),
        pydantic.Field(alias="completedAt", description="ISO 8601 timestamp when the dispatch completed, or null."),
    ] = None
    """
    ISO 8601 timestamp when the dispatch completed, or null.
    """

    canceled_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="canceledAt"),
        pydantic.Field(alias="canceledAt", description="ISO 8601 timestamp when the dispatch was canceled, or null."),
    ] = None
    """
    ISO 8601 timestamp when the dispatch was canceled, or null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
