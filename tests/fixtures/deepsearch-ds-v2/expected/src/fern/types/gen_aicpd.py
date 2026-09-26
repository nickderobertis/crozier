

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gen_ai_partial_params import GenAiPartialParams
from .gen_aicpd_config import GenAicpdConfig


class GenAicpd(UniversalBaseModel):
    """
    GenAI integration for watsonx settings
    """

    config: GenAicpdConfig
    proj_params: typing.Optional[GenAiPartialParams] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
