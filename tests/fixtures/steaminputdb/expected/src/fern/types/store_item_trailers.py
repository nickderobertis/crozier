

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .store_item_trailers_trailer import StoreItemTrailersTrailer


class StoreItemTrailers(UniversalBaseModel):
    highlights: typing.Optional[typing.List[StoreItemTrailersTrailer]] = None
    other_trailers: typing.Optional[typing.List[StoreItemTrailersTrailer]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
