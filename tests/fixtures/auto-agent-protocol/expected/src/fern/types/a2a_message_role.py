

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class A2AMessageRole(enum.StrEnum):
    ROLE_USER = "ROLE_USER"
    ROLE_AGENT = "ROLE_AGENT"

    def visit(self, role_user: typing.Callable[[], T_Result], role_agent: typing.Callable[[], T_Result]) -> T_Result:
        if self is A2AMessageRole.ROLE_USER:
            return role_user()
        if self is A2AMessageRole.ROLE_AGENT:
            return role_agent()
