

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelOptionsMessengerMessengerCategory(enum.StrEnum):
    """
    The use of different category tags enables the business to send messages for different use cases. For Facebook Messenger they need to comply with their [Messaging Types policy](https://developers.facebook.com/docs/messenger-platform/send-messages#messaging_types). Vonage maps our `category` to their `messaging_type`. If `message_tag` is used, then an additional `tag` for that type is mandatory. By default Vonage sends the `response` category to Facebook Messenger.
    """

    RESPONSE = "response"
    UPDATE = "update"
    MESSAGE_TAG = "message_tag"

    def visit(
        self,
        response: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        message_tag: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelOptionsMessengerMessengerCategory.RESPONSE:
            return response()
        if self is ChannelOptionsMessengerMessengerCategory.UPDATE:
            return update()
        if self is ChannelOptionsMessengerMessengerCategory.MESSAGE_TAG:
            return message_tag()
