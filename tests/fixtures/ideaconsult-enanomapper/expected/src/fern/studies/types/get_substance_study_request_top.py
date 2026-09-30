

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSubstanceStudyRequestTop(enum.StrEnum):
    P_CHEM = "P-CHEM"
    ECOTOX = "ECOTOX"
    ENV_FATE = "ENV FATE"
    TOX = "TOX"
    EXPOSURE = "EXPOSURE"

    def visit(
        self,
        p_chem: typing.Callable[[], T_Result],
        ecotox: typing.Callable[[], T_Result],
        env_fate: typing.Callable[[], T_Result],
        tox: typing.Callable[[], T_Result],
        exposure: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSubstanceStudyRequestTop.P_CHEM:
            return p_chem()
        if self is GetSubstanceStudyRequestTop.ECOTOX:
            return ecotox()
        if self is GetSubstanceStudyRequestTop.ENV_FATE:
            return env_fate()
        if self is GetSubstanceStudyRequestTop.TOX:
            return tox()
        if self is GetSubstanceStudyRequestTop.EXPOSURE:
            return exposure()
