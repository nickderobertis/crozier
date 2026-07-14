

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SortBy(str, enum.Enum):
    """ """

    NAME = "name"
    CREATED_ON = "createdOn"

    def visit(self, name: typing.Callable[[], T_Result], created_on: typing.Callable[[], T_Result]) -> T_Result:
        if self is SortBy.NAME:
            return name()
        if self is SortBy.CREATED_ON:
            return created_on()
