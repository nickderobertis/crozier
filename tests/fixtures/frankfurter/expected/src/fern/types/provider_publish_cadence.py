

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderPublishCadence(enum.StrEnum):
    """
    How often the provider publishes rates. Determines the unit of publishes_missed: a count of days, ISO weeks, or calendar months. Null for historical-only providers with no scheduled cadence.
    """

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    def visit(
        self,
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderPublishCadence.DAILY:
            return daily()
        if self is ProviderPublishCadence.WEEKLY:
            return weekly()
        if self is ProviderPublishCadence.MONTHLY:
            return monthly()
