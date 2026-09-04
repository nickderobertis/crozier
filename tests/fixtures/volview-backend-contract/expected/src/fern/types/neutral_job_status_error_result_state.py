

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NeutralJobStatusErrorResultState(enum.StrEnum):
    UNAVAILABLE = "unavailable"

    def visit(self, unavailable: typing.Callable[[], T_Result]) -> T_Result:
        if self is NeutralJobStatusErrorResultState.UNAVAILABLE:
            return unavailable()
