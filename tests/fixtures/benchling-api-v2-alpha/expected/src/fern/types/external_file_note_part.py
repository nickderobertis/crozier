

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_note_part import BaseNotePart
from .entry_link import EntryLink
from .external_file_note_part_type import ExternalFileNotePartType


class ExternalFileNotePart(BaseNotePart):
    """
    An attached user-uploaded file
    """

    external_file_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="externalFileId"),
        pydantic.Field(
            alias="externalFileId",
            description="The ID of the external file. Use the 'Get an external file' endpoint to retrieve metadata about it.",
        ),
    ] = None
    """
    The ID of the external file. Use the 'Get an external file' endpoint to retrieve metadata about it.
    """

    links: typing.Optional[typing.List[EntryLink]] = pydantic.Field(default=None)
    """
    Array of links referenced in the caption via an @-mention, hyperlink, or the drag-n-dropped preview attached to the note.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The caption of the file attachment.
    """

    type: typing.Optional[ExternalFileNotePartType] = pydantic.Field(default=None)
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
