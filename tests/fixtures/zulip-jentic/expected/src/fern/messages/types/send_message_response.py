

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendMessageResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    id: int = pydantic.Field()
    """
    The unique ID assigned to the sent message.
    """

    automatic_new_visibility_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    If the message's sender had configured their [visibility policy settings](/help/mute-a-topic)
    to potentially automatically follow or unmute topics when sending messages,
    and one of these policies did in fact change the user's visibility policy
    for the topic where this message was sent, the new value for that user's
    visibility policy for the recipient topic.
    
    Only present if the sender's visibility was in fact changed.
    
    The value can be either [unmuted or followed](/api/update-user-topic#parameter-visibility_policy).
    
    Clients will also be notified about the change in policy via a
    `user_topic` event as usual. This field is intended to be used by clients
    to explicitly inform the user when a topic's visibility policy was changed
    automatically due to sending a message.
    
    For example, the Zulip web application uses this field to decide whether
    to display a warning or notice suggesting to unmute the topic after
    sending a message to a muted channel. Such a notice would be confusing in
    the event that the act of sending the message had already resulted in the
    user automatically unmuting or following the topic in question.
    
    **Changes**: New in Zulip 8.0 (feature level 218).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
