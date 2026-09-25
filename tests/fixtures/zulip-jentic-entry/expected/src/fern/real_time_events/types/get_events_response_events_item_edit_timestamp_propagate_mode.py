

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemEditTimestampPropagateMode(enum.StrEnum):
    """
    Only present if this event moved messages to a different
    topic and/or channel.

    The choice the editing user made about which messages should be
    affected by a channel/topic edit:

    - `"change_one"`: Just change the one indicated in `message_id`.
    - `"change_later"`: Change messages in the same topic that had
      been sent after this one.
    - `"change_all"`: Change all messages in that topic.

    This parameter should be used to decide whether to change
    navigation and compose box state in response to the edit. For
    example, if the user was previously in topic narrow, and the
    topic was edited with `"change_later"` or `"change_all"`, the Zulip
    web app will automatically navigate to the new topic narrow.
    Similarly, a message being composed to the old topic should
    have its recipient changed to the new topic.

    This navigation makes it much more convenient to move content
    between topics without disruption or messages continuing
    to be sent to the pre-edit topic by accident.
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
        if self is GetEventsResponseEventsItemEditTimestampPropagateMode.CHANGE_ONE:
            return change_one()
        if self is GetEventsResponseEventsItemEditTimestampPropagateMode.CHANGE_LATER:
            return change_later()
        if self is GetEventsResponseEventsItemEditTimestampPropagateMode.CHANGE_ALL:
            return change_all()
