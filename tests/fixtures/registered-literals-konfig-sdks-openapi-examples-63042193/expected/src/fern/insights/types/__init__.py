



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .insights_get_job_timeseries_data_request_granularity import InsightsGetJobTimeseriesDataRequestGranularity
    from .insights_get_project_summary_metrics_request_reporting_window import (
        InsightsGetProjectSummaryMetricsRequestReportingWindow,
    )
    from .insights_get_project_workflow_job_metrics_request_reporting_window import (
        InsightsGetProjectWorkflowJobMetricsRequestReportingWindow,
    )
    from .insights_get_project_workflow_metrics_request_reporting_window import (
        InsightsGetProjectWorkflowMetricsRequestReportingWindow,
    )
    from .insights_get_summary_metrics_with_trends_request_reporting_window import (
        InsightsGetSummaryMetricsWithTrendsRequestReportingWindow,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "InsightsGetJobTimeseriesDataRequestGranularity": ".insights_get_job_timeseries_data_request_granularity",
    "InsightsGetProjectSummaryMetricsRequestReportingWindow": ".insights_get_project_summary_metrics_request_reporting_window",
    "InsightsGetProjectWorkflowJobMetricsRequestReportingWindow": ".insights_get_project_workflow_job_metrics_request_reporting_window",
    "InsightsGetProjectWorkflowMetricsRequestReportingWindow": ".insights_get_project_workflow_metrics_request_reporting_window",
    "InsightsGetSummaryMetricsWithTrendsRequestReportingWindow": ".insights_get_summary_metrics_with_trends_request_reporting_window",
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
    "InsightsGetJobTimeseriesDataRequestGranularity",
    "InsightsGetProjectSummaryMetricsRequestReportingWindow",
    "InsightsGetProjectWorkflowJobMetricsRequestReportingWindow",
    "InsightsGetProjectWorkflowMetricsRequestReportingWindow",
    "InsightsGetSummaryMetricsWithTrendsRequestReportingWindow",
]
