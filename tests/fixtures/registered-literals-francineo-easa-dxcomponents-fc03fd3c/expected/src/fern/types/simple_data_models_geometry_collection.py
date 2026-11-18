

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounding_box import BoundingBox
from .simple_data_models_geometry_collection_geometries_item import SimpleDataModelsGeometryCollectionGeometriesItem
from .simple_data_models_geometry_collection_type import SimpleDataModelsGeometryCollectionType


class SimpleDataModelsGeometryCollection(UniversalBaseModel):
    type: SimpleDataModelsGeometryCollectionType
    geometries: typing.List[SimpleDataModelsGeometryCollectionGeometriesItem]
    bbox: typing.Optional[BoundingBox] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
