

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .feature_collection_geo_json_type import FeatureCollectionGeoJsonType
from .feature_geo_json import FeatureGeoJson
from .link import Link
from .number_matched import NumberMatched
from .number_returned import NumberReturned
from .time_stamp import TimeStamp


class FeatureCollectionGeoJson(UniversalBaseModel):
    type: FeatureCollectionGeoJsonType
    features: typing.List[FeatureGeoJson]
    links: typing.Optional[typing.List[Link]] = None
    time_stamp: typing_extensions.Annotated[
        typing.Optional[TimeStamp], FieldMetadata(alias="timeStamp"), pydantic.Field(alias="timeStamp")
    ] = None
    number_matched: typing_extensions.Annotated[
        typing.Optional[NumberMatched], FieldMetadata(alias="numberMatched"), pydantic.Field(alias="numberMatched")
    ] = None
    number_returned: typing_extensions.Annotated[
        typing.Optional[NumberReturned], FieldMetadata(alias="numberReturned"), pydantic.Field(alias="numberReturned")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(FeatureCollectionGeoJson)
