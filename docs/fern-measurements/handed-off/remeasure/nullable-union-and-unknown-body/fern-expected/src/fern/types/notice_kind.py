

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoticeKind(enum.StrEnum):
    NOTICE = "notice"

    def visit(self, notice: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoticeKind.NOTICE:
            return notice()
