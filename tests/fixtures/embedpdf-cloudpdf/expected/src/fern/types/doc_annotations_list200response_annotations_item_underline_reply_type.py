

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemUnderlineReplyType(enum.StrEnum):
    REPLY = "reply"
    GROUP = "group"

    def visit(self, reply: typing.Callable[[], T_Result], group: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemUnderlineReplyType.REPLY:
            return reply()
        if self is DocAnnotationsList200ResponseAnnotationsItemUnderlineReplyType.GROUP:
            return group()
