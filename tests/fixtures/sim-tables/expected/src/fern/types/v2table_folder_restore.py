

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2folder import V2Folder
from .v2table_folder_restore_restored_items import V2TableFolderRestoreRestoredItems


class V2TableFolderRestore(UniversalBaseModel):
    """
    The restored folder and the counts of items it brought back.
    """

    folder: V2Folder = pydantic.Field()
    """
    The restored folder, at the path it actually landed on — which is not always the path requested.
    """

    restored_items: typing_extensions.Annotated[
        V2TableFolderRestoreRestoredItems,
        FieldMetadata(alias="restoredItems"),
        pydantic.Field(alias="restoredItems", description="What the restore brought back."),
    ]
    """
    What the restore brought back.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
