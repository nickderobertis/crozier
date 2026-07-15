

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connector_auth_type import ConnectorAuthType
from .connector_doc import ConnectorDoc
from .connector_event import ConnectorEvent
from .connector_oauth_credentials_source import ConnectorOauthCredentialsSource
from .connector_oauth_grant_type import ConnectorOauthGrantType
from .connector_oauth_scopes_item import ConnectorOauthScopesItem
from .connector_setting import ConnectorSetting
from .connector_status import ConnectorStatus
from .connector_tls_support import ConnectorTlsSupport
from .connector_unified_apis_item import ConnectorUnifiedApisItem
from .linked_connector_resource import LinkedConnectorResource
from .resource_id import ResourceId
from .webhook_support import WebhookSupport


class Connector(UniversalBaseModel):
    auth_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether a connector only supports authentication. In this case the connector is not mapped to a Unified API, but can be used with the Proxy API
    """

    auth_type: typing.Optional[ConnectorAuthType] = pydantic.Field(default=None)
    """
    Type of authorization used by the connector
    """

    blind_mapped: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Set to `true` when connector was implemented from downstream docs only and without API access. This state indicates that integration will require Apideck support, and access to downstream API to validate mapping quality.
    """

    configurable_resources: typing.Optional[typing.List[ResourceId]] = pydantic.Field(default=None)
    """
    List of resources that have settings that can be configured.
    """

    custom_scopes: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Set to `true` when connector allows the definition of custom scopes.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the object.
    """

    docs: typing.Optional[typing.List[ConnectorDoc]] = None
    free_trial_available: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Set to `true` when the connector offers a free trial. Use `signup_url` to sign up for a free trial
    """

    has_sandbox_credentials: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether Apideck Sandbox OAuth credentials are available.
    """

    icon_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to a small square icon for the connector.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the connector.
    """

    logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the full logo for the connector.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the connector.
    """

    oauth_credentials_source: typing.Optional[ConnectorOauthCredentialsSource] = pydantic.Field(default=None)
    """
    Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault.
    """

    oauth_grant_type: typing.Optional[ConnectorOauthGrantType] = pydantic.Field(default=None)
    """
    OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types
    """

    oauth_scopes: typing.Optional[typing.List[ConnectorOauthScopesItem]] = pydantic.Field(default=None)
    """
    List of OAuth Scopes available for this connector.
    """

    service_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Service provider identifier
    """

    settings: typing.Optional[typing.List[ConnectorSetting]] = None
    signup_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the connector's signup page.
    """

    status: typing.Optional[ConnectorStatus] = None
    supported_events: typing.Optional[typing.List[ConnectorEvent]] = pydantic.Field(default=None)
    """
    List of events that are supported on the connector across all Unified APIs.
    """

    supported_resources: typing.Optional[typing.List[LinkedConnectorResource]] = pydantic.Field(default=None)
    """
    List of resources that are supported on the connector.
    """

    tls_support: typing.Optional[ConnectorTlsSupport] = None
    unified_apis: typing.Optional[typing.List[ConnectorUnifiedApisItem]] = pydantic.Field(default=None)
    """
    List of Unified APIs that feature this connector.
    """

    webhook_support: typing.Optional[WebhookSupport] = None
    website_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the connector's website.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
