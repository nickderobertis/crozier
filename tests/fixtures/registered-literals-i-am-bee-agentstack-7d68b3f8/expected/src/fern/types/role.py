

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Role(enum.StrEnum):
    """
    Identifies the sender of the message. `user` for the client, `agent` for the service.
    """

    AGENT = "agent"
    USER = "user"

    def visit(self, agent: typing.Callable[[], T_Result], user: typing.Callable[[], T_Result]) -> T_Result:
        if self is Role.AGENT:
            return agent()
        if self is Role.USER:
            return user()
