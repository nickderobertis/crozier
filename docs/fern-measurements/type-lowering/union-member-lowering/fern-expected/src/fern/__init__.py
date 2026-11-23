



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ExposureUnit,
        ExposureUnitOne,
        ExposureUnitZero,
        FilterBand,
        FilterBandOne,
        FilterBandZero,
        ImageSize,
        LensReading,
        Presence,
        SensorReading,
        Session,
        SessionCalibrationsValueItem,
        SessionCalibrationsValueItemOffset,
        SessionProblem,
        SessionProblemDetailsItem,
        SessionProblemDetailsItemDescription,
        SessionProblemDetailsItemDescriptionDescription,
        SessionProblemDetailsItemDescriptionIssue,
        SessionProblemDetailsItemOne,
        SessionProblemDetailsItemOneDescription,
        SessionProblemDetailsItemOneIssue,
        SessionProblemDetailsItemThree,
        SessionProblemDetailsItemThreeIssue,
        SessionReadingBatchesItemItem,
        SessionReadingBatchesItemItem_Lens,
        SessionReadingBatchesItemItem_Sensor,
        SessionReadingsByOwnerValueValue,
        SessionReadingsByOwnerValueValue_Lens,
        SessionReadingsByOwnerValueValue_Sensor,
    )
    from .errors import UnprocessableEntityError
    from . import sessions
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ExposureUnit": ".types",
    "ExposureUnitOne": ".types",
    "ExposureUnitZero": ".types",
    "FernApi": ".client",
    "FilterBand": ".types",
    "FilterBandOne": ".types",
    "FilterBandZero": ".types",
    "ImageSize": ".types",
    "LensReading": ".types",
    "Presence": ".types",
    "SensorReading": ".types",
    "Session": ".types",
    "SessionCalibrationsValueItem": ".types",
    "SessionCalibrationsValueItemOffset": ".types",
    "SessionProblem": ".types",
    "SessionProblemDetailsItem": ".types",
    "SessionProblemDetailsItemDescription": ".types",
    "SessionProblemDetailsItemDescriptionDescription": ".types",
    "SessionProblemDetailsItemDescriptionIssue": ".types",
    "SessionProblemDetailsItemOne": ".types",
    "SessionProblemDetailsItemOneDescription": ".types",
    "SessionProblemDetailsItemOneIssue": ".types",
    "SessionProblemDetailsItemThree": ".types",
    "SessionProblemDetailsItemThreeIssue": ".types",
    "SessionReadingBatchesItemItem": ".types",
    "SessionReadingBatchesItemItem_Lens": ".types",
    "SessionReadingBatchesItemItem_Sensor": ".types",
    "SessionReadingsByOwnerValueValue": ".types",
    "SessionReadingsByOwnerValueValue_Lens": ".types",
    "SessionReadingsByOwnerValueValue_Sensor": ".types",
    "UnprocessableEntityError": ".errors",
    "__version__": ".version",
    "sessions": ".sessions",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ExposureUnit",
    "ExposureUnitOne",
    "ExposureUnitZero",
    "FernApi",
    "FilterBand",
    "FilterBandOne",
    "FilterBandZero",
    "ImageSize",
    "LensReading",
    "Presence",
    "SensorReading",
    "Session",
    "SessionCalibrationsValueItem",
    "SessionCalibrationsValueItemOffset",
    "SessionProblem",
    "SessionProblemDetailsItem",
    "SessionProblemDetailsItemDescription",
    "SessionProblemDetailsItemDescriptionDescription",
    "SessionProblemDetailsItemDescriptionIssue",
    "SessionProblemDetailsItemOne",
    "SessionProblemDetailsItemOneDescription",
    "SessionProblemDetailsItemOneIssue",
    "SessionProblemDetailsItemThree",
    "SessionProblemDetailsItemThreeIssue",
    "SessionReadingBatchesItemItem",
    "SessionReadingBatchesItemItem_Lens",
    "SessionReadingBatchesItemItem_Sensor",
    "SessionReadingsByOwnerValueValue",
    "SessionReadingsByOwnerValueValue_Lens",
    "SessionReadingsByOwnerValueValue_Sensor",
    "UnprocessableEntityError",
    "__version__",
    "sessions",
]
