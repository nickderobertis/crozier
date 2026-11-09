

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ClearingProgressInfo(UniversalBaseModel):
    total_files_of_interest: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalFilesOfInterest"),
        pydantic.Field(alias="totalFilesOfInterest", description="Total number of targeted files to be cleared"),
    ] = None
    """
    Total number of targeted files to be cleared
    """

    total_files_cleared: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalFilesCleared"),
        pydantic.Field(alias="totalFilesCleared", description="Total number of files cleared"),
    ] = None
    """
    Total number of files cleared
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
