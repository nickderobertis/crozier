

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2upload_backed_table_import_target_existing_mode import V2UploadBackedTableImportTargetExistingMode


class V2UploadBackedTableImportTargetExisting(UniversalBaseModel):
    table_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tableId"),
        pydantic.Field(alias="tableId", description="Existing target table identifier."),
    ]
    """
    Existing target table identifier.
    """

    mode: V2UploadBackedTableImportTargetExistingMode = pydantic.Field()
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
