

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FourHundredFourDetailsItemIssue(enum.StrEnum):
    INVALID_RESOURCE_ID = "INVALID_RESOURCE_ID"

    def visit(self, invalid_resource_id: typing.Callable[[], T_Result]) -> T_Result:
        if self is FourHundredFourDetailsItemIssue.INVALID_RESOURCE_ID:
            return invalid_resource_id()
