



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DeleteExperimentResponse,
        GetActiveExperimentResponse,
        GetActiveExperimentResponseExperiment,
        GetActiveExperimentResponseExperimentStatus,
        GetActiveExperimentResponseExperimentStatusOne,
        GetActiveExperimentResponseExperimentStatusTwo,
        GetActiveExperimentResponseExperimentStatusZero,
        GetActiveExperimentResponseExperimentStopReason,
        GetActiveExperimentResponseExperimentStopReasonOne,
        GetActiveExperimentResponseExperimentStopReasonThree,
        GetActiveExperimentResponseExperimentStopReasonTwo,
        GetActiveExperimentResponseExperimentStopReasonZero,
        GetExperimentResponse,
        GetExperimentResponseStatus,
        GetExperimentResponseStopReason,
        GetExperimentResponseStopReasonOne,
        GetExperimentResponseStopReasonThree,
        GetExperimentResponseStopReasonTwo,
        GetExperimentResponseStopReasonZero,
        ListExperimentsRequestStatus,
        ListExperimentsResponse,
        ListExperimentsResponseExperimentsItem,
        ListExperimentsResponseExperimentsItemStatus,
        ListExperimentsResponseExperimentsItemStopReason,
        ListExperimentsResponseExperimentsItemStopReasonOne,
        ListExperimentsResponseExperimentsItemStopReasonThree,
        ListExperimentsResponseExperimentsItemStopReasonTwo,
        ListExperimentsResponseExperimentsItemStopReasonZero,
        StartExperimentResponse,
        StartExperimentResponseStatus,
        StartExperimentResponseStopReason,
        StartExperimentResponseStopReasonOne,
        StartExperimentResponseStopReasonThree,
        StartExperimentResponseStopReasonTwo,
        StartExperimentResponseStopReasonZero,
        StopExperimentResponse,
        StopExperimentResponseStatus,
        StopExperimentResponseStopReason,
        StopExperimentResponseStopReasonOne,
        StopExperimentResponseStopReasonThree,
        StopExperimentResponseStopReasonTwo,
        StopExperimentResponseStopReasonZero,
        UpdateExperimentResponse,
        UpdateExperimentResponseStatus,
        UpdateExperimentResponseStopReason,
        UpdateExperimentResponseStopReasonOne,
        UpdateExperimentResponseStopReasonThree,
        UpdateExperimentResponseStopReasonTwo,
        UpdateExperimentResponseStopReasonZero,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteExperimentResponse": ".types",
    "GetActiveExperimentResponse": ".types",
    "GetActiveExperimentResponseExperiment": ".types",
    "GetActiveExperimentResponseExperimentStatus": ".types",
    "GetActiveExperimentResponseExperimentStatusOne": ".types",
    "GetActiveExperimentResponseExperimentStatusTwo": ".types",
    "GetActiveExperimentResponseExperimentStatusZero": ".types",
    "GetActiveExperimentResponseExperimentStopReason": ".types",
    "GetActiveExperimentResponseExperimentStopReasonOne": ".types",
    "GetActiveExperimentResponseExperimentStopReasonThree": ".types",
    "GetActiveExperimentResponseExperimentStopReasonTwo": ".types",
    "GetActiveExperimentResponseExperimentStopReasonZero": ".types",
    "GetExperimentResponse": ".types",
    "GetExperimentResponseStatus": ".types",
    "GetExperimentResponseStopReason": ".types",
    "GetExperimentResponseStopReasonOne": ".types",
    "GetExperimentResponseStopReasonThree": ".types",
    "GetExperimentResponseStopReasonTwo": ".types",
    "GetExperimentResponseStopReasonZero": ".types",
    "ListExperimentsRequestStatus": ".types",
    "ListExperimentsResponse": ".types",
    "ListExperimentsResponseExperimentsItem": ".types",
    "ListExperimentsResponseExperimentsItemStatus": ".types",
    "ListExperimentsResponseExperimentsItemStopReason": ".types",
    "ListExperimentsResponseExperimentsItemStopReasonOne": ".types",
    "ListExperimentsResponseExperimentsItemStopReasonThree": ".types",
    "ListExperimentsResponseExperimentsItemStopReasonTwo": ".types",
    "ListExperimentsResponseExperimentsItemStopReasonZero": ".types",
    "StartExperimentResponse": ".types",
    "StartExperimentResponseStatus": ".types",
    "StartExperimentResponseStopReason": ".types",
    "StartExperimentResponseStopReasonOne": ".types",
    "StartExperimentResponseStopReasonThree": ".types",
    "StartExperimentResponseStopReasonTwo": ".types",
    "StartExperimentResponseStopReasonZero": ".types",
    "StopExperimentResponse": ".types",
    "StopExperimentResponseStatus": ".types",
    "StopExperimentResponseStopReason": ".types",
    "StopExperimentResponseStopReasonOne": ".types",
    "StopExperimentResponseStopReasonThree": ".types",
    "StopExperimentResponseStopReasonTwo": ".types",
    "StopExperimentResponseStopReasonZero": ".types",
    "UpdateExperimentResponse": ".types",
    "UpdateExperimentResponseStatus": ".types",
    "UpdateExperimentResponseStopReason": ".types",
    "UpdateExperimentResponseStopReasonOne": ".types",
    "UpdateExperimentResponseStopReasonThree": ".types",
    "UpdateExperimentResponseStopReasonTwo": ".types",
    "UpdateExperimentResponseStopReasonZero": ".types",
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
    "DeleteExperimentResponse",
    "GetActiveExperimentResponse",
    "GetActiveExperimentResponseExperiment",
    "GetActiveExperimentResponseExperimentStatus",
    "GetActiveExperimentResponseExperimentStatusOne",
    "GetActiveExperimentResponseExperimentStatusTwo",
    "GetActiveExperimentResponseExperimentStatusZero",
    "GetActiveExperimentResponseExperimentStopReason",
    "GetActiveExperimentResponseExperimentStopReasonOne",
    "GetActiveExperimentResponseExperimentStopReasonThree",
    "GetActiveExperimentResponseExperimentStopReasonTwo",
    "GetActiveExperimentResponseExperimentStopReasonZero",
    "GetExperimentResponse",
    "GetExperimentResponseStatus",
    "GetExperimentResponseStopReason",
    "GetExperimentResponseStopReasonOne",
    "GetExperimentResponseStopReasonThree",
    "GetExperimentResponseStopReasonTwo",
    "GetExperimentResponseStopReasonZero",
    "ListExperimentsRequestStatus",
    "ListExperimentsResponse",
    "ListExperimentsResponseExperimentsItem",
    "ListExperimentsResponseExperimentsItemStatus",
    "ListExperimentsResponseExperimentsItemStopReason",
    "ListExperimentsResponseExperimentsItemStopReasonOne",
    "ListExperimentsResponseExperimentsItemStopReasonThree",
    "ListExperimentsResponseExperimentsItemStopReasonTwo",
    "ListExperimentsResponseExperimentsItemStopReasonZero",
    "StartExperimentResponse",
    "StartExperimentResponseStatus",
    "StartExperimentResponseStopReason",
    "StartExperimentResponseStopReasonOne",
    "StartExperimentResponseStopReasonThree",
    "StartExperimentResponseStopReasonTwo",
    "StartExperimentResponseStopReasonZero",
    "StopExperimentResponse",
    "StopExperimentResponseStatus",
    "StopExperimentResponseStopReason",
    "StopExperimentResponseStopReasonOne",
    "StopExperimentResponseStopReasonThree",
    "StopExperimentResponseStopReasonTwo",
    "StopExperimentResponseStopReasonZero",
    "UpdateExperimentResponse",
    "UpdateExperimentResponseStatus",
    "UpdateExperimentResponseStopReason",
    "UpdateExperimentResponseStopReasonOne",
    "UpdateExperimentResponseStopReasonThree",
    "UpdateExperimentResponseStopReasonTwo",
    "UpdateExperimentResponseStopReasonZero",
]
