

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferIntentCreateNetwork(enum.StrEnum):
    """
    The network or rails used for the transfer. Defaults to `same-day-ach`.

    For transfers submitted as either `ach` or `same-day-ach` the cutoff for same-day is 9:30 AM Pacific Time and the cutoff for next-day transfers is 5:30 PM Pacific Time. It is recommended to submit a transfer at least 15 minutes before the cutoff time in order to ensure that it will be processed before the cutoff. Any transfer that is indicated as `same-day-ach` and that misses the same-day cutoff, but is submitted in time for the next-day cutoff, will be sent over next-day rails and will not incur same-day charges. Note that both legs of the transfer will be downgraded if applicable.
    """

    ACH = "ach"
    SAME_DAY_ACH = "same-day-ach"

    def visit(self, ach: typing.Callable[[], T_Result], same_day_ach: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransferIntentCreateNetwork.ACH:
            return ach()
        if self is TransferIntentCreateNetwork.SAME_DAY_ACH:
            return same_day_ach()
