

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .column_data_set_data_axis import ColumnDataSetDataAxis
from .column_data_set_rows_item import ColumnDataSetRowsItem
from .data_set_attributes import DataSetAttributes
from .data_set_window import DataSetWindow
from .datum import Datum


class ColumnDataSet(UniversalBaseModel):
    """
    Column-oriented dataset with rows header.

    Timeseries data layout with a rows header containing
    the index data.
    The data array contains series data prefixed by series attributes.
    The `rows` index is prefix by the names of these series attributes.
    Result for render options `data_axis=row` and `header_array=column`.
    """

    attributes: typing.Optional[DataSetAttributes] = None
    window_spec: typing.Optional[DataSetWindow] = None
    data_axis: typing.Optional[ColumnDataSetDataAxis] = None
    rows: typing.List[ColumnDataSetRowsItem] = pydantic.Field()
    """
    Header Attributes for the index data.
    
    The initial string-valued headers (normally `resource`, `metric`,`aggregation`) indicate that row to contain series attributes.
    
    The remaining object-valued row headers contain the index data.
    """

    column_names: typing.List[str] = pydantic.Field()
    """
    Short names for the columns in the data set.
    These names are the `name` alias if given in the series specification, otherwise is composed of the `resource`, `metric` and `aggregation` attributes, concatenated with the `render.key_separator` (default `.`) as separator.
    """

    data: typing.List[typing.List[typing.Optional[Datum]]] = pydantic.Field()
    """
    All metric observation values for a single series. Prefixed by the series attributes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
