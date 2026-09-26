

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Mclass(enum.StrEnum):
    """
    Media class.
    """

    CAPACITY = "capacity"
    STAGING = "staging"
    PMEM = "pmem"

    def visit(
        self,
        capacity: typing.Callable[[], T_Result],
        staging: typing.Callable[[], T_Result],
        pmem: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Mclass.CAPACITY:
            return capacity()
        if self is Mclass.STAGING:
            return staging()
        if self is Mclass.PMEM:
            return pmem()
