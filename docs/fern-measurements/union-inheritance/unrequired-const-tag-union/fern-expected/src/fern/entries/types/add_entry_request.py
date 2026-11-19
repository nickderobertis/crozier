

import typing

from ...types.studio_note import StudioNote
from ...types.studio_reminder import StudioReminder

AddEntryRequest = typing.Union[StudioNote, StudioReminder]
