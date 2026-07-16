

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CustomFieldUiVisibilityLabel(str, enum.Enum):
    READ_WRITE = "Read/Write"
    READ_ONLY = "Read-only"
    HIDDEN = "Hidden"

    def visit(
        self,
        read_write: typing.Callable[[], T_Result],
        read_only: typing.Callable[[], T_Result],
        hidden: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomFieldUiVisibilityLabel.READ_WRITE:
            return read_write()
        if self is CustomFieldUiVisibilityLabel.READ_ONLY:
            return read_only()
        if self is CustomFieldUiVisibilityLabel.HIDDEN:
            return hidden()
