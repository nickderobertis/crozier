

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .api_pagination import ApiPagination


class EndpointGetConversationsIdMessages(UniversalBaseModel):
    data: typing.Optional[typing.List["Message"]] = None
    pagination: typing.Optional[ApiPagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .conversation import Conversation
from .message import Message

update_forward_refs(EndpointGetConversationsIdMessages, Conversation=Conversation, Message=Message)
