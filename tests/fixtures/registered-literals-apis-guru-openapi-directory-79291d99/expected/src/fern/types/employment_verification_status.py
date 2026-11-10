

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmploymentVerificationStatus(enum.StrEnum):
    """
    Current employment status.
    """

    EMPLOYMENT_STATUS_ACTIVE = "EMPLOYMENT_STATUS_ACTIVE"
    EMPLOYMENT_STATUS_INACTIVE = "EMPLOYMENT_STATUS_INACTIVE"

    def visit(
        self,
        employment_status_active: typing.Callable[[], T_Result],
        employment_status_inactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmploymentVerificationStatus.EMPLOYMENT_STATUS_ACTIVE:
            return employment_status_active()
        if self is EmploymentVerificationStatus.EMPLOYMENT_STATUS_INACTIVE:
            return employment_status_inactive()
