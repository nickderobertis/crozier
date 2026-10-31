



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_extraction_pipeline_request_grounding import CreateExtractionPipelineRequestGrounding
    from .create_extraction_pipeline_request_llm_options import CreateExtractionPipelineRequestLlmOptions
    from .create_extraction_pipeline_request_llm_options_reasoning_effort import (
        CreateExtractionPipelineRequestLlmOptionsReasoningEffort,
    )
    from .create_extraction_pipeline_request_llm_options_reasoning_effort_one import (
        CreateExtractionPipelineRequestLlmOptionsReasoningEffortOne,
    )
    from .create_extraction_pipeline_request_llm_options_reasoning_effort_zero import (
        CreateExtractionPipelineRequestLlmOptionsReasoningEffortZero,
    )
    from .update_extraction_pipeline_request_grounding import UpdateExtractionPipelineRequestGrounding
    from .update_extraction_pipeline_request_llm_options import UpdateExtractionPipelineRequestLlmOptions
    from .update_extraction_pipeline_request_llm_options_reasoning_effort import (
        UpdateExtractionPipelineRequestLlmOptionsReasoningEffort,
    )
    from .update_extraction_pipeline_request_llm_options_reasoning_effort_one import (
        UpdateExtractionPipelineRequestLlmOptionsReasoningEffortOne,
    )
    from .update_extraction_pipeline_request_llm_options_reasoning_effort_zero import (
        UpdateExtractionPipelineRequestLlmOptionsReasoningEffortZero,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateExtractionPipelineRequestGrounding": ".create_extraction_pipeline_request_grounding",
    "CreateExtractionPipelineRequestLlmOptions": ".create_extraction_pipeline_request_llm_options",
    "CreateExtractionPipelineRequestLlmOptionsReasoningEffort": ".create_extraction_pipeline_request_llm_options_reasoning_effort",
    "CreateExtractionPipelineRequestLlmOptionsReasoningEffortOne": ".create_extraction_pipeline_request_llm_options_reasoning_effort_one",
    "CreateExtractionPipelineRequestLlmOptionsReasoningEffortZero": ".create_extraction_pipeline_request_llm_options_reasoning_effort_zero",
    "UpdateExtractionPipelineRequestGrounding": ".update_extraction_pipeline_request_grounding",
    "UpdateExtractionPipelineRequestLlmOptions": ".update_extraction_pipeline_request_llm_options",
    "UpdateExtractionPipelineRequestLlmOptionsReasoningEffort": ".update_extraction_pipeline_request_llm_options_reasoning_effort",
    "UpdateExtractionPipelineRequestLlmOptionsReasoningEffortOne": ".update_extraction_pipeline_request_llm_options_reasoning_effort_one",
    "UpdateExtractionPipelineRequestLlmOptionsReasoningEffortZero": ".update_extraction_pipeline_request_llm_options_reasoning_effort_zero",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "CreateExtractionPipelineRequestGrounding",
    "CreateExtractionPipelineRequestLlmOptions",
    "CreateExtractionPipelineRequestLlmOptionsReasoningEffort",
    "CreateExtractionPipelineRequestLlmOptionsReasoningEffortOne",
    "CreateExtractionPipelineRequestLlmOptionsReasoningEffortZero",
    "UpdateExtractionPipelineRequestGrounding",
    "UpdateExtractionPipelineRequestLlmOptions",
    "UpdateExtractionPipelineRequestLlmOptionsReasoningEffort",
    "UpdateExtractionPipelineRequestLlmOptionsReasoningEffortOne",
    "UpdateExtractionPipelineRequestLlmOptionsReasoningEffortZero",
]
