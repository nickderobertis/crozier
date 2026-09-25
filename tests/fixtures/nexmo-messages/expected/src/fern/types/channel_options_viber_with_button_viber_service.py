

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_options_viber_with_button_viber_service_action import ChannelOptionsViberWithButtonViberServiceAction
from .channel_options_viber_with_button_viber_service_category import ChannelOptionsViberWithButtonViberServiceCategory


class ChannelOptionsViberWithButtonViberService(UniversalBaseModel):
    action: typing.Optional[ChannelOptionsViberWithButtonViberServiceAction] = pydantic.Field(default=None)
    """
    Node for Viber action buttons.
    """

    category: typing.Optional[ChannelOptionsViberWithButtonViberServiceCategory] = pydantic.Field(default=None)
    """
    The use of different category tags enables the business to send messages for different use cases. For Viber Business Messages the first message sent from a business to a user must be personal, informative & a targeted message - not promotional. By default Vonage sends the `transaction` category to Viber Business Messages.
    """

    ttl: typing.Optional[int] = pydantic.Field(default=None)
    """
    Set the time-to-live of message to be delivered in seconds. i.e. if the message is not delivered in 600 seconds then delete the message.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Viber-specific type definition. To use "template", please contact your Vonage Account Manager to setup your templates. To find out more please visit the [product page](https://www.vonage.com/communications-apis/messages/)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
