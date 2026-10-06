

import typing

from .column_header import ColumnHeader
from .row_index_column_header import RowIndexColumnHeader

SeriesDataSetColumnsItem = typing.Union[RowIndexColumnHeader, ColumnHeader]
