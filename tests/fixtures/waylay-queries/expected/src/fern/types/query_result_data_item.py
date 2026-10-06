

import typing

from .column_data_set import ColumnDataSet
from .object_data_set import ObjectDataSet
from .row_data_set import RowDataSet
from .series_data_set import SeriesDataSet

QueryResultDataItem = typing.Union[RowDataSet, SeriesDataSet, ColumnDataSet, ObjectDataSet]
