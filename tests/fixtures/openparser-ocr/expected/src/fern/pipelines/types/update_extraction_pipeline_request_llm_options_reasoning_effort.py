

import typing

from .update_extraction_pipeline_request_llm_options_reasoning_effort_one import (
    UpdateExtractionPipelineRequestLlmOptionsReasoningEffortOne,
)
from .update_extraction_pipeline_request_llm_options_reasoning_effort_zero import (
    UpdateExtractionPipelineRequestLlmOptionsReasoningEffortZero,
)

UpdateExtractionPipelineRequestLlmOptionsReasoningEffort = typing.Union[
    UpdateExtractionPipelineRequestLlmOptionsReasoningEffortZero,
    UpdateExtractionPipelineRequestLlmOptionsReasoningEffortOne,
]
