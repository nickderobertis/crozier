

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .playlists_response_playlists_item import PlaylistsResponsePlaylistsItem


class PlaylistsResponse(UniversalBaseModel):
    has_next: typing.Optional[bool] = None
    has_previous: typing.Optional[bool] = None
    next_page_number: typing.Optional[int] = None
    page_number: typing.Optional[int] = None
    playlists: typing.Optional[typing.List[PlaylistsResponsePlaylistsItem]] = None
    previous_page_number: typing.Optional[int] = None
    total: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
