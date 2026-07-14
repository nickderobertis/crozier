

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SchemaChange(str, enum.Enum):
    NO_CHANGE = "no_change"
    NON_BREAKING = "non_breaking"
    BREAKING = "breaking"

    def visit(
        self,
        no_change: typing.Callable[[], T_Result],
        non_breaking: typing.Callable[[], T_Result],
        breaking: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchemaChange.NO_CHANGE:
            return no_change()
        if self is SchemaChange.NON_BREAKING:
            return non_breaking()
        if self is SchemaChange.BREAKING:
            return breaking()
