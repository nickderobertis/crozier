

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefIndexRevisionPageKind(enum.StrEnum):
    OBJECT_NUMBER = "objectNumber"

    def visit(self, object_number: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocFormsGet200ResponseFieldsItemComboboxWidgetsItemRefIndexRevisionPageKind.OBJECT_NUMBER:
            return object_number()
