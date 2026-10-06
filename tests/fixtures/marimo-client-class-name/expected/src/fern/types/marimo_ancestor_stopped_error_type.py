

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoAncestorStoppedErrorType(enum.StrEnum):
    ANCESTOR_STOPPED = "ancestor-stopped"

    def visit(self, ancestor_stopped: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoAncestorStoppedErrorType.ANCESTOR_STOPPED:
            return ancestor_stopped()
