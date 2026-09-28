

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TitlerConflictErrorError(enum.StrEnum):
    TITLE_IS_MANUAL = "title_is_manual"
    TITLE_IN_FLIGHT = "title_in_flight"
    TITLE_STATE_CHANGED = "title_state_changed"

    def visit(
        self,
        title_is_manual: typing.Callable[[], T_Result],
        title_in_flight: typing.Callable[[], T_Result],
        title_state_changed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TitlerConflictErrorError.TITLE_IS_MANUAL:
            return title_is_manual()
        if self is TitlerConflictErrorError.TITLE_IN_FLIGHT:
            return title_in_flight()
        if self is TitlerConflictErrorError.TITLE_STATE_CHANGED:
            return title_state_changed()
