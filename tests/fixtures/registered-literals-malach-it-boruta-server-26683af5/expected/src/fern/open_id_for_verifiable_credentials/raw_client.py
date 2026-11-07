

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.credential_response import CredentialResponse
from ..types.o_auth_error import OAuthError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOpenIdForVerifiableCredentialsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def issue_a_credential(
        self,
        *,
        format: typing.Optional[str] = OMIT,
        credential_definition: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        proof: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CredentialResponse]:
        """
        Parameters
        ----------
        format : typing.Optional[str]

        credential_definition : typing.Optional[typing.Dict[str, typing.Any]]

        types : typing.Optional[typing.Sequence[str]]

        proof : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CredentialResponse]
            Credential or deferred credential response
        """
        _response = self._client_wrapper.httpx_client.request(
            "openid/credential",
            method="POST",
            json={
                "format": format,
                "credential_definition": credential_definition,
                "types": types,
                "proof": proof,
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
                    CredentialResponse,
                    parse_obj_as(
                        type_=CredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def retrieve_a_deferred_credential(
        self, *, acceptance_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CredentialResponse]:
        """
        The route uses the spelling implemented by the service: defered-credential.

        Parameters
        ----------
        acceptance_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CredentialResponse]
            Credential or deferred credential response
        """
        _response = self._client_wrapper.httpx_client.request(
            "openid/defered-credential",
            method="POST",
            json={
                "acceptance_token": acceptance_token,
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
                    CredentialResponse,
                    parse_obj_as(
                        type_=CredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
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


class AsyncRawOpenIdForVerifiableCredentialsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def issue_a_credential(
        self,
        *,
        format: typing.Optional[str] = OMIT,
        credential_definition: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        types: typing.Optional[typing.Sequence[str]] = OMIT,
        proof: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CredentialResponse]:
        """
        Parameters
        ----------
        format : typing.Optional[str]

        credential_definition : typing.Optional[typing.Dict[str, typing.Any]]

        types : typing.Optional[typing.Sequence[str]]

        proof : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CredentialResponse]
            Credential or deferred credential response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "openid/credential",
            method="POST",
            json={
                "format": format,
                "credential_definition": credential_definition,
                "types": types,
                "proof": proof,
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
                    CredentialResponse,
                    parse_obj_as(
                        type_=CredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def retrieve_a_deferred_credential(
        self, *, acceptance_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CredentialResponse]:
        """
        The route uses the spelling implemented by the service: defered-credential.

        Parameters
        ----------
        acceptance_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CredentialResponse]
            Credential or deferred credential response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "openid/defered-credential",
            method="POST",
            json={
                "acceptance_token": acceptance_token,
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
                    CredentialResponse,
                    parse_obj_as(
                        type_=CredentialResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        OAuthError,
                        parse_obj_as(
                            type_=OAuthError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
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
