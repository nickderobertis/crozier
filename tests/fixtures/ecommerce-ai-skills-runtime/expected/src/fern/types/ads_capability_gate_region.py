

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdsCapabilityGateRegion(enum.StrEnum):
    NA = "na"
    EU = "eu"
    FE = "fe"

    def visit(
        self, na: typing.Callable[[], T_Result], eu: typing.Callable[[], T_Result], fe: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AdsCapabilityGateRegion.NA:
            return na()
        if self is AdsCapabilityGateRegion.EU:
            return eu()
        if self is AdsCapabilityGateRegion.FE:
            return fe()
