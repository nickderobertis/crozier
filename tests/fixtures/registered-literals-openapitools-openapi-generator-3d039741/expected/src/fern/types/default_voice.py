

import typing

from .default_custom_voice import DefaultCustomVoice
from .default_voice_ids import DefaultVoiceIds

DefaultVoice = typing.Union[DefaultVoiceIds, DefaultCustomVoice]
