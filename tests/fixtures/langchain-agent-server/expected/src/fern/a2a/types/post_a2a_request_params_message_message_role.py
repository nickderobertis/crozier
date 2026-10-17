

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostA2ARequestParamsMessageMessageRole(enum.StrEnum):
    """
    A2A role for the message sender.
    """

    USER = "user"
    AGENT = "agent"

    def visit(self, user: typing.Callable[[], T_Result], agent: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostA2ARequestParamsMessageMessageRole.USER:
            return user()
        if self is PostA2ARequestParamsMessageMessageRole.AGENT:
            return agent()
