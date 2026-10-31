

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .moderation_state import ModerationState


class ModerationAction(UniversalBaseModel):
    id: str
    label: str
    resulting_state: typing_extensions.Annotated[
        ModerationState, FieldMetadata(alias="resultingState"), pydantic.Field(alias="resultingState")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
