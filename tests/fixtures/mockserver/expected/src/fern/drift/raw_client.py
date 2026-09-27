

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from .types.get_mockserver_drift_response import GetMockserverDriftResponse
from .types.put_mockserver_drift_clear_response import PutMockserverDriftClearResponse
from pydantic import ValidationError


class RawDriftClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_recorded_mock_drift(
        self,
        *,
        expectation_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetMockserverDriftResponse]:
        """
        Returns recorded drift records (differences between expectations and observed responses), optionally filtered by expectation id and limited in count.

        Parameters
        ----------
        expectation_id : typing.Optional[str]
            only return drift records for the given expectation id

        limit : typing.Optional[int]
            maximum number of recent drift records to return (default 50, capped at 500), ignored when expectationId is supplied

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMockserverDriftResponse]
            drift records returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/drift",
            method="GET",
            params={
                "expectationId": expectation_id,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverDriftResponse,
                    parse_obj_as(
                        type_=GetMockserverDriftResponse,
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

    def clear_all_recorded_mock_drift(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PutMockserverDriftClearResponse]:
        """
        removes all recorded drift records

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverDriftClearResponse]
            drift records cleared
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/drift/clear",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverDriftClearResponse,
                    parse_obj_as(
                        type_=PutMockserverDriftClearResponse,
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


class AsyncRawDriftClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_recorded_mock_drift(
        self,
        *,
        expectation_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetMockserverDriftResponse]:
        """
        Returns recorded drift records (differences between expectations and observed responses), optionally filtered by expectation id and limited in count.

        Parameters
        ----------
        expectation_id : typing.Optional[str]
            only return drift records for the given expectation id

        limit : typing.Optional[int]
            maximum number of recent drift records to return (default 50, capped at 500), ignored when expectationId is supplied

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMockserverDriftResponse]
            drift records returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/drift",
            method="GET",
            params={
                "expectationId": expectation_id,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMockserverDriftResponse,
                    parse_obj_as(
                        type_=GetMockserverDriftResponse,
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

    async def clear_all_recorded_mock_drift(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PutMockserverDriftClearResponse]:
        """
        removes all recorded drift records

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverDriftClearResponse]
            drift records cleared
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/drift/clear",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PutMockserverDriftClearResponse,
                    parse_obj_as(
                        type_=PutMockserverDriftClearResponse,
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
