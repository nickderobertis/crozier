



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AlertsLookupKeyModelFilter,
        AlertsLookupKeyModelFilterTimeRange,
        AlertsLookupKeyModelFilterTimeRange_Absolute,
        AlertsLookupKeyModelFilterTimeRange_Relative,
        AlertsLookupKeyModelFilterTimeRange_ToNow,
        GetAlertCountRequestStatus,
        GetAlertsGroupedRequestAlertStatus,
        GetAlertsGroupedRequestPolicyRemediable,
        GetAlertsGroupedRequestPolicySeverity,
        GetAlertsGroupedRequestPolicyType,
        GetAlertsRequestAlertStatus,
        GetAlertsRequestPolicyRemediable,
        GetAlertsRequestPolicySeverity,
        GetAlertsRequestPolicyType,
        GetAlertsRequestTimeType,
        GetAlertsRequestTimeUnit,
        GetAlertsV2RequestAlertStatus,
        GetAlertsV2RequestPolicyRemediable,
        GetAlertsV2RequestPolicySeverity,
        GetAlertsV2RequestPolicyType,
        GetAlertsV2RequestTimeType,
        GetAlertsV2RequestTimeUnit,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AlertsLookupKeyModelFilter": ".types",
    "AlertsLookupKeyModelFilterTimeRange": ".types",
    "AlertsLookupKeyModelFilterTimeRange_Absolute": ".types",
    "AlertsLookupKeyModelFilterTimeRange_Relative": ".types",
    "AlertsLookupKeyModelFilterTimeRange_ToNow": ".types",
    "GetAlertCountRequestStatus": ".types",
    "GetAlertsGroupedRequestAlertStatus": ".types",
    "GetAlertsGroupedRequestPolicyRemediable": ".types",
    "GetAlertsGroupedRequestPolicySeverity": ".types",
    "GetAlertsGroupedRequestPolicyType": ".types",
    "GetAlertsRequestAlertStatus": ".types",
    "GetAlertsRequestPolicyRemediable": ".types",
    "GetAlertsRequestPolicySeverity": ".types",
    "GetAlertsRequestPolicyType": ".types",
    "GetAlertsRequestTimeType": ".types",
    "GetAlertsRequestTimeUnit": ".types",
    "GetAlertsV2RequestAlertStatus": ".types",
    "GetAlertsV2RequestPolicyRemediable": ".types",
    "GetAlertsV2RequestPolicySeverity": ".types",
    "GetAlertsV2RequestPolicyType": ".types",
    "GetAlertsV2RequestTimeType": ".types",
    "GetAlertsV2RequestTimeUnit": ".types",
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
    "AlertsLookupKeyModelFilter",
    "AlertsLookupKeyModelFilterTimeRange",
    "AlertsLookupKeyModelFilterTimeRange_Absolute",
    "AlertsLookupKeyModelFilterTimeRange_Relative",
    "AlertsLookupKeyModelFilterTimeRange_ToNow",
    "GetAlertCountRequestStatus",
    "GetAlertsGroupedRequestAlertStatus",
    "GetAlertsGroupedRequestPolicyRemediable",
    "GetAlertsGroupedRequestPolicySeverity",
    "GetAlertsGroupedRequestPolicyType",
    "GetAlertsRequestAlertStatus",
    "GetAlertsRequestPolicyRemediable",
    "GetAlertsRequestPolicySeverity",
    "GetAlertsRequestPolicyType",
    "GetAlertsRequestTimeType",
    "GetAlertsRequestTimeUnit",
    "GetAlertsV2RequestAlertStatus",
    "GetAlertsV2RequestPolicyRemediable",
    "GetAlertsV2RequestPolicySeverity",
    "GetAlertsV2RequestPolicyType",
    "GetAlertsV2RequestTimeType",
    "GetAlertsV2RequestTimeUnit",
]
