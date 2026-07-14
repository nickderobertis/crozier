

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListUsersPublicRequestPeriod(str, enum.Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"
    ALL = "all"

    def visit(
        self,
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        quarterly: typing.Callable[[], T_Result],
        yearly: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListUsersPublicRequestPeriod.DAILY:
            return daily()
        if self is ListUsersPublicRequestPeriod.WEEKLY:
            return weekly()
        if self is ListUsersPublicRequestPeriod.MONTHLY:
            return monthly()
        if self is ListUsersPublicRequestPeriod.QUARTERLY:
            return quarterly()
        if self is ListUsersPublicRequestPeriod.YEARLY:
            return yearly()
        if self is ListUsersPublicRequestPeriod.ALL:
            return all_()
