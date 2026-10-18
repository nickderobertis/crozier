

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collect_field import CollectField
from .prompt_params_prompt_template import PromptParamsPromptTemplate


class PromptParams(UniversalBaseModel):
    content: typing.Optional[str] = None
    collect_fields: typing.Optional[typing.List[CollectField]] = None
    context_endpoint: typing.Optional[str] = None
    prompt_template: typing.Optional[PromptParamsPromptTemplate] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
