

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KeyToMultiValueKeyMatchStyleKeyMatchStyle(enum.StrEnum):
    MATCHING_KEY = "MATCHING_KEY"
    SUB_SET = "SUB_SET"

    def visit(self, matching_key: typing.Callable[[], T_Result], sub_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is KeyToMultiValueKeyMatchStyleKeyMatchStyle.MATCHING_KEY:
            return matching_key()
        if self is KeyToMultiValueKeyMatchStyleKeyMatchStyle.SUB_SET:
            return sub_set()
