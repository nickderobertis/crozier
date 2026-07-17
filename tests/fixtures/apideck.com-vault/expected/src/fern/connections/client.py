

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.auth_type import AuthType
from ..types.connection_configuration_item import ConnectionConfigurationItem
from ..types.connection_state import ConnectionState
from ..types.connection_status import ConnectionStatus
from ..types.create_connection_response import CreateConnectionResponse
from ..types.form_field import FormField
from ..types.get_connection_response import GetConnectionResponse
from ..types.get_connections_response import GetConnectionsResponse
from ..types.integration_state import IntegrationState
from ..types.o_auth_grant_type import OAuthGrantType
from ..types.unexpected_error_response import UnexpectedErrorResponse
from ..types.update_connection_response import UpdateConnectionResponse
from ..types.webhook_subscription import WebhookSubscription
from .raw_client import AsyncRawConnectionsClient, RawConnectionsClient
from .types.connection_import_data_credentials import ConnectionImportDataCredentials


OMIT = typing.cast(typing.Any, ...)


class ConnectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectionsClient
        """
        return self._raw_client

    def authorize(
        self,
        service_id: str,
        application_id: str,
        *,
        state: str,
        redirect_uri: str,
        scope: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnexpectedErrorResponse:
        """
        __In most cases the authorize link is provided in the ``/connections`` endpoint. Normally you don't need to manually generate these links.__

        Use this endpoint to authenticate a user with a connector. It will return a 301 redirect to the downstream connector endpoints.

        Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.

        Vault handles the complete Authorization Code Grant Type Flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application.

        Parameters
        ----------
        service_id : str
            Service ID of the resource to return

        application_id : str
            Application ID of the resource to return

        state : str
            An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.

        redirect_uri : str
            URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.

        scope : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector's documentation for the available scopes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnexpectedErrorResponse
            Unexpected error

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.authorize(
            service_id="pipedrive",
            application_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
            state="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk",
            redirect_uri="http://example.com/integrations",
        )
        """
        _response = self._raw_client.authorize(
            service_id,
            application_id,
            state=state,
            redirect_uri=redirect_uri,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    def callback(
        self, *, state: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UnexpectedErrorResponse:
        """
        This endpoint gets called after the triggering the authorize flow.

        Callback links need a state and code parameter to verify the validity of the request.

        Parameters
        ----------
        state : str
            An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.

        code : str
            An authorization code from the connector which Apideck Vault will later exchange for an access token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnexpectedErrorResponse
            Unexpected error

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.callback(
            state="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk",
            code="g0ZGZmNjVmOWI",
        )
        """
        _response = self._raw_client.callback(state=state, code=code, request_options=request_options)
        return _response.data

    def all_(
        self,
        *,
        apideck_consumer_id: str,
        api: typing.Optional[str] = None,
        configured: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionsResponse:
        """
        This endpoint includes all the configured integrations and contains the required assets
        to build an integrations page where your users can install integrations.
        OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows.

        Parameters
        ----------
        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        api : typing.Optional[str]
            Scope results to Unified API

        configured : typing.Optional[bool]
            Scopes results to connections that have been configured or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionsResponse
            Connections

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.all_(
            apideck_consumer_id="x-apideck-consumer-id",
            api="crm",
        )
        """
        _response = self._raw_client.all_(
            apideck_consumer_id=apideck_consumer_id, api=api, configured=configured, request_options=request_options
        )
        return _response.data

    def one(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionResponse:
        """
        Get a connection

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionResponse
            Connection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.one(
            unified_api="crm",
            service_id="pipedrive",
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.one(
            unified_api, service_id, apideck_consumer_id=apideck_consumer_id, request_options=request_options
        )
        return _response.data

    def add(
        self,
        unified_api_: str,
        service_id_: str,
        *,
        apideck_consumer_id: str,
        auth_type: typing.Optional[AuthType] = OMIT,
        authorize_url: typing.Optional[str] = OMIT,
        configurable_resources: typing.Optional[typing.Sequence[str]] = OMIT,
        configuration: typing.Optional[typing.Sequence[ConnectionConfigurationItem]] = OMIT,
        created_at: typing.Optional[float] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        form_fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        has_guide: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        integration_state: typing.Optional[IntegrationState] = OMIT,
        logo: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings_required_for_authorization: typing.Optional[typing.Sequence[str]] = OMIT,
        state: typing.Optional[ConnectionState] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        subscriptions: typing.Optional[typing.Sequence[WebhookSubscription]] = OMIT,
        tag_line: typing.Optional[str] = OMIT,
        unified_api: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[float] = OMIT,
        validation_support: typing.Optional[bool] = OMIT,
        website: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponse:
        """
        Create an authorized connection

        Parameters
        ----------
        unified_api_ : str
            Unified API

        service_id_ : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        auth_type : typing.Optional[AuthType]

        authorize_url : typing.Optional[str]
            The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        configurable_resources : typing.Optional[typing.Sequence[str]]

        configuration : typing.Optional[typing.Sequence[ConnectionConfigurationItem]]

        created_at : typing.Optional[float]

        enabled : typing.Optional[bool]
            Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.

        form_fields : typing.Optional[typing.Sequence[FormField]]
            The settings that are wanted to create a connection.

        has_guide : typing.Optional[bool]
            Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).

        icon : typing.Optional[str]
            A visual icon of the connection, that will be shown in the Vault

        id : typing.Optional[str]
            The unique identifier of the connection.

        integration_state : typing.Optional[IntegrationState]

        logo : typing.Optional[str]
            The logo of the connection, that will be shown in the Vault

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Attach your own consumer specific metadata

        name : typing.Optional[str]
            The name of the connection

        oauth_grant_type : typing.Optional[OAuthGrantType]

        resource_schema_support : typing.Optional[typing.Sequence[str]]

        resource_settings_support : typing.Optional[typing.Sequence[str]]

        revoke_url : typing.Optional[str]
            The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        service_id : typing.Optional[str]
            The ID of the service this connection belongs to.

        settings : typing.Optional[typing.Dict[str, typing.Any]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        settings_required_for_authorization : typing.Optional[typing.Sequence[str]]
            List of settings that are required to be configured on integration before authorization can occur

        state : typing.Optional[ConnectionState]

        status : typing.Optional[ConnectionStatus]
            Status of the connection.

        subscriptions : typing.Optional[typing.Sequence[WebhookSubscription]]

        tag_line : typing.Optional[str]

        unified_api : typing.Optional[str]
            The unified API category where the connection belongs to.

        updated_at : typing.Optional[float]

        validation_support : typing.Optional[bool]

        website : typing.Optional[str]
            The website URL of the connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionResponse
            Connection created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.add(
            unified_api_="crm",
            service_id_="pipedrive",
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.add(
            unified_api_,
            service_id_,
            apideck_consumer_id=apideck_consumer_id,
            auth_type=auth_type,
            authorize_url=authorize_url,
            configurable_resources=configurable_resources,
            configuration=configuration,
            created_at=created_at,
            enabled=enabled,
            form_fields=form_fields,
            has_guide=has_guide,
            icon=icon,
            id=id,
            integration_state=integration_state,
            logo=logo,
            metadata=metadata,
            name=name,
            oauth_grant_type=oauth_grant_type,
            resource_schema_support=resource_schema_support,
            resource_settings_support=resource_settings_support,
            revoke_url=revoke_url,
            service_id=service_id,
            settings=settings,
            settings_required_for_authorization=settings_required_for_authorization,
            state=state,
            status=status,
            subscriptions=subscriptions,
            tag_line=tag_line,
            unified_api=unified_api,
            updated_at=updated_at,
            validation_support=validation_support,
            website=website,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a connection

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.delete(
            unified_api="crm",
            service_id="pipedrive",
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.delete(
            unified_api, service_id, apideck_consumer_id=apideck_consumer_id, request_options=request_options
        )
        return _response.data

    def update(
        self,
        unified_api_: str,
        service_id_: str,
        *,
        apideck_consumer_id: str,
        auth_type: typing.Optional[AuthType] = OMIT,
        authorize_url: typing.Optional[str] = OMIT,
        configurable_resources: typing.Optional[typing.Sequence[str]] = OMIT,
        configuration: typing.Optional[typing.Sequence[ConnectionConfigurationItem]] = OMIT,
        created_at: typing.Optional[float] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        form_fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        has_guide: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        integration_state: typing.Optional[IntegrationState] = OMIT,
        logo: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings_required_for_authorization: typing.Optional[typing.Sequence[str]] = OMIT,
        state: typing.Optional[ConnectionState] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        subscriptions: typing.Optional[typing.Sequence[WebhookSubscription]] = OMIT,
        tag_line: typing.Optional[str] = OMIT,
        unified_api: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[float] = OMIT,
        validation_support: typing.Optional[bool] = OMIT,
        website: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateConnectionResponse:
        """
        Update a connection

        Parameters
        ----------
        unified_api_ : str
            Unified API

        service_id_ : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        auth_type : typing.Optional[AuthType]

        authorize_url : typing.Optional[str]
            The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        configurable_resources : typing.Optional[typing.Sequence[str]]

        configuration : typing.Optional[typing.Sequence[ConnectionConfigurationItem]]

        created_at : typing.Optional[float]

        enabled : typing.Optional[bool]
            Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.

        form_fields : typing.Optional[typing.Sequence[FormField]]
            The settings that are wanted to create a connection.

        has_guide : typing.Optional[bool]
            Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).

        icon : typing.Optional[str]
            A visual icon of the connection, that will be shown in the Vault

        id : typing.Optional[str]
            The unique identifier of the connection.

        integration_state : typing.Optional[IntegrationState]

        logo : typing.Optional[str]
            The logo of the connection, that will be shown in the Vault

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Attach your own consumer specific metadata

        name : typing.Optional[str]
            The name of the connection

        oauth_grant_type : typing.Optional[OAuthGrantType]

        resource_schema_support : typing.Optional[typing.Sequence[str]]

        resource_settings_support : typing.Optional[typing.Sequence[str]]

        revoke_url : typing.Optional[str]
            The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        service_id : typing.Optional[str]
            The ID of the service this connection belongs to.

        settings : typing.Optional[typing.Dict[str, typing.Any]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        settings_required_for_authorization : typing.Optional[typing.Sequence[str]]
            List of settings that are required to be configured on integration before authorization can occur

        state : typing.Optional[ConnectionState]

        status : typing.Optional[ConnectionStatus]
            Status of the connection.

        subscriptions : typing.Optional[typing.Sequence[WebhookSubscription]]

        tag_line : typing.Optional[str]

        unified_api : typing.Optional[str]
            The unified API category where the connection belongs to.

        updated_at : typing.Optional[float]

        validation_support : typing.Optional[bool]

        website : typing.Optional[str]
            The website URL of the connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateConnectionResponse
            Connection updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.update(
            unified_api_="crm",
            service_id_="pipedrive",
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.update(
            unified_api_,
            service_id_,
            apideck_consumer_id=apideck_consumer_id,
            auth_type=auth_type,
            authorize_url=authorize_url,
            configurable_resources=configurable_resources,
            configuration=configuration,
            created_at=created_at,
            enabled=enabled,
            form_fields=form_fields,
            has_guide=has_guide,
            icon=icon,
            id=id,
            integration_state=integration_state,
            logo=logo,
            metadata=metadata,
            name=name,
            oauth_grant_type=oauth_grant_type,
            resource_schema_support=resource_schema_support,
            resource_settings_support=resource_settings_support,
            revoke_url=revoke_url,
            service_id=service_id,
            settings=settings,
            settings_required_for_authorization=settings_required_for_authorization,
            state=state,
            status=status,
            subscriptions=subscriptions,
            tag_line=tag_line,
            unified_api=unified_api,
            updated_at=updated_at,
            validation_support=validation_support,
            website=website,
            request_options=request_options,
        )
        return _response.data

    def import_(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        credentials: typing.Optional[ConnectionImportDataCredentials] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponse:
        """
        Import an authorized connection.

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        credentials : typing.Optional[ConnectionImportDataCredentials]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Attach your own consumer specific metadata

        settings : typing.Optional[typing.Dict[str, typing.Any]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionResponse
            Connection created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.import_(
            unified_api="crm",
            service_id="pipedrive",
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.import_(
            unified_api,
            service_id,
            apideck_consumer_id=apideck_consumer_id,
            credentials=credentials,
            metadata=metadata,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    def token(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionResponse:
        """
        Get an access token for a connection and store it in Vault. Currently only supported for connections with the client_credentials OAuth grant type.

        Note that the access token will not be returned in the response. A 200 response code indicates a valid access token was stored on the connection.

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionResponse
            Connection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.token(
            unified_api="crm",
            service_id="pipedrive",
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.token(
            unified_api, service_id, apideck_consumer_id=apideck_consumer_id, request_options=request_options
        )
        return _response.data

    def connection_settings_all(
        self,
        unified_api: str,
        service_id: str,
        resource: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionResponse:
        """
        This endpoint returns custom settings and their defaults required by connection for a given resource.

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        resource : str
            Resource Name

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionResponse
            Connection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.connection_settings_all(
            unified_api="crm",
            service_id="pipedrive",
            resource="leads",
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.connection_settings_all(
            unified_api, service_id, resource, apideck_consumer_id=apideck_consumer_id, request_options=request_options
        )
        return _response.data

    def connection_settings_update(
        self,
        unified_api_: str,
        service_id_: str,
        resource: str,
        *,
        apideck_consumer_id: str,
        auth_type: typing.Optional[AuthType] = OMIT,
        authorize_url: typing.Optional[str] = OMIT,
        configurable_resources: typing.Optional[typing.Sequence[str]] = OMIT,
        configuration: typing.Optional[typing.Sequence[ConnectionConfigurationItem]] = OMIT,
        created_at: typing.Optional[float] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        form_fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        has_guide: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        integration_state: typing.Optional[IntegrationState] = OMIT,
        logo: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings_required_for_authorization: typing.Optional[typing.Sequence[str]] = OMIT,
        state: typing.Optional[ConnectionState] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        subscriptions: typing.Optional[typing.Sequence[WebhookSubscription]] = OMIT,
        tag_line: typing.Optional[str] = OMIT,
        unified_api: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[float] = OMIT,
        validation_support: typing.Optional[bool] = OMIT,
        website: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateConnectionResponse:
        """
        Update default values for a connection's resource settings

        Parameters
        ----------
        unified_api_ : str
            Unified API

        service_id_ : str
            Service ID of the resource to return

        resource : str
            Resource Name

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        auth_type : typing.Optional[AuthType]

        authorize_url : typing.Optional[str]
            The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        configurable_resources : typing.Optional[typing.Sequence[str]]

        configuration : typing.Optional[typing.Sequence[ConnectionConfigurationItem]]

        created_at : typing.Optional[float]

        enabled : typing.Optional[bool]
            Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.

        form_fields : typing.Optional[typing.Sequence[FormField]]
            The settings that are wanted to create a connection.

        has_guide : typing.Optional[bool]
            Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).

        icon : typing.Optional[str]
            A visual icon of the connection, that will be shown in the Vault

        id : typing.Optional[str]
            The unique identifier of the connection.

        integration_state : typing.Optional[IntegrationState]

        logo : typing.Optional[str]
            The logo of the connection, that will be shown in the Vault

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Attach your own consumer specific metadata

        name : typing.Optional[str]
            The name of the connection

        oauth_grant_type : typing.Optional[OAuthGrantType]

        resource_schema_support : typing.Optional[typing.Sequence[str]]

        resource_settings_support : typing.Optional[typing.Sequence[str]]

        revoke_url : typing.Optional[str]
            The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        service_id : typing.Optional[str]
            The ID of the service this connection belongs to.

        settings : typing.Optional[typing.Dict[str, typing.Any]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        settings_required_for_authorization : typing.Optional[typing.Sequence[str]]
            List of settings that are required to be configured on integration before authorization can occur

        state : typing.Optional[ConnectionState]

        status : typing.Optional[ConnectionStatus]
            Status of the connection.

        subscriptions : typing.Optional[typing.Sequence[WebhookSubscription]]

        tag_line : typing.Optional[str]

        unified_api : typing.Optional[str]
            The unified API category where the connection belongs to.

        updated_at : typing.Optional[float]

        validation_support : typing.Optional[bool]

        website : typing.Optional[str]
            The website URL of the connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateConnectionResponse
            Connection updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.connection_settings_update(
            unified_api_="crm",
            service_id_="pipedrive",
            resource="leads",
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.connection_settings_update(
            unified_api_,
            service_id_,
            resource,
            apideck_consumer_id=apideck_consumer_id,
            auth_type=auth_type,
            authorize_url=authorize_url,
            configurable_resources=configurable_resources,
            configuration=configuration,
            created_at=created_at,
            enabled=enabled,
            form_fields=form_fields,
            has_guide=has_guide,
            icon=icon,
            id=id,
            integration_state=integration_state,
            logo=logo,
            metadata=metadata,
            name=name,
            oauth_grant_type=oauth_grant_type,
            resource_schema_support=resource_schema_support,
            resource_settings_support=resource_settings_support,
            revoke_url=revoke_url,
            service_id=service_id,
            settings=settings,
            settings_required_for_authorization=settings_required_for_authorization,
            state=state,
            status=status,
            subscriptions=subscriptions,
            tag_line=tag_line,
            unified_api=unified_api,
            updated_at=updated_at,
            validation_support=validation_support,
            website=website,
            request_options=request_options,
        )
        return _response.data

    def revoke(
        self,
        service_id: str,
        application_id: str,
        *,
        state: str,
        redirect_uri: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnexpectedErrorResponse:
        """
        __In most cases the authorize link is provided in the ``/connections`` endpoint. Normally you don't need to manually generate these links.__

        Use this endpoint to revoke an existing OAuth connector.

        Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.

        Vault handles the complete revoke flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application.

        Parameters
        ----------
        service_id : str
            Service ID of the resource to return

        application_id : str
            Application ID of the resource to return

        state : str
            An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.

        redirect_uri : str
            URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnexpectedErrorResponse
            Unexpected error

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.revoke(
            service_id="pipedrive",
            application_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
            state="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk",
            redirect_uri="http://example.com/integrations",
        )
        """
        _response = self._raw_client.revoke(
            service_id, application_id, state=state, redirect_uri=redirect_uri, request_options=request_options
        )
        return _response.data


class AsyncConnectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectionsClient
        """
        return self._raw_client

    async def authorize(
        self,
        service_id: str,
        application_id: str,
        *,
        state: str,
        redirect_uri: str,
        scope: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnexpectedErrorResponse:
        """
        __In most cases the authorize link is provided in the ``/connections`` endpoint. Normally you don't need to manually generate these links.__

        Use this endpoint to authenticate a user with a connector. It will return a 301 redirect to the downstream connector endpoints.

        Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.

        Vault handles the complete Authorization Code Grant Type Flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application.

        Parameters
        ----------
        service_id : str
            Service ID of the resource to return

        application_id : str
            Application ID of the resource to return

        state : str
            An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.

        redirect_uri : str
            URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.

        scope : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector's documentation for the available scopes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnexpectedErrorResponse
            Unexpected error

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.authorize(
                service_id="pipedrive",
                application_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
                state="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk",
                redirect_uri="http://example.com/integrations",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.authorize(
            service_id,
            application_id,
            state=state,
            redirect_uri=redirect_uri,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    async def callback(
        self, *, state: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UnexpectedErrorResponse:
        """
        This endpoint gets called after the triggering the authorize flow.

        Callback links need a state and code parameter to verify the validity of the request.

        Parameters
        ----------
        state : str
            An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.

        code : str
            An authorization code from the connector which Apideck Vault will later exchange for an access token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnexpectedErrorResponse
            Unexpected error

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.callback(
                state="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk",
                code="g0ZGZmNjVmOWI",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.callback(state=state, code=code, request_options=request_options)
        return _response.data

    async def all_(
        self,
        *,
        apideck_consumer_id: str,
        api: typing.Optional[str] = None,
        configured: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionsResponse:
        """
        This endpoint includes all the configured integrations and contains the required assets
        to build an integrations page where your users can install integrations.
        OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows.

        Parameters
        ----------
        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        api : typing.Optional[str]
            Scope results to Unified API

        configured : typing.Optional[bool]
            Scopes results to connections that have been configured or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionsResponse
            Connections

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.all_(
                apideck_consumer_id="x-apideck-consumer-id",
                api="crm",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            apideck_consumer_id=apideck_consumer_id, api=api, configured=configured, request_options=request_options
        )
        return _response.data

    async def one(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionResponse:
        """
        Get a connection

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionResponse
            Connection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.one(
                unified_api="crm",
                service_id="pipedrive",
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(
            unified_api, service_id, apideck_consumer_id=apideck_consumer_id, request_options=request_options
        )
        return _response.data

    async def add(
        self,
        unified_api_: str,
        service_id_: str,
        *,
        apideck_consumer_id: str,
        auth_type: typing.Optional[AuthType] = OMIT,
        authorize_url: typing.Optional[str] = OMIT,
        configurable_resources: typing.Optional[typing.Sequence[str]] = OMIT,
        configuration: typing.Optional[typing.Sequence[ConnectionConfigurationItem]] = OMIT,
        created_at: typing.Optional[float] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        form_fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        has_guide: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        integration_state: typing.Optional[IntegrationState] = OMIT,
        logo: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings_required_for_authorization: typing.Optional[typing.Sequence[str]] = OMIT,
        state: typing.Optional[ConnectionState] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        subscriptions: typing.Optional[typing.Sequence[WebhookSubscription]] = OMIT,
        tag_line: typing.Optional[str] = OMIT,
        unified_api: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[float] = OMIT,
        validation_support: typing.Optional[bool] = OMIT,
        website: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponse:
        """
        Create an authorized connection

        Parameters
        ----------
        unified_api_ : str
            Unified API

        service_id_ : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        auth_type : typing.Optional[AuthType]

        authorize_url : typing.Optional[str]
            The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        configurable_resources : typing.Optional[typing.Sequence[str]]

        configuration : typing.Optional[typing.Sequence[ConnectionConfigurationItem]]

        created_at : typing.Optional[float]

        enabled : typing.Optional[bool]
            Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.

        form_fields : typing.Optional[typing.Sequence[FormField]]
            The settings that are wanted to create a connection.

        has_guide : typing.Optional[bool]
            Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).

        icon : typing.Optional[str]
            A visual icon of the connection, that will be shown in the Vault

        id : typing.Optional[str]
            The unique identifier of the connection.

        integration_state : typing.Optional[IntegrationState]

        logo : typing.Optional[str]
            The logo of the connection, that will be shown in the Vault

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Attach your own consumer specific metadata

        name : typing.Optional[str]
            The name of the connection

        oauth_grant_type : typing.Optional[OAuthGrantType]

        resource_schema_support : typing.Optional[typing.Sequence[str]]

        resource_settings_support : typing.Optional[typing.Sequence[str]]

        revoke_url : typing.Optional[str]
            The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        service_id : typing.Optional[str]
            The ID of the service this connection belongs to.

        settings : typing.Optional[typing.Dict[str, typing.Any]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        settings_required_for_authorization : typing.Optional[typing.Sequence[str]]
            List of settings that are required to be configured on integration before authorization can occur

        state : typing.Optional[ConnectionState]

        status : typing.Optional[ConnectionStatus]
            Status of the connection.

        subscriptions : typing.Optional[typing.Sequence[WebhookSubscription]]

        tag_line : typing.Optional[str]

        unified_api : typing.Optional[str]
            The unified API category where the connection belongs to.

        updated_at : typing.Optional[float]

        validation_support : typing.Optional[bool]

        website : typing.Optional[str]
            The website URL of the connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionResponse
            Connection created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.add(
                unified_api_="crm",
                service_id_="pipedrive",
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            unified_api_,
            service_id_,
            apideck_consumer_id=apideck_consumer_id,
            auth_type=auth_type,
            authorize_url=authorize_url,
            configurable_resources=configurable_resources,
            configuration=configuration,
            created_at=created_at,
            enabled=enabled,
            form_fields=form_fields,
            has_guide=has_guide,
            icon=icon,
            id=id,
            integration_state=integration_state,
            logo=logo,
            metadata=metadata,
            name=name,
            oauth_grant_type=oauth_grant_type,
            resource_schema_support=resource_schema_support,
            resource_settings_support=resource_settings_support,
            revoke_url=revoke_url,
            service_id=service_id,
            settings=settings,
            settings_required_for_authorization=settings_required_for_authorization,
            state=state,
            status=status,
            subscriptions=subscriptions,
            tag_line=tag_line,
            unified_api=unified_api,
            updated_at=updated_at,
            validation_support=validation_support,
            website=website,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a connection

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.delete(
                unified_api="crm",
                service_id="pipedrive",
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            unified_api, service_id, apideck_consumer_id=apideck_consumer_id, request_options=request_options
        )
        return _response.data

    async def update(
        self,
        unified_api_: str,
        service_id_: str,
        *,
        apideck_consumer_id: str,
        auth_type: typing.Optional[AuthType] = OMIT,
        authorize_url: typing.Optional[str] = OMIT,
        configurable_resources: typing.Optional[typing.Sequence[str]] = OMIT,
        configuration: typing.Optional[typing.Sequence[ConnectionConfigurationItem]] = OMIT,
        created_at: typing.Optional[float] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        form_fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        has_guide: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        integration_state: typing.Optional[IntegrationState] = OMIT,
        logo: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings_required_for_authorization: typing.Optional[typing.Sequence[str]] = OMIT,
        state: typing.Optional[ConnectionState] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        subscriptions: typing.Optional[typing.Sequence[WebhookSubscription]] = OMIT,
        tag_line: typing.Optional[str] = OMIT,
        unified_api: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[float] = OMIT,
        validation_support: typing.Optional[bool] = OMIT,
        website: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateConnectionResponse:
        """
        Update a connection

        Parameters
        ----------
        unified_api_ : str
            Unified API

        service_id_ : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        auth_type : typing.Optional[AuthType]

        authorize_url : typing.Optional[str]
            The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        configurable_resources : typing.Optional[typing.Sequence[str]]

        configuration : typing.Optional[typing.Sequence[ConnectionConfigurationItem]]

        created_at : typing.Optional[float]

        enabled : typing.Optional[bool]
            Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.

        form_fields : typing.Optional[typing.Sequence[FormField]]
            The settings that are wanted to create a connection.

        has_guide : typing.Optional[bool]
            Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).

        icon : typing.Optional[str]
            A visual icon of the connection, that will be shown in the Vault

        id : typing.Optional[str]
            The unique identifier of the connection.

        integration_state : typing.Optional[IntegrationState]

        logo : typing.Optional[str]
            The logo of the connection, that will be shown in the Vault

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Attach your own consumer specific metadata

        name : typing.Optional[str]
            The name of the connection

        oauth_grant_type : typing.Optional[OAuthGrantType]

        resource_schema_support : typing.Optional[typing.Sequence[str]]

        resource_settings_support : typing.Optional[typing.Sequence[str]]

        revoke_url : typing.Optional[str]
            The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        service_id : typing.Optional[str]
            The ID of the service this connection belongs to.

        settings : typing.Optional[typing.Dict[str, typing.Any]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        settings_required_for_authorization : typing.Optional[typing.Sequence[str]]
            List of settings that are required to be configured on integration before authorization can occur

        state : typing.Optional[ConnectionState]

        status : typing.Optional[ConnectionStatus]
            Status of the connection.

        subscriptions : typing.Optional[typing.Sequence[WebhookSubscription]]

        tag_line : typing.Optional[str]

        unified_api : typing.Optional[str]
            The unified API category where the connection belongs to.

        updated_at : typing.Optional[float]

        validation_support : typing.Optional[bool]

        website : typing.Optional[str]
            The website URL of the connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateConnectionResponse
            Connection updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.update(
                unified_api_="crm",
                service_id_="pipedrive",
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            unified_api_,
            service_id_,
            apideck_consumer_id=apideck_consumer_id,
            auth_type=auth_type,
            authorize_url=authorize_url,
            configurable_resources=configurable_resources,
            configuration=configuration,
            created_at=created_at,
            enabled=enabled,
            form_fields=form_fields,
            has_guide=has_guide,
            icon=icon,
            id=id,
            integration_state=integration_state,
            logo=logo,
            metadata=metadata,
            name=name,
            oauth_grant_type=oauth_grant_type,
            resource_schema_support=resource_schema_support,
            resource_settings_support=resource_settings_support,
            revoke_url=revoke_url,
            service_id=service_id,
            settings=settings,
            settings_required_for_authorization=settings_required_for_authorization,
            state=state,
            status=status,
            subscriptions=subscriptions,
            tag_line=tag_line,
            unified_api=unified_api,
            updated_at=updated_at,
            validation_support=validation_support,
            website=website,
            request_options=request_options,
        )
        return _response.data

    async def import_(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        credentials: typing.Optional[ConnectionImportDataCredentials] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponse:
        """
        Import an authorized connection.

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        credentials : typing.Optional[ConnectionImportDataCredentials]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Attach your own consumer specific metadata

        settings : typing.Optional[typing.Dict[str, typing.Any]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionResponse
            Connection created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.import_(
                unified_api="crm",
                service_id="pipedrive",
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_(
            unified_api,
            service_id,
            apideck_consumer_id=apideck_consumer_id,
            credentials=credentials,
            metadata=metadata,
            settings=settings,
            request_options=request_options,
        )
        return _response.data

    async def token(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionResponse:
        """
        Get an access token for a connection and store it in Vault. Currently only supported for connections with the client_credentials OAuth grant type.

        Note that the access token will not be returned in the response. A 200 response code indicates a valid access token was stored on the connection.

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionResponse
            Connection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.token(
                unified_api="crm",
                service_id="pipedrive",
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.token(
            unified_api, service_id, apideck_consumer_id=apideck_consumer_id, request_options=request_options
        )
        return _response.data

    async def connection_settings_all(
        self,
        unified_api: str,
        service_id: str,
        resource: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionResponse:
        """
        This endpoint returns custom settings and their defaults required by connection for a given resource.

        Parameters
        ----------
        unified_api : str
            Unified API

        service_id : str
            Service ID of the resource to return

        resource : str
            Resource Name

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionResponse
            Connection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.connection_settings_all(
                unified_api="crm",
                service_id="pipedrive",
                resource="leads",
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connection_settings_all(
            unified_api, service_id, resource, apideck_consumer_id=apideck_consumer_id, request_options=request_options
        )
        return _response.data

    async def connection_settings_update(
        self,
        unified_api_: str,
        service_id_: str,
        resource: str,
        *,
        apideck_consumer_id: str,
        auth_type: typing.Optional[AuthType] = OMIT,
        authorize_url: typing.Optional[str] = OMIT,
        configurable_resources: typing.Optional[typing.Sequence[str]] = OMIT,
        configuration: typing.Optional[typing.Sequence[ConnectionConfigurationItem]] = OMIT,
        created_at: typing.Optional[float] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        form_fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        has_guide: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        integration_state: typing.Optional[IntegrationState] = OMIT,
        logo: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings_required_for_authorization: typing.Optional[typing.Sequence[str]] = OMIT,
        state: typing.Optional[ConnectionState] = OMIT,
        status: typing.Optional[ConnectionStatus] = OMIT,
        subscriptions: typing.Optional[typing.Sequence[WebhookSubscription]] = OMIT,
        tag_line: typing.Optional[str] = OMIT,
        unified_api: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[float] = OMIT,
        validation_support: typing.Optional[bool] = OMIT,
        website: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateConnectionResponse:
        """
        Update default values for a connection's resource settings

        Parameters
        ----------
        unified_api_ : str
            Unified API

        service_id_ : str
            Service ID of the resource to return

        resource : str
            Resource Name

        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        auth_type : typing.Optional[AuthType]

        authorize_url : typing.Optional[str]
            The OAuth redirect URI. Redirect your users to this URI to let them authorize your app in the connector's UI. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        configurable_resources : typing.Optional[typing.Sequence[str]]

        configuration : typing.Optional[typing.Sequence[ConnectionConfigurationItem]]

        created_at : typing.Optional[float]

        enabled : typing.Optional[bool]
            Whether the connection is enabled or not. You can enable or disable a connection using the Update Connection API.

        form_fields : typing.Optional[typing.Sequence[FormField]]
            The settings that are wanted to create a connection.

        has_guide : typing.Optional[bool]
            Whether the connector has a guide available in the developer docs or not (https://docs.apideck.com/connectors/{service_id}/docs/consumer+connection).

        icon : typing.Optional[str]
            A visual icon of the connection, that will be shown in the Vault

        id : typing.Optional[str]
            The unique identifier of the connection.

        integration_state : typing.Optional[IntegrationState]

        logo : typing.Optional[str]
            The logo of the connection, that will be shown in the Vault

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Attach your own consumer specific metadata

        name : typing.Optional[str]
            The name of the connection

        oauth_grant_type : typing.Optional[OAuthGrantType]

        resource_schema_support : typing.Optional[typing.Sequence[str]]

        resource_settings_support : typing.Optional[typing.Sequence[str]]

        revoke_url : typing.Optional[str]
            The OAuth revoke URI. Redirect your users to this URI to revoke this connection. Before you can use this URI, you must add `redirect_uri` as a query parameter. Your users will be redirected to this `redirect_uri` after they granted access to your app in the connector's UI.

        service_id : typing.Optional[str]
            The ID of the service this connection belongs to.

        settings : typing.Optional[typing.Dict[str, typing.Any]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        settings_required_for_authorization : typing.Optional[typing.Sequence[str]]
            List of settings that are required to be configured on integration before authorization can occur

        state : typing.Optional[ConnectionState]

        status : typing.Optional[ConnectionStatus]
            Status of the connection.

        subscriptions : typing.Optional[typing.Sequence[WebhookSubscription]]

        tag_line : typing.Optional[str]

        unified_api : typing.Optional[str]
            The unified API category where the connection belongs to.

        updated_at : typing.Optional[float]

        validation_support : typing.Optional[bool]

        website : typing.Optional[str]
            The website URL of the connection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateConnectionResponse
            Connection updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.connection_settings_update(
                unified_api_="crm",
                service_id_="pipedrive",
                resource="leads",
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connection_settings_update(
            unified_api_,
            service_id_,
            resource,
            apideck_consumer_id=apideck_consumer_id,
            auth_type=auth_type,
            authorize_url=authorize_url,
            configurable_resources=configurable_resources,
            configuration=configuration,
            created_at=created_at,
            enabled=enabled,
            form_fields=form_fields,
            has_guide=has_guide,
            icon=icon,
            id=id,
            integration_state=integration_state,
            logo=logo,
            metadata=metadata,
            name=name,
            oauth_grant_type=oauth_grant_type,
            resource_schema_support=resource_schema_support,
            resource_settings_support=resource_settings_support,
            revoke_url=revoke_url,
            service_id=service_id,
            settings=settings,
            settings_required_for_authorization=settings_required_for_authorization,
            state=state,
            status=status,
            subscriptions=subscriptions,
            tag_line=tag_line,
            unified_api=unified_api,
            updated_at=updated_at,
            validation_support=validation_support,
            website=website,
            request_options=request_options,
        )
        return _response.data

    async def revoke(
        self,
        service_id: str,
        application_id: str,
        *,
        state: str,
        redirect_uri: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnexpectedErrorResponse:
        """
        __In most cases the authorize link is provided in the ``/connections`` endpoint. Normally you don't need to manually generate these links.__

        Use this endpoint to revoke an existing OAuth connector.

        Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.

        Vault handles the complete revoke flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application.

        Parameters
        ----------
        service_id : str
            Service ID of the resource to return

        application_id : str
            Application ID of the resource to return

        state : str
            An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.

        redirect_uri : str
            URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnexpectedErrorResponse
            Unexpected error

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.revoke(
                service_id="pipedrive",
                application_id="dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX",
                state="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk",
                redirect_uri="http://example.com/integrations",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke(
            service_id, application_id, state=state, redirect_uri=redirect_uri, request_options=request_options
        )
        return _response.data
