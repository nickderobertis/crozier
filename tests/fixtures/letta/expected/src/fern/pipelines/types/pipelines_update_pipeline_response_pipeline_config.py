

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_update_pipeline_response_pipeline_config_data import PipelinesUpdatePipelineResponsePipelineConfigData
from .pipelines_update_pipeline_response_pipeline_config_type import PipelinesUpdatePipelineResponsePipelineConfigType


class PipelinesUpdatePipelineResponsePipelineConfig(UniversalBaseModel):
    type: PipelinesUpdatePipelineResponsePipelineConfigType
    data: PipelinesUpdatePipelineResponsePipelineConfigData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
