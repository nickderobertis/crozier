

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audio_field import AudioField
from .audio_length_sec_field import AudioLengthSecField
from .episode_description_field import EpisodeDescriptionField
from .episode_id_field import EpisodeIdField
from .episode_image_field import EpisodeImageField
from .episode_ln_edit_url_field import EpisodeLnEditUrlField
from .episode_ln_url_field import EpisodeLnUrlField
from .episode_name_field import EpisodeNameField
from .episode_pub_date_ms_field import EpisodePubDateMsField
from .episode_thumbnail_field import EpisodeThumbnailField
from .explicit_field import ExplicitField
from .link_field import LinkField
from .maybe_audio_invalid_field import MaybeAudioInvalidField
from .podcast_minimum import PodcastMinimum


class EpisodeSimple(UniversalBaseModel):
    audio: typing.Optional[AudioField] = None
    audio_length_sec: typing.Optional[AudioLengthSecField] = None
    description: typing.Optional[EpisodeDescriptionField] = None
    explicit_content: typing.Optional[ExplicitField] = None
    id: typing.Optional[EpisodeIdField] = None
    image: typing.Optional[EpisodeImageField] = None
    link: typing.Optional[LinkField] = None
    listennotes_edit_url: typing.Optional[EpisodeLnEditUrlField] = None
    listennotes_url: typing.Optional[EpisodeLnUrlField] = None
    maybe_audio_invalid: typing.Optional[MaybeAudioInvalidField] = None
    podcast: typing.Optional[PodcastMinimum] = None
    pub_date_ms: typing.Optional[EpisodePubDateMsField] = None
    thumbnail: typing.Optional[EpisodeThumbnailField] = None
    title: typing.Optional[EpisodeNameField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
