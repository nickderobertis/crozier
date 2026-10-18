

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegionsInfoOutputRecommendationsSmartGroupCode(enum.StrEnum):
    AMERICAS = "americas"
    EMEA = "emea"
    APAC = "apac"

    def visit(
        self,
        americas: typing.Callable[[], T_Result],
        emea: typing.Callable[[], T_Result],
        apac: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RegionsInfoOutputRecommendationsSmartGroupCode.AMERICAS:
            return americas()
        if self is RegionsInfoOutputRecommendationsSmartGroupCode.EMEA:
            return emea()
        if self is RegionsInfoOutputRecommendationsSmartGroupCode.APAC:
            return apac()
