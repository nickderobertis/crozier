

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataToRefresh(enum.StrEnum):
    ACTIVITY = "activity"
    STATE = "state"
    CREATOR = "creator"

    def visit(
        self,
        activity: typing.Callable[[], T_Result],
        state: typing.Callable[[], T_Result],
        creator: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataToRefresh.ACTIVITY:
            return activity()
        if self is DataToRefresh.STATE:
            return state()
        if self is DataToRefresh.CREATOR:
            return creator()
