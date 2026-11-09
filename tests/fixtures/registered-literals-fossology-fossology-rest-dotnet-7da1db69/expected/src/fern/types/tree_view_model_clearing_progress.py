

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TreeViewModelClearingProgress(UniversalBaseModel):
    """
    The progress of clearing.
    """

    files_cleared: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="filesCleared"),
        pydantic.Field(alias="filesCleared", description="The number of files cleared."),
    ] = None
    """
    The number of files cleared.
    """

    files_to_be_cleared: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="filesToBeCleared"),
        pydantic.Field(alias="filesToBeCleared", description="The number of files to be cleared."),
    ] = None
    """
    The number of files to be cleared.
    """

    total_files_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalFilesCount"),
        pydantic.Field(alias="totalFilesCount", description="The total count of files."),
    ] = None
    """
    The total count of files.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
