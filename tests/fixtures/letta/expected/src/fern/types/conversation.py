

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Conversation(UniversalBaseModel):
    """
    Represents a conversation on an agent for concurrent messaging.
    """

    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was last updated.
    """

    id: str = pydantic.Field()
    """
    The unique identifier of the conversation.
    """

    agent_id: str = pydantic.Field()
    """
    The ID of the agent this conversation belongs to.
    """

    summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    A summary of the conversation.
    """

    in_context_message_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The IDs of in-context messages for the conversation.
    """

    isolated_block_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    IDs of blocks that are isolated (specific to this conversation, overriding agent defaults).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
