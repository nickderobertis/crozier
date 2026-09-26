

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIdentityQuality(enum.StrEnum):
    DURABLE = "durable"
    WEAK = "weak"

    def visit(self, durable: typing.Callable[[], T_Result], weak: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIdentityQuality.DURABLE:
            return durable()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIdentityQuality.WEAK:
            return weak()
