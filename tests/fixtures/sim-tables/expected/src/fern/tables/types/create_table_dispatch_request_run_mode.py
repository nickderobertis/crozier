

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTableDispatchRequestRunMode(enum.StrEnum):
    """
    Whether to run all or only incomplete cells.
    """

    ALL = "all"
    INCOMPLETE = "incomplete"

    def visit(self, all_: typing.Callable[[], T_Result], incomplete: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateTableDispatchRequestRunMode.ALL:
            return all_()
        if self is CreateTableDispatchRequestRunMode.INCOMPLETE:
            return incomplete()
