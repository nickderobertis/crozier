

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_preview_pipeline_request_producer_config_data import PipelinesPreviewPipelineRequestProducerConfigData
from .pipelines_preview_pipeline_request_producer_config_type import PipelinesPreviewPipelineRequestProducerConfigType


class PipelinesPreviewPipelineRequestProducerConfig(UniversalBaseModel):
    type: PipelinesPreviewPipelineRequestProducerConfigType
    data: PipelinesPreviewPipelineRequestProducerConfigData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
