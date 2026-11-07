

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
from ..types.signed_payload import SignedPayload
from .types.declare_intent_response import DeclareIntentResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIntentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def declare_intent(
        self, *, signed_intent: SignedPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeclareIntentResponse]:
        """
        Submits a signed intent declaration. The server computes a risk score,
        security tier, and policy decision (approve/escalate/block).

        Parameters
        ----------
        signed_intent : SignedPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeclareIntentResponse]
            Policy decision
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/intent/declare",
            method="POST",
            json={
                "signed_intent": convert_and_respect_annotation_metadata(
                    object_=signed_intent, annotation=SignedPayload, direction="write"
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
                    DeclareIntentResponse,
                    parse_obj_as(
                        type_=DeclareIntentResponse,
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


class AsyncRawIntentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def declare_intent(
        self, *, signed_intent: SignedPayload, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeclareIntentResponse]:
        """
        Submits a signed intent declaration. The server computes a risk score,
        security tier, and policy decision (approve/escalate/block).

        Parameters
        ----------
        signed_intent : SignedPayload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeclareIntentResponse]
            Policy decision
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/intent/declare",
            method="POST",
            json={
                "signed_intent": convert_and_respect_annotation_metadata(
                    object_=signed_intent, annotation=SignedPayload, direction="write"
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
                    DeclareIntentResponse,
                    parse_obj_as(
                        type_=DeclareIntentResponse,
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
