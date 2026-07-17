

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListStackSetsRequestStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListStackSetsRequestStatus.ACTIVE:
            return active()
        if self is GetListStackSetsRequestStatus.DELETED:
            return deleted()
