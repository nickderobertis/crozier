

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_part_source_text import FilePartSourceText


class ResourceSource(UniversalBaseModel):
    text: FilePartSourceText
    client_name: typing_extensions.Annotated[str, FieldMetadata(alias="clientName"), pydantic.Field(alias="clientName")]
    uri: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
