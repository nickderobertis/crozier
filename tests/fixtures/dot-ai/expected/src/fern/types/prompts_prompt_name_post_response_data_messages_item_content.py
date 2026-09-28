

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_prompt_name_post_response_data_messages_item_content_type import (
    PromptsPromptNamePostResponseDataMessagesItemContentType,
)


class PromptsPromptNamePostResponseDataMessagesItemContent(UniversalBaseModel):
    """
    Message content
    """

    type: PromptsPromptNamePostResponseDataMessagesItemContentType
    text: str = pydantic.Field()
    """
    Message text content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
