

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_rejected_choice_window_window import MapRejectedChoiceWindowWindow


class MapRejectedChoiceWindow(UniversalBaseModel):
    window: typing_extensions.Annotated[
        MapRejectedChoiceWindowWindow, FieldMetadata(alias="Window"), pydantic.Field(alias="Window")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
