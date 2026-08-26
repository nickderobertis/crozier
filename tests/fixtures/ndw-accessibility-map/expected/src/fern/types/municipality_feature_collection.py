

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feature_collection_type import FeatureCollectionType
from .municipality_feature import MunicipalityFeature


class MunicipalityFeatureCollection(UniversalBaseModel):
    features: typing.List[MunicipalityFeature]
    type: FeatureCollectionType = pydantic.Field()
    """
    Type of the element
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
