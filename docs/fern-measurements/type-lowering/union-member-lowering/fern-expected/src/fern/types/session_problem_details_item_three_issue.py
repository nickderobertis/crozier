

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionProblemDetailsItemThreeIssue(enum.StrEnum):
    CLOUD_COVER = "CLOUD_COVER"

    def visit(self, cloud_cover: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionProblemDetailsItemThreeIssue.CLOUD_COVER:
            return cloud_cover()
