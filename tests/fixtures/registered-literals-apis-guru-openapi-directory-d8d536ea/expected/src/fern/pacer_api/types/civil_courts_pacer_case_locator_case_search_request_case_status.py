

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus(enum.StrEnum):
    OPEN = "open"
    CLOSED = "closed"

    def visit(self, open: typing.Callable[[], T_Result], closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus.OPEN:
            return open()
        if self is CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus.CLOSED:
            return closed()
