

import typing

from .create_extraction_pipeline_request_llm_options_reasoning_effort_one import (
    CreateExtractionPipelineRequestLlmOptionsReasoningEffortOne,
)
from .create_extraction_pipeline_request_llm_options_reasoning_effort_zero import (
    CreateExtractionPipelineRequestLlmOptionsReasoningEffortZero,
)

CreateExtractionPipelineRequestLlmOptionsReasoningEffort = typing.Union[
    CreateExtractionPipelineRequestLlmOptionsReasoningEffortZero,
    CreateExtractionPipelineRequestLlmOptionsReasoningEffortOne,
]
