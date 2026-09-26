

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocText200Response(UniversalBaseModel):
    text: str
    char_count: typing_extensions.Annotated[int, FieldMetadata(alias="charCount"), pydantic.Field(alias="charCount")]
    char_map: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[typing.Any]]],
        FieldMetadata(alias="charMap"),
        pydantic.Field(alias="charMap"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
