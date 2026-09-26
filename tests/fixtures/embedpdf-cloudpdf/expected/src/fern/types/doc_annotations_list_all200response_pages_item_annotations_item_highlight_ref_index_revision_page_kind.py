

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefIndexRevisionPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRefIndexRevisionPageKind.OBJECT_NUMBER
        ):
            return object_number()
