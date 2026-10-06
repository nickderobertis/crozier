

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.alignment import Alignment
from ..types.http_validation_error import HttpValidationError
from ..types.interpolation_method import InterpolationMethod
from ..types.query_input_aggregation import QueryInputAggregation
from ..types.query_input_from import QueryInputFrom
from ..types.query_input_interpolation import QueryInputInterpolation
from ..types.query_input_until import QueryInputUntil
from ..types.query_result import QueryResult
from ..types.render import Render
from ..types.render_mode import RenderMode
from ..types.series_spec import SeriesSpec
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawExecuteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def execute_query(
        self,
        *,
        resource: typing.Optional[str] = None,
        metric: typing.Optional[str] = None,
        aggregation: typing.Optional[str] = None,
        interpolation: typing.Optional[InterpolationMethod] = None,
        freq: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        until: typing.Optional[str] = None,
        window: typing.Optional[str] = None,
        periods: typing.Optional[int] = None,
        render: typing.Optional[RenderMode] = None,
        accept: typing.Optional[str] = None,
        query_input_resource: typing.Optional[str] = OMIT,
        query_input_metric: typing.Optional[str] = OMIT,
        query_input_aggregation: typing.Optional[QueryInputAggregation] = OMIT,
        query_input_interpolation: typing.Optional[QueryInputInterpolation] = OMIT,
        query_input_freq: typing.Optional[str] = OMIT,
        query_input_from_: typing.Optional[QueryInputFrom] = OMIT,
        query_input_until: typing.Optional[QueryInputUntil] = OMIT,
        query_input_window: typing.Optional[str] = OMIT,
        query_input_periods: typing.Optional[int] = OMIT,
        align: typing.Optional[Alignment] = OMIT,
        data: typing.Optional[typing.Sequence[SeriesSpec]] = OMIT,
        query_input_render: typing.Optional[Render] = OMIT,
        lookback: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueryResult]:
        """
        Execute a timeseries query.

        Executes the timeseries query specified in the request body,
        after applying any overrides from the url parameters.

        Note that string values in the query body can contain `{var_name}` placeholders.
        These will get replaced with by `var_name` bindings
        in the query body for that variable.

        ```json
        {
            "station_id": "29758",
            "resource": "weather_station_{station_id}",
            ...
        }
        ```
        results in using a `weather_station_29758` resource.

        Parameters
        ----------
        resource : typing.Optional[str]
            Default Resource Override.

        metric : typing.Optional[str]
            Default Metric Override.

        aggregation : typing.Optional[str]

        interpolation : typing.Optional[InterpolationMethod]

        freq : typing.Optional[str]
            Override for the `freq` query attribute.

        from_ : typing.Optional[str]

        until : typing.Optional[str]

        window : typing.Optional[str]

        periods : typing.Optional[int]

        render : typing.Optional[RenderMode]

        accept : typing.Optional[str]
            Use a 'text/csv' accept header to get CSV formatted results.

        query_input_resource : typing.Optional[str]
            Default resource for the series in the query.

        query_input_metric : typing.Optional[str]
            Default metric for the series in the query.

        query_input_aggregation : typing.Optional[QueryInputAggregation]
            Default aggregation method(s) for the series in the query.

        query_input_interpolation : typing.Optional[QueryInputInterpolation]
            Default Interpolation method for the series (if aggregated).

        query_input_freq : typing.Optional[str]
            Interval used to aggregate or regularize data. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.

        query_input_from_ : typing.Optional[QueryInputFrom]
            The start of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)  specifiers.

        query_input_until : typing.Optional[QueryInputUntil]
            The end (not-inclusive) of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)specifiers.

        query_input_window : typing.Optional[str]
            The absolute size of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.

        query_input_periods : typing.Optional[int]
            The size of the time window in number of `freq` units. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.

        align : typing.Optional[Alignment]

        data : typing.Optional[typing.Sequence[SeriesSpec]]
            List of series specifications. When not specified, a single default series specification is assumed(`[{}]`, using the default `metric`,`resource`, ... ).

        query_input_render : typing.Optional[Render]

        lookback : typing.Optional[bool]
            If enabled, the **last-known value** for each of the series will be taken into account in the result.
            For **unaggregated** series, that value will be included as is (with a timestamp before the result window).
            For **aggregated** series, that value will be used at the first timestamp, but only if
             * no aggregated value on the first timestamp could be computed
             * and the aggregation is compatible with the value, i.e. in mean, min, max, first, last, median

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "queries/v1/data",
            method="POST",
            params={
                "resource": resource,
                "metric": metric,
                "aggregation": aggregation,
                "interpolation": interpolation,
                "freq": freq,
                "from": from_,
                "until": until,
                "window": window,
                "periods": periods,
                "render": render,
            },
            json={
                "resource": resource,
                "metric": metric,
                "aggregation": convert_and_respect_annotation_metadata(
                    object_=aggregation, annotation=typing.Optional[QueryInputAggregation], direction="write"
                ),
                "interpolation": convert_and_respect_annotation_metadata(
                    object_=interpolation, annotation=QueryInputInterpolation, direction="write"
                ),
                "freq": freq,
                "from": convert_and_respect_annotation_metadata(
                    object_=from_, annotation=QueryInputFrom, direction="write"
                ),
                "until": convert_and_respect_annotation_metadata(
                    object_=until, annotation=QueryInputUntil, direction="write"
                ),
                "window": window,
                "periods": periods,
                "align": convert_and_respect_annotation_metadata(
                    object_=align, annotation=Alignment, direction="write"
                ),
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Sequence[SeriesSpec], direction="write"
                ),
                "render": convert_and_respect_annotation_metadata(object_=render, annotation=Render, direction="write"),
                "lookback": lookback,
            },
            headers={
                "content-type": "application/json",
                "accept": str(accept) if accept is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryResult,
                    parse_obj_as(
                        type_=QueryResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def by_name(
        self,
        query_name: str,
        *,
        resource: typing.Optional[str] = None,
        metric: typing.Optional[str] = None,
        aggregation: typing.Optional[str] = None,
        interpolation: typing.Optional[InterpolationMethod] = None,
        freq: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        until: typing.Optional[str] = None,
        window: typing.Optional[str] = None,
        periods: typing.Optional[int] = None,
        render: typing.Optional[RenderMode] = None,
        accept: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[QueryResult]:
        """
        Execute a named timeseries query.

        Retrieves a stored query definition by name,
        applies overrides from the url parameters, and executes it.

        Parameters
        ----------
        query_name : str

        resource : typing.Optional[str]
            Default Resource Override.

        metric : typing.Optional[str]
            Default Metric Override.

        aggregation : typing.Optional[str]

        interpolation : typing.Optional[InterpolationMethod]

        freq : typing.Optional[str]
            Override for the `freq` query attribute.

        from_ : typing.Optional[str]

        until : typing.Optional[str]

        window : typing.Optional[str]

        periods : typing.Optional[int]

        render : typing.Optional[RenderMode]

        accept : typing.Optional[str]
            Use a 'text/csv' accept header to get CSV formatted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"queries/v1/data/{encode_path_param(query_name)}",
            method="GET",
            params={
                "resource": resource,
                "metric": metric,
                "aggregation": aggregation,
                "interpolation": interpolation,
                "freq": freq,
                "from": from_,
                "until": until,
                "window": window,
                "periods": periods,
                "render": render,
            },
            headers={
                "accept": str(accept) if accept is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryResult,
                    parse_obj_as(
                        type_=QueryResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawExecuteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def execute_query(
        self,
        *,
        resource: typing.Optional[str] = None,
        metric: typing.Optional[str] = None,
        aggregation: typing.Optional[str] = None,
        interpolation: typing.Optional[InterpolationMethod] = None,
        freq: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        until: typing.Optional[str] = None,
        window: typing.Optional[str] = None,
        periods: typing.Optional[int] = None,
        render: typing.Optional[RenderMode] = None,
        accept: typing.Optional[str] = None,
        query_input_resource: typing.Optional[str] = OMIT,
        query_input_metric: typing.Optional[str] = OMIT,
        query_input_aggregation: typing.Optional[QueryInputAggregation] = OMIT,
        query_input_interpolation: typing.Optional[QueryInputInterpolation] = OMIT,
        query_input_freq: typing.Optional[str] = OMIT,
        query_input_from_: typing.Optional[QueryInputFrom] = OMIT,
        query_input_until: typing.Optional[QueryInputUntil] = OMIT,
        query_input_window: typing.Optional[str] = OMIT,
        query_input_periods: typing.Optional[int] = OMIT,
        align: typing.Optional[Alignment] = OMIT,
        data: typing.Optional[typing.Sequence[SeriesSpec]] = OMIT,
        query_input_render: typing.Optional[Render] = OMIT,
        lookback: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueryResult]:
        """
        Execute a timeseries query.

        Executes the timeseries query specified in the request body,
        after applying any overrides from the url parameters.

        Note that string values in the query body can contain `{var_name}` placeholders.
        These will get replaced with by `var_name` bindings
        in the query body for that variable.

        ```json
        {
            "station_id": "29758",
            "resource": "weather_station_{station_id}",
            ...
        }
        ```
        results in using a `weather_station_29758` resource.

        Parameters
        ----------
        resource : typing.Optional[str]
            Default Resource Override.

        metric : typing.Optional[str]
            Default Metric Override.

        aggregation : typing.Optional[str]

        interpolation : typing.Optional[InterpolationMethod]

        freq : typing.Optional[str]
            Override for the `freq` query attribute.

        from_ : typing.Optional[str]

        until : typing.Optional[str]

        window : typing.Optional[str]

        periods : typing.Optional[int]

        render : typing.Optional[RenderMode]

        accept : typing.Optional[str]
            Use a 'text/csv' accept header to get CSV formatted results.

        query_input_resource : typing.Optional[str]
            Default resource for the series in the query.

        query_input_metric : typing.Optional[str]
            Default metric for the series in the query.

        query_input_aggregation : typing.Optional[QueryInputAggregation]
            Default aggregation method(s) for the series in the query.

        query_input_interpolation : typing.Optional[QueryInputInterpolation]
            Default Interpolation method for the series (if aggregated).

        query_input_freq : typing.Optional[str]
            Interval used to aggregate or regularize data. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.

        query_input_from_ : typing.Optional[QueryInputFrom]
            The start of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)  specifiers.

        query_input_until : typing.Optional[QueryInputUntil]
            The end (not-inclusive) of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)specifiers.

        query_input_window : typing.Optional[str]
            The absolute size of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.

        query_input_periods : typing.Optional[int]
            The size of the time window in number of `freq` units. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.

        align : typing.Optional[Alignment]

        data : typing.Optional[typing.Sequence[SeriesSpec]]
            List of series specifications. When not specified, a single default series specification is assumed(`[{}]`, using the default `metric`,`resource`, ... ).

        query_input_render : typing.Optional[Render]

        lookback : typing.Optional[bool]
            If enabled, the **last-known value** for each of the series will be taken into account in the result.
            For **unaggregated** series, that value will be included as is (with a timestamp before the result window).
            For **aggregated** series, that value will be used at the first timestamp, but only if
             * no aggregated value on the first timestamp could be computed
             * and the aggregation is compatible with the value, i.e. in mean, min, max, first, last, median

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "queries/v1/data",
            method="POST",
            params={
                "resource": resource,
                "metric": metric,
                "aggregation": aggregation,
                "interpolation": interpolation,
                "freq": freq,
                "from": from_,
                "until": until,
                "window": window,
                "periods": periods,
                "render": render,
            },
            json={
                "resource": resource,
                "metric": metric,
                "aggregation": convert_and_respect_annotation_metadata(
                    object_=aggregation, annotation=typing.Optional[QueryInputAggregation], direction="write"
                ),
                "interpolation": convert_and_respect_annotation_metadata(
                    object_=interpolation, annotation=QueryInputInterpolation, direction="write"
                ),
                "freq": freq,
                "from": convert_and_respect_annotation_metadata(
                    object_=from_, annotation=QueryInputFrom, direction="write"
                ),
                "until": convert_and_respect_annotation_metadata(
                    object_=until, annotation=QueryInputUntil, direction="write"
                ),
                "window": window,
                "periods": periods,
                "align": convert_and_respect_annotation_metadata(
                    object_=align, annotation=Alignment, direction="write"
                ),
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Sequence[SeriesSpec], direction="write"
                ),
                "render": convert_and_respect_annotation_metadata(object_=render, annotation=Render, direction="write"),
                "lookback": lookback,
            },
            headers={
                "content-type": "application/json",
                "accept": str(accept) if accept is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryResult,
                    parse_obj_as(
                        type_=QueryResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def by_name(
        self,
        query_name: str,
        *,
        resource: typing.Optional[str] = None,
        metric: typing.Optional[str] = None,
        aggregation: typing.Optional[str] = None,
        interpolation: typing.Optional[InterpolationMethod] = None,
        freq: typing.Optional[str] = None,
        from_: typing.Optional[str] = None,
        until: typing.Optional[str] = None,
        window: typing.Optional[str] = None,
        periods: typing.Optional[int] = None,
        render: typing.Optional[RenderMode] = None,
        accept: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[QueryResult]:
        """
        Execute a named timeseries query.

        Retrieves a stored query definition by name,
        applies overrides from the url parameters, and executes it.

        Parameters
        ----------
        query_name : str

        resource : typing.Optional[str]
            Default Resource Override.

        metric : typing.Optional[str]
            Default Metric Override.

        aggregation : typing.Optional[str]

        interpolation : typing.Optional[InterpolationMethod]

        freq : typing.Optional[str]
            Override for the `freq` query attribute.

        from_ : typing.Optional[str]

        until : typing.Optional[str]

        window : typing.Optional[str]

        periods : typing.Optional[int]

        render : typing.Optional[RenderMode]

        accept : typing.Optional[str]
            Use a 'text/csv' accept header to get CSV formatted results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"queries/v1/data/{encode_path_param(query_name)}",
            method="GET",
            params={
                "resource": resource,
                "metric": metric,
                "aggregation": aggregation,
                "interpolation": interpolation,
                "freq": freq,
                "from": from_,
                "until": until,
                "window": window,
                "periods": periods,
                "render": render,
            },
            headers={
                "accept": str(accept) if accept is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryResult,
                    parse_obj_as(
                        type_=QueryResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
