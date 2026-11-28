

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .assay_run_note_part_type import AssayRunNotePartType
from .base_note_part import BaseNotePart


class AssayRunNotePart(BaseNotePart):
    assay_run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assayRunId"), pydantic.Field(alias="assayRunId")
    ] = None
    assay_run_schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assayRunSchemaId"), pydantic.Field(alias="assayRunSchemaId")
    ] = None
    type: typing.Optional[AssayRunNotePartType] = pydantic.Field(default=None)
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
