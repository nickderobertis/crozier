

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LessonCompletionResponseBelt(UniversalBaseModel):
    belt: str
    bp_per_level: typing_extensions.Annotated[
        float, FieldMetadata(alias="bpPerLevel"), pydantic.Field(alias="bpPerLevel")
    ]
    bp_to_next_level: typing_extensions.Annotated[
        float, FieldMetadata(alias="bpToNextLevel"), pydantic.Field(alias="bpToNextLevel")
    ]
    is_max_level: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isMaxLevel"), pydantic.Field(alias="isMaxLevel")
    ]
    level: int
    progress_in_level: typing_extensions.Annotated[
        float, FieldMetadata(alias="progressInLevel"), pydantic.Field(alias="progressInLevel")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
