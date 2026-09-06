

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class OptionFieldType(enum.StrEnum):
    """
    The [Option field type](/data/reference/field-types-item-values#option)
    """

    OPTION = "Option"

    def visit(self, option: typing.Callable[[], T_Result]) -> T_Result:
        if self is OptionFieldType.OPTION:
            return option()
