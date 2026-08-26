

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .active_line_notification_op import ActiveLineNotificationOp
from .cell_id import CellId


class ActiveLineNotification(UniversalBaseModel):
    """
    Reports the line a cell's frame watcher is currently executing.

        Emitted on a timed heartbeat while a cell runs (only when the line
        changed), so the editor can highlight the live line. A `None` line
        clears the highlight (e.g. when the cell finishes).

        Attributes:
            cell_id: Cell whose frame is being watched.
            line: 1-based line within the cell, or `None` to clear.
    """

    cell_id: CellId
    line: typing.Optional[int] = None
    op: ActiveLineNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
