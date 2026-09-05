

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .playlist_description_field import PlaylistDescriptionField
from .playlist_id_field import PlaylistIdField
from .playlist_image_field import PlaylistImageField
from .playlist_last_timestamp_ms_field import PlaylistLastTimestampMsField
from .playlist_listennotes_url_field import PlaylistListennotesUrlField
from .playlist_name_field import PlaylistNameField
from .playlist_thumbnail_field import PlaylistThumbnailField
from .playlist_visibility_field import PlaylistVisibilityField


class PlaylistsResponsePlaylistsItem(UniversalBaseModel):
    """
    A playlist
    """

    description: typing.Optional[PlaylistDescriptionField] = None
    episode_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of episodes (including custom audio) in this playlist.
    """

    id: typing.Optional[PlaylistIdField] = None
    image: typing.Optional[PlaylistImageField] = None
    last_timestamp_ms: typing.Optional[PlaylistLastTimestampMsField] = None
    listennotes_url: typing.Optional[PlaylistListennotesUrlField] = None
    name: typing.Optional[PlaylistNameField] = None
    podcast_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of podcasts in this playlist.
    """

    thumbnail: typing.Optional[PlaylistThumbnailField] = None
    total_audio_length_sec: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total audio length of all episodes in this playlist, in seconds.
    """

    visibility: typing.Optional[PlaylistVisibilityField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
