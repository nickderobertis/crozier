

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.get_full_text_search_response import GetFullTextSearchResponse
from .types.post_faceted_search_facet_class_facet_id_response import PostFacetedSearchFacetClassFacetIdResponse
from .types.post_faceted_search_result_class_count_response import PostFacetedSearchResultClassCountResponse
from .types.post_faceted_search_result_class_paginated_response import PostFacetedSearchResultClassPaginatedResponse
from .types.post_result_class_page_uri_response import PostResultClassPageUriResponse


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def return_faceted_search_results_with_pagination(
        self,
        result_class: str,
        *,
        page: typing.Optional[int] = OMIT,
        pagesize: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[str] = OMIT,
        sort_direction: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostFacetedSearchResultClassPaginatedResponse:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        page : typing.Optional[int]

        pagesize : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostFacetedSearchResultClassPaginatedResponse
            Paginated search results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.return_faceted_search_results_with_pagination(
            result_class="perspective1",
        )
        """
        _response = self._raw_client.return_faceted_search_results_with_pagination(
            result_class,
            page=page,
            pagesize=pagesize,
            sort_by=sort_by,
            sort_direction=sort_direction,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    def return_all_search_results_as_a_csv_file(
        self,
        result_class: str,
        *,
        facet_class: str,
        result_format: str,
        constraints: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        facet_class : str
            The class for facet configs

        result_format : str
            Result format, only support for CSV for now.

        constraints : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            All search results as a CSV file
        """
        with self._raw_client.return_all_search_results_as_a_csv_file(
            result_class,
            facet_class=facet_class,
            result_format=result_format,
            constraints=constraints,
            request_options=request_options,
        ) as r:
            yield from r.data

    def return_all_search_results(
        self,
        result_class: str,
        *,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            All search results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.return_all_search_results(
            result_class="placesMsProduced",
        )
        """
        _response = self._raw_client.return_all_search_results(
            result_class, constraints=constraints, request_options=request_options
        )
        return _response.data

    def return_the_total_count_of_the_faceted_search_results(
        self,
        result_class: str,
        *,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostFacetedSearchResultClassCountResponse:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostFacetedSearchResultClassCountResponse
            The total count of the faceted search results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.return_the_total_count_of_the_faceted_search_results(
            result_class="perspective1",
        )
        """
        _response = self._raw_client.return_the_total_count_of_the_faceted_search_results(
            result_class, constraints=constraints, request_options=request_options
        )
        return _response.data

    def return_values_for_a_single_facet(
        self,
        facet_class: str,
        id: str,
        *,
        sort_by: typing.Optional[str] = OMIT,
        sort_direction: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        constrain_self: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostFacetedSearchFacetClassFacetIdResponse:
        """
        Parameters
        ----------
        facet_class : str
            The class of the facet

        id : str
            The id of the facet

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        constrain_self : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostFacetedSearchFacetClassFacetIdResponse
            Facet values

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.return_values_for_a_single_facet(
            facet_class="perspective1",
            id="language",
        )
        """
        _response = self._raw_client.return_values_for_a_single_facet(
            facet_class,
            id,
            sort_by=sort_by,
            sort_direction=sort_direction,
            constraints=constraints,
            constrain_self=constrain_self,
            request_options=request_options,
        )
        return _response.data

    def return_information_about_a_single_resource_optionally_applying_facet_filters(
        self,
        result_class: str,
        uri: str,
        *,
        facet_class: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostResultClassPageUriResponse:
        """
        Parameters
        ----------
        result_class : str
            The class of the resource

        uri : str
            The URI of the resource

        facet_class : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostResultClassPageUriResponse
            Information about a single resource

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.return_information_about_a_single_resource_optionally_applying_facet_filters(
            result_class="perspective1",
            uri="http://ldf.fi/mmm/manifestation_singleton/bibale_10003",
        )
        """
        _response = self._raw_client.return_information_about_a_single_resource_optionally_applying_facet_filters(
            result_class, uri, facet_class=facet_class, constraints=constraints, request_options=request_options
        )
        return _response.data

    def full_text_search(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFullTextSearchResponse:
        """
        Parameters
        ----------
        q : str
            The query string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFullTextSearchResponse
            Full text search results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.full_text_search(
            q="q",
        )
        """
        _response = self._raw_client.full_text_search(q=q, request_options=request_options)
        return _response.data

    def federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search(
        self,
        *,
        perspective_id: str,
        dataset: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        q: typing.Optional[str] = None,
        lat_min: typing.Optional[float] = None,
        long_min: typing.Optional[float] = None,
        lat_max: typing.Optional[float] = None,
        long_max: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        perspective_id : str

        dataset : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        q : typing.Optional[str]
            The query string

        lat_min : typing.Optional[float]

        long_min : typing.Optional[float]

        lat_max : typing.Optional[float]

        long_max : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Federated search results

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search(
            perspective_id="perspectiveID",
            dataset=["dataset"],
        )
        """
        _response = self._raw_client.federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search(
            perspective_id=perspective_id,
            dataset=dataset,
            q=q,
            lat_min=lat_min,
            long_min=long_min,
            lat_max=lat_max,
            long_max=long_max,
            request_options=request_options,
        )
        return _response.data

    def make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend(
        self,
        *,
        layer_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        layer_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            An array of GeoJSON layers.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend(
            layer_id=["layerID"],
        )
        """
        _response = self._raw_client.make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend(
            layer_id=layer_id, request_options=request_options
        )
        return _response.data

    def route_for_password_protected_wms_layers(
        self,
        *,
        service: str,
        request: str,
        layers: str,
        styles: str,
        format: str,
        transparent: bool,
        version: str,
        width: float,
        height: float,
        crs: str,
        bbox: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        service : str

        request : str

        layers : str

        styles : str

        format : str

        transparent : bool

        version : str

        width : float

        height : float

        crs : str

        bbox : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Image
        """
        with self._raw_client.route_for_password_protected_wms_layers(
            service=service,
            request=request,
            layers=layers,
            styles=styles,
            format=format,
            transparent=transparent,
            version=version,
            width=width,
            height=height,
            crs=crs,
            bbox=bbox,
            request_options=request_options,
        ) as r:
            yield from r.data

    def route_for_nls_wmts_api_only_for_contract_customers(
        self, *, layer_id: str, x: str, y: str, z: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        layer_id : str

        x : str

        y : str

        z : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            An array of GeoJSON layers.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.route_for_nls_wmts_api_only_for_contract_customers(
            layer_id="layerID",
            x="x",
            y="y",
            z="z",
        )
        """
        _response = self._raw_client.route_for_nls_wmts_api_only_for_contract_customers(
            layer_id=layer_id, x=x, y=y, z=z, request_options=request_options
        )
        return _response.data

    def route_for_nls_wmts_api_free_but_requires_an_api_key(
        self, *, layer_id: str, x: str, y: str, z: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        layer_id : str

        x : str

        y : str

        z : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            An array of GeoJSON layers.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.route_for_nls_wmts_api_free_but_requires_an_api_key(
            layer_id="layerID",
            x="x",
            y="y",
            z="z",
        )
        """
        _response = self._raw_client.route_for_nls_wmts_api_free_but_requires_an_api_key(
            layer_id=layer_id, x=x, y=y, z=z, request_options=request_options
        )
        return _response.data

    def route_for_nls_vectortiles_api_free_but_requires_an_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Styles for vector tiles as JSON

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.route_for_nls_vectortiles_api_free_but_requires_an_api_key()
        """
        _response = self._raw_client.route_for_nls_vectortiles_api_free_but_requires_an_api_key(
            request_options=request_options
        )
        return _response.data

    def retrieve_a_vo_id_description(
        self, perspective_id: str, result_class: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        perspective_id : str

        result_class : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            VoID description as JSON.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.retrieve_a_vo_id_description(
            perspective_id="perspective1",
            result_class="perspective1KnowledgeGraphMetadata",
        )
        """
        _response = self._raw_client.retrieve_a_vo_id_description(
            perspective_id, result_class, request_options=request_options
        )
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def return_faceted_search_results_with_pagination(
        self,
        result_class: str,
        *,
        page: typing.Optional[int] = OMIT,
        pagesize: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[str] = OMIT,
        sort_direction: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostFacetedSearchResultClassPaginatedResponse:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        page : typing.Optional[int]

        pagesize : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostFacetedSearchResultClassPaginatedResponse
            Paginated search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.return_faceted_search_results_with_pagination(
                result_class="perspective1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_faceted_search_results_with_pagination(
            result_class,
            page=page,
            pagesize=pagesize,
            sort_by=sort_by,
            sort_direction=sort_direction,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    async def return_all_search_results_as_a_csv_file(
        self,
        result_class: str,
        *,
        facet_class: str,
        result_format: str,
        constraints: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        facet_class : str
            The class for facet configs

        result_format : str
            Result format, only support for CSV for now.

        constraints : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            All search results as a CSV file
        """
        async with self._raw_client.return_all_search_results_as_a_csv_file(
            result_class,
            facet_class=facet_class,
            result_format=result_format,
            constraints=constraints,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def return_all_search_results(
        self,
        result_class: str,
        *,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            All search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.return_all_search_results(
                result_class="placesMsProduced",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_all_search_results(
            result_class, constraints=constraints, request_options=request_options
        )
        return _response.data

    async def return_the_total_count_of_the_faceted_search_results(
        self,
        result_class: str,
        *,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostFacetedSearchResultClassCountResponse:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostFacetedSearchResultClassCountResponse
            The total count of the faceted search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.return_the_total_count_of_the_faceted_search_results(
                result_class="perspective1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_the_total_count_of_the_faceted_search_results(
            result_class, constraints=constraints, request_options=request_options
        )
        return _response.data

    async def return_values_for_a_single_facet(
        self,
        facet_class: str,
        id: str,
        *,
        sort_by: typing.Optional[str] = OMIT,
        sort_direction: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        constrain_self: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostFacetedSearchFacetClassFacetIdResponse:
        """
        Parameters
        ----------
        facet_class : str
            The class of the facet

        id : str
            The id of the facet

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        constrain_self : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostFacetedSearchFacetClassFacetIdResponse
            Facet values

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.return_values_for_a_single_facet(
                facet_class="perspective1",
                id="language",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_values_for_a_single_facet(
            facet_class,
            id,
            sort_by=sort_by,
            sort_direction=sort_direction,
            constraints=constraints,
            constrain_self=constrain_self,
            request_options=request_options,
        )
        return _response.data

    async def return_information_about_a_single_resource_optionally_applying_facet_filters(
        self,
        result_class: str,
        uri: str,
        *,
        facet_class: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostResultClassPageUriResponse:
        """
        Parameters
        ----------
        result_class : str
            The class of the resource

        uri : str
            The URI of the resource

        facet_class : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostResultClassPageUriResponse
            Information about a single resource

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.return_information_about_a_single_resource_optionally_applying_facet_filters(
                result_class="perspective1",
                uri="http://ldf.fi/mmm/manifestation_singleton/bibale_10003",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_information_about_a_single_resource_optionally_applying_facet_filters(
            result_class, uri, facet_class=facet_class, constraints=constraints, request_options=request_options
        )
        return _response.data

    async def full_text_search(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetFullTextSearchResponse:
        """
        Parameters
        ----------
        q : str
            The query string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFullTextSearchResponse
            Full text search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.full_text_search(
                q="q",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.full_text_search(q=q, request_options=request_options)
        return _response.data

    async def federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search(
        self,
        *,
        perspective_id: str,
        dataset: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        q: typing.Optional[str] = None,
        lat_min: typing.Optional[float] = None,
        long_min: typing.Optional[float] = None,
        lat_max: typing.Optional[float] = None,
        long_max: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        perspective_id : str

        dataset : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        q : typing.Optional[str]
            The query string

        lat_min : typing.Optional[float]

        long_min : typing.Optional[float]

        lat_max : typing.Optional[float]

        long_max : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Federated search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search(
                perspective_id="perspectiveID",
                dataset=["dataset"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search(
            perspective_id=perspective_id,
            dataset=dataset,
            q=q,
            lat_min=lat_min,
            long_min=long_min,
            lat_max=lat_max,
            long_max=long_max,
            request_options=request_options,
        )
        return _response.data

    async def make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend(
        self,
        *,
        layer_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        layer_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            An array of GeoJSON layers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend(
                layer_id=["layerID"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend(
            layer_id=layer_id, request_options=request_options
        )
        return _response.data

    async def route_for_password_protected_wms_layers(
        self,
        *,
        service: str,
        request: str,
        layers: str,
        styles: str,
        format: str,
        transparent: bool,
        version: str,
        width: float,
        height: float,
        crs: str,
        bbox: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        service : str

        request : str

        layers : str

        styles : str

        format : str

        transparent : bool

        version : str

        width : float

        height : float

        crs : str

        bbox : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Image
        """
        async with self._raw_client.route_for_password_protected_wms_layers(
            service=service,
            request=request,
            layers=layers,
            styles=styles,
            format=format,
            transparent=transparent,
            version=version,
            width=width,
            height=height,
            crs=crs,
            bbox=bbox,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def route_for_nls_wmts_api_only_for_contract_customers(
        self, *, layer_id: str, x: str, y: str, z: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        layer_id : str

        x : str

        y : str

        z : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            An array of GeoJSON layers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.route_for_nls_wmts_api_only_for_contract_customers(
                layer_id="layerID",
                x="x",
                y="y",
                z="z",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route_for_nls_wmts_api_only_for_contract_customers(
            layer_id=layer_id, x=x, y=y, z=z, request_options=request_options
        )
        return _response.data

    async def route_for_nls_wmts_api_free_but_requires_an_api_key(
        self, *, layer_id: str, x: str, y: str, z: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        layer_id : str

        x : str

        y : str

        z : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            An array of GeoJSON layers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.route_for_nls_wmts_api_free_but_requires_an_api_key(
                layer_id="layerID",
                x="x",
                y="y",
                z="z",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route_for_nls_wmts_api_free_but_requires_an_api_key(
            layer_id=layer_id, x=x, y=y, z=z, request_options=request_options
        )
        return _response.data

    async def route_for_nls_vectortiles_api_free_but_requires_an_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Styles for vector tiles as JSON

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.route_for_nls_vectortiles_api_free_but_requires_an_api_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.route_for_nls_vectortiles_api_free_but_requires_an_api_key(
            request_options=request_options
        )
        return _response.data

    async def retrieve_a_vo_id_description(
        self, perspective_id: str, result_class: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        perspective_id : str

        result_class : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            VoID description as JSON.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.retrieve_a_vo_id_description(
                perspective_id="perspective1",
                result_class="perspective1KnowledgeGraphMetadata",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_vo_id_description(
            perspective_id, result_class, request_options=request_options
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
