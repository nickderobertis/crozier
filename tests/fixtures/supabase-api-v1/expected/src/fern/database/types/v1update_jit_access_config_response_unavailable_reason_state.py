

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1UpdateJitAccessConfigResponseUnavailableReasonState(enum.StrEnum):
    UNAVAILABLE = "unavailable"

    def visit(self, unavailable: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1UpdateJitAccessConfigResponseUnavailableReasonState.UNAVAILABLE:
            return unavailable()
