

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RequestTransformV2TemplateEngine(enum.StrEnum):
    KRITI = "Kriti"

    def visit(self, kriti: typing.Callable[[], T_Result]) -> T_Result:
        if self is RequestTransformV2TemplateEngine.KRITI:
            return kriti()
