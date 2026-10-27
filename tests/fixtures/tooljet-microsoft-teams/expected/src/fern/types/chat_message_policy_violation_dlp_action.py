

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatMessagePolicyViolationDlpAction(enum.StrEnum):
    NONE = "none"
    NOTIFY_SENDER = "notifySender"
    BLOCK_ACCESS = "blockAccess"
    BLOCK_ACCESS_EXTERNAL = "blockAccessExternal"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        notify_sender: typing.Callable[[], T_Result],
        block_access: typing.Callable[[], T_Result],
        block_access_external: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatMessagePolicyViolationDlpAction.NONE:
            return none()
        if self is ChatMessagePolicyViolationDlpAction.NOTIFY_SENDER:
            return notify_sender()
        if self is ChatMessagePolicyViolationDlpAction.BLOCK_ACCESS:
            return block_access()
        if self is ChatMessagePolicyViolationDlpAction.BLOCK_ACCESS_EXTERNAL:
            return block_access_external()
