

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FormTitleBlockGroupType(enum.StrEnum):
    FORM_TITLE = "FORM_TITLE"

    def visit(self, form_title: typing.Callable[[], T_Result]) -> T_Result:
        if self is FormTitleBlockGroupType.FORM_TITLE:
            return form_title()
