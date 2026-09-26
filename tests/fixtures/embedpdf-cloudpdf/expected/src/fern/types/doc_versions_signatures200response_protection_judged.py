

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsSignatures200ResponseProtectionJudged(enum.StrEnum):
    NONE = "none"
    LTA = "lta"
    FILL = "fill"
    ANNOTATE = "annotate"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        lta: typing.Callable[[], T_Result],
        fill: typing.Callable[[], T_Result],
        annotate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocVersionsSignatures200ResponseProtectionJudged.NONE:
            return none()
        if self is DocVersionsSignatures200ResponseProtectionJudged.LTA:
            return lta()
        if self is DocVersionsSignatures200ResponseProtectionJudged.FILL:
            return fill()
        if self is DocVersionsSignatures200ResponseProtectionJudged.ANNOTATE:
            return annotate()
