

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubscriptionCadence(enum.StrEnum):
    """
    Determines the billing cadence of a [Subscription](https://developer.squareup.com/reference/square_2021-08-18/objects/Subscription)
    """

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    EVERY_TWO_WEEKS = "EVERY_TWO_WEEKS"
    THIRTY_DAYS = "THIRTY_DAYS"
    SIXTY_DAYS = "SIXTY_DAYS"
    NINETY_DAYS = "NINETY_DAYS"
    MONTHLY = "MONTHLY"
    EVERY_TWO_MONTHS = "EVERY_TWO_MONTHS"
    QUARTERLY = "QUARTERLY"
    EVERY_FOUR_MONTHS = "EVERY_FOUR_MONTHS"
    EVERY_SIX_MONTHS = "EVERY_SIX_MONTHS"
    ANNUAL = "ANNUAL"
    EVERY_TWO_YEARS = "EVERY_TWO_YEARS"

    def visit(
        self,
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        every_two_weeks: typing.Callable[[], T_Result],
        thirty_days: typing.Callable[[], T_Result],
        sixty_days: typing.Callable[[], T_Result],
        ninety_days: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        every_two_months: typing.Callable[[], T_Result],
        quarterly: typing.Callable[[], T_Result],
        every_four_months: typing.Callable[[], T_Result],
        every_six_months: typing.Callable[[], T_Result],
        annual: typing.Callable[[], T_Result],
        every_two_years: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionCadence.DAILY:
            return daily()
        if self is SubscriptionCadence.WEEKLY:
            return weekly()
        if self is SubscriptionCadence.EVERY_TWO_WEEKS:
            return every_two_weeks()
        if self is SubscriptionCadence.THIRTY_DAYS:
            return thirty_days()
        if self is SubscriptionCadence.SIXTY_DAYS:
            return sixty_days()
        if self is SubscriptionCadence.NINETY_DAYS:
            return ninety_days()
        if self is SubscriptionCadence.MONTHLY:
            return monthly()
        if self is SubscriptionCadence.EVERY_TWO_MONTHS:
            return every_two_months()
        if self is SubscriptionCadence.QUARTERLY:
            return quarterly()
        if self is SubscriptionCadence.EVERY_FOUR_MONTHS:
            return every_four_months()
        if self is SubscriptionCadence.EVERY_SIX_MONTHS:
            return every_six_months()
        if self is SubscriptionCadence.ANNUAL:
            return annual()
        if self is SubscriptionCadence.EVERY_TWO_YEARS:
            return every_two_years()
