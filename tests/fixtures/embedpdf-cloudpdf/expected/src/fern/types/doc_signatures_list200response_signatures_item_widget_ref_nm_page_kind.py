

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesList200ResponseSignaturesItemWidgetRefNmPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocSignaturesList200ResponseSignaturesItemWidgetRefNmPageKind.OBJECT_NUMBER:
            return object_number()
