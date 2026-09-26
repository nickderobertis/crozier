



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .absolute_time_range_config_model import AbsoluteTimeRangeConfigModel
    from .absolute_time_range_config_model_value import AbsoluteTimeRangeConfigModelValue
    from .relative_time_duration_model import RelativeTimeDurationModel
    from .relative_time_duration_model_unit import RelativeTimeDurationModelUnit
    from .relative_time_range_config_model import RelativeTimeRangeConfigModel
    from .relative_time_range_config_model_relative_time_type import RelativeTimeRangeConfigModelRelativeTimeType
    from .relative_time_range_config_model_value import RelativeTimeRangeConfigModelValue
    from .relative_time_range_config_model_value_unit import RelativeTimeRangeConfigModelValueUnit
    from .saved_recent_search import SavedRecentSearch
    from .search_model import SearchModel
    from .search_model_cloud_type import SearchModelCloudType
    from .search_model_search_type import SearchModelSearchType
    from .search_model_time_range import (
        SearchModelTimeRange,
        SearchModelTimeRange_Absolute,
        SearchModelTimeRange_Relative,
        SearchModelTimeRange_ToNow,
    )
    from .search_response_model_search_model import SearchResponseModelSearchModel
    from .search_response_model_search_model_cloud_type import SearchResponseModelSearchModelCloudType
    from .search_response_model_search_model_search_type import SearchResponseModelSearchModelSearchType
    from .search_response_model_search_model_time_range import (
        SearchResponseModelSearchModelTimeRange,
        SearchResponseModelSearchModelTimeRange_Absolute,
        SearchResponseModelSearchModelTimeRange_Relative,
        SearchResponseModelSearchModelTimeRange_ToNow,
    )
    from .time_model import TimeModel
    from .time_range_config_model import (
        TimeRangeConfigModel,
        TimeRangeConfigModel_Absolute,
        TimeRangeConfigModel_Relative,
        TimeRangeConfigModel_ToNow,
    )
    from .to_now_time_range_config_model import ToNowTimeRangeConfigModel
    from .to_now_time_range_config_model_value import ToNowTimeRangeConfigModelValue
    from .ui_filter_model import UiFilterModel
    from .ui_filter_model_operator import UiFilterModelOperator
_dynamic_imports: typing.Dict[str, str] = {
    "AbsoluteTimeRangeConfigModel": ".absolute_time_range_config_model",
    "AbsoluteTimeRangeConfigModelValue": ".absolute_time_range_config_model_value",
    "RelativeTimeDurationModel": ".relative_time_duration_model",
    "RelativeTimeDurationModelUnit": ".relative_time_duration_model_unit",
    "RelativeTimeRangeConfigModel": ".relative_time_range_config_model",
    "RelativeTimeRangeConfigModelRelativeTimeType": ".relative_time_range_config_model_relative_time_type",
    "RelativeTimeRangeConfigModelValue": ".relative_time_range_config_model_value",
    "RelativeTimeRangeConfigModelValueUnit": ".relative_time_range_config_model_value_unit",
    "SavedRecentSearch": ".saved_recent_search",
    "SearchModel": ".search_model",
    "SearchModelCloudType": ".search_model_cloud_type",
    "SearchModelSearchType": ".search_model_search_type",
    "SearchModelTimeRange": ".search_model_time_range",
    "SearchModelTimeRange_Absolute": ".search_model_time_range",
    "SearchModelTimeRange_Relative": ".search_model_time_range",
    "SearchModelTimeRange_ToNow": ".search_model_time_range",
    "SearchResponseModelSearchModel": ".search_response_model_search_model",
    "SearchResponseModelSearchModelCloudType": ".search_response_model_search_model_cloud_type",
    "SearchResponseModelSearchModelSearchType": ".search_response_model_search_model_search_type",
    "SearchResponseModelSearchModelTimeRange": ".search_response_model_search_model_time_range",
    "SearchResponseModelSearchModelTimeRange_Absolute": ".search_response_model_search_model_time_range",
    "SearchResponseModelSearchModelTimeRange_Relative": ".search_response_model_search_model_time_range",
    "SearchResponseModelSearchModelTimeRange_ToNow": ".search_response_model_search_model_time_range",
    "TimeModel": ".time_model",
    "TimeRangeConfigModel": ".time_range_config_model",
    "TimeRangeConfigModel_Absolute": ".time_range_config_model",
    "TimeRangeConfigModel_Relative": ".time_range_config_model",
    "TimeRangeConfigModel_ToNow": ".time_range_config_model",
    "ToNowTimeRangeConfigModel": ".to_now_time_range_config_model",
    "ToNowTimeRangeConfigModelValue": ".to_now_time_range_config_model_value",
    "UiFilterModel": ".ui_filter_model",
    "UiFilterModelOperator": ".ui_filter_model_operator",
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
]
