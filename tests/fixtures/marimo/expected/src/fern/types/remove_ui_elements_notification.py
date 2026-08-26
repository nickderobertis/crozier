

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cell_id import CellId
from .remove_ui_elements_notification_op import RemoveUiElementsNotificationOp


class RemoveUiElementsNotification(UniversalBaseModel):
    """
    Removes UI elements associated with a cell.

        Sent when cell is re-executed or deleted.

        Attributes:
            cell_id: Cell whose UI elements should be removed.
    """

    cell_id: CellId
    op: RemoveUiElementsNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
