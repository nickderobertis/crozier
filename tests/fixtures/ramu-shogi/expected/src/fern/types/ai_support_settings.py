

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ai_support_player_settings import AiSupportPlayerSettings


class AiSupportSettings(UniversalBaseModel):
    b: AiSupportPlayerSettings
    w: AiSupportPlayerSettings
    search_depth: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="searchDepth"), pydantic.Field(alias="searchDepth")
    ] = None
    search_time_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="searchTimeMs"), pydantic.Field(alias="searchTimeMs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
