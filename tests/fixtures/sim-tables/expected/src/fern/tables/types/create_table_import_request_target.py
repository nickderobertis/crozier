

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.folder_path_input import FolderPathInput
from .create_table_import_request_target_existing_mode import CreateTableImportRequestTargetExistingMode


class CreateTableImportRequestTarget_New(UniversalBaseModel):
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


class CreateTableImportRequestTarget_Existing(UniversalBaseModel):
    """
    New or existing table import target.
    """

    type: typing.Literal["existing"] = "existing"
    table_id: typing_extensions.Annotated[str, FieldMetadata(alias="tableId"), pydantic.Field(alias="tableId")]
    mode: CreateTableImportRequestTargetExistingMode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CreateTableImportRequestTarget = typing_extensions.Annotated[
    typing.Union[CreateTableImportRequestTarget_New, CreateTableImportRequestTarget_Existing],
    pydantic.Field(discriminator="type"),
]
