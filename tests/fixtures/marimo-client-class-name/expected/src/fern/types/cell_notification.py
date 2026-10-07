

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_id import CellId
from .cell_notification_console import CellNotificationConsole
from .cell_notification_op import CellNotificationOp
from .cell_notification_status import CellNotificationStatus
from .cell_output import CellOutput


class CellNotification(UniversalBaseModel):
    """
    Updates a cell's state in the frontend.

        This is a partial update: each field carries its own "unchanged" semantics,
        documented per field below. Most fields treat None as "unchanged"; fields
        that need to distinguish "unchanged" from "clear" use msgspec.UNSET for the
        former and None for the latter.

        Attributes:
            cell_id: Unique identifier of the cell being updated.
            output: Cell's output. Use CellOutput.empty() to clear.
            console: Console messages. Single/list appends, [] clears, None unchanged.
            status: Execution status (idle/running/stale/queued/disabled-transitively).
            stale_inputs: Whether cell has stale inputs from changed dependencies.
            run_id: Execution run ID for tracing. Auto-set from context.
            serialization: Top-level reusability hint. UNSET unchanged, None clears, str sets.
            timestamp: Creation timestamp, auto-set.
    """

    cell_id: CellId
    console: typing.Optional[CellNotificationConsole] = None
    op: CellNotificationOp
    output: typing.Optional[CellOutput] = None
    run_id: typing.Optional[str] = None
    serialization: typing.Optional[str] = None
    stale_inputs: typing.Optional[bool] = None
    status: typing.Optional[CellNotificationStatus] = None
    timestamp: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
