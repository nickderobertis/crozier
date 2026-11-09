

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFileRequestDisposition(enum.StrEnum):
    INLINE = "inline"
    ATTACHMENT = "attachment"

    def visit(self, inline: typing.Callable[[], T_Result], attachment: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetFileRequestDisposition.INLINE:
            return inline()
        if self is GetFileRequestDisposition.ATTACHMENT:
            return attachment()
