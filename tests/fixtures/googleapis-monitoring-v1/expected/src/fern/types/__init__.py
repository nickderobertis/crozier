



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .aggregation import Aggregation
    from .aggregation_cross_series_reducer import AggregationCrossSeriesReducer
    from .aggregation_function import AggregationFunction
    from .aggregation_per_series_aligner import AggregationPerSeriesAligner
    from .alert_chart import AlertChart
    from .axis import Axis
    from .axis_scale import AxisScale
    from .breakdown import Breakdown
    from .breakdown_sort_order import BreakdownSortOrder
    from .chart_options import ChartOptions
    from .chart_options_mode import ChartOptionsMode
    from .collapsible_group import CollapsibleGroup
    from .column import Column
    from .column_layout import ColumnLayout
    from .column_settings import ColumnSettings
    from .dashboard import Dashboard
    from .dashboard_filter import DashboardFilter
    from .dashboard_filter_filter_type import DashboardFilterFilterType
    from .data_set import DataSet
    from .data_set_plot_type import DataSetPlotType
    from .data_set_target_axis import DataSetTargetAxis
    from .dimension import Dimension
    from .dimension_sort_order import DimensionSortOrder
    from .dropped_labels import DroppedLabels
    from .empty import Empty
    from .error_reporting_panel import ErrorReportingPanel
    from .field import Field
    from .field_cardinality import FieldCardinality
    from .field_kind import FieldKind
    from .gauge_view import GaugeView
    from .grid_layout import GridLayout
    from .http_body import HttpBody
    from .incident_list import IncidentList
    from .interval import Interval
    from .list_dashboards_response import ListDashboardsResponse
    from .list_metrics_scopes_by_monitored_project_response import ListMetricsScopesByMonitoredProjectResponse
    from .logs_panel import LogsPanel
    from .measure import Measure
    from .metrics_scope import MetricsScope
    from .monitored_project import MonitoredProject
    from .monitored_resource import MonitoredResource
    from .mosaic_layout import MosaicLayout
    from .oauth_scope import OauthScope
    from .operation import Operation
    from .operation_metadata import OperationMetadata
    from .operation_metadata_state import OperationMetadataState
    from .ops_analytics_query import OpsAnalyticsQuery
    from .option import Option
    from .parameter import Parameter
    from .pick_time_series_filter import PickTimeSeriesFilter
    from .pick_time_series_filter_direction import PickTimeSeriesFilterDirection
    from .pick_time_series_filter_ranking_method import PickTimeSeriesFilterRankingMethod
    from .pie_chart import PieChart
    from .pie_chart_chart_type import PieChartChartType
    from .pie_chart_data_set import PieChartDataSet
    from .ratio_part import RatioPart
    from .row import Row
    from .row_layout import RowLayout
    from .scorecard import Scorecard
    from .section_header import SectionHeader
    from .single_view_group import SingleViewGroup
    from .source_context import SourceContext
    from .span_context import SpanContext
    from .spark_chart_view import SparkChartView
    from .spark_chart_view_spark_chart_type import SparkChartViewSparkChartType
    from .statistical_time_series_filter import StatisticalTimeSeriesFilter
    from .statistical_time_series_filter_ranking_method import StatisticalTimeSeriesFilterRankingMethod
    from .status import Status
    from .table_data_set import TableDataSet
    from .table_display_options import TableDisplayOptions
    from .text import Text
    from .text_format import TextFormat
    from .text_style import TextStyle
    from .text_style_font_size import TextStyleFontSize
    from .text_style_horizontal_alignment import TextStyleHorizontalAlignment
    from .text_style_padding import TextStylePadding
    from .text_style_pointer_location import TextStylePointerLocation
    from .text_style_vertical_alignment import TextStyleVerticalAlignment
    from .threshold import Threshold
    from .threshold_color import ThresholdColor
    from .threshold_direction import ThresholdDirection
    from .threshold_target_axis import ThresholdTargetAxis
    from .tile import Tile
    from .time_series_filter import TimeSeriesFilter
    from .time_series_filter_ratio import TimeSeriesFilterRatio
    from .time_series_query import TimeSeriesQuery
    from .time_series_table import TimeSeriesTable
    from .time_series_table_metric_visualization import TimeSeriesTableMetricVisualization
    from .type import Type
    from .type_syntax import TypeSyntax
    from .widget import Widget
    from .xy_chart import XyChart
_dynamic_imports: typing.Dict[str, str] = {
    "Aggregation": ".aggregation",
    "AggregationCrossSeriesReducer": ".aggregation_cross_series_reducer",
    "AggregationFunction": ".aggregation_function",
    "AggregationPerSeriesAligner": ".aggregation_per_series_aligner",
    "AlertChart": ".alert_chart",
    "Axis": ".axis",
    "AxisScale": ".axis_scale",
    "Breakdown": ".breakdown",
    "BreakdownSortOrder": ".breakdown_sort_order",
    "ChartOptions": ".chart_options",
    "ChartOptionsMode": ".chart_options_mode",
    "CollapsibleGroup": ".collapsible_group",
    "Column": ".column",
    "ColumnLayout": ".column_layout",
    "ColumnSettings": ".column_settings",
    "Dashboard": ".dashboard",
    "DashboardFilter": ".dashboard_filter",
    "DashboardFilterFilterType": ".dashboard_filter_filter_type",
    "DataSet": ".data_set",
    "DataSetPlotType": ".data_set_plot_type",
    "DataSetTargetAxis": ".data_set_target_axis",
    "Dimension": ".dimension",
    "DimensionSortOrder": ".dimension_sort_order",
    "DroppedLabels": ".dropped_labels",
    "Empty": ".empty",
    "ErrorReportingPanel": ".error_reporting_panel",
    "Field": ".field",
    "FieldCardinality": ".field_cardinality",
    "FieldKind": ".field_kind",
    "GaugeView": ".gauge_view",
    "GridLayout": ".grid_layout",
    "HttpBody": ".http_body",
    "IncidentList": ".incident_list",
    "Interval": ".interval",
    "ListDashboardsResponse": ".list_dashboards_response",
    "ListMetricsScopesByMonitoredProjectResponse": ".list_metrics_scopes_by_monitored_project_response",
    "LogsPanel": ".logs_panel",
    "Measure": ".measure",
    "MetricsScope": ".metrics_scope",
    "MonitoredProject": ".monitored_project",
    "MonitoredResource": ".monitored_resource",
    "MosaicLayout": ".mosaic_layout",
    "OauthScope": ".oauth_scope",
    "Operation": ".operation",
    "OperationMetadata": ".operation_metadata",
    "OperationMetadataState": ".operation_metadata_state",
    "OpsAnalyticsQuery": ".ops_analytics_query",
    "Option": ".option",
    "Parameter": ".parameter",
    "PickTimeSeriesFilter": ".pick_time_series_filter",
    "PickTimeSeriesFilterDirection": ".pick_time_series_filter_direction",
    "PickTimeSeriesFilterRankingMethod": ".pick_time_series_filter_ranking_method",
    "PieChart": ".pie_chart",
    "PieChartChartType": ".pie_chart_chart_type",
    "PieChartDataSet": ".pie_chart_data_set",
    "RatioPart": ".ratio_part",
    "Row": ".row",
    "RowLayout": ".row_layout",
    "Scorecard": ".scorecard",
    "SectionHeader": ".section_header",
    "SingleViewGroup": ".single_view_group",
    "SourceContext": ".source_context",
    "SpanContext": ".span_context",
    "SparkChartView": ".spark_chart_view",
    "SparkChartViewSparkChartType": ".spark_chart_view_spark_chart_type",
    "StatisticalTimeSeriesFilter": ".statistical_time_series_filter",
    "StatisticalTimeSeriesFilterRankingMethod": ".statistical_time_series_filter_ranking_method",
    "Status": ".status",
    "TableDataSet": ".table_data_set",
    "TableDisplayOptions": ".table_display_options",
    "Text": ".text",
    "TextFormat": ".text_format",
    "TextStyle": ".text_style",
    "TextStyleFontSize": ".text_style_font_size",
    "TextStyleHorizontalAlignment": ".text_style_horizontal_alignment",
    "TextStylePadding": ".text_style_padding",
    "TextStylePointerLocation": ".text_style_pointer_location",
    "TextStyleVerticalAlignment": ".text_style_vertical_alignment",
    "Threshold": ".threshold",
    "ThresholdColor": ".threshold_color",
    "ThresholdDirection": ".threshold_direction",
    "ThresholdTargetAxis": ".threshold_target_axis",
    "Tile": ".tile",
    "TimeSeriesFilter": ".time_series_filter",
    "TimeSeriesFilterRatio": ".time_series_filter_ratio",
    "TimeSeriesQuery": ".time_series_query",
    "TimeSeriesTable": ".time_series_table",
    "TimeSeriesTableMetricVisualization": ".time_series_table_metric_visualization",
    "Type": ".type",
    "TypeSyntax": ".type_syntax",
    "Widget": ".widget",
    "XyChart": ".xy_chart",
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
    "Aggregation",
    "AggregationCrossSeriesReducer",
    "AggregationFunction",
    "AggregationPerSeriesAligner",
    "AlertChart",
    "Axis",
    "AxisScale",
    "Breakdown",
    "BreakdownSortOrder",
    "ChartOptions",
    "ChartOptionsMode",
    "CollapsibleGroup",
    "Column",
    "ColumnLayout",
    "ColumnSettings",
    "Dashboard",
    "DashboardFilter",
    "DashboardFilterFilterType",
    "DataSet",
    "DataSetPlotType",
    "DataSetTargetAxis",
    "Dimension",
    "DimensionSortOrder",
    "DroppedLabels",
    "Empty",
    "ErrorReportingPanel",
    "Field",
    "FieldCardinality",
    "FieldKind",
    "GaugeView",
    "GridLayout",
    "HttpBody",
    "IncidentList",
    "Interval",
    "ListDashboardsResponse",
    "ListMetricsScopesByMonitoredProjectResponse",
    "LogsPanel",
    "Measure",
    "MetricsScope",
    "MonitoredProject",
    "MonitoredResource",
    "MosaicLayout",
    "OauthScope",
    "Operation",
    "OperationMetadata",
    "OperationMetadataState",
    "OpsAnalyticsQuery",
    "Option",
    "Parameter",
    "PickTimeSeriesFilter",
    "PickTimeSeriesFilterDirection",
    "PickTimeSeriesFilterRankingMethod",
    "PieChart",
    "PieChartChartType",
    "PieChartDataSet",
    "RatioPart",
    "Row",
    "RowLayout",
    "Scorecard",
    "SectionHeader",
    "SingleViewGroup",
    "SourceContext",
    "SpanContext",
    "SparkChartView",
    "SparkChartViewSparkChartType",
    "StatisticalTimeSeriesFilter",
    "StatisticalTimeSeriesFilterRankingMethod",
    "Status",
    "TableDataSet",
    "TableDisplayOptions",
    "Text",
    "TextFormat",
    "TextStyle",
    "TextStyleFontSize",
    "TextStyleHorizontalAlignment",
    "TextStylePadding",
    "TextStylePointerLocation",
    "TextStyleVerticalAlignment",
    "Threshold",
    "ThresholdColor",
    "ThresholdDirection",
    "ThresholdTargetAxis",
    "Tile",
    "TimeSeriesFilter",
    "TimeSeriesFilterRatio",
    "TimeSeriesQuery",
    "TimeSeriesTable",
    "TimeSeriesTableMetricVisualization",
    "Type",
    "TypeSyntax",
    "Widget",
    "XyChart",
]
