

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexRevisionPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocFormsGet200ResponseFieldsItemTextWidgetsItemRefIndexRevisionPageKind.OBJECT_NUMBER:
            return object_number()
