

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_get_response_data_prompts_item import PromptsGetResponseDataPromptsItem


class PromptsGetResponseData(UniversalBaseModel):
    prompts: typing.List[PromptsGetResponseDataPromptsItem] = pydantic.Field()
    """
    List of available prompts
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
