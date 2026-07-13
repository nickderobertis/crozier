

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.app_get_application_api_usage_response import AppGetApplicationApiUsageResponse
from .types.app_get_bungie_applications_response import AppGetBungieApplicationsResponse


class RawAppClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getapplicationapiusage(
        self,
        application_id: int,
        *,
        end: typing.Optional[dt.datetime] = None,
        start: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AppGetApplicationApiUsageResponse]:
        """
        Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

        Parameters
        ----------
        application_id : int
            ID of the application to get usage statistics.

        end : typing.Optional[dt.datetime]
            End time for query. Goes to now if not specified.

        start : typing.Optional[dt.datetime]
            Start time for query. Goes to 24 hours ago if not specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AppGetApplicationApiUsageResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"App/ApiUsage/{jsonable_encoder(application_id)}/",
            method="GET",
            params={
                "end": serialize_datetime(end) if end is not None else None,
                "start": serialize_datetime(start) if start is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AppGetApplicationApiUsageResponse,
                    parse_obj_as(
                        type_=AppGetApplicationApiUsageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getbungieapplications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AppGetBungieApplicationsResponse]:
        """
        Get list of applications created by Bungie.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AppGetBungieApplicationsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "App/FirstParty/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AppGetBungieApplicationsResponse,
                    parse_obj_as(
                        type_=AppGetBungieApplicationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAppClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getapplicationapiusage(
        self,
        application_id: int,
        *,
        end: typing.Optional[dt.datetime] = None,
        start: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AppGetApplicationApiUsageResponse]:
        """
        Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

        Parameters
        ----------
        application_id : int
            ID of the application to get usage statistics.

        end : typing.Optional[dt.datetime]
            End time for query. Goes to now if not specified.

        start : typing.Optional[dt.datetime]
            Start time for query. Goes to 24 hours ago if not specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AppGetApplicationApiUsageResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"App/ApiUsage/{jsonable_encoder(application_id)}/",
            method="GET",
            params={
                "end": serialize_datetime(end) if end is not None else None,
                "start": serialize_datetime(start) if start is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AppGetApplicationApiUsageResponse,
                    parse_obj_as(
                        type_=AppGetApplicationApiUsageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getbungieapplications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AppGetBungieApplicationsResponse]:
        """
        Get list of applications created by Bungie.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AppGetBungieApplicationsResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "App/FirstParty/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AppGetBungieApplicationsResponse,
                    parse_obj_as(
                        type_=AppGetBungieApplicationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
