

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritablePowerFeedStatus(str, enum.Enum):
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
        if self is WritablePowerFeedStatus.OFFLINE:
            return offline()
        if self is WritablePowerFeedStatus.ACTIVE:
            return active()
        if self is WritablePowerFeedStatus.PLANNED:
            return planned()
        if self is WritablePowerFeedStatus.FAILED:
            return failed()
