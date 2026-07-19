

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_get_pipeline_response_pipeline_config_data import PipelinesGetPipelineResponsePipelineConfigData
from .pipelines_get_pipeline_response_pipeline_config_type import PipelinesGetPipelineResponsePipelineConfigType


class PipelinesGetPipelineResponsePipelineConfig(UniversalBaseModel):
    type: PipelinesGetPipelineResponsePipelineConfigType
    data: PipelinesGetPipelineResponsePipelineConfigData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
