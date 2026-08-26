

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .feature_collection import FeatureCollection


class AccessibilityResponseGeoJson(FeatureCollection):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
