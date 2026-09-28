

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_workspace_file_import_source_type import V2TableWorkspaceFileImportSourceType


class V2TableWorkspaceFileImportSource(UniversalBaseModel):
    """
    Existing workspace file used as a CSV import source.
    """

    type: V2TableWorkspaceFileImportSourceType = pydantic.Field()
    """
    Workspace-file source discriminator.
    """

    file_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fileId"),
        pydantic.Field(alias="fileId", description="Existing workspace file identifier."),
    ]
    """
    Existing workspace file identifier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
