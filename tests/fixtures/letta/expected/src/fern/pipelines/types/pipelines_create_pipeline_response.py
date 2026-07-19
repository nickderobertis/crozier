

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_create_pipeline_response_pipeline import PipelinesCreatePipelineResponsePipeline


class PipelinesCreatePipelineResponse(UniversalBaseModel):
    pipeline: PipelinesCreatePipelineResponsePipeline

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
