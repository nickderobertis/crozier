

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2delete_table_folder_data_deleted_items import V2DeleteTableFolderDataDeletedItems


class V2DeleteTableFolderData(UniversalBaseModel):
    """
    Folder deletion acknowledgement and deleted-resource counts.
    """

    path: str = pydantic.Field()
    """
    Canonical path of the deleted folder.
    """

    deleted: bool = pydantic.Field()
    """
    Confirms that the folder was deleted.
    """

    deleted_items: typing_extensions.Annotated[
        V2DeleteTableFolderDataDeletedItems,
        FieldMetadata(alias="deletedItems"),
        pydantic.Field(alias="deletedItems", description="Deleted resource counts."),
    ]
    """
    Deleted resource counts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
