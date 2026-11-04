

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DriveStatistics(UniversalBaseModel):
    total_files: typing_extensions.Annotated[int, FieldMetadata(alias="totalFiles"), pydantic.Field(alias="totalFiles")]
    total_folders: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalFolders"), pydantic.Field(alias="totalFolders")
    ]
    total_bytes: typing_extensions.Annotated[int, FieldMetadata(alias="totalBytes"), pydantic.Field(alias="totalBytes")]
    trashed_files: typing_extensions.Annotated[
        int, FieldMetadata(alias="trashedFiles"), pydantic.Field(alias="trashedFiles")
    ]
    active_shares: typing_extensions.Annotated[
        int, FieldMetadata(alias="activeShares"), pydantic.Field(alias="activeShares")
    ]
    open_uploads: typing_extensions.Annotated[
        int, FieldMetadata(alias="openUploads"), pydantic.Field(alias="openUploads")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
