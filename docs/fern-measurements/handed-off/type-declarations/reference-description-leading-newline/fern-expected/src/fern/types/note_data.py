

import typing

from .photo_note import PhotoNote
from .text_note import TextNote

NoteData = typing.Union[TextNote, PhotoNote]
