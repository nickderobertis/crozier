

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Channel(enum.StrEnum):
    """
    Defines the supported notification channels.
    This is used to route messages to the appropriate handlers and templates.
    """

    EMAIL = "email"

    def visit(self, email: typing.Callable[[], T_Result]) -> T_Result:
        if self is Channel.EMAIL:
            return email()
