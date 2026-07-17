

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateBulkDataExporterConfigsResponseItemStatus(enum.StrEnum):
    """
    Status
    """

    TWO_HUNDRED_ONE = "201"

    def visit(self, two_hundred_one: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateBulkDataExporterConfigsResponseItemStatus.TWO_HUNDRED_ONE:
            return two_hundred_one()
