

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecurringTransactionFrequency(enum.StrEnum):
    """
    Describes the frequency of the transaction stream.

    `WEEKLY`: Assigned to a transaction stream that occurs approximately every week.

    `BIWEEKLY`: Assigned to a transaction stream that occurs approximately every 2 weeks.

    `SEMI_MONTHLY`: Assigned to a transaction stream that occurs approximately twice per month. This frequency is typically seen for inflow transaction streams.

    `MONTHLY`: Assigned to a transaction stream that occurs approximately every month.

    `ANNUALLY`: Assigned to a transaction stream that occurs approximately every year.

    `UNKNOWN`: Assigned to a transaction stream that does not fit any of the pre-defined frequencies.
    """

    UNKNOWN = "UNKNOWN"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    SEMI_MONTHLY = "SEMI_MONTHLY"
    MONTHLY = "MONTHLY"
    ANNUALLY = "ANNUALLY"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        biweekly: typing.Callable[[], T_Result],
        semi_monthly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        annually: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RecurringTransactionFrequency.UNKNOWN:
            return unknown()
        if self is RecurringTransactionFrequency.WEEKLY:
            return weekly()
        if self is RecurringTransactionFrequency.BIWEEKLY:
            return biweekly()
        if self is RecurringTransactionFrequency.SEMI_MONTHLY:
            return semi_monthly()
        if self is RecurringTransactionFrequency.MONTHLY:
            return monthly()
        if self is RecurringTransactionFrequency.ANNUALLY:
            return annually()
