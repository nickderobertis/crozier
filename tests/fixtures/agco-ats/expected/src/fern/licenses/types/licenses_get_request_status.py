

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class LicensesGetRequestStatus(enum.StrEnum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    ALL = "All"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LicensesGetRequestStatus.ACTIVE:
            return active()
        if self is LicensesGetRequestStatus.INACTIVE:
            return inactive()
        if self is LicensesGetRequestStatus.ALL:
            return all_()
