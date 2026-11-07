

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_category import FileCategory


class FileCategoryStatistics(UniversalBaseModel):
    category: FileCategory
    total_files: typing_extensions.Annotated[int, FieldMetadata(alias="totalFiles"), pydantic.Field(alias="totalFiles")]
    total_size: typing_extensions.Annotated[int, FieldMetadata(alias="totalSize"), pydantic.Field(alias="totalSize")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
