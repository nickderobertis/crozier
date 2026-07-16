

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreateBulkDataExporterConfigsResponseItemStatus(str, enum.Enum):
    """
    Status
    """

    TWO_HUNDRED_ONE = "201"

    def visit(self, two_hundred_one: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateBulkDataExporterConfigsResponseItemStatus.TWO_HUNDRED_ONE:
            return two_hundred_one()
