

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CollectFieldFieldType(enum.StrEnum):
    FIELD_TYPE_EMAIL = "field_type_email"

    def visit(self, field_type_email: typing.Callable[[], T_Result]) -> T_Result:
        if self is CollectFieldFieldType.FIELD_TYPE_EMAIL:
            return field_type_email()
