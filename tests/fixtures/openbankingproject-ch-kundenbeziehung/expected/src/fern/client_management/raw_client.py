

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.client_configuration import ClientConfiguration
from ..types.client_registration_response import ClientRegistrationResponse
from ..types.error_response import ErrorResponse
from .types.client_registration_request_grant_types_item import ClientRegistrationRequestGrantTypesItem
from .types.client_registration_request_id_token_signed_response_alg import (
    ClientRegistrationRequestIdTokenSignedResponseAlg,
)
from .types.client_registration_request_industry_type import ClientRegistrationRequestIndustryType
from .types.client_registration_request_response_types_item import ClientRegistrationRequestResponseTypesItem
from .types.client_registration_request_token_endpoint_auth_method import (
    ClientRegistrationRequestTokenEndpointAuthMethod,
)
from .types.client_registration_request_token_endpoint_auth_signing_alg import (
    ClientRegistrationRequestTokenEndpointAuthSigningAlg,
)
from .types.client_update_request_industry_type import ClientUpdateRequestIndustryType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawClientManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register_client(
        self,
        *,
        redirect_uris: typing.Sequence[str],
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        grant_types: typing.Optional[typing.Sequence[ClientRegistrationRequestGrantTypesItem]] = OMIT,
        response_types: typing.Optional[typing.Sequence[ClientRegistrationRequestResponseTypesItem]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        token_endpoint_auth_method: typing.Optional[ClientRegistrationRequestTokenEndpointAuthMethod] = OMIT,
        token_endpoint_auth_signing_alg: typing.Optional[ClientRegistrationRequestTokenEndpointAuthSigningAlg] = OMIT,
        require_pushed_authorization_requests: typing.Optional[bool] = OMIT,
        require_signed_request_object: typing.Optional[bool] = OMIT,
        id_token_signed_response_alg: typing.Optional[ClientRegistrationRequestIdTokenSignedResponseAlg] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        industry_type: typing.Optional[ClientRegistrationRequestIndustryType] = OMIT,
        finma_license: typing.Optional[str] = OMIT,
        swiss_qr_support: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ClientRegistrationResponse]:
        """
        RFC 7591 compliant dynamic client registration with FAPI 2.0 enhancements.

        Parameters
        ----------
        redirect_uris : typing.Sequence[str]
            Authorized redirect URIs

        client_name : typing.Optional[str]
            Human-readable client name

        client_uri : typing.Optional[str]
            Client website URL

        grant_types : typing.Optional[typing.Sequence[ClientRegistrationRequestGrantTypesItem]]

        response_types : typing.Optional[typing.Sequence[ClientRegistrationRequestResponseTypesItem]]

        scope : typing.Optional[str]

        token_endpoint_auth_method : typing.Optional[ClientRegistrationRequestTokenEndpointAuthMethod]

        token_endpoint_auth_signing_alg : typing.Optional[ClientRegistrationRequestTokenEndpointAuthSigningAlg]

        require_pushed_authorization_requests : typing.Optional[bool]

        require_signed_request_object : typing.Optional[bool]

        id_token_signed_response_alg : typing.Optional[ClientRegistrationRequestIdTokenSignedResponseAlg]

        jwks_uri : typing.Optional[str]
            URL for client's JWK Set

        industry_type : typing.Optional[ClientRegistrationRequestIndustryType]

        finma_license : typing.Optional[str]
            FINMA license number if applicable

        swiss_qr_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClientRegistrationResponse]
            Client registered successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "register",
            method="POST",
            json={
                "client_name": client_name,
                "client_uri": client_uri,
                "redirect_uris": redirect_uris,
                "grant_types": grant_types,
                "response_types": response_types,
                "scope": scope,
                "token_endpoint_auth_method": token_endpoint_auth_method,
                "token_endpoint_auth_signing_alg": token_endpoint_auth_signing_alg,
                "require_pushed_authorization_requests": require_pushed_authorization_requests,
                "require_signed_request_object": require_signed_request_object,
                "id_token_signed_response_alg": id_token_signed_response_alg,
                "jwks_uri": jwks_uri,
                "industry_type": industry_type,
                "finma_license": finma_license,
                "swiss_qr_support": swiss_qr_support,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientRegistrationResponse,
                    parse_obj_as(
                        type_=ClientRegistrationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_client_configuration(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ClientConfiguration]:
        """
        Retrieve client configuration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClientConfiguration]
            Client configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            f"register/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientConfiguration,
                    parse_obj_as(
                        type_=ClientConfiguration,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_client_configuration(
        self,
        client_id: str,
        *,
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        industry_type: typing.Optional[ClientUpdateRequestIndustryType] = OMIT,
        finma_license: typing.Optional[str] = OMIT,
        swiss_qr_support: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ClientConfiguration]:
        """
        Update client configuration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        client_name : typing.Optional[str]

        client_uri : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        scope : typing.Optional[str]

        jwks_uri : typing.Optional[str]

        industry_type : typing.Optional[ClientUpdateRequestIndustryType]

        finma_license : typing.Optional[str]

        swiss_qr_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClientConfiguration]
            Client updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"register/{encode_path_param(client_id)}",
            method="PUT",
            json={
                "client_name": client_name,
                "client_uri": client_uri,
                "redirect_uris": redirect_uris,
                "scope": scope,
                "jwks_uri": jwks_uri,
                "industry_type": industry_type,
                "finma_license": finma_license,
                "swiss_qr_support": swiss_qr_support,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientConfiguration,
                    parse_obj_as(
                        type_=ClientConfiguration,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete client registration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"register/{encode_path_param(client_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawClientManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register_client(
        self,
        *,
        redirect_uris: typing.Sequence[str],
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        grant_types: typing.Optional[typing.Sequence[ClientRegistrationRequestGrantTypesItem]] = OMIT,
        response_types: typing.Optional[typing.Sequence[ClientRegistrationRequestResponseTypesItem]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        token_endpoint_auth_method: typing.Optional[ClientRegistrationRequestTokenEndpointAuthMethod] = OMIT,
        token_endpoint_auth_signing_alg: typing.Optional[ClientRegistrationRequestTokenEndpointAuthSigningAlg] = OMIT,
        require_pushed_authorization_requests: typing.Optional[bool] = OMIT,
        require_signed_request_object: typing.Optional[bool] = OMIT,
        id_token_signed_response_alg: typing.Optional[ClientRegistrationRequestIdTokenSignedResponseAlg] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        industry_type: typing.Optional[ClientRegistrationRequestIndustryType] = OMIT,
        finma_license: typing.Optional[str] = OMIT,
        swiss_qr_support: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ClientRegistrationResponse]:
        """
        RFC 7591 compliant dynamic client registration with FAPI 2.0 enhancements.

        Parameters
        ----------
        redirect_uris : typing.Sequence[str]
            Authorized redirect URIs

        client_name : typing.Optional[str]
            Human-readable client name

        client_uri : typing.Optional[str]
            Client website URL

        grant_types : typing.Optional[typing.Sequence[ClientRegistrationRequestGrantTypesItem]]

        response_types : typing.Optional[typing.Sequence[ClientRegistrationRequestResponseTypesItem]]

        scope : typing.Optional[str]

        token_endpoint_auth_method : typing.Optional[ClientRegistrationRequestTokenEndpointAuthMethod]

        token_endpoint_auth_signing_alg : typing.Optional[ClientRegistrationRequestTokenEndpointAuthSigningAlg]

        require_pushed_authorization_requests : typing.Optional[bool]

        require_signed_request_object : typing.Optional[bool]

        id_token_signed_response_alg : typing.Optional[ClientRegistrationRequestIdTokenSignedResponseAlg]

        jwks_uri : typing.Optional[str]
            URL for client's JWK Set

        industry_type : typing.Optional[ClientRegistrationRequestIndustryType]

        finma_license : typing.Optional[str]
            FINMA license number if applicable

        swiss_qr_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClientRegistrationResponse]
            Client registered successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "register",
            method="POST",
            json={
                "client_name": client_name,
                "client_uri": client_uri,
                "redirect_uris": redirect_uris,
                "grant_types": grant_types,
                "response_types": response_types,
                "scope": scope,
                "token_endpoint_auth_method": token_endpoint_auth_method,
                "token_endpoint_auth_signing_alg": token_endpoint_auth_signing_alg,
                "require_pushed_authorization_requests": require_pushed_authorization_requests,
                "require_signed_request_object": require_signed_request_object,
                "id_token_signed_response_alg": id_token_signed_response_alg,
                "jwks_uri": jwks_uri,
                "industry_type": industry_type,
                "finma_license": finma_license,
                "swiss_qr_support": swiss_qr_support,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientRegistrationResponse,
                    parse_obj_as(
                        type_=ClientRegistrationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_client_configuration(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ClientConfiguration]:
        """
        Retrieve client configuration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClientConfiguration]
            Client configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"register/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientConfiguration,
                    parse_obj_as(
                        type_=ClientConfiguration,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_client_configuration(
        self,
        client_id: str,
        *,
        client_name: typing.Optional[str] = OMIT,
        client_uri: typing.Optional[str] = OMIT,
        redirect_uris: typing.Optional[typing.Sequence[str]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        jwks_uri: typing.Optional[str] = OMIT,
        industry_type: typing.Optional[ClientUpdateRequestIndustryType] = OMIT,
        finma_license: typing.Optional[str] = OMIT,
        swiss_qr_support: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ClientConfiguration]:
        """
        Update client configuration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        client_name : typing.Optional[str]

        client_uri : typing.Optional[str]

        redirect_uris : typing.Optional[typing.Sequence[str]]

        scope : typing.Optional[str]

        jwks_uri : typing.Optional[str]

        industry_type : typing.Optional[ClientUpdateRequestIndustryType]

        finma_license : typing.Optional[str]

        swiss_qr_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClientConfiguration]
            Client updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"register/{encode_path_param(client_id)}",
            method="PUT",
            json={
                "client_name": client_name,
                "client_uri": client_uri,
                "redirect_uris": redirect_uris,
                "scope": scope,
                "jwks_uri": jwks_uri,
                "industry_type": industry_type,
                "finma_license": finma_license,
                "swiss_qr_support": swiss_qr_support,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientConfiguration,
                    parse_obj_as(
                        type_=ClientConfiguration,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_client(
        self, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete client registration using registration access token

        Parameters
        ----------
        client_id : str
            OAuth client identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"register/{encode_path_param(client_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
