

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FeedbackResponseSchemaStatus(enum.StrEnum):
    SUCCESS = "success"

    def visit(self, success: typing.Callable[[], T_Result]) -> T_Result:
        if self is FeedbackResponseSchemaStatus.SUCCESS:
            return success()
