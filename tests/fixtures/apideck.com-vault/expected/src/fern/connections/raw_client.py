

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.auth_type import AuthType
from ..types.bad_request_response import BadRequestResponse
from ..types.connection_configuration_item import ConnectionConfigurationItem
from ..types.connection_state import ConnectionState
from ..types.connection_status import ConnectionStatus
from ..types.create_connection_response import CreateConnectionResponse
from ..types.form_field import FormField
from ..types.get_connection_response import GetConnectionResponse
from ..types.get_connections_response import GetConnectionsResponse
from ..types.integration_state import IntegrationState
from ..types.not_found_response import NotFoundResponse
from ..types.o_auth_grant_type import OAuthGrantType
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unexpected_error_response import UnexpectedErrorResponse
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_connection_response import UpdateConnectionResponse
from ..types.webhook_subscription import WebhookSubscription
from .types.connection_import_data_credentials import ConnectionImportDataCredentials


OMIT = typing.cast(typing.Any, ...)


class RawConnectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def authorize(
        self,
        service_id: str,
        application_id: str,
        *,
        state: str,
        redirect_uri: str,
        scope: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UnexpectedErrorResponse]:
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
        HttpResponse[UnexpectedErrorResponse]
            Unexpected error
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/authorize/{jsonable_encoder(service_id)}/{jsonable_encoder(application_id)}",
            method="GET",
            params={
                "state": state,
                "redirect_uri": redirect_uri,
                "scope": scope,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnexpectedErrorResponse,
                    parse_obj_as(
                        type_=UnexpectedErrorResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def callback(
        self, *, state: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UnexpectedErrorResponse]:
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
        HttpResponse[UnexpectedErrorResponse]
            Unexpected error
        """
        _response = self._client_wrapper.httpx_client.request(
            "vault/callback",
            method="GET",
            params={
                "state": state,
                "code": code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnexpectedErrorResponse,
                    parse_obj_as(
                        type_=UnexpectedErrorResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def all_(
        self,
        *,
        apideck_consumer_id: str,
        api: typing.Optional[str] = None,
        configured: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConnectionsResponse]:
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
        HttpResponse[GetConnectionsResponse]
            Connections
        """
        _response = self._client_wrapper.httpx_client.request(
            "vault/connections",
            method="GET",
            params={
                "api": api,
                "configured": configured,
            },
            headers={
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectionsResponse,
                    parse_obj_as(
                        type_=GetConnectionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def one(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConnectionResponse]:
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
        HttpResponse[GetConnectionResponse]
            Connection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}",
            method="GET",
            headers={
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectionResponse,
                    parse_obj_as(
                        type_=GetConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
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
    ) -> HttpResponse[CreateConnectionResponse]:
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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

        settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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
        HttpResponse[CreateConnectionResponse]
            Connection created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api_)}/{jsonable_encoder(service_id_)}",
            method="POST",
            json={
                "auth_type": auth_type,
                "authorize_url": authorize_url,
                "configurable_resources": configurable_resources,
                "configuration": convert_and_respect_annotation_metadata(
                    object_=configuration, annotation=typing.Sequence[ConnectionConfigurationItem], direction="write"
                ),
                "created_at": created_at,
                "enabled": enabled,
                "form_fields": convert_and_respect_annotation_metadata(
                    object_=form_fields, annotation=typing.Sequence[FormField], direction="write"
                ),
                "has_guide": has_guide,
                "icon": icon,
                "id": id,
                "integration_state": integration_state,
                "logo": logo,
                "metadata": metadata,
                "name": name,
                "oauth_grant_type": oauth_grant_type,
                "resource_schema_support": resource_schema_support,
                "resource_settings_support": resource_settings_support,
                "revoke_url": revoke_url,
                "service_id": service_id,
                "settings": settings,
                "settings_required_for_authorization": settings_required_for_authorization,
                "state": state,
                "status": status,
                "subscriptions": convert_and_respect_annotation_metadata(
                    object_=subscriptions, annotation=typing.Sequence[WebhookSubscription], direction="write"
                ),
                "tag_line": tag_line,
                "unified_api": unified_api,
                "updated_at": updated_at,
                "validation_support": validation_support,
                "website": website,
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateConnectionResponse,
                    parse_obj_as(
                        type_=CreateConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}",
            method="DELETE",
            headers={
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
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
    ) -> HttpResponse[UpdateConnectionResponse]:
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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

        settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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
        HttpResponse[UpdateConnectionResponse]
            Connection updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api_)}/{jsonable_encoder(service_id_)}",
            method="PATCH",
            json={
                "auth_type": auth_type,
                "authorize_url": authorize_url,
                "configurable_resources": configurable_resources,
                "configuration": convert_and_respect_annotation_metadata(
                    object_=configuration, annotation=typing.Sequence[ConnectionConfigurationItem], direction="write"
                ),
                "created_at": created_at,
                "enabled": enabled,
                "form_fields": convert_and_respect_annotation_metadata(
                    object_=form_fields, annotation=typing.Sequence[FormField], direction="write"
                ),
                "has_guide": has_guide,
                "icon": icon,
                "id": id,
                "integration_state": integration_state,
                "logo": logo,
                "metadata": metadata,
                "name": name,
                "oauth_grant_type": oauth_grant_type,
                "resource_schema_support": resource_schema_support,
                "resource_settings_support": resource_settings_support,
                "revoke_url": revoke_url,
                "service_id": service_id,
                "settings": settings,
                "settings_required_for_authorization": settings_required_for_authorization,
                "state": state,
                "status": status,
                "subscriptions": convert_and_respect_annotation_metadata(
                    object_=subscriptions, annotation=typing.Sequence[WebhookSubscription], direction="write"
                ),
                "tag_line": tag_line,
                "unified_api": unified_api,
                "updated_at": updated_at,
                "validation_support": validation_support,
                "website": website,
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateConnectionResponse,
                    parse_obj_as(
                        type_=UpdateConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def import_(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        credentials: typing.Optional[ConnectionImportDataCredentials] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateConnectionResponse]:
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Attach your own consumer specific metadata

        settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateConnectionResponse]
            Connection created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}/import",
            method="POST",
            json={
                "credentials": convert_and_respect_annotation_metadata(
                    object_=credentials, annotation=ConnectionImportDataCredentials, direction="write"
                ),
                "metadata": metadata,
                "settings": settings,
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateConnectionResponse,
                    parse_obj_as(
                        type_=CreateConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def token(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConnectionResponse]:
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
        HttpResponse[GetConnectionResponse]
            Connection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}/token",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectionResponse,
                    parse_obj_as(
                        type_=GetConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def connection_settings_all(
        self,
        unified_api: str,
        service_id: str,
        resource: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConnectionResponse]:
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
        HttpResponse[GetConnectionResponse]
            Connection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}/{jsonable_encoder(resource)}/config",
            method="GET",
            headers={
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectionResponse,
                    parse_obj_as(
                        type_=GetConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
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
    ) -> HttpResponse[UpdateConnectionResponse]:
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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

        settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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
        HttpResponse[UpdateConnectionResponse]
            Connection updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api_)}/{jsonable_encoder(service_id_)}/{jsonable_encoder(resource)}/config",
            method="PATCH",
            json={
                "auth_type": auth_type,
                "authorize_url": authorize_url,
                "configurable_resources": configurable_resources,
                "configuration": convert_and_respect_annotation_metadata(
                    object_=configuration, annotation=typing.Sequence[ConnectionConfigurationItem], direction="write"
                ),
                "created_at": created_at,
                "enabled": enabled,
                "form_fields": convert_and_respect_annotation_metadata(
                    object_=form_fields, annotation=typing.Sequence[FormField], direction="write"
                ),
                "has_guide": has_guide,
                "icon": icon,
                "id": id,
                "integration_state": integration_state,
                "logo": logo,
                "metadata": metadata,
                "name": name,
                "oauth_grant_type": oauth_grant_type,
                "resource_schema_support": resource_schema_support,
                "resource_settings_support": resource_settings_support,
                "revoke_url": revoke_url,
                "service_id": service_id,
                "settings": settings,
                "settings_required_for_authorization": settings_required_for_authorization,
                "state": state,
                "status": status,
                "subscriptions": convert_and_respect_annotation_metadata(
                    object_=subscriptions, annotation=typing.Sequence[WebhookSubscription], direction="write"
                ),
                "tag_line": tag_line,
                "unified_api": unified_api,
                "updated_at": updated_at,
                "validation_support": validation_support,
                "website": website,
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateConnectionResponse,
                    parse_obj_as(
                        type_=UpdateConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def revoke(
        self,
        service_id: str,
        application_id: str,
        *,
        state: str,
        redirect_uri: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UnexpectedErrorResponse]:
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
        HttpResponse[UnexpectedErrorResponse]
            Unexpected error
        """
        _response = self._client_wrapper.httpx_client.request(
            f"vault/revoke/{jsonable_encoder(service_id)}/{jsonable_encoder(application_id)}",
            method="GET",
            params={
                "state": state,
                "redirect_uri": redirect_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnexpectedErrorResponse,
                    parse_obj_as(
                        type_=UnexpectedErrorResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawConnectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def authorize(
        self,
        service_id: str,
        application_id: str,
        *,
        state: str,
        redirect_uri: str,
        scope: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UnexpectedErrorResponse]:
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
        AsyncHttpResponse[UnexpectedErrorResponse]
            Unexpected error
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/authorize/{jsonable_encoder(service_id)}/{jsonable_encoder(application_id)}",
            method="GET",
            params={
                "state": state,
                "redirect_uri": redirect_uri,
                "scope": scope,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnexpectedErrorResponse,
                    parse_obj_as(
                        type_=UnexpectedErrorResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def callback(
        self, *, state: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UnexpectedErrorResponse]:
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
        AsyncHttpResponse[UnexpectedErrorResponse]
            Unexpected error
        """
        _response = await self._client_wrapper.httpx_client.request(
            "vault/callback",
            method="GET",
            params={
                "state": state,
                "code": code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnexpectedErrorResponse,
                    parse_obj_as(
                        type_=UnexpectedErrorResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def all_(
        self,
        *,
        apideck_consumer_id: str,
        api: typing.Optional[str] = None,
        configured: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetConnectionsResponse]:
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
        AsyncHttpResponse[GetConnectionsResponse]
            Connections
        """
        _response = await self._client_wrapper.httpx_client.request(
            "vault/connections",
            method="GET",
            params={
                "api": api,
                "configured": configured,
            },
            headers={
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectionsResponse,
                    parse_obj_as(
                        type_=GetConnectionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def one(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetConnectionResponse]:
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
        AsyncHttpResponse[GetConnectionResponse]
            Connection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}",
            method="GET",
            headers={
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectionResponse,
                    parse_obj_as(
                        type_=GetConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
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
    ) -> AsyncHttpResponse[CreateConnectionResponse]:
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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

        settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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
        AsyncHttpResponse[CreateConnectionResponse]
            Connection created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api_)}/{jsonable_encoder(service_id_)}",
            method="POST",
            json={
                "auth_type": auth_type,
                "authorize_url": authorize_url,
                "configurable_resources": configurable_resources,
                "configuration": convert_and_respect_annotation_metadata(
                    object_=configuration, annotation=typing.Sequence[ConnectionConfigurationItem], direction="write"
                ),
                "created_at": created_at,
                "enabled": enabled,
                "form_fields": convert_and_respect_annotation_metadata(
                    object_=form_fields, annotation=typing.Sequence[FormField], direction="write"
                ),
                "has_guide": has_guide,
                "icon": icon,
                "id": id,
                "integration_state": integration_state,
                "logo": logo,
                "metadata": metadata,
                "name": name,
                "oauth_grant_type": oauth_grant_type,
                "resource_schema_support": resource_schema_support,
                "resource_settings_support": resource_settings_support,
                "revoke_url": revoke_url,
                "service_id": service_id,
                "settings": settings,
                "settings_required_for_authorization": settings_required_for_authorization,
                "state": state,
                "status": status,
                "subscriptions": convert_and_respect_annotation_metadata(
                    object_=subscriptions, annotation=typing.Sequence[WebhookSubscription], direction="write"
                ),
                "tag_line": tag_line,
                "unified_api": unified_api,
                "updated_at": updated_at,
                "validation_support": validation_support,
                "website": website,
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateConnectionResponse,
                    parse_obj_as(
                        type_=CreateConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}",
            method="DELETE",
            headers={
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
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
    ) -> AsyncHttpResponse[UpdateConnectionResponse]:
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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

        settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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
        AsyncHttpResponse[UpdateConnectionResponse]
            Connection updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api_)}/{jsonable_encoder(service_id_)}",
            method="PATCH",
            json={
                "auth_type": auth_type,
                "authorize_url": authorize_url,
                "configurable_resources": configurable_resources,
                "configuration": convert_and_respect_annotation_metadata(
                    object_=configuration, annotation=typing.Sequence[ConnectionConfigurationItem], direction="write"
                ),
                "created_at": created_at,
                "enabled": enabled,
                "form_fields": convert_and_respect_annotation_metadata(
                    object_=form_fields, annotation=typing.Sequence[FormField], direction="write"
                ),
                "has_guide": has_guide,
                "icon": icon,
                "id": id,
                "integration_state": integration_state,
                "logo": logo,
                "metadata": metadata,
                "name": name,
                "oauth_grant_type": oauth_grant_type,
                "resource_schema_support": resource_schema_support,
                "resource_settings_support": resource_settings_support,
                "revoke_url": revoke_url,
                "service_id": service_id,
                "settings": settings,
                "settings_required_for_authorization": settings_required_for_authorization,
                "state": state,
                "status": status,
                "subscriptions": convert_and_respect_annotation_metadata(
                    object_=subscriptions, annotation=typing.Sequence[WebhookSubscription], direction="write"
                ),
                "tag_line": tag_line,
                "unified_api": unified_api,
                "updated_at": updated_at,
                "validation_support": validation_support,
                "website": website,
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateConnectionResponse,
                    parse_obj_as(
                        type_=UpdateConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def import_(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        credentials: typing.Optional[ConnectionImportDataCredentials] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateConnectionResponse]:
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Attach your own consumer specific metadata

        settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Connection settings. Values will persist to `form_fields` with corresponding id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateConnectionResponse]
            Connection created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}/import",
            method="POST",
            json={
                "credentials": convert_and_respect_annotation_metadata(
                    object_=credentials, annotation=ConnectionImportDataCredentials, direction="write"
                ),
                "metadata": metadata,
                "settings": settings,
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateConnectionResponse,
                    parse_obj_as(
                        type_=CreateConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def token(
        self,
        unified_api: str,
        service_id: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetConnectionResponse]:
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
        AsyncHttpResponse[GetConnectionResponse]
            Connection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}/token",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectionResponse,
                    parse_obj_as(
                        type_=GetConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def connection_settings_all(
        self,
        unified_api: str,
        service_id: str,
        resource: str,
        *,
        apideck_consumer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetConnectionResponse]:
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
        AsyncHttpResponse[GetConnectionResponse]
            Connection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api)}/{jsonable_encoder(service_id)}/{jsonable_encoder(resource)}/config",
            method="GET",
            headers={
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectionResponse,
                    parse_obj_as(
                        type_=GetConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
        metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        name: typing.Optional[str] = OMIT,
        oauth_grant_type: typing.Optional[OAuthGrantType] = OMIT,
        resource_schema_support: typing.Optional[typing.Sequence[str]] = OMIT,
        resource_settings_support: typing.Optional[typing.Sequence[str]] = OMIT,
        revoke_url: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
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
    ) -> AsyncHttpResponse[UpdateConnectionResponse]:
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

        metadata : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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

        settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
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
        AsyncHttpResponse[UpdateConnectionResponse]
            Connection updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/connections/{jsonable_encoder(unified_api_)}/{jsonable_encoder(service_id_)}/{jsonable_encoder(resource)}/config",
            method="PATCH",
            json={
                "auth_type": auth_type,
                "authorize_url": authorize_url,
                "configurable_resources": configurable_resources,
                "configuration": convert_and_respect_annotation_metadata(
                    object_=configuration, annotation=typing.Sequence[ConnectionConfigurationItem], direction="write"
                ),
                "created_at": created_at,
                "enabled": enabled,
                "form_fields": convert_and_respect_annotation_metadata(
                    object_=form_fields, annotation=typing.Sequence[FormField], direction="write"
                ),
                "has_guide": has_guide,
                "icon": icon,
                "id": id,
                "integration_state": integration_state,
                "logo": logo,
                "metadata": metadata,
                "name": name,
                "oauth_grant_type": oauth_grant_type,
                "resource_schema_support": resource_schema_support,
                "resource_settings_support": resource_settings_support,
                "revoke_url": revoke_url,
                "service_id": service_id,
                "settings": settings,
                "settings_required_for_authorization": settings_required_for_authorization,
                "state": state,
                "status": status,
                "subscriptions": convert_and_respect_annotation_metadata(
                    object_=subscriptions, annotation=typing.Sequence[WebhookSubscription], direction="write"
                ),
                "tag_line": tag_line,
                "unified_api": unified_api,
                "updated_at": updated_at,
                "validation_support": validation_support,
                "website": website,
            },
            headers={
                "content-type": "application/json",
                "x-apideck-consumer-id": str(apideck_consumer_id) if apideck_consumer_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateConnectionResponse,
                    parse_obj_as(
                        type_=UpdateConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def revoke(
        self,
        service_id: str,
        application_id: str,
        *,
        state: str,
        redirect_uri: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UnexpectedErrorResponse]:
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
        AsyncHttpResponse[UnexpectedErrorResponse]
            Unexpected error
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"vault/revoke/{jsonable_encoder(service_id)}/{jsonable_encoder(application_id)}",
            method="GET",
            params={
                "state": state,
                "redirect_uri": redirect_uri,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnexpectedErrorResponse,
                    parse_obj_as(
                        type_=UnexpectedErrorResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
