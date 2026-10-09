

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .movie_summary import MovieSummary
from .pagination_meta import PaginationMeta


class MovieListResponse(UniversalBaseModel):
    """
    Movie list response used by Kodi source as `json["movies"]`.
    """

    movies: typing.List[MovieSummary]
    meta: typing.Optional[PaginationMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
