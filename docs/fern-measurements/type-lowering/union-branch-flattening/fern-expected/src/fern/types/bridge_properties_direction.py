

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BridgePropertiesDirection(enum.StrEnum):
    BRIDGE = "Bridge"

    def visit(self, bridge: typing.Callable[[], T_Result]) -> T_Result:
        if self is BridgePropertiesDirection.BRIDGE:
            return bridge()
