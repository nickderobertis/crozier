

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelType(enum.StrEnum):
    EMAIL = "EMAIL"
    WEBHOOK = "WEBHOOK"

    def visit(self, email: typing.Callable[[], T_Result], webhook: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChannelType.EMAIL:
            return email()
        if self is ChannelType.WEBHOOK:
            return webhook()
