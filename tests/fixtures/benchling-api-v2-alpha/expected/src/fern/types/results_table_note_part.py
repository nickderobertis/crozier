

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_note_part import BaseNotePart
from .results_table_note_part_type import ResultsTableNotePartType
from .structured_table_api_identifiers import StructuredTableApiIdentifiers


class ResultsTableNotePart(BaseNotePart, StructuredTableApiIdentifiers):
    assay_result_schema_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="assayResultSchemaId"), pydantic.Field(alias="assayResultSchemaId")
    ] = None
    type: typing.Optional[ResultsTableNotePartType] = pydantic.Field(default=None)
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
