

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
from ..types.delegation_token import DelegationToken
from ..types.error import Error
from ..types.token_request_grant_type import TokenRequestGrantType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTokenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def issue_delegation_token(
        self,
        *,
        grant_type: TokenRequestGrantType,
        code_verifier: str,
        device_code: typing.Optional[str] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[str] = OMIT,
        audience: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DelegationToken]:
        """
        Issues a `DelegationToken` bound to a citizen authentication event.
        Supports two grant flows:
          - Device Authorization Grant per RFC 8628 (agent-first flows).
          - Token Exchange per RFC 8693 (ministry-to-ministry hand-off).
        PKCE per RFC 7636 is REQUIRED on all grant types. The issued token is a JWT
        per RFC 9068 with `aal_asserted` claim carrying NIST SP 800-63-4 AAL.

        Parameters
        ----------
        grant_type : TokenRequestGrantType
            Device grant (RFC 8628) or token exchange (RFC 8693).

        code_verifier : str
            PKCE code verifier (RFC 7636).

        device_code : typing.Optional[str]

        subject_token : typing.Optional[str]

        subject_token_type : typing.Optional[str]

        audience : typing.Optional[str]

        scope : typing.Optional[str]
            Space-separated scope string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DelegationToken]
            Token issued.
        """
        _response = self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            data={
                "grant_type": grant_type,
                "code_verifier": code_verifier,
                "device_code": device_code,
                "subject_token": subject_token,
                "subject_token_type": subject_token_type,
                "audience": audience,
                "scope": scope,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DelegationToken,
                    parse_obj_as(
                        type_=DelegationToken,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawTokenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def issue_delegation_token(
        self,
        *,
        grant_type: TokenRequestGrantType,
        code_verifier: str,
        device_code: typing.Optional[str] = OMIT,
        subject_token: typing.Optional[str] = OMIT,
        subject_token_type: typing.Optional[str] = OMIT,
        audience: typing.Optional[str] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DelegationToken]:
        """
        Issues a `DelegationToken` bound to a citizen authentication event.
        Supports two grant flows:
          - Device Authorization Grant per RFC 8628 (agent-first flows).
          - Token Exchange per RFC 8693 (ministry-to-ministry hand-off).
        PKCE per RFC 7636 is REQUIRED on all grant types. The issued token is a JWT
        per RFC 9068 with `aal_asserted` claim carrying NIST SP 800-63-4 AAL.

        Parameters
        ----------
        grant_type : TokenRequestGrantType
            Device grant (RFC 8628) or token exchange (RFC 8693).

        code_verifier : str
            PKCE code verifier (RFC 7636).

        device_code : typing.Optional[str]

        subject_token : typing.Optional[str]

        subject_token_type : typing.Optional[str]

        audience : typing.Optional[str]

        scope : typing.Optional[str]
            Space-separated scope string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DelegationToken]
            Token issued.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "token",
            method="POST",
            data={
                "grant_type": grant_type,
                "code_verifier": code_verifier,
                "device_code": device_code,
                "subject_token": subject_token,
                "subject_token_type": subject_token_type,
                "audience": audience,
                "scope": scope,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DelegationToken,
                    parse_obj_as(
                        type_=DelegationToken,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
