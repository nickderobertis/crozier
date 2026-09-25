

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gen_ai_partial_params import GenAiPartialParams
from .gen_aihf_inference_api_config import GenAihfInferenceApiConfig


class GenAihfInferenceApi(UniversalBaseModel):
    """
    GenAI integration for Inference API settings
    """

    config: GenAihfInferenceApiConfig
    proj_params: typing.Optional[GenAiPartialParams] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
