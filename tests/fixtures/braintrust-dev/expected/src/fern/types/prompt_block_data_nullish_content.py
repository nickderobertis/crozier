

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompt_block_data_nullish_content_type import PromptBlockDataNullishContentType


class PromptBlockDataNullishContent(UniversalBaseModel):
    type: PromptBlockDataNullishContentType
    content: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
