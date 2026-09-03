

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FapiConfigurationFapiComplianceLevel(enum.StrEnum):
    FULL = "full"
    PARTIAL = "partial"

    def visit(self, full: typing.Callable[[], T_Result], partial: typing.Callable[[], T_Result]) -> T_Result:
        if self is FapiConfigurationFapiComplianceLevel.FULL:
            return full()
        if self is FapiConfigurationFapiComplianceLevel.PARTIAL:
            return partial()
