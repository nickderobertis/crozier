

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_note_part import BaseNotePart
from .entry_link import EntryLink
from .text_box_note_part_type import TextBoxNotePartType


class TextBoxNotePart(BaseNotePart):
    links: typing.Optional[typing.List[EntryLink]] = pydantic.Field(default=None)
    """
    Array of links referenced via an @-mention, hyperlink, or the drag-n-dropped preview attached to the note.
    """

    name: typing.Optional[str] = None
    text: typing.Optional[str] = None
    type: typing.Optional[TextBoxNotePartType] = pydantic.Field(default=None)
    """
    The type of the note.  Type determines what other fields are present.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
