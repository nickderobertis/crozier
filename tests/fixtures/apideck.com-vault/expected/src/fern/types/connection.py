

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .auth_type import AuthType
from .connection_configuration_item import ConnectionConfigurationItem
from .connection_state import ConnectionState
from .connection_status import ConnectionStatus
from .form_field import FormField
from .integration_state import IntegrationState
from .o_auth_grant_type import OAuthGrantType
from .webhook_subscription import WebhookSubscription


class Connection(UniversalBaseModel):
    auth_type: typing.Optional[AuthType] = None
    authorize_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
    """

    configurable_resources: typing.Optional[typing.List[str]] = None
    configuration: typing.Optional[typing.List[ConnectionConfigurationItem]] = None
    created_at: typing.Optional[float] = None
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.
    """

    form_fields: typing.Optional[typing.List[FormField]] = pydantic.Field(default=None)
    """
    The settings that are wanted to create a connection.
    """

    has_guide: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    A visual icon of the connection, that will be shown in the Vault
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the connection.
    """

    integration_state: typing.Optional[IntegrationState] = None
    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    The logo of the connection, that will be shown in the Vault
    """

    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Attach your own consumer specific metadata
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the connection
    """

    oauth_grant_type: typing.Optional[OAuthGrantType] = None
    resource_schema_support: typing.Optional[typing.List[str]] = None
    resource_settings_support: typing.Optional[typing.List[str]] = None
    revoke_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.
    """

    service_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the service this connection belongs to.
    """

    settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Connection settings. Values will persist to `form_fields` with corresponding id
    """

    settings_required_for_authorization: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of settings that are required to be configured on integration before authorization can occur
    """

    state: typing.Optional[ConnectionState] = None
    status: typing.Optional[ConnectionStatus] = pydantic.Field(default=None)
    """
    Status of the connection.
    """

    subscriptions: typing.Optional[typing.List[WebhookSubscription]] = None
    tag_line: typing.Optional[str] = None
    unified_api: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unified API category where the connection belongs to.
    """

    updated_at: typing.Optional[float] = None
    validation_support: typing.Optional[bool] = None
    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The website URL of the connection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
