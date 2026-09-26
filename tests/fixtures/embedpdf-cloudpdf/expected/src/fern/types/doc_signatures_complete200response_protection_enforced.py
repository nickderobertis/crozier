

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesComplete200ResponseProtectionEnforced(enum.StrEnum):
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
        if self is DocSignaturesComplete200ResponseProtectionEnforced.NONE:
            return none()
        if self is DocSignaturesComplete200ResponseProtectionEnforced.LTA:
            return lta()
        if self is DocSignaturesComplete200ResponseProtectionEnforced.FILL:
            return fill()
        if self is DocSignaturesComplete200ResponseProtectionEnforced.ANNOTATE:
            return annotate()
