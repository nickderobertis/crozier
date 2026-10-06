

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_set_attributes import DataSetAttributes
from .data_set_window import DataSetWindow
from .object_data import ObjectData


class ObjectDataSet(UniversalBaseModel):
    """
    Data result in object format.

    Result item when render option `render.header_array` is not set.

    The data values are keyed by their attributes (`resource`, `metric`, `aggregation`),
    according to the render options:
    * _hierachical_: for each level, a sub-object is created
      (e.g. `render.mode=hier_dict`)
    * _flattened_: the attributes are '.'-separated concatenation
      of the attributes (e.g `render.mode=flat_dict`)
    * _mixed_: (.e.g. `render.mode=metric_flat_dict`) a single level
        (e.g. `metric`) is used as main key, any remaining levels
        (`resource`,`aggregation`) are indicated with a flattened subkey.

    When `render.rollup=true`, the attribute levels that are the same for all series are
    not used as key, but reported as a data or table attribute.
    """

    attributes: typing.Optional[DataSetAttributes] = None
    window_spec: typing.Optional[DataSetWindow] = None
    data: typing.List[ObjectData]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
