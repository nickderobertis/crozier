

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BuyPhoneNumberRequestInboundAgentTwo(enum.StrEnum):
    DEFAULT = "default"

    def visit(self, default: typing.Callable[[], T_Result]) -> T_Result:
        if self is BuyPhoneNumberRequestInboundAgentTwo.DEFAULT:
            return default()
