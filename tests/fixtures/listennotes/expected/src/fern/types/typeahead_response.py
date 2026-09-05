

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .genre import Genre
from .podcast_typeahead_result import PodcastTypeaheadResult


class TypeaheadResponse(UniversalBaseModel):
    genres: typing.Optional[typing.List[Genre]] = pydantic.Field(default=None)
    """
    Genre suggestions. It'll show up when the **show_genres** parameter is *1*.
    """

    podcasts: typing.Optional[typing.List[PodcastTypeaheadResult]] = pydantic.Field(default=None)
    """
    Podcast suggestions. It'll show up when the **show_podcasts** parameter is 1.
    """

    terms: typing.List[str] = pydantic.Field()
    """
    Search term suggestions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
