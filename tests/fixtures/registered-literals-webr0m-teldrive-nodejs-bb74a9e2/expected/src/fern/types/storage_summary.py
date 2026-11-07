

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StorageSummary(UniversalBaseModel):
    logical_bytes: typing_extensions.Annotated[
        int, FieldMetadata(alias="logicalBytes"), pydantic.Field(alias="logicalBytes")
    ]
    active_files: typing_extensions.Annotated[
        int, FieldMetadata(alias="activeFiles"), pydantic.Field(alias="activeFiles")
    ]
    active_folders: typing_extensions.Annotated[
        int, FieldMetadata(alias="activeFolders"), pydantic.Field(alias="activeFolders")
    ]
    trashed_files: typing_extensions.Annotated[
        int, FieldMetadata(alias="trashedFiles"), pydantic.Field(alias="trashedFiles")
    ]
    spam_bytes: typing_extensions.Annotated[int, FieldMetadata(alias="spamBytes"), pydantic.Field(alias="spamBytes")]
    trash_bytes: typing_extensions.Annotated[int, FieldMetadata(alias="trashBytes"), pydantic.Field(alias="trashBytes")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
