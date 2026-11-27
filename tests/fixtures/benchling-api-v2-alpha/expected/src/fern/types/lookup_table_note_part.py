

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .lookup_table_note_part_type import LookupTableNotePartType
from .structured_table_api_identifiers import StructuredTableApiIdentifiers


class LookupTableNotePart(StructuredTableApiIdentifiers):
    type: typing.Optional[LookupTableNotePartType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
