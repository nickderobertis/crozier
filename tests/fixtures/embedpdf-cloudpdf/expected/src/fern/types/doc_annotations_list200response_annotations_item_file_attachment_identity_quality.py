

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIdentityQuality(enum.StrEnum):
    DURABLE = "durable"
    WEAK = "weak"

    def visit(self, durable: typing.Callable[[], T_Result], weak: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIdentityQuality.DURABLE:
            return durable()
        if self is DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIdentityQuality.WEAK:
            return weak()
