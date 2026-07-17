

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PowerFeedStatusLabel(enum.StrEnum):
    OFFLINE = "Offline"
    ACTIVE = "Active"
    PLANNED = "Planned"
    FAILED = "Failed"

    def visit(
        self,
        offline: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PowerFeedStatusLabel.OFFLINE:
            return offline()
        if self is PowerFeedStatusLabel.ACTIVE:
            return active()
        if self is PowerFeedStatusLabel.PLANNED:
            return planned()
        if self is PowerFeedStatusLabel.FAILED:
            return failed()
