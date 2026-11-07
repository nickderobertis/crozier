

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .feature_collection_geo_json_type import FeatureCollectionGeoJsonType
from .feature_geo_json import FeatureGeoJson
from .link import Link


class FeatureCollectionGeoJson(UniversalBaseModel):
    type: FeatureCollectionGeoJsonType
    features: typing.List[FeatureGeoJson]
    links: typing.Optional[typing.List[Link]] = None
    time_stamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="timeStamp"),
        pydantic.Field(
            alias="timeStamp", description="This property indicates the time and date when the response was generated."
        ),
    ] = None
    """
    This property indicates the time and date when the response was generated.
    """

    number_matched: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberMatched"),
        pydantic.Field(
            alias="numberMatched",
            description="The number of features of the feature type that match the selection\nparameters like `bbox`.",
        ),
    ] = None
    """
    The number of features of the feature type that match the selection
    parameters like `bbox`.
    """

    number_returned: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberReturned"),
        pydantic.Field(
            alias="numberReturned",
            description='The number of features in the feature collection.\n\nA server may omit this information in a response, if the information\nabout the number of features is not known or difficult to compute.\n\nIf the value is provided, the value shall be identical to the number\nof items in the "features" array.',
        ),
    ] = None
    """
    The number of features in the feature collection.
    
    A server may omit this information in a response, if the information
    about the number of features is not known or difficult to compute.
    
    If the value is provided, the value shall be identical to the number
    of items in the "features" array.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(FeatureCollectionGeoJson)
