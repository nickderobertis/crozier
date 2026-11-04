

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ThemingBackground(UniversalBaseModel):
    background_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundImage"), pydantic.Field(alias="backgroundImage")
    ] = None
    background_color: typing_extensions.Annotated[
        str, FieldMetadata(alias="backgroundColor"), pydantic.Field(alias="backgroundColor")
    ]
    version: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
