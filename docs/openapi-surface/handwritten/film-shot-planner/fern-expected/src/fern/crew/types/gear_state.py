

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GearState(enum.StrEnum):
    PACKED = "packed"
    MISSING = "missing"

    def visit(self, packed: typing.Callable[[], T_Result], missing: typing.Callable[[], T_Result]) -> T_Result:
        if self is GearState.PACKED:
            return packed()
        if self is GearState.MISSING:
            return missing()
