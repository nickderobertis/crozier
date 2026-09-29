

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_progress_response_level_belt import CurrentUserProgressResponseLevelBelt


class CurrentUserProgressResponseLevel(UniversalBaseModel):
    belt: CurrentUserProgressResponseLevelBelt
    bp_per_level: typing_extensions.Annotated[
        int, FieldMetadata(alias="bpPerLevel"), pydantic.Field(alias="bpPerLevel")
    ]
    bp_to_next_level: typing_extensions.Annotated[
        int, FieldMetadata(alias="bpToNextLevel"), pydantic.Field(alias="bpToNextLevel")
    ]
    is_max_level: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isMaxLevel"), pydantic.Field(alias="isMaxLevel")
    ]
    level: int
    progress_in_level: typing_extensions.Annotated[
        int, FieldMetadata(alias="progressInLevel"), pydantic.Field(alias="progressInLevel")
    ]
    total_brain_power: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalBrainPower"), pydantic.Field(alias="totalBrainPower")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
