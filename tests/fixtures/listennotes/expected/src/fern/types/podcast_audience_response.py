

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .podcast_audience_response_by_regions_item import PodcastAudienceResponseByRegionsItem


class PodcastAudienceResponse(UniversalBaseModel):
    by_regions: typing.Optional[typing.List[PodcastAudienceResponseByRegionsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
