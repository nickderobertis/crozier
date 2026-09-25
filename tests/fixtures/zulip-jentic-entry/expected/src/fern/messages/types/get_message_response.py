

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_message_response_message import GetMessageResponseMessage


class GetMessageResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    raw_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The raw Markdown content of the message.
    
    See the help center article on [message formatting](/help/format-your-message-using-markdown) for details on Zulip-flavored Markdown.
    
    **Deprecated** and to be removed once no longer required for
    legacy clients. Modern clients should prefer passing
    `"apply_markdown": false` to request raw message content.
    """

    message: typing.Optional[GetMessageResponseMessage] = pydantic.Field(default=None)
    """
    An object containing details of the message.
    
    **Changes**: New in Zulip 5.0 (feature level 120).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
