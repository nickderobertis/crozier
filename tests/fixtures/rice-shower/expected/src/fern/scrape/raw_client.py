

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.not_found_error_body import NotFoundErrorBody
from .types.get_all_scrape_metrics_response_item import GetAllScrapeMetricsResponseItem
from .types.get_all_scrape_status_response_item import GetAllScrapeStatusResponseItem
from .types.get_system_scrape_metrics_response import GetSystemScrapeMetricsResponse
from .types.get_system_scrape_status_response import GetSystemScrapeStatusResponse
from pydantic import ValidationError


class RawScrapeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_all_scrape_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetAllScrapeMetricsResponseItem]]:
        """
        Retrieve scraping metrics for all active systems, including per-system error counts and success totals

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetAllScrapeMetricsResponseItem]]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            "scrape/metrics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetAllScrapeMetricsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetAllScrapeMetricsResponseItem],
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

    def get_system_scrape_metrics(
        self, system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSystemScrapeMetricsResponse]:
        """
        Retrieve scraping metrics for a specific system by its ID

        Parameters
        ----------
        system_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSystemScrapeMetricsResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"scrape/metrics/{encode_path_param(system_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSystemScrapeMetricsResponse,
                    parse_obj_as(
                        type_=GetSystemScrapeMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    def get_all_scrape_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetAllScrapeStatusResponseItem]]:
        """
        Retrieve windowed scrape status (success/error counts in last 1m, 10m, and since start) for all active systems

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetAllScrapeStatusResponseItem]]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            "scrape/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetAllScrapeStatusResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetAllScrapeStatusResponseItem],
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

    def get_system_scrape_status(
        self, system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSystemScrapeStatusResponse]:
        """
        Retrieve windowed scrape status for a specific system by its ID

        Parameters
        ----------
        system_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSystemScrapeStatusResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"scrape/status/{encode_path_param(system_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSystemScrapeStatusResponse,
                    parse_obj_as(
                        type_=GetSystemScrapeStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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


class AsyncRawScrapeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_all_scrape_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetAllScrapeMetricsResponseItem]]:
        """
        Retrieve scraping metrics for all active systems, including per-system error counts and success totals

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetAllScrapeMetricsResponseItem]]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "scrape/metrics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetAllScrapeMetricsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetAllScrapeMetricsResponseItem],
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

    async def get_system_scrape_metrics(
        self, system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSystemScrapeMetricsResponse]:
        """
        Retrieve scraping metrics for a specific system by its ID

        Parameters
        ----------
        system_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSystemScrapeMetricsResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"scrape/metrics/{encode_path_param(system_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSystemScrapeMetricsResponse,
                    parse_obj_as(
                        type_=GetSystemScrapeMetricsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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

    async def get_all_scrape_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetAllScrapeStatusResponseItem]]:
        """
        Retrieve windowed scrape status (success/error counts in last 1m, 10m, and since start) for all active systems

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetAllScrapeStatusResponseItem]]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "scrape/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetAllScrapeStatusResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetAllScrapeStatusResponseItem],
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

    async def get_system_scrape_status(
        self, system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSystemScrapeStatusResponse]:
        """
        Retrieve windowed scrape status for a specific system by its ID

        Parameters
        ----------
        system_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSystemScrapeStatusResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"scrape/status/{encode_path_param(system_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSystemScrapeStatusResponse,
                    parse_obj_as(
                        type_=GetSystemScrapeStatusResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundErrorBody,
                        parse_obj_as(
                            type_=NotFoundErrorBody,
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
