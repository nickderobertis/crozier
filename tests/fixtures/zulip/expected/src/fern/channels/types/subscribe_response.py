

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubscribeResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    subscribed: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic.Field(default=None)
    """
    A dictionary where the key is the ID of the user and the value
    is a list of the names of the channels that user was subscribed
    to as a result of the request.
    
    **Changes**: Before Zulip 10.0 (feature level 289), the user
    keys were Zulip API email addresses, not user ID.
    """

    already_subscribed: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic.Field(default=None)
    """
    A dictionary where the key is the ID of the user and the value
    is a list of the names of the channels that where the user was
    not added as a subscriber in this request, because they were
    already a subscriber.
    
    **Changes**: Before Zulip 10.0 (feature level 289), the user
    keys were Zulip API email addresses, not user IDs.
    """

    unauthorized: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of names of channels that the requesting user/bot was not
    authorized to subscribe to. Only present if `"authorization_errors_fatal": false`.
    """

    new_subscription_messages_sent: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Only present if the parameter `send_new_subscription_messages`
    in the request was `true`.
    
    Whether Notification Bot DMs in fact sent to the added
    subscribers as requested by the `send_new_subscription_messages`
    parameter. Clients may find this value useful to communicate
    with users about the effect of this request.
    
    **Changes**: New in Zulip 11.0 (feature level 397).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
