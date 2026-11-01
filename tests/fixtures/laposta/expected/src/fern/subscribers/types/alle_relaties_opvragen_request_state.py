

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AlleRelatiesOpvragenRequestState(enum.StrEnum):
    ACTIVE = "active"
    DELETED = "deleted"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlleRelatiesOpvragenRequestState.ACTIVE:
            return active()
        if self is AlleRelatiesOpvragenRequestState.DELETED:
            return deleted()
