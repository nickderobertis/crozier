

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.jwk_set_response import JwkSetResponse
from ..types.o_auth2metadata_response import OAuth2MetadataResponse
from pydantic import ValidationError


class RawOAuth2DiscoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_jwks(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[JwkSetResponse]:
        """
        Returns the broker's aggregated public signing keys in JWK Set format (RFC 7517).

        Clients use this single endpoint to verify any token the broker asks them to trust,
        regardless of operating mode. Only public key material is included — private keys
        are never exposed.

        **Mode-dependent content**:
        - `local` mode: returns only the broker's locally-generated signing keys.
        - `proxy` mode: republishes the upstream authorization server's public keys verbatim.
        - `hybrid` mode: returns the union of local signing keys and upstream keys in a
          single JWKS document. If any `kid` appears in both sets, the endpoint returns 500.

        **Availability**: Served in all three modes (`local`, `proxy`, `hybrid`). Returns
        503 if the upstream JWKS is unavailable (proxy/hybrid modes). Returns 500 if a
        duplicate `kid` is detected across local and upstream key sets (hybrid mode).

        **Caching**: Responses include `Cache-Control: public, max-age=300` to allow
        clients to cache the key set for 5 minutes. Clients should respect this header
        and implement key rotation by periodically refreshing the JWKS.

        **Key Rotation**: When signing keys are rotated, the new key appears in the
        JWKS immediately. Previous keys remain in the set until removed by an admin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JwkSetResponse]
            JWK Set containing public signing keys
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth2/jwks.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JwkSetResponse,
                    parse_obj_as(
                        type_=JwkSetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def get_o_auth2server_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OAuth2MetadataResponse]:
        """
        Returns the broker's OAuth2 authorization server metadata as defined
        in RFC 8414. This enables dynamic client discovery of the broker's
        OAuth2 capabilities and endpoints.

        **Mode-specific behavior**:
        - `proxy` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint, which republishes upstream keys.
        - `local` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint, which serves locally-generated signing keys.
        - `hybrid` mode: `issuer` is the broker's public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint (union of local and upstream keys). The
          metadata reflects the union of capabilities for both proxy and local grant types.

        **Caching**: Responses include `Cache-Control: public, max-age=3600` to allow
        clients to cache metadata for 1 hour.

        **No Authentication**: This endpoint is publicly accessible as required by RFC 8414.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OAuth2MetadataResponse]
            OAuth2 Authorization Server Metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            ".well-known/oauth-authorization-server",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OAuth2MetadataResponse,
                    parse_obj_as(
                        type_=OAuth2MetadataResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawOAuth2DiscoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_jwks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JwkSetResponse]:
        """
        Returns the broker's aggregated public signing keys in JWK Set format (RFC 7517).

        Clients use this single endpoint to verify any token the broker asks them to trust,
        regardless of operating mode. Only public key material is included — private keys
        are never exposed.

        **Mode-dependent content**:
        - `local` mode: returns only the broker's locally-generated signing keys.
        - `proxy` mode: republishes the upstream authorization server's public keys verbatim.
        - `hybrid` mode: returns the union of local signing keys and upstream keys in a
          single JWKS document. If any `kid` appears in both sets, the endpoint returns 500.

        **Availability**: Served in all three modes (`local`, `proxy`, `hybrid`). Returns
        503 if the upstream JWKS is unavailable (proxy/hybrid modes). Returns 500 if a
        duplicate `kid` is detected across local and upstream key sets (hybrid mode).

        **Caching**: Responses include `Cache-Control: public, max-age=300` to allow
        clients to cache the key set for 5 minutes. Clients should respect this header
        and implement key rotation by periodically refreshing the JWKS.

        **Key Rotation**: When signing keys are rotated, the new key appears in the
        JWKS immediately. Previous keys remain in the set until removed by an admin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JwkSetResponse]
            JWK Set containing public signing keys
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth2/jwks.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JwkSetResponse,
                    parse_obj_as(
                        type_=JwkSetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def get_o_auth2server_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OAuth2MetadataResponse]:
        """
        Returns the broker's OAuth2 authorization server metadata as defined
        in RFC 8414. This enables dynamic client discovery of the broker's
        OAuth2 capabilities and endpoints.

        **Mode-specific behavior**:
        - `proxy` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint, which republishes upstream keys.
        - `local` mode: `issuer` is the broker's own public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint, which serves locally-generated signing keys.
        - `hybrid` mode: `issuer` is the broker's public URL. `jwks_uri` points to the
          broker's `/oauth2/jwks.json` endpoint (union of local and upstream keys). The
          metadata reflects the union of capabilities for both proxy and local grant types.

        **Caching**: Responses include `Cache-Control: public, max-age=3600` to allow
        clients to cache metadata for 1 hour.

        **No Authentication**: This endpoint is publicly accessible as required by RFC 8414.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OAuth2MetadataResponse]
            OAuth2 Authorization Server Metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            ".well-known/oauth-authorization-server",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OAuth2MetadataResponse,
                    parse_obj_as(
                        type_=OAuth2MetadataResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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
