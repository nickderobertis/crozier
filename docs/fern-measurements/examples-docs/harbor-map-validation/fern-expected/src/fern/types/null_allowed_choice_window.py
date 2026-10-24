

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .null_allowed_choice_window_window import NullAllowedChoiceWindowWindow


class NullAllowedChoiceWindow(UniversalBaseModel):
    window: typing_extensions.Annotated[
        NullAllowedChoiceWindowWindow, FieldMetadata(alias="Window"), pydantic.Field(alias="Window")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
