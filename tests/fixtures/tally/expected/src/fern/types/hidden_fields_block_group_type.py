

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HiddenFieldsBlockGroupType(enum.StrEnum):
    HIDDEN_FIELDS = "HIDDEN_FIELDS"

    def visit(self, hidden_fields: typing.Callable[[], T_Result]) -> T_Result:
        if self is HiddenFieldsBlockGroupType.HIDDEN_FIELDS:
            return hidden_fields()
