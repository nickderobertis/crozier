

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MemberState(enum.StrEnum):
    """
    The state that the member is in. Possible values are `invited`, `joined`, `left`, or `unknown`
    """

    INVITED = "invited"
    JOINED = "joined"
    LEFT = "left"
    UNKNOWN = "unknown"

    def visit(
        self,
        invited: typing.Callable[[], T_Result],
        joined: typing.Callable[[], T_Result],
        left: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MemberState.INVITED:
            return invited()
        if self is MemberState.JOINED:
            return joined()
        if self is MemberState.LEFT:
            return left()
        if self is MemberState.UNKNOWN:
            return unknown()
