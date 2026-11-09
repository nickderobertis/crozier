

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_alerts_response import GetAlertsResponse
from pydantic import ValidationError


class RawAlertClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_alerts(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        monitor_uid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAlertsResponse]:
        """
        Get list of defined Alerts

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        monitor_uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAlertsResponse]
            The response body from GET /alerts
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/alerts",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "monitorUID": monitor_uid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAlertsResponse,
                    parse_obj_as(
                        type_=GetAlertsResponse,
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


class AsyncRawAlertClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_alerts(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        monitor_uid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAlertsResponse]:
        """
        Get list of defined Alerts

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        monitor_uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAlertsResponse]
            The response body from GET /alerts
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/alerts",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "monitorUID": monitor_uid,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAlertsResponse,
                    parse_obj_as(
                        type_=GetAlertsResponse,
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
