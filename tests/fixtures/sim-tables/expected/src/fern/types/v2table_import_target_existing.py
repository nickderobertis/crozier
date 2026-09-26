

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_import_target_existing_mode import V2TableImportTargetExistingMode


class V2TableImportTargetExisting(UniversalBaseModel):
    table_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tableId"),
        pydantic.Field(alias="tableId", description="Existing target table identifier."),
    ]
    """
    Existing target table identifier.
    """

    mode: V2TableImportTargetExistingMode = pydantic.Field()
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
