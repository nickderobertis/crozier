

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .added_at import AddedAt
from .folder_id import FolderId
from .library_id import LibraryId


class Folder(UniversalBaseModel):
    """
    Folder used in library
    """

    id: typing.Optional[FolderId] = None
    full_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fullPath"),
        pydantic.Field(alias="fullPath", description="The path on the server for the folder. (Read Only)"),
    ] = None
    """
    The path on the server for the folder. (Read Only)
    """

    library_id: typing_extensions.Annotated[
        typing.Optional[LibraryId], FieldMetadata(alias="libraryId"), pydantic.Field(alias="libraryId")
    ] = None
    added_at: typing_extensions.Annotated[
        typing.Optional[AddedAt], FieldMetadata(alias="addedAt"), pydantic.Field(alias="addedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
