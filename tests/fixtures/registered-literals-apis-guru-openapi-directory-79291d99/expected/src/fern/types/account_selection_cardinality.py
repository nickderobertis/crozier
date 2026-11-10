

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountSelectionCardinality(enum.StrEnum):
    """
    The application requires that accounts be limited to a specific cardinality.
    `MULTI_SELECT`: indicates that the user should be allowed to pick multiple accounts.
    `SINGLE_SELECT`: indicates that the user should be allowed to pick only a single account.
    `ALL`: indicates that the user must share all of their accounts and should not be given the opportunity to de-select
    """

    SINGLE_SELECT = "SINGLE_SELECT"
    MULTI_SELECT = "MULTI_SELECT"
    ALL = "ALL"

    def visit(
        self,
        single_select: typing.Callable[[], T_Result],
        multi_select: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountSelectionCardinality.SINGLE_SELECT:
            return single_select()
        if self is AccountSelectionCardinality.MULTI_SELECT:
            return multi_select()
        if self is AccountSelectionCardinality.ALL:
            return all_()
