



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .monitoring_projects_dashboards_create_request_alt import MonitoringProjectsDashboardsCreateRequestAlt
    from .monitoring_projects_dashboards_create_request_xgafv import MonitoringProjectsDashboardsCreateRequestXgafv
    from .monitoring_projects_dashboards_delete_request_alt import MonitoringProjectsDashboardsDeleteRequestAlt
    from .monitoring_projects_dashboards_delete_request_xgafv import MonitoringProjectsDashboardsDeleteRequestXgafv
    from .monitoring_projects_dashboards_get_request_alt import MonitoringProjectsDashboardsGetRequestAlt
    from .monitoring_projects_dashboards_get_request_xgafv import MonitoringProjectsDashboardsGetRequestXgafv
    from .monitoring_projects_dashboards_list_request_alt import MonitoringProjectsDashboardsListRequestAlt
    from .monitoring_projects_dashboards_list_request_xgafv import MonitoringProjectsDashboardsListRequestXgafv
    from .monitoring_projects_dashboards_patch_request_alt import MonitoringProjectsDashboardsPatchRequestAlt
    from .monitoring_projects_dashboards_patch_request_xgafv import MonitoringProjectsDashboardsPatchRequestXgafv
    from .monitoring_projects_location_prometheus_api_v1label_values_request_alt import (
        MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt,
    )
    from .monitoring_projects_location_prometheus_api_v1label_values_request_xgafv import (
        MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv,
    )
    from .monitoring_projects_location_prometheus_api_v1labels_request_alt import (
        MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt,
    )
    from .monitoring_projects_location_prometheus_api_v1labels_request_xgafv import (
        MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv,
    )
    from .monitoring_projects_location_prometheus_api_v1metadata_list_request_alt import (
        MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt,
    )
    from .monitoring_projects_location_prometheus_api_v1metadata_list_request_xgafv import (
        MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv,
    )
    from .monitoring_projects_location_prometheus_api_v1query_exemplars_request_alt import (
        MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt,
    )
    from .monitoring_projects_location_prometheus_api_v1query_exemplars_request_xgafv import (
        MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv,
    )
    from .monitoring_projects_location_prometheus_api_v1query_range_request_alt import (
        MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt,
    )
    from .monitoring_projects_location_prometheus_api_v1query_range_request_xgafv import (
        MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv,
    )
    from .monitoring_projects_location_prometheus_api_v1query_request_alt import (
        MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt,
    )
    from .monitoring_projects_location_prometheus_api_v1query_request_xgafv import (
        MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv,
    )
    from .monitoring_projects_location_prometheus_api_v1series_request_alt import (
        MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt,
    )
    from .monitoring_projects_location_prometheus_api_v1series_request_xgafv import (
        MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "MonitoringProjectsDashboardsCreateRequestAlt": ".monitoring_projects_dashboards_create_request_alt",
    "MonitoringProjectsDashboardsCreateRequestXgafv": ".monitoring_projects_dashboards_create_request_xgafv",
    "MonitoringProjectsDashboardsDeleteRequestAlt": ".monitoring_projects_dashboards_delete_request_alt",
    "MonitoringProjectsDashboardsDeleteRequestXgafv": ".monitoring_projects_dashboards_delete_request_xgafv",
    "MonitoringProjectsDashboardsGetRequestAlt": ".monitoring_projects_dashboards_get_request_alt",
    "MonitoringProjectsDashboardsGetRequestXgafv": ".monitoring_projects_dashboards_get_request_xgafv",
    "MonitoringProjectsDashboardsListRequestAlt": ".monitoring_projects_dashboards_list_request_alt",
    "MonitoringProjectsDashboardsListRequestXgafv": ".monitoring_projects_dashboards_list_request_xgafv",
    "MonitoringProjectsDashboardsPatchRequestAlt": ".monitoring_projects_dashboards_patch_request_alt",
    "MonitoringProjectsDashboardsPatchRequestXgafv": ".monitoring_projects_dashboards_patch_request_xgafv",
    "MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt": ".monitoring_projects_location_prometheus_api_v1label_values_request_alt",
    "MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv": ".monitoring_projects_location_prometheus_api_v1label_values_request_xgafv",
    "MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt": ".monitoring_projects_location_prometheus_api_v1labels_request_alt",
    "MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv": ".monitoring_projects_location_prometheus_api_v1labels_request_xgafv",
    "MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt": ".monitoring_projects_location_prometheus_api_v1metadata_list_request_alt",
    "MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv": ".monitoring_projects_location_prometheus_api_v1metadata_list_request_xgafv",
    "MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt": ".monitoring_projects_location_prometheus_api_v1query_exemplars_request_alt",
    "MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv": ".monitoring_projects_location_prometheus_api_v1query_exemplars_request_xgafv",
    "MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt": ".monitoring_projects_location_prometheus_api_v1query_range_request_alt",
    "MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv": ".monitoring_projects_location_prometheus_api_v1query_range_request_xgafv",
    "MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt": ".monitoring_projects_location_prometheus_api_v1query_request_alt",
    "MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv": ".monitoring_projects_location_prometheus_api_v1query_request_xgafv",
    "MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt": ".monitoring_projects_location_prometheus_api_v1series_request_alt",
    "MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv": ".monitoring_projects_location_prometheus_api_v1series_request_xgafv",
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
    "MonitoringProjectsDashboardsCreateRequestAlt",
    "MonitoringProjectsDashboardsCreateRequestXgafv",
    "MonitoringProjectsDashboardsDeleteRequestAlt",
    "MonitoringProjectsDashboardsDeleteRequestXgafv",
    "MonitoringProjectsDashboardsGetRequestAlt",
    "MonitoringProjectsDashboardsGetRequestXgafv",
    "MonitoringProjectsDashboardsListRequestAlt",
    "MonitoringProjectsDashboardsListRequestXgafv",
    "MonitoringProjectsDashboardsPatchRequestAlt",
    "MonitoringProjectsDashboardsPatchRequestXgafv",
    "MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt",
    "MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv",
    "MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt",
    "MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv",
    "MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt",
    "MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv",
    "MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt",
    "MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv",
    "MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt",
    "MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv",
    "MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt",
    "MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv",
    "MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt",
    "MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv",
]
