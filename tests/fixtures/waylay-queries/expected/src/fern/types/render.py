

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_axis_option import DataAxisOption
from .header_array_option import HeaderArrayOption
from .render_hierarchical import RenderHierarchical
from .render_mode import RenderMode


class Render(UniversalBaseModel):
    """
    Configures the representation of data sets returned by the query API.
    """

    mode: typing.Optional[RenderMode] = pydantic.Field(default=None)
    """
    A render mode combines a number of render option under a single name. Each option can still be overriden by an explicit value.
    """

    roll_up: typing.Optional[bool] = pydantic.Field(default=None)
    """
    move up attributes on rows (or columns) that are the same for             all rows (or columns) to a table attribute.             Levels enumerated in 'hierarchical' are excluded.
    """

    hierarchical: typing.Optional[RenderHierarchical] = pydantic.Field(default=None)
    """
    if true, use hierarchical objects to represent multiple row (or column) dimensions, otherwise multi-keys get concatenated with a dot-delimiter. If the value is a list, only these levels are kept as separate levels, while remaining levels get concatenated keys
    """

    value_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    if set, use this key in the value object to report data values
    """

    show_levels: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if set, report the levels used in the data values (either hierarchical or flat)
    """

    iso_timestamp: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if set, render timestamps in a row or column index with both epoch and iso representations
    """

    row_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    if set, use this key as name of the row-dimension for single-dimensional rows
    """

    column_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    if set, use this key as name of the column-dimension for single-dimensional columns
    """

    header_array: typing.Optional[HeaderArrayOption] = pydantic.Field(default=None)
    """
    if set, report data as an header and an array.  
    """

    data_axis: typing.Optional[DataAxisOption] = pydantic.Field(default=None)
    """
    orientation of the tabular data as a array of arrays
    """

    key_seperator: typing.Optional[str] = pydantic.Field(default=None)
    """
    character used to concatenate multi-key columns or rows when required
    """

    key_skip_empty: typing.Optional[bool] = pydantic.Field(default=None)
    """
    skip empty values in concatenating multi-key column or row headers
    """

    include_window_spec: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if set, include window specification in render modes that support it
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
