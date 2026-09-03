

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostCompleteSignupRedirectResponseResponseStatus(enum.StrEnum):
    COMPLETED = "COMPLETED"

    def visit(self, completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostCompleteSignupRedirectResponseResponseStatus.COMPLETED:
            return completed()
