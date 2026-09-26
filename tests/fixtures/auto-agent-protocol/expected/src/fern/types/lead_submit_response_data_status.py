

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LeadSubmitResponseDataStatus(enum.StrEnum):
    """
    Overall lead status. `duplicate` indicates the dealer recognized the same buyer/vehicle combination from a recent prior submission and merged it. `rejected` indicates the dealer did not accept the lead (e.g. consent invalid, vehicle no longer available, dealer not serving the buyer's region).
    """

    RECEIVED = "received"
    DUPLICATE = "duplicate"
    REJECTED = "rejected"

    def visit(
        self,
        received: typing.Callable[[], T_Result],
        duplicate: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LeadSubmitResponseDataStatus.RECEIVED:
            return received()
        if self is LeadSubmitResponseDataStatus.DUPLICATE:
            return duplicate()
        if self is LeadSubmitResponseDataStatus.REJECTED:
            return rejected()
