

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListExperimentsResponseExperimentsItemStopReasonThree(enum.StrEnum):
    EXTERNAL_STOP = "external_stop"

    def visit(self, external_stop: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListExperimentsResponseExperimentsItemStopReasonThree.EXTERNAL_STOP:
            return external_stop()
