

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_prompt_name_post_response_data_files_item import PromptsPromptNamePostResponseDataFilesItem
from .prompts_prompt_name_post_response_data_messages_item import PromptsPromptNamePostResponseDataMessagesItem


class PromptsPromptNamePostResponseData(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Prompt description
    """

    messages: typing.List[PromptsPromptNamePostResponseDataMessagesItem] = pydantic.Field()
    """
    Prompt messages
    """

    files: typing.Optional[typing.List[PromptsPromptNamePostResponseDataFilesItem]] = pydantic.Field(default=None)
    """
    Supporting files for folder-based skills (base64-encoded)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
