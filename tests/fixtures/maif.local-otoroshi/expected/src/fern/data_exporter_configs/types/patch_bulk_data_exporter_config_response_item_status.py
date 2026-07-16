

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PatchBulkDataExporterConfigResponseItemStatus(str, enum.Enum):
    """
    Status
    """

    TWO_HUNDRED = "200"

    def visit(self, two_hundred: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchBulkDataExporterConfigResponseItemStatus.TWO_HUNDRED:
            return two_hundred()
