

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_get_pipeline_response_pipeline import PipelinesGetPipelineResponsePipeline


class PipelinesGetPipelineResponse(UniversalBaseModel):
    pipeline: PipelinesGetPipelineResponsePipeline

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
