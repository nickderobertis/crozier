

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.alarms_list_response import AlarmsListResponse
from ..types.error_response import ErrorResponse
from .types.list_alarms_request_status import ListAlarmsRequestStatus
from pydantic import ValidationError


class RawAlarmsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_alarms(
        self,
        *,
        status: ListAlarmsRequestStatus,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AlarmsListResponse]:
        """
        List alarms filtered by status

        Parameters
        ----------
        status : ListAlarmsRequestStatus
            Filter alarms by status. Required parameter. Allowed values:
              - ACTIVE
              - DEACTIVE

        page : typing.Optional[int]
            The page number

        page_size : typing.Optional[int]
            The number of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AlarmsListResponse]
            A list of alarms
        """
        _response = self._client_wrapper.httpx_client.request(
            "alarms",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlarmsListResponse,
                    parse_obj_as(
                        type_=AlarmsListResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_deactive_alarms(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Delete all deactive alarms

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "alarms",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deactivate_alarm(
        self, alarm_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deactivate an alarm

        Parameters
        ----------
        alarm_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"alarms/{encode_path_param(alarm_id)}/deactivate",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAlarmsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_alarms(
        self,
        *,
        status: ListAlarmsRequestStatus,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AlarmsListResponse]:
        """
        List alarms filtered by status

        Parameters
        ----------
        status : ListAlarmsRequestStatus
            Filter alarms by status. Required parameter. Allowed values:
              - ACTIVE
              - DEACTIVE

        page : typing.Optional[int]
            The page number

        page_size : typing.Optional[int]
            The number of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AlarmsListResponse]
            A list of alarms
        """
        _response = await self._client_wrapper.httpx_client.request(
            "alarms",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlarmsListResponse,
                    parse_obj_as(
                        type_=AlarmsListResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_deactive_alarms(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete all deactive alarms

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "alarms",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deactivate_alarm(
        self, alarm_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deactivate an alarm

        Parameters
        ----------
        alarm_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"alarms/{encode_path_param(alarm_id)}/deactivate",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
