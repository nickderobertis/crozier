

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .playlist_item_data import PlaylistItemData
from .playlist_item_type import PlaylistItemType


class PlaylistItem(UniversalBaseModel):
    """
    An item in a playlist
    """

    added_at_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp (in milliseconds) when this item is added.
    """

    data: typing.Optional[PlaylistItemData] = None
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Playlist item id.
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notes for this item.
    """

    type: typing.Optional[PlaylistItemType] = pydantic.Field(default=None)
    """
    The type of this playlist item.
    If a playlist is **episode_list**, then an item could be either **episode** or **custom_audio**.
    If it's **podcast_list**, then an item can only be **podcast**.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
