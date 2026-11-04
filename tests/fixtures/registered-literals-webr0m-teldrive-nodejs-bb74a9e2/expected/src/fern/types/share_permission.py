

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SharePermission(enum.StrEnum):
    READ = "read"
    EDIT = "edit"

    def visit(self, read: typing.Callable[[], T_Result], edit: typing.Callable[[], T_Result]) -> T_Result:
        if self is SharePermission.READ:
            return read()
        if self is SharePermission.EDIT:
            return edit()
