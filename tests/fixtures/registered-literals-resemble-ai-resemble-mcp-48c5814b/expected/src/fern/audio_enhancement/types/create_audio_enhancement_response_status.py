

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateAudioEnhancementResponseStatus(enum.StrEnum):
    PENDING = "pending"

    def visit(self, pending: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateAudioEnhancementResponseStatus.PENDING:
            return pending()
