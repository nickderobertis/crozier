

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrgTokenStatus(enum.StrEnum):
    ACTIVE = "active"
    REVOKED = "revoked"

    def visit(self, active: typing.Callable[[], T_Result], revoked: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrgTokenStatus.ACTIVE:
            return active()
        if self is OrgTokenStatus.REVOKED:
            return revoked()
