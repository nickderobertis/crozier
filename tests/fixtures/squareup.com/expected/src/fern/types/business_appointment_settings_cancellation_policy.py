

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BusinessAppointmentSettingsCancellationPolicy(enum.StrEnum):
    """
    The category of the seller’s cancellation policy.
    """

    CANCELLATION_TREATED_AS_NO_SHOW = "CANCELLATION_TREATED_AS_NO_SHOW"
    CUSTOM_POLICY = "CUSTOM_POLICY"

    def visit(
        self,
        cancellation_treated_as_no_show: typing.Callable[[], T_Result],
        custom_policy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BusinessAppointmentSettingsCancellationPolicy.CANCELLATION_TREATED_AS_NO_SHOW:
            return cancellation_treated_as_no_show()
        if self is BusinessAppointmentSettingsCancellationPolicy.CUSTOM_POLICY:
            return custom_policy()
