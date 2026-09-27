

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.expectation import Expectation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOidcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def mock_oidc_provider(
        self,
        *,
        issuer: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        private_key_pem: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        token_expiry_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Expectation]]:
        """
        Generates a set of expectations that emulate an OpenID Connect / OAuth2 provider (discovery document, JWKS, token, authorize, userinfo and related endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        issuer : typing.Optional[str]
            issuer URL advertised in the discovery document and token claims

        client_id : typing.Optional[str]
            OAuth2 client identifier

        client_secret : typing.Optional[str]
            OAuth2 client secret

        private_key_pem : typing.Optional[str]
            PEM-encoded signing private key (never serialized back in responses)

        scopes : typing.Optional[typing.Sequence[str]]
            supported OAuth2 / OIDC scopes

        token_expiry_seconds : typing.Optional[int]
            lifetime of issued access tokens in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Expectation]]
            OIDC provider expectations created
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/oidc",
            method="PUT",
            json={
                "issuer": issuer,
                "clientId": client_id,
                "clientSecret": client_secret,
                "privateKeyPem": private_key_pem,
                "scopes": scopes,
                "tokenExpirySeconds": token_expiry_seconds,
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
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawOidcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def mock_oidc_provider(
        self,
        *,
        issuer: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        private_key_pem: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        token_expiry_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Expectation]]:
        """
        Generates a set of expectations that emulate an OpenID Connect / OAuth2 provider (discovery document, JWKS, token, authorize, userinfo and related endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        issuer : typing.Optional[str]
            issuer URL advertised in the discovery document and token claims

        client_id : typing.Optional[str]
            OAuth2 client identifier

        client_secret : typing.Optional[str]
            OAuth2 client secret

        private_key_pem : typing.Optional[str]
            PEM-encoded signing private key (never serialized back in responses)

        scopes : typing.Optional[typing.Sequence[str]]
            supported OAuth2 / OIDC scopes

        token_expiry_seconds : typing.Optional[int]
            lifetime of issued access tokens in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Expectation]]
            OIDC provider expectations created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/oidc",
            method="PUT",
            json={
                "issuer": issuer,
                "clientId": client_id,
                "clientSecret": client_secret,
                "privateKeyPem": private_key_pem,
                "scopes": scopes,
                "tokenExpirySeconds": token_expiry_seconds,
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
                    typing.List[Expectation],
                    parse_obj_as(
                        type_=typing.List[Expectation],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
