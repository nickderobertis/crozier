

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeletebulkDataExporterConfigResponseItemStatus(str, enum.Enum):
    """
    Status
    """

    TWO_HUNDRED = "200"

    def visit(self, two_hundred: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeletebulkDataExporterConfigResponseItemStatus.TWO_HUNDRED:
            return two_hundred()
