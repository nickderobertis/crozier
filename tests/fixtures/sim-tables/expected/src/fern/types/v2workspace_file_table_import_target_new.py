

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .folder_path_input import FolderPathInput


class V2WorkspaceFileTableImportTargetNew(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the table to create.
    """

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
