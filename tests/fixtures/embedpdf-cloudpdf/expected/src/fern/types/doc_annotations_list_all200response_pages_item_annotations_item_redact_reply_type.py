

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactReplyType(enum.StrEnum):
    REPLY = "reply"
    GROUP = "group"

    def visit(self, reply: typing.Callable[[], T_Result], group: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactReplyType.REPLY:
            return reply()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactReplyType.GROUP:
            return group()
