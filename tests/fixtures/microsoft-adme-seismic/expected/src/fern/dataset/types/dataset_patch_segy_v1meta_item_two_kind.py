

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetPatchSegyV1MetaItemTwoKind(enum.StrEnum):
    """
    The kind of reference, constant 'DateTime', for FrameOfReferenceDateTime.
    """

    DATE_TIME = "DateTime"

    def visit(self, date_time: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetPatchSegyV1MetaItemTwoKind.DATE_TIME:
            return date_time()
