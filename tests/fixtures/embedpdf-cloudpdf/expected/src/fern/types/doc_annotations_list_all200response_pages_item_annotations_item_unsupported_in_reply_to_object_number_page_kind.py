

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedInReplyToObjectNumberPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedInReplyToObjectNumberPageKind.OBJECT_NUMBER
        ):
            return object_number()
