

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexRevisionPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocVersionsSignatures200ResponseSignaturesItemWidgetRefIndexRevisionPageKind.OBJECT_NUMBER:
            return object_number()
