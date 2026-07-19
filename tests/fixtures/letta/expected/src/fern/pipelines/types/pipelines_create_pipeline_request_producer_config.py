

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_create_pipeline_request_producer_config_data import PipelinesCreatePipelineRequestProducerConfigData
from .pipelines_create_pipeline_request_producer_config_type import PipelinesCreatePipelineRequestProducerConfigType


class PipelinesCreatePipelineRequestProducerConfig(UniversalBaseModel):
    type: PipelinesCreatePipelineRequestProducerConfigType
    data: PipelinesCreatePipelineRequestProducerConfigData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
