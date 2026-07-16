

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PayRunStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    POSTED = "POSTED"

    def visit(self, draft: typing.Callable[[], T_Result], posted: typing.Callable[[], T_Result]) -> T_Result:
        if self is PayRunStatus.DRAFT:
            return draft()
        if self is PayRunStatus.POSTED:
            return posted()
