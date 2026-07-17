

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LedgerAccountStatus(enum.StrEnum):
    """
    The status of the account.
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
        if self is LedgerAccountStatus.ACTIVE:
            return active()
        if self is LedgerAccountStatus.INACTIVE:
            return inactive()
        if self is LedgerAccountStatus.ARCHIVED:
            return archived()
