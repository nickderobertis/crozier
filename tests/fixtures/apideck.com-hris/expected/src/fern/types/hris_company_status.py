

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HrisCompanyStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    TRIAL = "trial"
    OTHER = "other"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        trial: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HrisCompanyStatus.ACTIVE:
            return active()
        if self is HrisCompanyStatus.INACTIVE:
            return inactive()
        if self is HrisCompanyStatus.TRIAL:
            return trial()
        if self is HrisCompanyStatus.OTHER:
            return other()
