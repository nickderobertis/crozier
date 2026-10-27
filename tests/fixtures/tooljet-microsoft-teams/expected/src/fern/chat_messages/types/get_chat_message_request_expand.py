

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChatMessageRequestExpand(enum.StrEnum):
    REPLIES = "replies"
    HOSTED_CONTENTS = "hostedContents"

    def visit(self, replies: typing.Callable[[], T_Result], hosted_contents: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChatMessageRequestExpand.REPLIES:
            return replies()
        if self is GetChatMessageRequestExpand.HOSTED_CONTENTS:
            return hosted_contents()
