

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_integration_type_configuration_response import ApplicationIntegrationTypeConfigurationResponse
from .application_o_auth2install_params_response import ApplicationOAuth2InstallParamsResponse
from .application_types import ApplicationTypes
from .snowflake_type import SnowflakeType
from .user_response import UserResponse


class InviteApplicationResponse(UniversalBaseModel):
    id: SnowflakeType
    name: str
    icon: typing.Optional[str] = None
    description: str
    type: typing.Optional[ApplicationTypes] = None
    cover_image: typing.Optional[str] = None
    primary_sku_id: typing.Optional[SnowflakeType] = None
    bot: typing.Optional[UserResponse] = None
    slug: typing.Optional[str] = None
    guild_id: typing.Optional[SnowflakeType] = None
    rpc_origins: typing.Optional[typing.List[typing.Optional[str]]] = None
    bot_public: typing.Optional[bool] = None
    bot_require_code_grant: typing.Optional[bool] = None
    terms_of_service_url: typing.Optional[str] = None
    privacy_policy_url: typing.Optional[str] = None
    custom_install_url: typing.Optional[str] = None
    install_params: typing.Optional[ApplicationOAuth2InstallParamsResponse] = None
    integration_types_config: typing.Optional[
        typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfigurationResponse]]
    ] = None
    verify_key: str
    flags: int
    max_participants: typing.Optional[int] = None
    tags: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
