

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FiveFactorCountryScorecardMethodologyVersion(enum.StrEnum):
    ONE00 = "1.0.0"

    def visit(self, one00: typing.Callable[[], T_Result]) -> T_Result:
        if self is FiveFactorCountryScorecardMethodologyVersion.ONE00:
            return one00()
