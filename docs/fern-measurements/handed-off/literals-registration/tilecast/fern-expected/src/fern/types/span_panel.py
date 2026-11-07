

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SpanPanel(UniversalBaseModel):
    screen_id: typing_extensions.Annotated[str, FieldMetadata(alias="screenId"), pydantic.Field(alias="screenId")]
    screen_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="screenName"), pydantic.Field(alias="screenName")
    ] = None
    order: int
    x: int
    y: int
    width: int
    height: int
    rotation: int
    bezel_left: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bezelLeft"), pydantic.Field(alias="bezelLeft")
    ] = None
    bezel_top: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bezelTop"), pydantic.Field(alias="bezelTop")
    ] = None
    bezel_right: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bezelRight"), pydantic.Field(alias="bezelRight")
    ] = None
    bezel_bottom: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="bezelBottom"), pydantic.Field(alias="bezelBottom")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
