

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchBulkDataExporterConfigResponseItemStatus(enum.StrEnum):
    """
    Status
    """

    TWO_HUNDRED = "200"

    def visit(self, two_hundred: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchBulkDataExporterConfigResponseItemStatus.TWO_HUNDRED:
            return two_hundred()
