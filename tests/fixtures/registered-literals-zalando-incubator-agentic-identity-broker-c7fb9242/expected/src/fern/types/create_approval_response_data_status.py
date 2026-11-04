

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateApprovalResponseDataStatus(enum.StrEnum):
    PENDING = "pending"

    def visit(self, pending: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateApprovalResponseDataStatus.PENDING:
            return pending()
