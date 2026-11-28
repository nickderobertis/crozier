

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_note_part import BaseNotePart
from .inventory_plate_table_note_part_mode import InventoryPlateTableNotePartMode
from .structured_table_api_identifiers import StructuredTableApiIdentifiers


class InventoryPlateTableNotePart(BaseNotePart, StructuredTableApiIdentifiers):
    destination_plate_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="destinationPlateSchemaId"),
        pydantic.Field(alias="destinationPlateSchemaId"),
    ] = None
    destination_well_schema_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="destinationWellSchemaId"),
        pydantic.Field(alias="destinationWellSchemaId"),
    ] = None
    mode: typing.Optional[InventoryPlateTableNotePartMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
