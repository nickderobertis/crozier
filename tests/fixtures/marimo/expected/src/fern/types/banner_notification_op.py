

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BannerNotificationOp(enum.StrEnum):
    BANNER = "banner"

    def visit(self, banner: typing.Callable[[], T_Result]) -> T_Result:
        if self is BannerNotificationOp.BANNER:
            return banner()
