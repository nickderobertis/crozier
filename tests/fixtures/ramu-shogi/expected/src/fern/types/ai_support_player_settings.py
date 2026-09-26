

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ai_support_player_settings_mode import AiSupportPlayerSettingsMode


class AiSupportPlayerSettings(UniversalBaseModel):
    mode: AiSupportPlayerSettingsMode
    limit_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="limitCount"), pydantic.Field(alias="limitCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
