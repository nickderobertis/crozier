

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSixtySevenOp(enum.StrEnum):
    UPDATE_DICT = "update_dict"

    def visit(self, update_dict: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemSixtySevenOp.UPDATE_DICT:
            return update_dict()
