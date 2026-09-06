

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_explicit_content_filter_types import ApplicationExplicitContentFilterTypes
from .application_form_partial_description import ApplicationFormPartialDescription
from .application_integration_type_configuration import ApplicationIntegrationTypeConfiguration
from .application_o_auth2install_params import ApplicationOAuth2InstallParams
from .application_types import ApplicationTypes
from .snowflake_type import SnowflakeType


class ApplicationFormPartial(UniversalBaseModel):
    description: typing.Optional[ApplicationFormPartialDescription] = None
    icon: typing.Optional[str] = None
    cover_image: typing.Optional[str] = None
    team_id: typing.Optional[SnowflakeType] = None
    flags: typing.Optional[int] = None
    interactions_endpoint_url: typing.Optional[str] = None
    explicit_content_filter: typing.Optional[ApplicationExplicitContentFilterTypes] = None
    max_participants: typing.Optional[int] = None
    type: typing.Optional[ApplicationTypes] = None
    tags: typing.Optional[typing.List[str]] = None
    custom_install_url: typing.Optional[str] = None
    install_params: typing.Optional[ApplicationOAuth2InstallParams] = None
    role_connections_verification_url: typing.Optional[str] = None
    integration_types_config: typing.Optional[
        typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
