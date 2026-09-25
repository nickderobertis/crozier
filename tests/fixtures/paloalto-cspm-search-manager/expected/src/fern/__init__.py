



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AbsoluteTimeRangeConfigModel,
        AbsoluteTimeRangeConfigModelValue,
        RelativeTimeDurationModel,
        RelativeTimeDurationModelUnit,
        RelativeTimeRangeConfigModel,
        RelativeTimeRangeConfigModelRelativeTimeType,
        RelativeTimeRangeConfigModelValue,
        RelativeTimeRangeConfigModelValueUnit,
        SavedRecentSearch,
        SearchModel,
        SearchModelCloudType,
        SearchModelSearchType,
        SearchModelTimeRange,
        SearchModelTimeRange_Absolute,
        SearchModelTimeRange_Relative,
        SearchModelTimeRange_ToNow,
        SearchResponseModelSearchModel,
        SearchResponseModelSearchModelCloudType,
        SearchResponseModelSearchModelSearchType,
        SearchResponseModelSearchModelTimeRange,
        SearchResponseModelSearchModelTimeRange_Absolute,
        SearchResponseModelSearchModelTimeRange_Relative,
        SearchResponseModelSearchModelTimeRange_ToNow,
        TimeModel,
        TimeRangeConfigModel,
        TimeRangeConfigModel_Absolute,
        TimeRangeConfigModel_Relative,
        TimeRangeConfigModel_ToNow,
        ToNowTimeRangeConfigModel,
        ToNowTimeRangeConfigModelValue,
        UiFilterModel,
        UiFilterModelOperator,
    )
    from .errors import BadRequestError, ConflictError, ForbiddenError, NotFoundError
    from . import search_manager
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AbsoluteTimeRangeConfigModel": ".types",
    "AbsoluteTimeRangeConfigModelValue": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConflictError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "NotFoundError": ".errors",
    "RelativeTimeDurationModel": ".types",
    "RelativeTimeDurationModelUnit": ".types",
    "RelativeTimeRangeConfigModel": ".types",
    "RelativeTimeRangeConfigModelRelativeTimeType": ".types",
    "RelativeTimeRangeConfigModelValue": ".types",
    "RelativeTimeRangeConfigModelValueUnit": ".types",
    "SavedRecentSearch": ".types",
    "SearchModel": ".types",
    "SearchModelCloudType": ".types",
    "SearchModelSearchType": ".types",
    "SearchModelTimeRange": ".types",
    "SearchModelTimeRange_Absolute": ".types",
    "SearchModelTimeRange_Relative": ".types",
    "SearchModelTimeRange_ToNow": ".types",
    "SearchResponseModelSearchModel": ".types",
    "SearchResponseModelSearchModelCloudType": ".types",
    "SearchResponseModelSearchModelSearchType": ".types",
    "SearchResponseModelSearchModelTimeRange": ".types",
    "SearchResponseModelSearchModelTimeRange_Absolute": ".types",
    "SearchResponseModelSearchModelTimeRange_Relative": ".types",
    "SearchResponseModelSearchModelTimeRange_ToNow": ".types",
    "TimeModel": ".types",
    "TimeRangeConfigModel": ".types",
    "TimeRangeConfigModel_Absolute": ".types",
    "TimeRangeConfigModel_Relative": ".types",
    "TimeRangeConfigModel_ToNow": ".types",
    "ToNowTimeRangeConfigModel": ".types",
    "ToNowTimeRangeConfigModelValue": ".types",
    "UiFilterModel": ".types",
    "UiFilterModelOperator": ".types",
    "__version__": ".version",
    "search_manager": ".search_manager",
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
    "AbsoluteTimeRangeConfigModel",
    "AbsoluteTimeRangeConfigModelValue",
    "AsyncFernApi",
    "BadRequestError",
    "ConflictError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "NotFoundError",
    "RelativeTimeDurationModel",
    "RelativeTimeDurationModelUnit",
    "RelativeTimeRangeConfigModel",
    "RelativeTimeRangeConfigModelRelativeTimeType",
    "RelativeTimeRangeConfigModelValue",
    "RelativeTimeRangeConfigModelValueUnit",
    "SavedRecentSearch",
    "SearchModel",
    "SearchModelCloudType",
    "SearchModelSearchType",
    "SearchModelTimeRange",
    "SearchModelTimeRange_Absolute",
    "SearchModelTimeRange_Relative",
    "SearchModelTimeRange_ToNow",
    "SearchResponseModelSearchModel",
    "SearchResponseModelSearchModelCloudType",
    "SearchResponseModelSearchModelSearchType",
    "SearchResponseModelSearchModelTimeRange",
    "SearchResponseModelSearchModelTimeRange_Absolute",
    "SearchResponseModelSearchModelTimeRange_Relative",
    "SearchResponseModelSearchModelTimeRange_ToNow",
    "TimeModel",
    "TimeRangeConfigModel",
    "TimeRangeConfigModel_Absolute",
    "TimeRangeConfigModel_Relative",
    "TimeRangeConfigModel_ToNow",
    "ToNowTimeRangeConfigModel",
    "ToNowTimeRangeConfigModelValue",
    "UiFilterModel",
    "UiFilterModelOperator",
    "__version__",
    "search_manager",
]
