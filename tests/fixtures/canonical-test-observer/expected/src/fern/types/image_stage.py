

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageStage(enum.StrEnum):
    PENDING = "pending"
    CURRENT = "current"

    def visit(self, pending: typing.Callable[[], T_Result], current: typing.Callable[[], T_Result]) -> T_Result:
        if self is ImageStage.PENDING:
            return pending()
        if self is ImageStage.CURRENT:
            return current()
