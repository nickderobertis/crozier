

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_note_part import BaseNotePart
from .entry_link import EntryLink
from .entry_table import EntryTable
from .table_note_part_type import TableNotePartType


class TableNotePart(BaseNotePart):
    """
    A table with rows and columns of text
    """

    links: typing.Optional[typing.List[EntryLink]] = pydantic.Field(default=None)
    """
    Array of links referenced in the caption via an @-mention, hyperlink, or the drag-n-dropped preview attached to the note.
    """

    table: typing.Optional[EntryTable] = None
    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The caption of the table.
    """

    type: typing.Optional[TableNotePartType] = pydantic.Field(default=None)
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
