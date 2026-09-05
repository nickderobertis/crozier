

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .curated_list_simple import CuratedListSimple


class GetCuratedPodcastsResponse(UniversalBaseModel):
    curated_lists: typing.List[CuratedListSimple]
    has_next: bool
    has_previous: bool
    next_page_number: int
    page_number: int
    previous_page_number: int
    total: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
