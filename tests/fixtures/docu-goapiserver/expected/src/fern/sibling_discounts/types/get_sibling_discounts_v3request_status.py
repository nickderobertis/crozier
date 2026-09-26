

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSiblingDiscountsV3RequestStatus(enum.StrEnum):
    ACTIVE = "active"
    HOLD = "hold"

    def visit(self, active: typing.Callable[[], T_Result], hold: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetSiblingDiscountsV3RequestStatus.ACTIVE:
            return active()
        if self is GetSiblingDiscountsV3RequestStatus.HOLD:
            return hold()
