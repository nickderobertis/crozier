

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_command_response_options_item import ApplicationCommandResponseOptionsItem
from .application_command_type import ApplicationCommandType
from .application_integration_type import ApplicationIntegrationType
from .interaction_context_type import InteractionContextType
from .snowflake_type import SnowflakeType


class ApplicationCommandResponse(UniversalBaseModel):
    id: SnowflakeType
    application_id: SnowflakeType
    version: SnowflakeType
    default_member_permissions: typing.Optional[str] = None
    type: ApplicationCommandType
    name: str
    name_localized: typing.Optional[str] = None
    name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    description: str
    description_localized: typing.Optional[str] = None
    description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    guild_id: typing.Optional[SnowflakeType] = None
    dm_permission: typing.Optional[bool] = None
    contexts: typing.Optional[typing.List[InteractionContextType]] = None
    integration_types: typing.Optional[typing.List[ApplicationIntegrationType]] = None
    options: typing.Optional[typing.List[ApplicationCommandResponseOptionsItem]] = None
    nsfw: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
