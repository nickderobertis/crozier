

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateSubscriptionsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    subscribed: typing.Dict[str, typing.List[str]] = pydantic.Field()
    """
    A dictionary where the key is the Zulip API email
    address of the user/bot and the value is a
    list of the names of the channels that were
    subscribed to as a result of the query.
    """

    already_subscribed: typing.Dict[str, typing.List[str]] = pydantic.Field()
    """
    A dictionary where the key is the Zulip API email
    address of the user/bot and the value is a
    list of the names of the channels that the
    user/bot is already subscribed to.
    """

    not_removed: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of the names of channels that the user
    is already unsubscribed from, and hence
    doesn't need to be unsubscribed.
    """

    removed: typing.List[str] = pydantic.Field()
    """
    A list of the names of channels which were unsubscribed
    from as a result of the query.
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
