

import typing

from ...types.legacy_presence_format import LegacyPresenceFormat
from ...types.modern_presence_format import ModernPresenceFormat

UpdatePresenceResponsePresencesValue = typing.Union[ModernPresenceFormat, typing.Dict[str, LegacyPresenceFormat]]
