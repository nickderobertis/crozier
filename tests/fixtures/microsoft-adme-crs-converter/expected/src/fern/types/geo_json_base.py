

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .geo_json_base_geo_json_variant_internal import GeoJsonBaseGeoJsonVariantInternal


class GeoJsonBase(UniversalBaseModel):
    bbox: typing.Optional[typing.List[float]] = None
    geo_json_variant_internal: typing_extensions.Annotated[
        typing.Optional[GeoJsonBaseGeoJsonVariantInternal],
        FieldMetadata(alias="geoJsonVariantInternal"),
        pydantic.Field(alias="geoJsonVariantInternal"),
    ] = None
    type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
