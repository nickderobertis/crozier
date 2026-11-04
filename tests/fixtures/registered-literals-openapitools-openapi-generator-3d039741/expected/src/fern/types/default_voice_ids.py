

import typing

from .default_voice_ids_one import DefaultVoiceIdsOne
from .default_voice_ids_zero import DefaultVoiceIdsZero

DefaultVoiceIds = typing.Union[DefaultVoiceIdsZero, DefaultVoiceIdsOne]
