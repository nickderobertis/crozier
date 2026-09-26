

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_table_import_request_target_existing_mode import CreateTableImportRequestTargetExistingMode


class CreateTableImportRequestTargetExisting(UniversalBaseModel):
    table_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tableId"),
        pydantic.Field(alias="tableId", description="Existing target table identifier."),
    ]
    """
    Existing target table identifier.
    """

    mode: CreateTableImportRequestTargetExistingMode = pydantic.Field()
    """
    Whether to append rows or replace existing rows.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
