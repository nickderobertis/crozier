

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1GetJitAccessConfigResponseUnavailableReasonState(enum.StrEnum):
    UNAVAILABLE = "unavailable"

    def visit(self, unavailable: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1GetJitAccessConfigResponseUnavailableReasonState.UNAVAILABLE:
            return unavailable()
