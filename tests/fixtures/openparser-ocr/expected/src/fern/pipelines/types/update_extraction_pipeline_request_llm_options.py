

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_extraction_pipeline_request_llm_options_reasoning_effort import (
    UpdateExtractionPipelineRequestLlmOptionsReasoningEffort,
)


class UpdateExtractionPipelineRequestLlmOptions(UniversalBaseModel):
    reasoning_effort: typing.Optional[UpdateExtractionPipelineRequestLlmOptionsReasoningEffort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
