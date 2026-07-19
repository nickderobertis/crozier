

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_update_pipeline_response_pipeline import PipelinesUpdatePipelineResponsePipeline


class PipelinesUpdatePipelineResponse(UniversalBaseModel):
    pipeline: PipelinesUpdatePipelineResponsePipeline

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
