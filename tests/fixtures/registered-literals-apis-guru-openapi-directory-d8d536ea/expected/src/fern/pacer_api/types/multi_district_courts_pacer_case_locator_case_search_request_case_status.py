

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus(enum.StrEnum):
    OPEN = "open"
    CLOSED = "closed"

    def visit(self, open: typing.Callable[[], T_Result], closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus.OPEN:
            return open()
        if self is MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus.CLOSED:
            return closed()
