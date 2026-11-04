



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CellRunResult,
        CommandRunResult,
        CommandRunStatus,
        EvalResultInput,
        EvalResultInputExtractedType,
        EvalResultInputId,
        EvalResultOutput,
        EvalResultOutputExtractedType,
        EvalResultOutputId,
        EvalTestCaseInput,
        EvalTestCaseOutput,
        GetMetricsFunctionResult,
        GetPromptsRequest,
        HttpValidationError,
        Prompt,
        PromptId,
        RunCodeResponseInput,
        RunCodeResponseOutput,
        RunJupyterResponse,
        RunStatus,
        TestConfig,
        TestConfigLanguage,
        TestConfigProvidedData,
        ValidationError,
        ValidationErrorLocItem,
    )
    from .errors import UnprocessableEntityError
    from . import datasets, sandbox
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .datasets import GetPromptByIdRequestId, ListIdsListIdsPostResponseItem, SubmitRequestId
    from .sandbox import RunCodeRequestLanguage, RunJupyterRequestKernel
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "CellRunResult": ".types",
    "CommandRunResult": ".types",
    "CommandRunStatus": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "EvalResultInput": ".types",
    "EvalResultInputExtractedType": ".types",
    "EvalResultInputId": ".types",
    "EvalResultOutput": ".types",
    "EvalResultOutputExtractedType": ".types",
    "EvalResultOutputId": ".types",
    "EvalTestCaseInput": ".types",
    "EvalTestCaseOutput": ".types",
    "FernApi": ".client",
    "GetMetricsFunctionResult": ".types",
    "GetPromptByIdRequestId": ".datasets",
    "GetPromptsRequest": ".types",
    "HttpValidationError": ".types",
    "ListIdsListIdsPostResponseItem": ".datasets",
    "Prompt": ".types",
    "PromptId": ".types",
    "RunCodeRequestLanguage": ".sandbox",
    "RunCodeResponseInput": ".types",
    "RunCodeResponseOutput": ".types",
    "RunJupyterRequestKernel": ".sandbox",
    "RunJupyterResponse": ".types",
    "RunStatus": ".types",
    "SubmitRequestId": ".datasets",
    "TestConfig": ".types",
    "TestConfigLanguage": ".types",
    "TestConfigProvidedData": ".types",
    "UnprocessableEntityError": ".errors",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "__version__": ".version",
    "datasets": ".datasets",
    "sandbox": ".sandbox",
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
    "AsyncFernApi",
    "CellRunResult",
    "CommandRunResult",
    "CommandRunStatus",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "EvalResultInput",
    "EvalResultInputExtractedType",
    "EvalResultInputId",
    "EvalResultOutput",
    "EvalResultOutputExtractedType",
    "EvalResultOutputId",
    "EvalTestCaseInput",
    "EvalTestCaseOutput",
    "FernApi",
    "GetMetricsFunctionResult",
    "GetPromptByIdRequestId",
    "GetPromptsRequest",
    "HttpValidationError",
    "ListIdsListIdsPostResponseItem",
    "Prompt",
    "PromptId",
    "RunCodeRequestLanguage",
    "RunCodeResponseInput",
    "RunCodeResponseOutput",
    "RunJupyterRequestKernel",
    "RunJupyterResponse",
    "RunStatus",
    "SubmitRequestId",
    "TestConfig",
    "TestConfigLanguage",
    "TestConfigProvidedData",
    "UnprocessableEntityError",
    "ValidationError",
    "ValidationErrorLocItem",
    "__version__",
    "datasets",
    "sandbox",
]
