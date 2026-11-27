

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NewBlankFormInstanceProviderType(enum.StrEnum):
    BLANK_FORM = "BLANK_FORM"

    def visit(self, blank_form: typing.Callable[[], T_Result]) -> T_Result:
        if self is NewBlankFormInstanceProviderType.BLANK_FORM:
            return blank_form()
