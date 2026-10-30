

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StrataAddServersRequestServersOne(enum.StrEnum):
    ALL = "ALL"

    def visit(self, all_: typing.Callable[[], T_Result]) -> T_Result:
        if self is StrataAddServersRequestServersOne.ALL:
            return all_()
