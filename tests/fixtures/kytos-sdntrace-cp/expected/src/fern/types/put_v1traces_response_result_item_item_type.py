

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PutV1TracesResponseResultItemItemType(enum.StrEnum):
    """
    Type of the step. May be "starting", "intermediary", "last", and "loop".
    """

    STARTING = "starting"
    INTERMEDIARY = "intermediary"
    LAST = "last"
    LOOP = "loop"

    def visit(
        self,
        starting: typing.Callable[[], T_Result],
        intermediary: typing.Callable[[], T_Result],
        last: typing.Callable[[], T_Result],
        loop: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutV1TracesResponseResultItemItemType.STARTING:
            return starting()
        if self is PutV1TracesResponseResultItemItemType.INTERMEDIARY:
            return intermediary()
        if self is PutV1TracesResponseResultItemItemType.LAST:
            return last()
        if self is PutV1TracesResponseResultItemItemType.LOOP:
            return loop()
