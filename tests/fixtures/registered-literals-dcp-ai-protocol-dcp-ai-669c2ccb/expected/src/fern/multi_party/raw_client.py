

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..types.error_response import ErrorResponse
from .types.multi_party_authorize_request_authorization import MultiPartyAuthorizeRequestAuthorization
from .types.multi_party_authorize_response import MultiPartyAuthorizeResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMultiPartyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def multi_party_authorize(
        self,
        *,
        authorization: MultiPartyAuthorizeRequestAuthorization,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MultiPartyAuthorizeResponse]:
        """
        Validates a multi-party authorization request. Requires at least the
        threshold number of authorizations including an owner signature.

        Parameters
        ----------
        authorization : MultiPartyAuthorizeRequestAuthorization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MultiPartyAuthorizeResponse]
            Authorization verified
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/multi-party/authorize",
            method="POST",
            json={
                "authorization": convert_and_respect_annotation_metadata(
                    object_=authorization, annotation=MultiPartyAuthorizeRequestAuthorization, direction="write"
                ),
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
                    MultiPartyAuthorizeResponse,
                    parse_obj_as(
                        type_=MultiPartyAuthorizeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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


class AsyncRawMultiPartyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def multi_party_authorize(
        self,
        *,
        authorization: MultiPartyAuthorizeRequestAuthorization,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MultiPartyAuthorizeResponse]:
        """
        Validates a multi-party authorization request. Requires at least the
        threshold number of authorizations including an owner signature.

        Parameters
        ----------
        authorization : MultiPartyAuthorizeRequestAuthorization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MultiPartyAuthorizeResponse]
            Authorization verified
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/multi-party/authorize",
            method="POST",
            json={
                "authorization": convert_and_respect_annotation_metadata(
                    object_=authorization, annotation=MultiPartyAuthorizeRequestAuthorization, direction="write"
                ),
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
                    MultiPartyAuthorizeResponse,
                    parse_obj_as(
                        type_=MultiPartyAuthorizeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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
