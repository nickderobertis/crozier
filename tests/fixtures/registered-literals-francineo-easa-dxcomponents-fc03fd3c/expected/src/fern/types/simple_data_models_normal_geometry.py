

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounding_box import BoundingBox
from .simple_data_models_normal_geometry_type import SimpleDataModelsNormalGeometryType


class SimpleDataModelsNormalGeometry(UniversalBaseModel):
    """
    Individual geometry entry not in a collection.
    """

    type: typing.Optional[SimpleDataModelsNormalGeometryType] = None
    coordinates: typing.Optional[typing.List[typing.List[typing.List[typing.List[float]]]]] = None
    bbox: typing.Optional[BoundingBox] = None
    extent: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
