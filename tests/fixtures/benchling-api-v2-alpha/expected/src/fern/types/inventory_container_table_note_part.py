

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_note_part import BaseNotePart
from .inventory_container_table_note_part_mode import InventoryContainerTableNotePartMode
from .structured_table_api_identifiers import StructuredTableApiIdentifiers


class InventoryContainerTableNotePart(BaseNotePart, StructuredTableApiIdentifiers):
    destination_container_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="destinationContainerSchemaId"),
        pydantic.Field(alias="destinationContainerSchemaId"),
    ] = None
    mode: typing.Optional[InventoryContainerTableNotePartMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
