

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SurveyStylingLogo(UniversalBaseModel):
    url: typing.Optional[str] = None
    bg_color: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bgColor"), pydantic.Field(alias="bgColor")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
