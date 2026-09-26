

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorBodyZeroMsg(enum.StrEnum):
    YOUR_ORGANIZATION_HAS_TURNED_OFF_MESSAGE_EDITING = "Your organization has turned off message editing"
    YOU_DONT_HAVE_PERMISSION_TO_EDIT_THIS_MESSAGE = "You don't have permission to edit this message"
    THE_TIME_LIMIT_FOR_EDITING_THIS_MESSAGE_HAS_PAST = "The time limit for editing this message has past"
    NOTHING_TO_CHANGE = "Nothing to change"
    TOPIC_CANT_BE_EMPTY = "Topic can't be empty"

    def visit(
        self,
        your_organization_has_turned_off_message_editing: typing.Callable[[], T_Result],
        you_dont_have_permission_to_edit_this_message: typing.Callable[[], T_Result],
        the_time_limit_for_editing_this_message_has_past: typing.Callable[[], T_Result],
        nothing_to_change: typing.Callable[[], T_Result],
        topic_cant_be_empty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BadRequestErrorBodyZeroMsg.YOUR_ORGANIZATION_HAS_TURNED_OFF_MESSAGE_EDITING:
            return your_organization_has_turned_off_message_editing()
        if self is BadRequestErrorBodyZeroMsg.YOU_DONT_HAVE_PERMISSION_TO_EDIT_THIS_MESSAGE:
            return you_dont_have_permission_to_edit_this_message()
        if self is BadRequestErrorBodyZeroMsg.THE_TIME_LIMIT_FOR_EDITING_THIS_MESSAGE_HAS_PAST:
            return the_time_limit_for_editing_this_message_has_past()
        if self is BadRequestErrorBodyZeroMsg.NOTHING_TO_CHANGE:
            return nothing_to_change()
        if self is BadRequestErrorBodyZeroMsg.TOPIC_CANT_BE_EMPTY:
            return topic_cant_be_empty()
