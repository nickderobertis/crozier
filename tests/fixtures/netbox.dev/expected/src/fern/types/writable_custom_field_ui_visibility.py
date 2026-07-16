

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableCustomFieldUiVisibility(str, enum.Enum):
    """
    Specifies the visibility of custom field in the UI
    """

    READ_WRITE = "read-write"
    READ_ONLY = "read-only"
    HIDDEN = "hidden"

    def visit(
        self,
        read_write: typing.Callable[[], T_Result],
        read_only: typing.Callable[[], T_Result],
        hidden: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableCustomFieldUiVisibility.READ_WRITE:
            return read_write()
        if self is WritableCustomFieldUiVisibility.READ_ONLY:
            return read_only()
        if self is WritableCustomFieldUiVisibility.HIDDEN:
            return hidden()
