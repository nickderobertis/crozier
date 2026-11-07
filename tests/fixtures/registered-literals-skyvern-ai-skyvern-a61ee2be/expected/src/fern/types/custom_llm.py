

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_llm_config import CustomLlmConfig


class CustomLlm(UniversalBaseModel):
    id: str
    organization_id: str
    config: CustomLlmConfig
    created_at: str
    modified_at: str
    valid: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
