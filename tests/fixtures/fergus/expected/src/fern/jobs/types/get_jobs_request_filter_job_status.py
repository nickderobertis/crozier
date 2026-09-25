

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJobsRequestFilterJobStatus(enum.StrEnum):
    ACTIVE = "Active"
    COMPLETED = "Completed"
    ESTIMATE_REJECTED = "Estimate Rejected"
    ESTIMATE_SENT = "Estimate Sent"
    INACTIVE = "Inactive"
    QUOTE_SENT = "Quote Sent"
    QUOTE_REJECTED = "Quote Rejected"
    TO_PRICE = "To Price"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        estimate_rejected: typing.Callable[[], T_Result],
        estimate_sent: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        quote_sent: typing.Callable[[], T_Result],
        quote_rejected: typing.Callable[[], T_Result],
        to_price: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetJobsRequestFilterJobStatus.ACTIVE:
            return active()
        if self is GetJobsRequestFilterJobStatus.COMPLETED:
            return completed()
        if self is GetJobsRequestFilterJobStatus.ESTIMATE_REJECTED:
            return estimate_rejected()
        if self is GetJobsRequestFilterJobStatus.ESTIMATE_SENT:
            return estimate_sent()
        if self is GetJobsRequestFilterJobStatus.INACTIVE:
            return inactive()
        if self is GetJobsRequestFilterJobStatus.QUOTE_SENT:
            return quote_sent()
        if self is GetJobsRequestFilterJobStatus.QUOTE_REJECTED:
            return quote_rejected()
        if self is GetJobsRequestFilterJobStatus.TO_PRICE:
            return to_price()
