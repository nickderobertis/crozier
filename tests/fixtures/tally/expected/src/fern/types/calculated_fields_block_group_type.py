

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CalculatedFieldsBlockGroupType(enum.StrEnum):
    CALCULATED_FIELDS = "CALCULATED_FIELDS"

    def visit(self, calculated_fields: typing.Callable[[], T_Result]) -> T_Result:
        if self is CalculatedFieldsBlockGroupType.CALCULATED_FIELDS:
            return calculated_fields()
