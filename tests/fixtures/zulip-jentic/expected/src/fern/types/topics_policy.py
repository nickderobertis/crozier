

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TopicsPolicy(enum.StrEnum):
    """
    Whether [named topics](/help/introduction-to-topics) and the empty
    topic (i.e., ["general chat" topic](/help/general-chat-topic))
    are enabled in this channel.

    - `"inherit"`: Messages can be sent to named topics in this channel,
      and the [organization-level `realm_topics_policy`][realm-topics-policy]
      is used for whether messages can be sent to the empty topic in this
      channel.
    - `"allow_empty_topic"`: Messages can be sent to both named topics and
      the empty topic in this channel.
    - `"disable_empty_topic"`: Messages can be sent to named topics in this
      channel, but the empty topic is disabled.
    - `"empty_topic_only"`: Messages can be sent to the empty topic in this
      channel, but named topics are disabled. See ["general chat"
      channels](/help/general-chat-channels).

    The `"empty_topic_only"` policy can only be set if all existing messages
    in the channel are already in the empty topic.

    When creating a new channel, if the `topics_policy` is not specified, the
    `"inherit"` option will be set.

    **Changes**: In Zulip 11.0 (feature level 404), the `"empty_topic_only"`
    option was added.

    New in Zulip 11.0 (feature level 392).

    [realm-topics-policy]: /help/require-topics#set-the-default-general-chat-topic-configuration
    """

    INHERIT = "inherit"
    ALLOW_EMPTY_TOPIC = "allow_empty_topic"
    DISABLE_EMPTY_TOPIC = "disable_empty_topic"
    EMPTY_TOPIC_ONLY = "empty_topic_only"

    def visit(
        self,
        inherit: typing.Callable[[], T_Result],
        allow_empty_topic: typing.Callable[[], T_Result],
        disable_empty_topic: typing.Callable[[], T_Result],
        empty_topic_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TopicsPolicy.INHERIT:
            return inherit()
        if self is TopicsPolicy.ALLOW_EMPTY_TOPIC:
            return allow_empty_topic()
        if self is TopicsPolicy.DISABLE_EMPTY_TOPIC:
            return disable_empty_topic()
        if self is TopicsPolicy.EMPTY_TOPIC_ONLY:
            return empty_topic_only()
