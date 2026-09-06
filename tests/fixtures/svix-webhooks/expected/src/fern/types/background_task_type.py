

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BackgroundTaskType(enum.StrEnum):
    ENDPOINT_RECOVER = "endpoint.recover"

    def visit(self, endpoint_recover: typing.Callable[[], T_Result]) -> T_Result:
        if self is BackgroundTaskType.ENDPOINT_RECOVER:
            return endpoint_recover()
