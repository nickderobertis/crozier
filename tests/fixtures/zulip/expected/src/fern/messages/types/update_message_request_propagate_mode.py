

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateMessageRequestPropagateMode(enum.StrEnum):
    """
    Which message(s) should be edited:

    - `"change_later"`: The target message and all following messages.
    - `"change_one"`: Only the target message.
    - `"change_all"`: All messages in this topic.

    Only the default value of `"change_one"` is valid when editing
    only the content of a message.

    This parameter determines both which messages get moved and also whether
    clients that are currently narrowed to the topic containing the message
    should navigate or adjust their compose box recipient to point to the
    post-edit channel/topic.
    """

    CHANGE_ONE = "change_one"
    CHANGE_LATER = "change_later"
    CHANGE_ALL = "change_all"

    def visit(
        self,
        change_one: typing.Callable[[], T_Result],
        change_later: typing.Callable[[], T_Result],
        change_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateMessageRequestPropagateMode.CHANGE_ONE:
            return change_one()
        if self is UpdateMessageRequestPropagateMode.CHANGE_LATER:
            return change_later()
        if self is UpdateMessageRequestPropagateMode.CHANGE_ALL:
            return change_all()
