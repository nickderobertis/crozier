

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .feature_type import FeatureType


class Feature(UniversalBaseModel):
    """
    GeoJSON feature
    """

    type: FeatureType
    id: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Identifier for the feature
    """

    geometry: typing.Any
    properties: typing.Optional["FeatureProperties"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .feature_properties import FeatureProperties

update_forward_refs(Feature, FeatureProperties=FeatureProperties)
