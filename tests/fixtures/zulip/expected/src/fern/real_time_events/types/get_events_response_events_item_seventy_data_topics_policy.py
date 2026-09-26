

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSeventyDataTopicsPolicy(enum.StrEnum):
    """
    The organization's default policy for sending channel messages to the
    [empty "general chat" topic](/help/general-chat-topic).

    - `"allow_empty_topic"`: Channel messages can be sent to the empty topic.
    - `"disable_empty_topic"`: Channel messages cannot be sent to the empty topic.

    **Changes**: New in Zulip 11.0 (feature level 392). Previously, this was
    controlled by the boolean realm `mandatory_topics` setting, which is now
    deprecated.
    """

    ALLOW_EMPTY_TOPIC = "allow_empty_topic"
    DISABLE_EMPTY_TOPIC = "disable_empty_topic"

    def visit(
        self, allow_empty_topic: typing.Callable[[], T_Result], disable_empty_topic: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetEventsResponseEventsItemSeventyDataTopicsPolicy.ALLOW_EMPTY_TOPIC:
            return allow_empty_topic()
        if self is GetEventsResponseEventsItemSeventyDataTopicsPolicy.DISABLE_EMPTY_TOPIC:
            return disable_empty_topic()
