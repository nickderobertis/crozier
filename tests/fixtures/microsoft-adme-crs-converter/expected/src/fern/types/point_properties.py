

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PointProperties(UniversalBaseModel):
    crossline: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="Crossline"), pydantic.Field(alias="Crossline")
    ] = None
    inline: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="Inline"), pydantic.Field(alias="Inline")
    ] = None
    label: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Label"), pydantic.Field(alias="Label")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
