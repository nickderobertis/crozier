

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartialRecordMethod(enum.StrEnum):
    DEFAULT = "DEFAULT"
    INDIVIDUAL = "INDIVIDUAL"

    def visit(self, default: typing.Callable[[], T_Result], individual: typing.Callable[[], T_Result]) -> T_Result:
        if self is PartialRecordMethod.DEFAULT:
            return default()
        if self is PartialRecordMethod.INDIVIDUAL:
            return individual()
