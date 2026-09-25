



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .alerts_lookup_key_model_filter import AlertsLookupKeyModelFilter
    from .alerts_lookup_key_model_filter_time_range import (
        AlertsLookupKeyModelFilterTimeRange,
        AlertsLookupKeyModelFilterTimeRange_Absolute,
        AlertsLookupKeyModelFilterTimeRange_Relative,
        AlertsLookupKeyModelFilterTimeRange_ToNow,
    )
    from .get_alert_count_request_status import GetAlertCountRequestStatus
    from .get_alerts_grouped_request_alert_status import GetAlertsGroupedRequestAlertStatus
    from .get_alerts_grouped_request_policy_remediable import GetAlertsGroupedRequestPolicyRemediable
    from .get_alerts_grouped_request_policy_severity import GetAlertsGroupedRequestPolicySeverity
    from .get_alerts_grouped_request_policy_type import GetAlertsGroupedRequestPolicyType
    from .get_alerts_request_alert_status import GetAlertsRequestAlertStatus
    from .get_alerts_request_policy_remediable import GetAlertsRequestPolicyRemediable
    from .get_alerts_request_policy_severity import GetAlertsRequestPolicySeverity
    from .get_alerts_request_policy_type import GetAlertsRequestPolicyType
    from .get_alerts_request_time_type import GetAlertsRequestTimeType
    from .get_alerts_request_time_unit import GetAlertsRequestTimeUnit
    from .get_alerts_v2request_alert_status import GetAlertsV2RequestAlertStatus
    from .get_alerts_v2request_policy_remediable import GetAlertsV2RequestPolicyRemediable
    from .get_alerts_v2request_policy_severity import GetAlertsV2RequestPolicySeverity
    from .get_alerts_v2request_policy_type import GetAlertsV2RequestPolicyType
    from .get_alerts_v2request_time_type import GetAlertsV2RequestTimeType
    from .get_alerts_v2request_time_unit import GetAlertsV2RequestTimeUnit
_dynamic_imports: typing.Dict[str, str] = {
    "AlertsLookupKeyModelFilter": ".alerts_lookup_key_model_filter",
    "AlertsLookupKeyModelFilterTimeRange": ".alerts_lookup_key_model_filter_time_range",
    "AlertsLookupKeyModelFilterTimeRange_Absolute": ".alerts_lookup_key_model_filter_time_range",
    "AlertsLookupKeyModelFilterTimeRange_Relative": ".alerts_lookup_key_model_filter_time_range",
    "AlertsLookupKeyModelFilterTimeRange_ToNow": ".alerts_lookup_key_model_filter_time_range",
    "GetAlertCountRequestStatus": ".get_alert_count_request_status",
    "GetAlertsGroupedRequestAlertStatus": ".get_alerts_grouped_request_alert_status",
    "GetAlertsGroupedRequestPolicyRemediable": ".get_alerts_grouped_request_policy_remediable",
    "GetAlertsGroupedRequestPolicySeverity": ".get_alerts_grouped_request_policy_severity",
    "GetAlertsGroupedRequestPolicyType": ".get_alerts_grouped_request_policy_type",
    "GetAlertsRequestAlertStatus": ".get_alerts_request_alert_status",
    "GetAlertsRequestPolicyRemediable": ".get_alerts_request_policy_remediable",
    "GetAlertsRequestPolicySeverity": ".get_alerts_request_policy_severity",
    "GetAlertsRequestPolicyType": ".get_alerts_request_policy_type",
    "GetAlertsRequestTimeType": ".get_alerts_request_time_type",
    "GetAlertsRequestTimeUnit": ".get_alerts_request_time_unit",
    "GetAlertsV2RequestAlertStatus": ".get_alerts_v2request_alert_status",
    "GetAlertsV2RequestPolicyRemediable": ".get_alerts_v2request_policy_remediable",
    "GetAlertsV2RequestPolicySeverity": ".get_alerts_v2request_policy_severity",
    "GetAlertsV2RequestPolicyType": ".get_alerts_v2request_policy_type",
    "GetAlertsV2RequestTimeType": ".get_alerts_v2request_time_type",
    "GetAlertsV2RequestTimeUnit": ".get_alerts_v2request_time_unit",
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
