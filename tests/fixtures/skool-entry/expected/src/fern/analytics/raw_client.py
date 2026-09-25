

import datetime as dt
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
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from .types.get_group_analytics_response import GetGroupAnalyticsResponse
from pydantic import ValidationError


class RawAnalyticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_group_analytics(
        self,
        group_slug: str,
        *,
        session_id: str,
        start_date: typing.Optional[dt.date] = None,
        end_date: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetGroupAnalyticsResponse]:
        """
        Retrieve analytics data for a Skool group.

        Parameters
        ----------
        group_slug : str

        session_id : str

        start_date : typing.Optional[dt.date]

        end_date : typing.Optional[dt.date]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetGroupAnalyticsResponse]
            Analytics data
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_slug)}/analytics/",
            method="GET",
            params={
                "session_id": session_id,
                "start_date": str(start_date) if start_date is not None else None,
                "end_date": str(end_date) if end_date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGroupAnalyticsResponse,
                    parse_obj_as(
                        type_=GetGroupAnalyticsResponse,
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


class AsyncRawAnalyticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_group_analytics(
        self,
        group_slug: str,
        *,
        session_id: str,
        start_date: typing.Optional[dt.date] = None,
        end_date: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetGroupAnalyticsResponse]:
        """
        Retrieve analytics data for a Skool group.

        Parameters
        ----------
        group_slug : str

        session_id : str

        start_date : typing.Optional[dt.date]

        end_date : typing.Optional[dt.date]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetGroupAnalyticsResponse]
            Analytics data
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/groups/{encode_path_param(group_slug)}/analytics/",
            method="GET",
            params={
                "session_id": session_id,
                "start_date": str(start_date) if start_date is not None else None,
                "end_date": str(end_date) if end_date is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGroupAnalyticsResponse,
                    parse_obj_as(
                        type_=GetGroupAnalyticsResponse,
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
