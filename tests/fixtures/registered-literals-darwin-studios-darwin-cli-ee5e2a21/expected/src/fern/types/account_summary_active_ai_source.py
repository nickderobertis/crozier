

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountSummaryActiveAiSource(enum.StrEnum):
    REQUESTED = "requested"
    ACTIVE_SELECTION = "active_selection"
    DEFAULT = "default"

    def visit(
        self,
        requested: typing.Callable[[], T_Result],
        active_selection: typing.Callable[[], T_Result],
        default: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountSummaryActiveAiSource.REQUESTED:
            return requested()
        if self is AccountSummaryActiveAiSource.ACTIVE_SELECTION:
            return active_selection()
        if self is AccountSummaryActiveAiSource.DEFAULT:
            return default()
