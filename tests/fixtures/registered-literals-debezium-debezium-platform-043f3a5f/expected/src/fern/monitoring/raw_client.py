

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.instant import Instant
from ..types.panel_query_response import PanelQueryResponse
from ..types.panels_list_response import PanelsListResponse
from pydantic import ValidationError


class RawMonitoringClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_available_monitoring_panels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PanelsListResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PanelsListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/monitoring/panels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PanelsListResponse,
                    parse_obj_as(
                        type_=PanelsListResponse,
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

    def query_monitoring_panel_data_for_a_specific_pipeline(
        self,
        id: str,
        *,
        end: Instant,
        pipeline_id: str,
        start: Instant,
        step: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PanelQueryResponse]:
        """
        Parameters
        ----------
        id : str

        end : Instant
            End time (ISO 8601)

        pipeline_id : str
            Pipeline identifier

        start : Instant
            Start time (ISO 8601)

        step : typing.Optional[str]
            Query resolution step (e.g. 15s, 1m)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PanelQueryResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/monitoring/panels/{encode_path_param(id)}/query",
            method="GET",
            params={
                "end": serialize_datetime(end),
                "pipeline_id": pipeline_id,
                "start": serialize_datetime(start),
                "step": step,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PanelQueryResponse,
                    parse_obj_as(
                        type_=PanelQueryResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawMonitoringClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_available_monitoring_panels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PanelsListResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PanelsListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/monitoring/panels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PanelsListResponse,
                    parse_obj_as(
                        type_=PanelsListResponse,
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

    async def query_monitoring_panel_data_for_a_specific_pipeline(
        self,
        id: str,
        *,
        end: Instant,
        pipeline_id: str,
        start: Instant,
        step: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PanelQueryResponse]:
        """
        Parameters
        ----------
        id : str

        end : Instant
            End time (ISO 8601)

        pipeline_id : str
            Pipeline identifier

        start : Instant
            Start time (ISO 8601)

        step : typing.Optional[str]
            Query resolution step (e.g. 15s, 1m)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PanelQueryResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/monitoring/panels/{encode_path_param(id)}/query",
            method="GET",
            params={
                "end": serialize_datetime(end),
                "pipeline_id": pipeline_id,
                "start": serialize_datetime(start),
                "step": step,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PanelQueryResponse,
                    parse_obj_as(
                        type_=PanelQueryResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
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
