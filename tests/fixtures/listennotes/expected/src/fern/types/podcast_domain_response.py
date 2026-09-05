

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .podcast_simple import PodcastSimple


class PodcastDomainResponse(UniversalBaseModel):
    has_next: typing.Optional[bool] = None
    has_previous: typing.Optional[bool] = None
    next_page_number: typing.Optional[int] = None
    page_number: typing.Optional[int] = None
    podcasts: typing.Optional[typing.List[PodcastSimple]] = None
    previous_page_number: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
