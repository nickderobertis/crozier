

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feature import Feature
from .feature_collection_type import FeatureCollectionType


class FeatureCollection(UniversalBaseModel):
    """
    GeoJSON feature collection
    """

    type: FeatureCollectionType = pydantic.Field()
    """
    Type of the element
    """

    features: typing.List[Feature]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
