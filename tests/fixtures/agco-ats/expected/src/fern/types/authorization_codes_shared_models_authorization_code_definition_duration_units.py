

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits(enum.StrEnum):
    """
    The units of duration used to calculate the Authorization Code. Defaults to 'Days'. May not be updated.
    """

    WEEKS = "Weeks"
    DAYS = "Days"
    HOURS = "Hours"
    MINUTES = "Minutes"

    def visit(
        self,
        weeks: typing.Callable[[], T_Result],
        days: typing.Callable[[], T_Result],
        hours: typing.Callable[[], T_Result],
        minutes: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits.WEEKS:
            return weeks()
        if self is AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits.DAYS:
            return days()
        if self is AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits.HOURS:
            return hours()
        if self is AuthorizationCodesSharedModelsAuthorizationCodeDefinitionDurationUnits.MINUTES:
            return minutes()
