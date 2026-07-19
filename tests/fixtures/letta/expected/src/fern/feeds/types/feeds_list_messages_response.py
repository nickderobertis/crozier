

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feeds_list_messages_response_messages_item import FeedsListMessagesResponseMessagesItem


class FeedsListMessagesResponse(UniversalBaseModel):
    messages: typing.List[FeedsListMessagesResponseMessagesItem]
    has_next_page: bool
    next_cursor: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
