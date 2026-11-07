

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelProviderState(enum.StrEnum):
    ONLINE = "online"
    OFFLINE = "offline"

    def visit(self, online: typing.Callable[[], T_Result], offline: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelProviderState.ONLINE:
            return online()
        if self is ModelProviderState.OFFLINE:
            return offline()
