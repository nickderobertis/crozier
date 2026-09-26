

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineReplyType(enum.StrEnum):
    REPLY = "reply"
    GROUP = "group"

    def visit(self, reply: typing.Callable[[], T_Result], group: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineReplyType.REPLY:
            return reply()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineReplyType.GROUP:
            return group()
