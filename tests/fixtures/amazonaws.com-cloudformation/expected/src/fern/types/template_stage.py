

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TemplateStage(enum.StrEnum):
    ORIGINAL = "Original"
    PROCESSED = "Processed"

    def visit(self, original: typing.Callable[[], T_Result], processed: typing.Callable[[], T_Result]) -> T_Result:
        if self is TemplateStage.ORIGINAL:
            return original()
        if self is TemplateStage.PROCESSED:
            return processed()
