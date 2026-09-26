

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PermissionReplyRequestReply(enum.StrEnum):
    ONCE = "once"
    ALWAYS = "always"
    REJECT = "reject"

    def visit(
        self,
        once: typing.Callable[[], T_Result],
        always: typing.Callable[[], T_Result],
        reject: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PermissionReplyRequestReply.ONCE:
            return once()
        if self is PermissionReplyRequestReply.ALWAYS:
            return always()
        if self is PermissionReplyRequestReply.REJECT:
            return reject()
