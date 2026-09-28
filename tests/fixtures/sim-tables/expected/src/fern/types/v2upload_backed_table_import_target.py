

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .folder_path_input import FolderPathInput
from .v2upload_backed_table_import_target_existing_mode import V2UploadBackedTableImportTargetExistingMode


class V2UploadBackedTableImportTarget_New(UniversalBaseModel):
    """
    New or existing table import target.
    """

    type: typing.Literal["new"] = "new"
    name: str
    folder_path: typing_extensions.Annotated[
        typing.Optional[FolderPathInput], FieldMetadata(alias="folderPath"), pydantic.Field(alias="folderPath")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class V2UploadBackedTableImportTarget_Existing(UniversalBaseModel):
    """
    New or existing table import target.
    """

    type: typing.Literal["existing"] = "existing"
    table_id: typing_extensions.Annotated[str, FieldMetadata(alias="tableId"), pydantic.Field(alias="tableId")]
    mode: V2UploadBackedTableImportTargetExistingMode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


V2UploadBackedTableImportTarget = typing_extensions.Annotated[
    typing.Union[V2UploadBackedTableImportTarget_New, V2UploadBackedTableImportTarget_Existing],
    pydantic.Field(discriminator="type"),
]
