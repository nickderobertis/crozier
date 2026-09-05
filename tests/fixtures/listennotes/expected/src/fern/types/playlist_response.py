

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .playlist_description_field import PlaylistDescriptionField
from .playlist_id_field import PlaylistIdField
from .playlist_image_field import PlaylistImageField
from .playlist_item import PlaylistItem
from .playlist_last_timestamp_ms_field import PlaylistLastTimestampMsField
from .playlist_listennotes_url_field import PlaylistListennotesUrlField
from .playlist_name_field import PlaylistNameField
from .playlist_response_type import PlaylistResponseType
from .playlist_thumbnail_field import PlaylistThumbnailField
from .playlist_visibility_field import PlaylistVisibilityField


class PlaylistResponse(UniversalBaseModel):
    description: typing.Optional[PlaylistDescriptionField] = None
    id: typing.Optional[PlaylistIdField] = None
    image: typing.Optional[PlaylistImageField] = None
    items: typing.Optional[typing.List[PlaylistItem]] = pydantic.Field(default=None)
    """
    A list of playlist items.
    """

    last_timestamp_ms: typing.Optional[PlaylistLastTimestampMsField] = None
    listennotes_url: typing.Optional[PlaylistListennotesUrlField] = None
    name: typing.Optional[PlaylistNameField] = None
    thumbnail: typing.Optional[PlaylistThumbnailField] = None
    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of items in this playlist.
    """

    total_audio_length_sec: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total audio length of all episodes in this playlist, in seconds. It will have a valid value only when type is **episode_list**. In other words, it will be 0 if type is **podcast_list**.
    """

    type: typing.Optional[PlaylistResponseType] = pydantic.Field(default=None)
    """
    The type of this playlist, which should be either **episode_list** or **podcast_list**.
    """

    visibility: typing.Optional[PlaylistVisibilityField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
