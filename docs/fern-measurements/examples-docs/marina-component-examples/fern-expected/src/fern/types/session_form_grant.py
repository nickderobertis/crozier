

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionFormGrant(enum.StrEnum):
    HARBOUR_PASS = "harbour_pass"
    REFRESH = "refresh"

    def visit(self, harbour_pass: typing.Callable[[], T_Result], refresh: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionFormGrant.HARBOUR_PASS:
            return harbour_pass()
        if self is SessionFormGrant.REFRESH:
            return refresh()
