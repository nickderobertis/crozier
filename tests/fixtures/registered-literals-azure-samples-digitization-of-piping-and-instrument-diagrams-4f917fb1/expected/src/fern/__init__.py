



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BoundingBox,
        ConnectedSymbolsConnectionItem,
        ConnectedSymbolsItem,
        FlowDirection,
        GraphConstructionInferenceResponse,
        HttpValidationError,
        ImageDetails,
        InferenceResult,
        Label,
        LineDetectionInferenceResponse,
        LineSegment,
        SymbolAndTextAssociated,
        SymbolDetectionInferenceResponse,
        TextDetectionInferenceResponse,
        TextRecognized,
        ValidationError,
        ValidationErrorLocItem,
    )
    from .errors import UnprocessableEntityError
    from . import pid_digitization
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .pid_digitization import GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BoundingBox": ".types",
    "ConnectedSymbolsConnectionItem": ".types",
    "ConnectedSymbolsItem": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FlowDirection": ".types",
    "GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse": ".pid_digitization",
    "GraphConstructionInferenceResponse": ".types",
    "HttpValidationError": ".types",
    "ImageDetails": ".types",
    "InferenceResult": ".types",
    "Label": ".types",
    "LineDetectionInferenceResponse": ".types",
    "LineSegment": ".types",
    "SymbolAndTextAssociated": ".types",
    "SymbolDetectionInferenceResponse": ".types",
    "TextDetectionInferenceResponse": ".types",
    "TextRecognized": ".types",
    "UnprocessableEntityError": ".errors",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "__version__": ".version",
    "pid_digitization": ".pid_digitization",
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
    "BoundingBox",
    "ConnectedSymbolsConnectionItem",
    "ConnectedSymbolsItem",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FlowDirection",
    "GetInferenceResultsApiPidDigitizationInferenceResultTypePidIdGetResponse",
    "GraphConstructionInferenceResponse",
    "HttpValidationError",
    "ImageDetails",
    "InferenceResult",
    "Label",
    "LineDetectionInferenceResponse",
    "LineSegment",
    "SymbolAndTextAssociated",
    "SymbolDetectionInferenceResponse",
    "TextDetectionInferenceResponse",
    "TextRecognized",
    "UnprocessableEntityError",
    "ValidationError",
    "ValidationErrorLocItem",
    "__version__",
    "pid_digitization",
]
