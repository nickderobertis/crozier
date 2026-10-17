

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompt_update_params_collect_fields import PromptUpdateParamsCollectFields
from .prompt_update_params_content import PromptUpdateParamsContent
from .prompt_update_params_context_endpoint import PromptUpdateParamsContextEndpoint
from .prompt_update_params_prompt_template import PromptUpdateParamsPromptTemplate


class PromptUpdateParams(UniversalBaseModel):
    content: typing.Optional[PromptUpdateParamsContent] = None
    collect_fields: typing.Optional[PromptUpdateParamsCollectFields] = None
    context_endpoint: typing.Optional[PromptUpdateParamsContextEndpoint] = None
    prompt_template: typing.Optional[PromptUpdateParamsPromptTemplate] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
