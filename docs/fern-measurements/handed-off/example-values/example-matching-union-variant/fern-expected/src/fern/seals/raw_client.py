

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.verify_seal_request_seal import VerifySealRequestSeal
from .types.verify_seal_response import VerifySealResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSealsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def verify_seal(
        self, *, seal: VerifySealRequestSeal, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VerifySealResponse]:
        """
        Parameters
        ----------
        seal : VerifySealRequestSeal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VerifySealResponse]
            Verified
        """
        _response = self._client_wrapper.httpx_client.request(
            "seals/verify",
            method="POST",
            json={
                "seal": convert_and_respect_annotation_metadata(
                    object_=seal, annotation=VerifySealRequestSeal, direction="write"
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
                    VerifySealResponse,
                    parse_obj_as(
                        type_=VerifySealResponse,
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


class AsyncRawSealsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def verify_seal(
        self, *, seal: VerifySealRequestSeal, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VerifySealResponse]:
        """
        Parameters
        ----------
        seal : VerifySealRequestSeal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VerifySealResponse]
            Verified
        """
        _response = await self._client_wrapper.httpx_client.request(
            "seals/verify",
            method="POST",
            json={
                "seal": convert_and_respect_annotation_metadata(
                    object_=seal, annotation=VerifySealRequestSeal, direction="write"
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
                    VerifySealResponse,
                    parse_obj_as(
                        type_=VerifySealResponse,
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
