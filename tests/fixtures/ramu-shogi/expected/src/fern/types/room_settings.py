

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ai_support_settings import AiSupportSettings
from .pass_rights_config import PassRightsConfig
from .time_control_settings import TimeControlSettings


class RoomSettings(UniversalBaseModel):
    start_sfen: typing_extensions.Annotated[str, FieldMetadata(alias="startSfen"), pydantic.Field(alias="startSfen")]
    time_control: typing_extensions.Annotated[
        TimeControlSettings, FieldMetadata(alias="timeControl"), pydantic.Field(alias="timeControl")
    ]
    pass_rights: typing_extensions.Annotated[
        typing.Optional[PassRightsConfig], FieldMetadata(alias="passRights"), pydantic.Field(alias="passRights")
    ] = None
    ai_support: typing_extensions.Annotated[
        typing.Optional[AiSupportSettings], FieldMetadata(alias="aiSupport"), pydantic.Field(alias="aiSupport")
    ] = None
    takeback: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
