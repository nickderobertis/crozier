

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJudgeTypesRequestSort(enum.StrEnum):
    NAME = "name"

    def visit(self, name: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetJudgeTypesRequestSort.NAME:
            return name()
