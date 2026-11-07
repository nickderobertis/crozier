

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VaultConnectionListConnectionsItemResolutionMode(enum.StrEnum):
    JUST_IN_TIME = "just_in_time"

    def visit(self, just_in_time: typing.Callable[[], T_Result]) -> T_Result:
        if self is VaultConnectionListConnectionsItemResolutionMode.JUST_IN_TIME:
            return just_in_time()
