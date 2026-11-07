

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
from ..types.bad_request_error_body import BadRequestErrorBody
from ..types.test_response_result import TestResponseResult
from .types.test_test_request_parameters import TestTestRequestParameters
from pydantic import ValidationError


class RawTestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def test_test(
        self,
        *,
        parameters: typing.Optional[TestTestRequestParameters] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TestResponseResult]:
        """
        Test.

        Parameters
        ----------
        parameters : typing.Optional[TestTestRequestParameters]
            Parameters for testing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestResponseResult]
            Request fulfilled, document follows
        """
        _response = self._client_wrapper.httpx_client.request(
            "test",
            method="GET",
            params={
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Optional[TestTestRequestParameters], direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestResponseResult,
                    parse_obj_as(
                        type_=TestResponseResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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


class AsyncRawTestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def test_test(
        self,
        *,
        parameters: typing.Optional[TestTestRequestParameters] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TestResponseResult]:
        """
        Test.

        Parameters
        ----------
        parameters : typing.Optional[TestTestRequestParameters]
            Parameters for testing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestResponseResult]
            Request fulfilled, document follows
        """
        _response = await self._client_wrapper.httpx_client.request(
            "test",
            method="GET",
            params={
                "parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Optional[TestTestRequestParameters], direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestResponseResult,
                    parse_obj_as(
                        type_=TestResponseResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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
