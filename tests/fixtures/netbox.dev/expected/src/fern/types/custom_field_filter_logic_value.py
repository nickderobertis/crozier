

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CustomFieldFilterLogicValue(str, enum.Enum):
    DISABLED = "disabled"
    LOOSE = "loose"
    EXACT = "exact"

    def visit(
        self,
        disabled: typing.Callable[[], T_Result],
        loose: typing.Callable[[], T_Result],
        exact: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomFieldFilterLogicValue.DISABLED:
            return disabled()
        if self is CustomFieldFilterLogicValue.LOOSE:
            return loose()
        if self is CustomFieldFilterLogicValue.EXACT:
            return exact()
