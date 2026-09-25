

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_options_messenger_messenger_category import ChannelOptionsMessengerMessengerCategory


class ChannelOptionsMessengerMessenger(UniversalBaseModel):
    category: typing.Optional[ChannelOptionsMessengerMessengerCategory] = pydantic.Field(default=None)
    """
    The use of different category tags enables the business to send messages for different use cases. For Facebook Messenger they need to comply with their [Messaging Types policy](https://developers.facebook.com/docs/messenger-platform/send-messages#messaging_types). Vonage maps our `category` to their `messaging_type`. If `message_tag` is used, then an additional `tag` for that type is mandatory. By default Vonage sends the `response` category to Facebook Messenger.
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    A tag describing the type and relevance of the 1:1 communication between your app and the end user. A full list of available tags is available [here](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
