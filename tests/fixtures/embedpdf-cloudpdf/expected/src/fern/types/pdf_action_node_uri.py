

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PdfActionNodeUri(UniversalBaseModel):
    subtype: str
    next: typing.List[typing.Any]
    uri: str
    is_map: typing_extensions.Annotated[bool, FieldMetadata(alias="isMap"), pydantic.Field(alias="isMap")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
