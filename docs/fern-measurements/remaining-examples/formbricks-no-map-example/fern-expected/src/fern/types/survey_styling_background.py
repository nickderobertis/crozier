

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_styling_background_bg_type import SurveyStylingBackgroundBgType


class SurveyStylingBackground(UniversalBaseModel):
    bg: typing.Optional[str] = None
    bg_type: typing_extensions.Annotated[
        typing.Optional[SurveyStylingBackgroundBgType], FieldMetadata(alias="bgType"), pydantic.Field(alias="bgType")
    ] = None
    brightness: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
