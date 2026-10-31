

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FilteredShareFolder(UniversalBaseModel):
    id: str
    name: str
    file_count: typing_extensions.Annotated[float, FieldMetadata(alias="fileCount"), pydantic.Field(alias="fileCount")]
    folder_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="folderCount"), pydantic.Field(alias="folderCount")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
