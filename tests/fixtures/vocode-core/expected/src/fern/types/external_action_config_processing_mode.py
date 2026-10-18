

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExternalActionConfigProcessingMode(enum.StrEnum):
    MUTED = "muted"

    def visit(self, muted: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExternalActionConfigProcessingMode.MUTED:
            return muted()
