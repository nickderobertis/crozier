

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CapabilityPaymentRequirementMode(enum.StrEnum):
    FREE = "free"
    FIXED = "fixed"
    QUOTE = "quote"
    USAGE = "usage"

    def visit(
        self,
        free: typing.Callable[[], T_Result],
        fixed: typing.Callable[[], T_Result],
        quote: typing.Callable[[], T_Result],
        usage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CapabilityPaymentRequirementMode.FREE:
            return free()
        if self is CapabilityPaymentRequirementMode.FIXED:
            return fixed()
        if self is CapabilityPaymentRequirementMode.QUOTE:
            return quote()
        if self is CapabilityPaymentRequirementMode.USAGE:
            return usage()
