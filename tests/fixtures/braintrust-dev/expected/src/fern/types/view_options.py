

import typing

from .view_options_chart_annotations import ViewOptionsChartAnnotations
from .view_options_options import ViewOptionsOptions

ViewOptions = typing.Union[ViewOptionsOptions, ViewOptionsChartAnnotations]
