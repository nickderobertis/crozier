

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CustomFieldFilterLogicLabel(str, enum.Enum):
    DISABLED = "Disabled"
    LOOSE = "Loose"
    EXACT = "Exact"

    def visit(
        self,
        disabled: typing.Callable[[], T_Result],
        loose: typing.Callable[[], T_Result],
        exact: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomFieldFilterLogicLabel.DISABLED:
            return disabled()
        if self is CustomFieldFilterLogicLabel.LOOSE:
            return loose()
        if self is CustomFieldFilterLogicLabel.EXACT:
            return exact()
