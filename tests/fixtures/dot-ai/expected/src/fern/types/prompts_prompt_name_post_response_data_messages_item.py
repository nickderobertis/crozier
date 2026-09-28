

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_prompt_name_post_response_data_messages_item_content import (
    PromptsPromptNamePostResponseDataMessagesItemContent,
)
from .prompts_prompt_name_post_response_data_messages_item_role import PromptsPromptNamePostResponseDataMessagesItemRole


class PromptsPromptNamePostResponseDataMessagesItem(UniversalBaseModel):
    role: PromptsPromptNamePostResponseDataMessagesItemRole = pydantic.Field()
    """
    Message role
    """

    content: PromptsPromptNamePostResponseDataMessagesItemContent = pydantic.Field()
    """
    Message content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
