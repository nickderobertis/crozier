

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_note_part import BaseNotePart
from .checkbox_note_part_type import CheckboxNotePartType
from .entry_link import EntryLink


class CheckboxNotePart(BaseNotePart):
    """
    One "line" of a checklist
    """

    checked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the checkbox is checked or not.
    """

    links: typing.Optional[typing.List[EntryLink]] = pydantic.Field(default=None)
    """
    Array of links referenced in text via an @-mention, hyperlink, or the drag-n-dropped preview attached to the note.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The textual contents of the note.
    """

    type: typing.Optional[CheckboxNotePartType] = pydantic.Field(default=None)
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
