

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audio_field import AudioField
from .audio_length_sec_field import AudioLengthSecField
from .episode_description_field import EpisodeDescriptionField
from .episode_id_field import EpisodeIdField
from .episode_ln_edit_url_field import EpisodeLnEditUrlField
from .episode_ln_url_field import EpisodeLnUrlField
from .episode_name_field import EpisodeNameField
from .episode_pub_date_ms_field import EpisodePubDateMsField
from .explicit_field import ExplicitField
from .image_field import ImageField
from .link_field import LinkField
from .maybe_audio_invalid_field import MaybeAudioInvalidField
from .thumbnail_field import ThumbnailField


class EpisodeMinimum(UniversalBaseModel):
    audio: typing.Optional[AudioField] = None
    audio_length_sec: typing.Optional[AudioLengthSecField] = None
    description: typing.Optional[EpisodeDescriptionField] = None
    explicit_content: typing.Optional[ExplicitField] = None
    id: typing.Optional[EpisodeIdField] = None
    image: typing.Optional[ImageField] = None
    link: typing.Optional[LinkField] = None
    listennotes_edit_url: typing.Optional[EpisodeLnEditUrlField] = None
    listennotes_url: typing.Optional[EpisodeLnUrlField] = None
    maybe_audio_invalid: typing.Optional[MaybeAudioInvalidField] = None
    pub_date_ms: typing.Optional[EpisodePubDateMsField] = None
    thumbnail: typing.Optional[ThumbnailField] = None
    title: typing.Optional[EpisodeNameField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
