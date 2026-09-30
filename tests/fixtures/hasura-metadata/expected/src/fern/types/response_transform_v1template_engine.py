

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseTransformV1TemplateEngine(enum.StrEnum):
    KRITI = "Kriti"

    def visit(self, kriti: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseTransformV1TemplateEngine.KRITI:
            return kriti()
