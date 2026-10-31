

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobInputStatus(enum.StrEnum):
    PENDING = "pending"
    INTERVIEW = "interview"
    DECLINED = "declined"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        interview: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobInputStatus.PENDING:
            return pending()
        if self is JobInputStatus.INTERVIEW:
            return interview()
        if self is JobInputStatus.DECLINED:
            return declined()
