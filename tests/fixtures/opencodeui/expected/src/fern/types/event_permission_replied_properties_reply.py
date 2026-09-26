

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventPermissionRepliedPropertiesReply(enum.StrEnum):
    ONCE = "once"
    ALWAYS = "always"
    REJECT = "reject"

    def visit(
        self,
        once: typing.Callable[[], T_Result],
        always: typing.Callable[[], T_Result],
        reject: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventPermissionRepliedPropertiesReply.ONCE:
            return once()
        if self is EventPermissionRepliedPropertiesReply.ALWAYS:
            return always()
        if self is EventPermissionRepliedPropertiesReply.REJECT:
            return reject()
