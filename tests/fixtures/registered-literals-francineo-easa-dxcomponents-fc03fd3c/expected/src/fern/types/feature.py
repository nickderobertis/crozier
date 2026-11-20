

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feature_type import FeatureType
from .uas_zone_version import UasZoneVersion


class Feature(UniversalBaseModel):
    """
    A GeoJSON Feature representing a UAS Zone.
    """

    type: typing.Optional[FeatureType] = None
    geometry: typing.Optional[typing.Any] = None
    properties: typing.Optional[UasZoneVersion] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
