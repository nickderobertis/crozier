

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiKeyUsageResponseUsagePeriod(enum.StrEnum):
    LIFETIME = "lifetime"

    def visit(self, lifetime: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiKeyUsageResponseUsagePeriod.LIFETIME:
            return lifetime()
