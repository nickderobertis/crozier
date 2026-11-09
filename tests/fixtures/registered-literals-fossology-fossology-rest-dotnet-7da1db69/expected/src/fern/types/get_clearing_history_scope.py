

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetClearingHistoryScope(enum.StrEnum):
    """
    Scope of the clearing
    """

    LOCAL = "local"
    PACKAGE = "package"
    GLOBAL = "global"

    def visit(
        self,
        local: typing.Callable[[], T_Result],
        package: typing.Callable[[], T_Result],
        global_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetClearingHistoryScope.LOCAL:
            return local()
        if self is GetClearingHistoryScope.PACKAGE:
            return package()
        if self is GetClearingHistoryScope.GLOBAL:
            return global_()
