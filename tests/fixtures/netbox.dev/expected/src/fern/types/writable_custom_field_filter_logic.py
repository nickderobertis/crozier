

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableCustomFieldFilterLogic(str, enum.Enum):
    """
    Loose matches any instance of a given string; exact matches the entire field.
    """

    DISABLED = "disabled"
    LOOSE = "loose"
    EXACT = "exact"

    def visit(
        self,
        disabled: typing.Callable[[], T_Result],
        loose: typing.Callable[[], T_Result],
        exact: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableCustomFieldFilterLogic.DISABLED:
            return disabled()
        if self is WritableCustomFieldFilterLogic.LOOSE:
            return loose()
        if self is WritableCustomFieldFilterLogic.EXACT:
            return exact()
