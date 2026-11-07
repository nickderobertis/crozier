

import typing

from .llm_metrics_item import LlmMetricsItem

LlmMetrics = typing.List[LlmMetricsItem]
"""
List of aggregated metrics to collect across the requested time span.
"""
