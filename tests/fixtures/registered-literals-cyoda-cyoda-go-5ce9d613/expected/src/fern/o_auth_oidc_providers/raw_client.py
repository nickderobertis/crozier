

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response_dto import ErrorResponseDto
from ..types.oidc_provider_response_dto import OidcProviderResponseDto
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOAuthOidcProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_oidc_providers(
        self, *, active_only: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[OidcProviderResponseDto]]:
        """
        Retrieves a list of all registered OIDC providers, including both active and inactive providers.

        Parameters
        ----------
        active_only : typing.Optional[str]
            If true, returns only active providers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[OidcProviderResponseDto]]
            List of OIDC providers retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/oidc/providers",
            method="GET",
            params={
                "activeOnly": active_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OidcProviderResponseDto],
                    parse_obj_as(
                        type_=typing.List[OidcProviderResponseDto],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def register_oidc_provider(
        self,
        *,
        well_known_config_uri: str,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OidcProviderResponseDto]:
        """
        Registers a new external OIDC provider for JWT validation. The provider's public keys will be
        discovered from the well-known configuration endpoint and used to validate JWT tokens.

        Parameters
        ----------
        well_known_config_uri : str
            URI to the OIDC provider's well-known configuration endpoint

        issuers : typing.Optional[typing.Sequence[str]]
            Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OidcProviderResponseDto]
            OIDC provider registered successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/oidc/providers",
            method="POST",
            json={
                "wellKnownConfigUri": well_known_config_uri,
                "issuers": issuers,
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
                    OidcProviderResponseDto,
                    parse_obj_as(
                        type_=OidcProviderResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def reload_oidc_providers(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Reloads all active OIDC provider configurations from the database and synchronizes
        cached keys with the remote JWKS endpoints.

        Key synchronization: For each provider, this operation fetches the current keys from
        the remote JWKS endpoint and invalidates any locally cached keys that no longer exist
        in the remote JWKS. This is useful for security when OIDC providers have rotated or
        revoked keys.

        This operation is useful when you want to ensure all nodes have the latest OIDC provider
        configurations and that any revoked keys are no longer trusted.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth/oidc/providers/reload",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def delete_oidc_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes an OIDC provider and all its associated JWK keys.
        The provider will first be invalidated (if not already) and then removed from storage.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/oidc/providers/{encode_path_param(id)}",
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def update_oidc_provider(
        self,
        id: str,
        *,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OidcProviderResponseDto]:
        """
        Updates configuration for an OIDC provider.

        Note: Updating the issuers list immediately deletes all cached keys for this provider.
        This ensures that JWTs from issuers that are no longer trusted cannot be validated using
        previously cached keys. The keys will be re-fetched from the remote JWKS endpoint with the
        new issuer configuration when they are next needed for JWT validation.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider

        issuers : typing.Optional[typing.Sequence[str]]
            Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OidcProviderResponseDto]
            OIDC provider issuers updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/oidc/providers/{encode_path_param(id)}",
            method="PATCH",
            json={
                "issuers": issuers,
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
                    OidcProviderResponseDto,
                    parse_obj_as(
                        type_=OidcProviderResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def invalidate_oidc_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Invalidates an OIDC provider, marking it as inactive and invalidating all loaded public keys
        associated with this provider. The provider configuration is retained but will no longer be
        used for JWT validation.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to invalidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/oidc/providers/{encode_path_param(id)}/invalidate",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def reactivate_oidc_provider(
        self,
        id: str,
        *,
        reactivate_keys: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OidcProviderResponseDto]:
        """
        Reactivates a previously invalidated OIDC provider. The provider will be marked as active
        and can be used for JWT validation again.
        This operation is idempotent - if the provider is already active, it returns the current state.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to reactivate

        reactivate_keys : typing.Optional[bool]
            If true, also reactivates all related JWK keys that were invalidated with this provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OidcProviderResponseDto]
            OIDC provider reactivated successfully or already active
        """
        _response = self._client_wrapper.httpx_client.request(
            f"oauth/oidc/providers/{encode_path_param(id)}/reactivate",
            method="POST",
            json={
                "reactivateKeys": reactivate_keys,
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
                    OidcProviderResponseDto,
                    parse_obj_as(
                        type_=OidcProviderResponseDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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


class AsyncRawOAuthOidcProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_oidc_providers(
        self, *, active_only: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[OidcProviderResponseDto]]:
        """
        Retrieves a list of all registered OIDC providers, including both active and inactive providers.

        Parameters
        ----------
        active_only : typing.Optional[str]
            If true, returns only active providers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[OidcProviderResponseDto]]
            List of OIDC providers retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/oidc/providers",
            method="GET",
            params={
                "activeOnly": active_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[OidcProviderResponseDto],
                    parse_obj_as(
                        type_=typing.List[OidcProviderResponseDto],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def register_oidc_provider(
        self,
        *,
        well_known_config_uri: str,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OidcProviderResponseDto]:
        """
        Registers a new external OIDC provider for JWT validation. The provider's public keys will be
        discovered from the well-known configuration endpoint and used to validate JWT tokens.

        Parameters
        ----------
        well_known_config_uri : str
            URI to the OIDC provider's well-known configuration endpoint

        issuers : typing.Optional[typing.Sequence[str]]
            Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OidcProviderResponseDto]
            OIDC provider registered successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/oidc/providers",
            method="POST",
            json={
                "wellKnownConfigUri": well_known_config_uri,
                "issuers": issuers,
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
                    OidcProviderResponseDto,
                    parse_obj_as(
                        type_=OidcProviderResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def reload_oidc_providers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Reloads all active OIDC provider configurations from the database and synchronizes
        cached keys with the remote JWKS endpoints.

        Key synchronization: For each provider, this operation fetches the current keys from
        the remote JWKS endpoint and invalidates any locally cached keys that no longer exist
        in the remote JWKS. This is useful for security when OIDC providers have rotated or
        revoked keys.

        This operation is useful when you want to ensure all nodes have the latest OIDC provider
        configurations and that any revoked keys are no longer trusted.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth/oidc/providers/reload",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def delete_oidc_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes an OIDC provider and all its associated JWK keys.
        The provider will first be invalidated (if not already) and then removed from storage.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/oidc/providers/{encode_path_param(id)}",
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def update_oidc_provider(
        self,
        id: str,
        *,
        issuers: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OidcProviderResponseDto]:
        """
        Updates configuration for an OIDC provider.

        Note: Updating the issuers list immediately deletes all cached keys for this provider.
        This ensures that JWTs from issuers that are no longer trusted cannot be validated using
        previously cached keys. The keys will be re-fetched from the remote JWKS endpoint with the
        new issuer configuration when they are next needed for JWT validation.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider

        issuers : typing.Optional[typing.Sequence[str]]
            Optional but highly recommended list of allowed issuer URIs from this OIDC provider. When present, JWT validation will require the 'iss' claim to match one of these values. When set to null or empty array, the 'iss' claim validation is skipped.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OidcProviderResponseDto]
            OIDC provider issuers updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/oidc/providers/{encode_path_param(id)}",
            method="PATCH",
            json={
                "issuers": issuers,
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
                    OidcProviderResponseDto,
                    parse_obj_as(
                        type_=OidcProviderResponseDto,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def invalidate_oidc_provider(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Invalidates an OIDC provider, marking it as inactive and invalidating all loaded public keys
        associated with this provider. The provider configuration is retained but will no longer be
        used for JWT validation.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to invalidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/oidc/providers/{encode_path_param(id)}/invalidate",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def reactivate_oidc_provider(
        self,
        id: str,
        *,
        reactivate_keys: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OidcProviderResponseDto]:
        """
        Reactivates a previously invalidated OIDC provider. The provider will be marked as active
        and can be used for JWT validation again.
        This operation is idempotent - if the provider is already active, it returns the current state.

        Parameters
        ----------
        id : str
            The ID of the OIDC provider to reactivate

        reactivate_keys : typing.Optional[bool]
            If true, also reactivates all related JWK keys that were invalidated with this provider

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OidcProviderResponseDto]
            OIDC provider reactivated successfully or already active
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"oauth/oidc/providers/{encode_path_param(id)}/reactivate",
            method="POST",
            json={
                "reactivateKeys": reactivate_keys,
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
                    OidcProviderResponseDto,
                    parse_obj_as(
                        type_=OidcProviderResponseDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
