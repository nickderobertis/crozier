



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cell_run_result import CellRunResult
    from .command_run_result import CommandRunResult
    from .command_run_status import CommandRunStatus
    from .eval_result_input import EvalResultInput
    from .eval_result_input_extracted_type import EvalResultInputExtractedType
    from .eval_result_input_id import EvalResultInputId
    from .eval_result_output import EvalResultOutput
    from .eval_result_output_extracted_type import EvalResultOutputExtractedType
    from .eval_result_output_id import EvalResultOutputId
    from .eval_test_case_input import EvalTestCaseInput
    from .eval_test_case_output import EvalTestCaseOutput
    from .get_metrics_function_result import GetMetricsFunctionResult
    from .get_prompts_request import GetPromptsRequest
    from .http_validation_error import HttpValidationError
    from .prompt import Prompt
    from .prompt_id import PromptId
    from .run_code_response_input import RunCodeResponseInput
    from .run_code_response_output import RunCodeResponseOutput
    from .run_jupyter_response import RunJupyterResponse
    from .run_status import RunStatus
    from .test_config import TestConfig
    from .test_config_language import TestConfigLanguage
    from .test_config_provided_data import TestConfigProvidedData
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "CellRunResult": ".cell_run_result",
    "CommandRunResult": ".command_run_result",
    "CommandRunStatus": ".command_run_status",
    "EvalResultInput": ".eval_result_input",
    "EvalResultInputExtractedType": ".eval_result_input_extracted_type",
    "EvalResultInputId": ".eval_result_input_id",
    "EvalResultOutput": ".eval_result_output",
    "EvalResultOutputExtractedType": ".eval_result_output_extracted_type",
    "EvalResultOutputId": ".eval_result_output_id",
    "EvalTestCaseInput": ".eval_test_case_input",
    "EvalTestCaseOutput": ".eval_test_case_output",
    "GetMetricsFunctionResult": ".get_metrics_function_result",
    "GetPromptsRequest": ".get_prompts_request",
    "HttpValidationError": ".http_validation_error",
    "Prompt": ".prompt",
    "PromptId": ".prompt_id",
    "RunCodeResponseInput": ".run_code_response_input",
    "RunCodeResponseOutput": ".run_code_response_output",
    "RunJupyterResponse": ".run_jupyter_response",
    "RunStatus": ".run_status",
    "TestConfig": ".test_config",
    "TestConfigLanguage": ".test_config_language",
    "TestConfigProvidedData": ".test_config_provided_data",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "CellRunResult",
    "CommandRunResult",
    "CommandRunStatus",
    "EvalResultInput",
    "EvalResultInputExtractedType",
    "EvalResultInputId",
    "EvalResultOutput",
    "EvalResultOutputExtractedType",
    "EvalResultOutputId",
    "EvalTestCaseInput",
    "EvalTestCaseOutput",
    "GetMetricsFunctionResult",
    "GetPromptsRequest",
    "HttpValidationError",
    "Prompt",
    "PromptId",
    "RunCodeResponseInput",
    "RunCodeResponseOutput",
    "RunJupyterResponse",
    "RunStatus",
    "TestConfig",
    "TestConfigLanguage",
    "TestConfigProvidedData",
    "ValidationError",
    "ValidationErrorLocItem",
]
