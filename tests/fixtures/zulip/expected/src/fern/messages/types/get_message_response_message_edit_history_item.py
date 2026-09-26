

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetMessageResponseMessageEditHistoryItem(UniversalBaseModel):
    prev_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if message's content was edited.
    
    The content of the message immediately prior to this
    edit event.
    """

    prev_rendered_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if message's content was edited.
    
    The rendered HTML representation of `prev_content`.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    prev_stream: typing.Optional[int] = pydantic.Field(default=None)
    """
    Only present if message's channel was edited.
    
    The channel ID of the message immediately prior to this
    edit event.
    
    **Changes**: New in Zulip 3.0 (feature level 1).
    """

    prev_topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if message's topic was edited.
    
    The topic of the message immediately prior to this
    edit event.
    
    **Changes**: New in Zulip 5.0 (feature level 118).
    Previously, this field was called `prev_subject`;
    clients are recommended to rename `prev_subject` to
    `prev_topic` if present for compatibility with
    older Zulip servers.
    """

    stream: typing.Optional[int] = pydantic.Field(default=None)
    """
    Only present if message's channel was edited.
    
    The ID of the channel containing the message
    immediately after this edit event.
    
    **Changes**: New in Zulip 5.0 (feature level 118).
    """

    timestamp: int = pydantic.Field()
    """
    The UNIX timestamp for the edit.
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if message's topic was edited.
    
    The topic of the message immediately after this edit event.
    
    **Changes**: New in Zulip 5.0 (feature level 118).
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user that made the edit.
    
    Will be `null` only for edit history
    events predating March 2017.
    
    Clients can display edit history events where this
    is `null` as modified by either the sender (for content
    edits) or an unknown user (for topic edits).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
