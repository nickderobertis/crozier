

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VariableOperationSchemaType(enum.StrEnum):
    SET = "SET"
    UNSET = "UNSET"

    def visit(self, set_: typing.Callable[[], T_Result], unset: typing.Callable[[], T_Result]) -> T_Result:
        if self is VariableOperationSchemaType.SET:
            return set_()
        if self is VariableOperationSchemaType.UNSET:
            return unset()
