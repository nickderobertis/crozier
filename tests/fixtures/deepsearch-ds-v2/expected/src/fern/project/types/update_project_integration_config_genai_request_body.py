

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.gen_ai_openai_config import GenAiOpenaiConfig
from ...types.gen_ai_partial_params import GenAiPartialParams
from ...types.gen_ai_watsonx_config import GenAiWatsonxConfig
from ...types.gen_aiaws_bedrock_config import GenAiawsBedrockConfig
from ...types.gen_aibam_config import GenAibamConfig
from ...types.gen_aicpd_config import GenAicpdConfig
from ...types.gen_aihf_inference_api_config import GenAihfInferenceApiConfig


class UpdateProjectIntegrationConfigGenaiRequestBody_Bam(UniversalBaseModel):
    kind: typing.Literal["bam"] = "bam"
    config: GenAibamConfig
    proj_params: typing.Optional[GenAiPartialParams] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateProjectIntegrationConfigGenaiRequestBody_Watsonx(UniversalBaseModel):
    kind: typing.Literal["watsonx"] = "watsonx"
    config: GenAiWatsonxConfig
    proj_params: typing.Optional[GenAiPartialParams] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateProjectIntegrationConfigGenaiRequestBody_Cpd(UniversalBaseModel):
    kind: typing.Literal["cpd"] = "cpd"
    config: GenAicpdConfig
    proj_params: typing.Optional[GenAiPartialParams] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateProjectIntegrationConfigGenaiRequestBody_HfApi(UniversalBaseModel):
    kind: typing.Literal["hf_api"] = "hf_api"
    config: GenAihfInferenceApiConfig
    proj_params: typing.Optional[GenAiPartialParams] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateProjectIntegrationConfigGenaiRequestBody_Openai(UniversalBaseModel):
    kind: typing.Literal["openai"] = "openai"
    config: GenAiOpenaiConfig
    proj_params: typing.Optional[GenAiPartialParams] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateProjectIntegrationConfigGenaiRequestBody_AwsBedrock(UniversalBaseModel):
    kind: typing.Literal["aws_bedrock"] = "aws_bedrock"
    config: GenAiawsBedrockConfig
    proj_params: typing.Optional[GenAiPartialParams] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UpdateProjectIntegrationConfigGenaiRequestBody = typing_extensions.Annotated[
    typing.Union[
        UpdateProjectIntegrationConfigGenaiRequestBody_Bam,
        UpdateProjectIntegrationConfigGenaiRequestBody_Watsonx,
        UpdateProjectIntegrationConfigGenaiRequestBody_Cpd,
        UpdateProjectIntegrationConfigGenaiRequestBody_HfApi,
        UpdateProjectIntegrationConfigGenaiRequestBody_Openai,
        UpdateProjectIntegrationConfigGenaiRequestBody_AwsBedrock,
    ],
    pydantic.Field(discriminator="kind"),
]
