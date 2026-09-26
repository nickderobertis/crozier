

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesComplete200ResponseStatus(enum.StrEnum):
    COMPLETED = "completed"
    ALREADY_COMPLETED = "already-completed"

    def visit(
        self, completed: typing.Callable[[], T_Result], already_completed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DocSignaturesComplete200ResponseStatus.COMPLETED:
            return completed()
        if self is DocSignaturesComplete200ResponseStatus.ALREADY_COMPLETED:
            return already_completed()
