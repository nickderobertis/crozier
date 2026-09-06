

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .store_item_trailers_adaptive_trailer import StoreItemTrailersAdaptiveTrailer
from .store_item_trailers_video_source import StoreItemTrailersVideoSource


class StoreItemTrailersTrailer(UniversalBaseModel):
    adaptive_trailers: typing.Optional[typing.List[StoreItemTrailersAdaptiveTrailer]] = None
    all_ages: typing.Optional[bool] = None
    microtrailer: typing.Optional[typing.List[StoreItemTrailersVideoSource]] = None
    screenshot_full: typing.Optional[str] = None
    screenshot_medium: typing.Optional[str] = None
    trailer480p: typing_extensions.Annotated[
        typing.Optional[typing.List[StoreItemTrailersVideoSource]],
        FieldMetadata(alias="trailer_480p"),
        pydantic.Field(alias="trailer_480p"),
    ] = None
    trailer_base_id: typing.Optional[int] = None
    trailer_category: typing.Optional[int] = None
    trailer_max: typing.Optional[typing.List[StoreItemTrailersVideoSource]] = None
    trailer_name: typing.Optional[str] = None
    trailer_url_format: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
