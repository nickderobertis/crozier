

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BannerNotificationAction(enum.StrEnum):
    RESTART = "restart"

    def visit(self, restart: typing.Callable[[], T_Result]) -> T_Result:
        if self is BannerNotificationAction.RESTART:
            return restart()
