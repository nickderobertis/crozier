

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_id import CellId
from .focus_cell_notification_op import FocusCellNotificationOp


class FocusCellNotification(UniversalBaseModel):
    """
    Focuses a cell (kiosk mode).

        Attributes:
            cell_id: Cell to focus.
    """

    cell_id: CellId
    op: FocusCellNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
