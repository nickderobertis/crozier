

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FormFieldValueReferenceType(enum.StrEnum):
    FORM_FIELD_VALUE = "FORM_FIELD_VALUE"

    def visit(self, form_field_value: typing.Callable[[], T_Result]) -> T_Result:
        if self is FormFieldValueReferenceType.FORM_FIELD_VALUE:
            return form_field_value()
