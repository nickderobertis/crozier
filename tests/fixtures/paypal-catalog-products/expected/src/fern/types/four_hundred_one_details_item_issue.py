

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FourHundredOneDetailsItemIssue(enum.StrEnum):
    INVALID_ACCOUNT_STATUS = "INVALID_ACCOUNT_STATUS"

    def visit(self, invalid_account_status: typing.Callable[[], T_Result]) -> T_Result:
        if self is FourHundredOneDetailsItemIssue.INVALID_ACCOUNT_STATUS:
            return invalid_account_status()
