

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BaseActivityFeedItemModelType(enum.StrEnum):
    COMMENT = "comment"

    def visit(self, comment: typing.Callable[[], T_Result]) -> T_Result:
        if self is BaseActivityFeedItemModelType.COMMENT:
            return comment()
