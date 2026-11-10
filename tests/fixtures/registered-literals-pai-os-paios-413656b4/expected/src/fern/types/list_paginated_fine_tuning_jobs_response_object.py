

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListPaginatedFineTuningJobsResponseObject(enum.StrEnum):
    LIST = "list"

    def visit(self, list_: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListPaginatedFineTuningJobsResponseObject.LIST:
            return list_()
