

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoAncestorPreventedErrorType(enum.StrEnum):
    ANCESTOR_PREVENTED = "ancestor-prevented"

    def visit(self, ancestor_prevented: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoAncestorPreventedErrorType.ANCESTOR_PREVENTED:
            return ancestor_prevented()
