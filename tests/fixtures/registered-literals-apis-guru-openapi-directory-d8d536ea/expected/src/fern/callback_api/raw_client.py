

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..types.callback_list_response import CallbackListResponse
from ..types.exception import Exception
from .types.get_callbacks_request_status import GetCallbacksRequestStatus
from pydantic import ValidationError


class RawCallbackApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCallbacksRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CallbackListResponse]:
        """
        Get list of callback types with count for a requested Date.

        Parameters
        ----------
        date : typing.Optional[dt.datetime]
            Date for which fetch the callback type list. By default, the date will be set to current date.

        status : typing.Optional[GetCallbacksRequestStatus]
            Status of the callbacks. Default status will fetch all callbacks.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CallbackListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "callbacks",
            method="GET",
            params={
                "date": serialize_datetime(date) if date is not None else None,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CallbackListResponse,
                    parse_obj_as(
                        type_=CallbackListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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


class AsyncRawCallbackApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCallbacksRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CallbackListResponse]:
        """
        Get list of callback types with count for a requested Date.

        Parameters
        ----------
        date : typing.Optional[dt.datetime]
            Date for which fetch the callback type list. By default, the date will be set to current date.

        status : typing.Optional[GetCallbacksRequestStatus]
            Status of the callbacks. Default status will fetch all callbacks.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CallbackListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "callbacks",
            method="GET",
            params={
                "date": serialize_datetime(date) if date is not None else None,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CallbackListResponse,
                    parse_obj_as(
                        type_=CallbackListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
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
