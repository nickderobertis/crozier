

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.counter_map import CounterMap
from ..types.daily_invocation_statistic import DailyInvocationStatistic
from ..types.test_conformance_metric import TestConformanceMetric
from ..types.test_result_summary import TestResultSummary
from ..types.weighted_metric_value import WeightedMetricValue
from pydantic import ValidationError


class RawMetricsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_conformance_metrics_aggregation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[WeightedMetricValue]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[WeightedMetricValue]]
            Get aggregated coverage metric value
        """
        _response = self._client_wrapper.httpx_client.request(
            "metrics/conformance/aggregate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WeightedMetricValue],
                    parse_obj_as(
                        type_=typing.List[WeightedMetricValue],
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

    def get_service_test_conformance_metric(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TestConformanceMetric]:
        """
        Parameters
        ----------
        service_id : str
            Unique Services identifier this metrics are related to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TestConformanceMetric]
            Test coverage metric for Service
        """
        _response = self._client_wrapper.httpx_client.request(
            f"metrics/conformance/service/{encode_path_param(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestConformanceMetric,
                    parse_obj_as(
                        type_=TestConformanceMetric,
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

    def get_aggregated_invocations_stats(
        self, *, day: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DailyInvocationStatistic]:
        """
        Parameters
        ----------
        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DailyInvocationStatistic]
            Aggregated invocation statistics for specified day
        """
        _response = self._client_wrapper.httpx_client.request(
            "metrics/invocations/global",
            method="GET",
            params={
                "day": day,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DailyInvocationStatistic,
                    parse_obj_as(
                        type_=DailyInvocationStatistic,
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

    def get_latest_aggregated_invocations_stats(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CounterMap]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Number of days to get back in time. Default is 20.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CounterMap]
            A map where keys are day (formatted using yyyyMMdd pattern) and values are counter of invocations on this day
        """
        _response = self._client_wrapper.httpx_client.request(
            "metrics/invocations/global/latest",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CounterMap,
                    parse_obj_as(
                        type_=CounterMap,
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

    def get_top_ivnocations_stats_by_day(
        self,
        *,
        day: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[DailyInvocationStatistic]]:
        """
        Parameters
        ----------
        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        limit : typing.Optional[int]
            The number of top invoked mocks to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[DailyInvocationStatistic]]
            Top invocations for a defined day
        """
        _response = self._client_wrapper.httpx_client.request(
            "metrics/invocations/top",
            method="GET",
            params={
                "day": day,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DailyInvocationStatistic],
                    parse_obj_as(
                        type_=typing.List[DailyInvocationStatistic],
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

    def get_invocation_stats_by_service(
        self,
        service_name: str,
        service_version: str,
        *,
        day: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DailyInvocationStatistic]:
        """
        Parameters
        ----------
        service_name : str
            Name of service to get statistics for

        service_version : str
            Version of service to get statistics for

        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DailyInvocationStatistic]
            Invocation statistics for service for specified day
        """
        _response = self._client_wrapper.httpx_client.request(
            f"metrics/invocations/{encode_path_param(service_name)}/{encode_path_param(service_version)}",
            method="GET",
            params={
                "day": day,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DailyInvocationStatistic,
                    parse_obj_as(
                        type_=DailyInvocationStatistic,
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

    def get_latest_test_results(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TestResultSummary]]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Number of days to consider for test results to return. Default is 7 (one week)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TestResultSummary]]
            Test results summary for specified <limit> last days.
        """
        _response = self._client_wrapper.httpx_client.request(
            "metrics/tests/latest",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TestResultSummary],
                    parse_obj_as(
                        type_=typing.List[TestResultSummary],
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


class AsyncRawMetricsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_conformance_metrics_aggregation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[WeightedMetricValue]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[WeightedMetricValue]]
            Get aggregated coverage metric value
        """
        _response = await self._client_wrapper.httpx_client.request(
            "metrics/conformance/aggregate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WeightedMetricValue],
                    parse_obj_as(
                        type_=typing.List[WeightedMetricValue],
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

    async def get_service_test_conformance_metric(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TestConformanceMetric]:
        """
        Parameters
        ----------
        service_id : str
            Unique Services identifier this metrics are related to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TestConformanceMetric]
            Test coverage metric for Service
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"metrics/conformance/service/{encode_path_param(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TestConformanceMetric,
                    parse_obj_as(
                        type_=TestConformanceMetric,
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

    async def get_aggregated_invocations_stats(
        self, *, day: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DailyInvocationStatistic]:
        """
        Parameters
        ----------
        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DailyInvocationStatistic]
            Aggregated invocation statistics for specified day
        """
        _response = await self._client_wrapper.httpx_client.request(
            "metrics/invocations/global",
            method="GET",
            params={
                "day": day,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DailyInvocationStatistic,
                    parse_obj_as(
                        type_=DailyInvocationStatistic,
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

    async def get_latest_aggregated_invocations_stats(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CounterMap]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Number of days to get back in time. Default is 20.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CounterMap]
            A map where keys are day (formatted using yyyyMMdd pattern) and values are counter of invocations on this day
        """
        _response = await self._client_wrapper.httpx_client.request(
            "metrics/invocations/global/latest",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CounterMap,
                    parse_obj_as(
                        type_=CounterMap,
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

    async def get_top_ivnocations_stats_by_day(
        self,
        *,
        day: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[DailyInvocationStatistic]]:
        """
        Parameters
        ----------
        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        limit : typing.Optional[int]
            The number of top invoked mocks to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[DailyInvocationStatistic]]
            Top invocations for a defined day
        """
        _response = await self._client_wrapper.httpx_client.request(
            "metrics/invocations/top",
            method="GET",
            params={
                "day": day,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[DailyInvocationStatistic],
                    parse_obj_as(
                        type_=typing.List[DailyInvocationStatistic],
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

    async def get_invocation_stats_by_service(
        self,
        service_name: str,
        service_version: str,
        *,
        day: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DailyInvocationStatistic]:
        """
        Parameters
        ----------
        service_name : str
            Name of service to get statistics for

        service_version : str
            Version of service to get statistics for

        day : typing.Optional[str]
            The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DailyInvocationStatistic]
            Invocation statistics for service for specified day
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"metrics/invocations/{encode_path_param(service_name)}/{encode_path_param(service_version)}",
            method="GET",
            params={
                "day": day,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DailyInvocationStatistic,
                    parse_obj_as(
                        type_=DailyInvocationStatistic,
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

    async def get_latest_test_results(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TestResultSummary]]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Number of days to consider for test results to return. Default is 7 (one week)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TestResultSummary]]
            Test results summary for specified <limit> last days.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "metrics/tests/latest",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TestResultSummary],
                    parse_obj_as(
                        type_=typing.List[TestResultSummary],
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
