

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus(enum.StrEnum):
    OPEN = "open"
    CLOSED = "closed"

    def visit(self, open: typing.Callable[[], T_Result], closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus.OPEN:
            return open()
        if self is CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus.CLOSED:
            return closed()
