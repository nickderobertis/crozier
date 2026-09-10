

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error404Message(enum.StrEnum):
    THE_SPECIFIED_RESOURCE_DOES_NOT_EXIST = "The specified resource does not exist."

    def visit(self, the_specified_resource_does_not_exist: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error404Message.THE_SPECIFIED_RESOURCE_DOES_NOT_EXIST:
            return the_specified_resource_does_not_exist()
