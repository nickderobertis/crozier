

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemButtonExternalType(enum.StrEnum):
    CTA = "cta"

    def visit(self, cta: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemButtonExternalType.CTA:
            return cta()
