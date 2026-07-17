

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaxRateStatus(enum.StrEnum):
    """
    Tax rate status
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaxRateStatus.ACTIVE:
            return active()
        if self is TaxRateStatus.INACTIVE:
            return inactive()
        if self is TaxRateStatus.ARCHIVED:
            return archived()
