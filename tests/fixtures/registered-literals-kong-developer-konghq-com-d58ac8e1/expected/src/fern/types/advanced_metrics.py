

import typing

from .advanced_metrics_item import AdvancedMetricsItem

AdvancedMetrics = typing.List[AdvancedMetricsItem]
"""
List of aggregated metrics to collect across the requested time span. If no metrics are specified, request_count will be computed by default.
"""
