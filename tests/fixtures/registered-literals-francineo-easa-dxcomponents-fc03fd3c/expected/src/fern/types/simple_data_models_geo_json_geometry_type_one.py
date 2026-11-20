

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounding_box import BoundingBox
from .simple_data_models_geo_json_geometry_type_one_type import SimpleDataModelsGeoJsonGeometryTypeOneType


class SimpleDataModelsGeoJsonGeometryTypeOne(UniversalBaseModel):
    type: SimpleDataModelsGeoJsonGeometryTypeOneType
    coordinates: typing.List[typing.List[float]]
    bbox: typing.Optional[BoundingBox] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
