

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostSignalResourceRequestAction(enum.StrEnum):
    SIGNAL_RESOURCE = "SignalResource"

    def visit(self, signal_resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSignalResourceRequestAction.SIGNAL_RESOURCE:
            return signal_resource()
