

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FileContentPatchHunksItem(UniversalBaseModel):
    old_start: typing_extensions.Annotated[float, FieldMetadata(alias="oldStart"), pydantic.Field(alias="oldStart")]
    old_lines: typing_extensions.Annotated[float, FieldMetadata(alias="oldLines"), pydantic.Field(alias="oldLines")]
    new_start: typing_extensions.Annotated[float, FieldMetadata(alias="newStart"), pydantic.Field(alias="newStart")]
    new_lines: typing_extensions.Annotated[float, FieldMetadata(alias="newLines"), pydantic.Field(alias="newLines")]
    lines: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
