

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RefreshStartedResponseStatus(enum.StrEnum):
    REFRESH_STARTED = "refresh_started"

    def visit(self, refresh_started: typing.Callable[[], T_Result]) -> T_Result:
        if self is RefreshStartedResponseStatus.REFRESH_STARTED:
            return refresh_started()
