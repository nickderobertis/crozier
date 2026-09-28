



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        MonitoringProjectsDashboardsCreateRequestAlt,
        MonitoringProjectsDashboardsCreateRequestXgafv,
        MonitoringProjectsDashboardsDeleteRequestAlt,
        MonitoringProjectsDashboardsDeleteRequestXgafv,
        MonitoringProjectsDashboardsGetRequestAlt,
        MonitoringProjectsDashboardsGetRequestXgafv,
        MonitoringProjectsDashboardsListRequestAlt,
        MonitoringProjectsDashboardsListRequestXgafv,
        MonitoringProjectsDashboardsPatchRequestAlt,
        MonitoringProjectsDashboardsPatchRequestXgafv,
        MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt,
        MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv,
        MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt,
        MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv,
        MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt,
        MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv,
        MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt,
        MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv,
        MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt,
        MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv,
        MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt,
        MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv,
        MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt,
        MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "MonitoringProjectsDashboardsCreateRequestAlt": ".types",
    "MonitoringProjectsDashboardsCreateRequestXgafv": ".types",
    "MonitoringProjectsDashboardsDeleteRequestAlt": ".types",
    "MonitoringProjectsDashboardsDeleteRequestXgafv": ".types",
    "MonitoringProjectsDashboardsGetRequestAlt": ".types",
    "MonitoringProjectsDashboardsGetRequestXgafv": ".types",
    "MonitoringProjectsDashboardsListRequestAlt": ".types",
    "MonitoringProjectsDashboardsListRequestXgafv": ".types",
    "MonitoringProjectsDashboardsPatchRequestAlt": ".types",
    "MonitoringProjectsDashboardsPatchRequestXgafv": ".types",
    "MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestAlt": ".types",
    "MonitoringProjectsLocationPrometheusApiV1LabelValuesRequestXgafv": ".types",
    "MonitoringProjectsLocationPrometheusApiV1LabelsRequestAlt": ".types",
    "MonitoringProjectsLocationPrometheusApiV1LabelsRequestXgafv": ".types",
    "MonitoringProjectsLocationPrometheusApiV1MetadataListRequestAlt": ".types",
    "MonitoringProjectsLocationPrometheusApiV1MetadataListRequestXgafv": ".types",
    "MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestAlt": ".types",
    "MonitoringProjectsLocationPrometheusApiV1QueryExemplarsRequestXgafv": ".types",
    "MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestAlt": ".types",
    "MonitoringProjectsLocationPrometheusApiV1QueryRangeRequestXgafv": ".types",
    "MonitoringProjectsLocationPrometheusApiV1QueryRequestAlt": ".types",
    "MonitoringProjectsLocationPrometheusApiV1QueryRequestXgafv": ".types",
    "MonitoringProjectsLocationPrometheusApiV1SeriesRequestAlt": ".types",
    "MonitoringProjectsLocationPrometheusApiV1SeriesRequestXgafv": ".types",
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
