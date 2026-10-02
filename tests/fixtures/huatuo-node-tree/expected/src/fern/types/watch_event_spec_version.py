

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WatchEventSpecVersion(enum.StrEnum):
    WATCH_EVENT_SPEC_VERSION10 = "1.0"

    def visit(self, watch_event_spec_version10: typing.Callable[[], T_Result]) -> T_Result:
        if self is WatchEventSpecVersion.WATCH_EVENT_SPEC_VERSION10:
            return watch_event_spec_version10()
