

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_get_response_data_prompts_item_arguments_item import PromptsGetResponseDataPromptsItemArgumentsItem


class PromptsGetResponseDataPromptsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Prompt name/identifier
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Prompt description
    """

    arguments: typing.Optional[typing.List[PromptsGetResponseDataPromptsItemArgumentsItem]] = pydantic.Field(
        default=None
    )
    """
    Prompt arguments
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
