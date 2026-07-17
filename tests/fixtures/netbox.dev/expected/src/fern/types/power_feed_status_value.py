

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PowerFeedStatusValue(enum.StrEnum):
    OFFLINE = "offline"
    ACTIVE = "active"
    PLANNED = "planned"
    FAILED = "failed"

    def visit(
        self,
        offline: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PowerFeedStatusValue.OFFLINE:
            return offline()
        if self is PowerFeedStatusValue.ACTIVE:
            return active()
        if self is PowerFeedStatusValue.PLANNED:
            return planned()
        if self is PowerFeedStatusValue.FAILED:
            return failed()
