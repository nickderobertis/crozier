

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.dashboard_dashboard_api_get_widget_items200response import DashboardDashboardApiGetWidgetItems200Response
from ..types.dashboard_dashboard_api_get_widgets200response import DashboardDashboardApiGetWidgets200Response
from pydantic import ValidationError


class RawDashboardDashboardApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_widgets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DashboardDashboardApiGetWidgets200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DashboardDashboardApiGetWidgets200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/dashboard/api/v1/widgets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DashboardDashboardApiGetWidgets200Response,
                    parse_obj_as(
                        type_=DashboardDashboardApiGetWidgets200Response,
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

    def get_widget_items(
        self,
        *,
        since_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        widgets: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DashboardDashboardApiGetWidgetItems200Response]:
        """
        Parameters
        ----------
        since_ids : typing.Optional[str]
            Array indexed by widget Ids, contains date/id from which we want the new items

        limit : typing.Optional[int]
            Limit number of result items per widget

        widgets : typing.Optional[str]
            Limit results to specific widgets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DashboardDashboardApiGetWidgetItems200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/dashboard/api/v1/widget-items",
            method="GET",
            params={
                "sinceIds": since_ids,
                "limit": limit,
                "widgets": widgets,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DashboardDashboardApiGetWidgetItems200Response,
                    parse_obj_as(
                        type_=DashboardDashboardApiGetWidgetItems200Response,
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


class AsyncRawDashboardDashboardApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_widgets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DashboardDashboardApiGetWidgets200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DashboardDashboardApiGetWidgets200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/dashboard/api/v1/widgets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DashboardDashboardApiGetWidgets200Response,
                    parse_obj_as(
                        type_=DashboardDashboardApiGetWidgets200Response,
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

    async def get_widget_items(
        self,
        *,
        since_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        widgets: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DashboardDashboardApiGetWidgetItems200Response]:
        """
        Parameters
        ----------
        since_ids : typing.Optional[str]
            Array indexed by widget Ids, contains date/id from which we want the new items

        limit : typing.Optional[int]
            Limit number of result items per widget

        widgets : typing.Optional[str]
            Limit results to specific widgets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DashboardDashboardApiGetWidgetItems200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/dashboard/api/v1/widget-items",
            method="GET",
            params={
                "sinceIds": since_ids,
                "limit": limit,
                "widgets": widgets,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DashboardDashboardApiGetWidgetItems200Response,
                    parse_obj_as(
                        type_=DashboardDashboardApiGetWidgetItems200Response,
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
