

import typing

from .custom_audio import CustomAudio
from .deleted_item import DeletedItem
from .episode_simple import EpisodeSimple
from .podcast_simple import PodcastSimple

PlaylistItemData = typing.Union[EpisodeSimple, PodcastSimple, CustomAudio, DeletedItem]
