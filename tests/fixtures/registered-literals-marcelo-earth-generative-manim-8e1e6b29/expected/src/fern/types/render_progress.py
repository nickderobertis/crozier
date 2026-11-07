

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RenderProgress(UniversalBaseModel):
    animation_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="animationIndex"), pydantic.Field(alias="animationIndex")
    ] = None
    percentage: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
