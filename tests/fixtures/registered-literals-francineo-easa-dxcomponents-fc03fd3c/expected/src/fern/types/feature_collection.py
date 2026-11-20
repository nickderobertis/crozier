

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bounding_box import BoundingBox
from .dataset_metadata import DatasetMetadata
from .feature import Feature
from .feature_collection_type import FeatureCollectionType


class FeatureCollection(UniversalBaseModel):
    """
    GeoJSON Features representing UAS Geographical Zones, plus additional foreign members capturing data set information.
    """

    name: typing.Optional[str] = None
    type: typing.Optional[FeatureCollectionType] = None
    bbox: typing.Optional[BoundingBox] = None
    features: typing.Optional[typing.List[Feature]] = None
    properties: typing.Optional[DatasetMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
