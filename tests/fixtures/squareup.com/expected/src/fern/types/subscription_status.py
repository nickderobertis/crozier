

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SubscriptionStatus(str, enum.Enum):
    """
    Possible subscription status values.
    """

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    CANCELED = "CANCELED"
    DEACTIVATED = "DEACTIVATED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        deactivated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionStatus.PENDING:
            return pending()
        if self is SubscriptionStatus.ACTIVE:
            return active()
        if self is SubscriptionStatus.CANCELED:
            return canceled()
        if self is SubscriptionStatus.DEACTIVATED:
            return deactivated()
