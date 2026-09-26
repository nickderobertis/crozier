

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemPolygonIdentityQuality(enum.StrEnum):
    DURABLE = "durable"
    WEAK = "weak"

    def visit(self, durable: typing.Callable[[], T_Result], weak: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonIdentityQuality.DURABLE:
            return durable()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonIdentityQuality.WEAK:
            return weak()
