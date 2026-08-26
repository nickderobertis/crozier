

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReloadNotificationOp(enum.StrEnum):
    RELOAD = "reload"

    def visit(self, reload: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReloadNotificationOp.RELOAD:
            return reload()
