

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alignment import Alignment
from ..types.interpolation_method import InterpolationMethod
from ..types.query_input_aggregation import QueryInputAggregation
from ..types.query_input_from import QueryInputFrom
from ..types.query_input_interpolation import QueryInputInterpolation
from ..types.query_input_until import QueryInputUntil
from ..types.query_result import QueryResult
from ..types.render import Render
from ..types.render_mode import RenderMode
from ..types.series_spec import SeriesSpec
from .raw_client import AsyncRawExecuteClient, RawExecuteClient


OMIT = typing.cast(typing.Any, ...)


class ExecuteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExecuteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExecuteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExecuteClient
        """
        return self._raw_client

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
    ) -> QueryResult:
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
        QueryResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.execute.execute_query(
            resource="13efb488-75ac-4dac-828a-d49c5c2ebbfc",
            metric="temperature",
        )
        """
        _response = self._raw_client.execute_query(
            resource=resource,
            metric=metric,
            aggregation=aggregation,
            interpolation=interpolation,
            freq=freq,
            from_=from_,
            until=until,
            window=window,
            periods=periods,
            render=render,
            accept=accept,
            query_input_resource=query_input_resource,
            query_input_metric=query_input_metric,
            query_input_aggregation=query_input_aggregation,
            query_input_interpolation=query_input_interpolation,
            query_input_freq=query_input_freq,
            query_input_from_=query_input_from_,
            query_input_until=query_input_until,
            query_input_window=query_input_window,
            query_input_periods=query_input_periods,
            align=align,
            data=data,
            query_input_render=query_input_render,
            lookback=lookback,
            request_options=request_options,
        )
        return _response.data

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
    ) -> QueryResult:
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
        QueryResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.execute.by_name(
            query_name="query_name",
            resource="13efb488-75ac-4dac-828a-d49c5c2ebbfc",
            metric="temperature",
        )
        """
        _response = self._raw_client.by_name(
            query_name,
            resource=resource,
            metric=metric,
            aggregation=aggregation,
            interpolation=interpolation,
            freq=freq,
            from_=from_,
            until=until,
            window=window,
            periods=periods,
            render=render,
            accept=accept,
            request_options=request_options,
        )
        return _response.data


class AsyncExecuteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExecuteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExecuteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExecuteClient
        """
        return self._raw_client

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
    ) -> QueryResult:
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
        QueryResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.execute.execute_query(
                resource="13efb488-75ac-4dac-828a-d49c5c2ebbfc",
                metric="temperature",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_query(
            resource=resource,
            metric=metric,
            aggregation=aggregation,
            interpolation=interpolation,
            freq=freq,
            from_=from_,
            until=until,
            window=window,
            periods=periods,
            render=render,
            accept=accept,
            query_input_resource=query_input_resource,
            query_input_metric=query_input_metric,
            query_input_aggregation=query_input_aggregation,
            query_input_interpolation=query_input_interpolation,
            query_input_freq=query_input_freq,
            query_input_from_=query_input_from_,
            query_input_until=query_input_until,
            query_input_window=query_input_window,
            query_input_periods=query_input_periods,
            align=align,
            data=data,
            query_input_render=query_input_render,
            lookback=lookback,
            request_options=request_options,
        )
        return _response.data

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
    ) -> QueryResult:
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
        QueryResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.execute.by_name(
                query_name="query_name",
                resource="13efb488-75ac-4dac-828a-d49c5c2ebbfc",
                metric="temperature",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.by_name(
            query_name,
            resource=resource,
            metric=metric,
            aggregation=aggregation,
            interpolation=interpolation,
            freq=freq,
            from_=from_,
            until=until,
            window=window,
            periods=periods,
            render=render,
            accept=accept,
            request_options=request_options,
        )
        return _response.data
