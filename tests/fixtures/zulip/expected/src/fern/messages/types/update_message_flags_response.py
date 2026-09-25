

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateMessageFlagsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    messages: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    An array with the IDs of the modified messages.
    """

    ignored_because_not_subscribed_channels: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Only present if the flag is `read` and the operation is `remove`.
    
    Zulip has an invariant that all unread messages must be in channels
    the user is subscribed to. This field will contain a list of the
    channels whose messages were skipped to mark as unread because the
    user is not subscribed to them.
    
    **Changes**: New in Zulip 10.0 (feature level 355).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
