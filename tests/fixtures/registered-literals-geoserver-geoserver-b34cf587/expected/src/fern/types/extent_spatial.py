

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extent_spatial_crs import ExtentSpatialCrs


class ExtentSpatial(UniversalBaseModel):
    """
    The spatial extent of the features in the collection.
    """

    bbox: typing.Optional[typing.List[typing.List[float]]] = pydantic.Field(default=None)
    """
    One or more bounding boxes that describe the spatial extent of the dataset.
    In the Core only a single bounding box is supported. Extensions may support
    additional areas. If multiple areas are provided, the union of the bounding
    boxes describes the spatial extent.
    """

    crs: typing.Optional[ExtentSpatialCrs] = pydantic.Field(default=None)
    """
    Coordinate reference system of the coordinates in the spatial extent
    (property `bbox`). The default reference system is WGS 84 longitude/latitude.
    In the Core this is the only supported coordinate reference system.
    Extensions may support additional coordinate reference systems and add
    additional enum values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
