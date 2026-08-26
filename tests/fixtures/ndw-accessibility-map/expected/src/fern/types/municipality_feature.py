

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feature_type import FeatureType
from .municipality_properties import MunicipalityProperties


class MunicipalityFeature(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier of the municipality in the municipality registry
    """

    properties: typing.Optional[MunicipalityProperties] = None
    type: FeatureType
    geometry: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
