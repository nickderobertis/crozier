

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataColumnPreviewNotificationOp(enum.StrEnum):
    DATA_COLUMN_PREVIEW = "data-column-preview"

    def visit(self, data_column_preview: typing.Callable[[], T_Result]) -> T_Result:
        if self is DataColumnPreviewNotificationOp.DATA_COLUMN_PREVIEW:
            return data_column_preview()
