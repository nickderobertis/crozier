

import typing

from ...types.legacy_presence_format import LegacyPresenceFormat
from ...types.modern_presence_format import ModernPresenceFormat

RegisterQueueResponsePresencesValue = typing.Union[ModernPresenceFormat, typing.Dict[str, LegacyPresenceFormat]]
