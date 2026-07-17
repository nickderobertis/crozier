

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WeightRule(enum.StrEnum):
    """
    Weight rule.
    """

    DOWNSTREAM = "downstream"
    UPSTREAM = "upstream"
    ABSOLUTE = "absolute"

    def visit(
        self,
        downstream: typing.Callable[[], T_Result],
        upstream: typing.Callable[[], T_Result],
        absolute: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WeightRule.DOWNSTREAM:
            return downstream()
        if self is WeightRule.UPSTREAM:
            return upstream()
        if self is WeightRule.ABSOLUTE:
            return absolute()
