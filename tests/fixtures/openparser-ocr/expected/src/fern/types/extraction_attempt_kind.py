

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionAttemptKind(enum.StrEnum):
    PRIMARY = "primary"
    REPAIR = "repair"

    def visit(self, primary: typing.Callable[[], T_Result], repair: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractionAttemptKind.PRIMARY:
            return primary()
        if self is ExtractionAttemptKind.REPAIR:
            return repair()
