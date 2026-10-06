

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_set_attributes import DataSetAttributes
from .data_set_window import DataSetWindow
from .datum import Datum
from .series_data_set_columns_item import SeriesDataSetColumnsItem
from .series_data_set_data_axis import SeriesDataSetDataAxis


class SeriesDataSet(UniversalBaseModel):
    """
    Column-oriented dataset.

    Timeseries data layout with a column header
    and a seperate data array for the time index and each series.
    Result for render options `data_axis=row` and `header_array=row`.
    """

    attributes: typing.Optional[DataSetAttributes] = None
    window_spec: typing.Optional[DataSetWindow] = None
    data_axis: typing.Optional[SeriesDataSetDataAxis] = None
    columns: typing.List[SeriesDataSetColumnsItem] = pydantic.Field()
    """
    Header Attributes for the column data.
    
    The initial string-valued headers (normally a single `timestamp`) indicate that column to contain row index data (i.e. timestamps).
    
    The remaining object-valued column headers identify and describe the actual series data.
    """

    column_names: typing.List[str] = pydantic.Field()
    """
    Short names for the columns in the data set.
    These names are the `name` alias if given in the series specification, otherwise is composed of the `resource`, `metric` and `aggregation` attributes, concatenated with the `render.key_separator` (default `.`) as separator.
    """

    data: typing.List[typing.List[typing.Optional[Datum]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
