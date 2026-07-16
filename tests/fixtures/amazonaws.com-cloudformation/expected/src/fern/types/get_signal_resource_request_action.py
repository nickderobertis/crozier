

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetSignalResourceRequestAction(str, enum.Enum):
    SIGNAL_RESOURCE = "SignalResource"

    def visit(self, signal_resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetSignalResourceRequestAction.SIGNAL_RESOURCE:
            return signal_resource()
