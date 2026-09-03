

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.fapi_configuration import FapiConfiguration
from ..types.jwk_set import JwkSet
from ..types.oidc_discovery import OidcDiscovery
from ..types.swiss_banking_metadata import SwissBankingMetadata
from pydantic import ValidationError


class RawDiscoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def openid_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OidcDiscovery]:
        """
        OpenID Connect Discovery 1.0 compliant discovery document with FAPI 2.0 metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OidcDiscovery]
            OpenID Connect configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            ".well-known/openid-configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OidcDiscovery,
                    parse_obj_as(
                        type_=OidcDiscovery,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def fapi_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FapiConfiguration]:
        """
        FAPI 2.0 specific configuration metadata for Swiss financial services.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FapiConfiguration]
            FAPI configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            ".well-known/fapi-configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FapiConfiguration,
                    parse_obj_as(
                        type_=FapiConfiguration,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def jwks(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[JwkSet]:
        """
        Public keys for JWT signature verification (RFC 7517).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JwkSet]
            JSON Web Key Set
        """
        _response = self._client_wrapper.httpx_client.request(
            ".well-known/jwks.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JwkSet,
                    parse_obj_as(
                        type_=JwkSet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def swiss_banking_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SwissBankingMetadata]:
        """
        Swiss Open Banking specific metadata including supported use cases and standards.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SwissBankingMetadata]
            Swiss banking metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            ".well-known/swiss-banking-metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SwissBankingMetadata,
                    parse_obj_as(
                        type_=SwissBankingMetadata,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDiscoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def openid_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OidcDiscovery]:
        """
        OpenID Connect Discovery 1.0 compliant discovery document with FAPI 2.0 metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OidcDiscovery]
            OpenID Connect configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            ".well-known/openid-configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OidcDiscovery,
                    parse_obj_as(
                        type_=OidcDiscovery,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def fapi_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FapiConfiguration]:
        """
        FAPI 2.0 specific configuration metadata for Swiss financial services.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FapiConfiguration]
            FAPI configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            ".well-known/fapi-configuration",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FapiConfiguration,
                    parse_obj_as(
                        type_=FapiConfiguration,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def jwks(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[JwkSet]:
        """
        Public keys for JWT signature verification (RFC 7517).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JwkSet]
            JSON Web Key Set
        """
        _response = await self._client_wrapper.httpx_client.request(
            ".well-known/jwks.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JwkSet,
                    parse_obj_as(
                        type_=JwkSet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def swiss_banking_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SwissBankingMetadata]:
        """
        Swiss Open Banking specific metadata including supported use cases and standards.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SwissBankingMetadata]
            Swiss banking metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            ".well-known/swiss-banking-metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SwissBankingMetadata,
                    parse_obj_as(
                        type_=SwissBankingMetadata,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
