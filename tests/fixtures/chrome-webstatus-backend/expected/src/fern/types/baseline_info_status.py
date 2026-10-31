

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BaselineInfoStatus(enum.StrEnum):
    LIMITED = "limited"
    NEWLY = "newly"
    WIDELY = "widely"

    def visit(
        self,
        limited: typing.Callable[[], T_Result],
        newly: typing.Callable[[], T_Result],
        widely: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BaselineInfoStatus.LIMITED:
            return limited()
        if self is BaselineInfoStatus.NEWLY:
            return newly()
        if self is BaselineInfoStatus.WIDELY:
            return widely()
