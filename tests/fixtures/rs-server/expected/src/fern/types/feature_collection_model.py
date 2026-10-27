

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feature import Feature


class FeatureCollectionModel(UniversalBaseModel):
    """
    Model representing a collection of features.

    This model is used to group multiple `Feature` objects into a single collection.

    Attributes:
        type (str): The type of the feature collection (e.g., "FeatureCollection").
        features (List[Feature]): A list of `Feature` objects included in the collection.
    """

    type: str
    features: typing.List[Feature]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
