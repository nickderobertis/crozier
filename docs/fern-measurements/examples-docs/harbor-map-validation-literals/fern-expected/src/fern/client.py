

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.closed_accepted_plan import ClosedAcceptedPlan
from .types.closed_rejected_plan import ClosedRejectedPlan
from .types.map_accepted_plan import MapAcceptedPlan
from .types.map_rejected_plan import MapRejectedPlan
from .types.null_allowed_plan import NullAllowedPlan
from .types.null_disallowed_plan import NullDisallowedPlan


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

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

    client = FernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
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

    def record_map_accepted(
        self, *, plan: MapAcceptedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : MapAcceptedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            FernApi,
            MapAcceptedChoiceWindow,
            MapAcceptedChoiceWindowWindow,
            MapAcceptedPlan,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.record_map_accepted(
            plan=MapAcceptedPlan(
                choice=MapAcceptedChoiceWindow(
                    window=MapAcceptedChoiceWindowWindow(
                        lookback={"days": 20},
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.record_map_accepted(plan=plan, request_options=request_options)
        return _response.data

    def record_map_rejected(
        self, *, plan: MapRejectedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : MapRejectedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            FernApi,
            MapRejectedChoiceWindow,
            MapRejectedChoiceWindowWindow,
            MapRejectedPlan,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.record_map_rejected(
            plan=MapRejectedPlan(
                choice=MapRejectedChoiceWindow(
                    window=MapRejectedChoiceWindowWindow(
                        lookback={"days": 20},
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.record_map_rejected(plan=plan, request_options=request_options)
        return _response.data

    def record_closed_accepted(
        self, *, plan: ClosedAcceptedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : ClosedAcceptedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            ClosedAcceptedChoiceWindow,
            ClosedAcceptedChoiceWindowWindow,
            ClosedAcceptedChoiceWindowWindowLookback,
            ClosedAcceptedPlan,
            FernApi,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.record_closed_accepted(
            plan=ClosedAcceptedPlan(
                choice=ClosedAcceptedChoiceWindow(
                    window=ClosedAcceptedChoiceWindowWindow(
                        lookback=ClosedAcceptedChoiceWindowWindowLookback(
                            days=20,
                        ),
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.record_closed_accepted(plan=plan, request_options=request_options)
        return _response.data

    def record_closed_rejected(
        self, *, plan: ClosedRejectedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : ClosedRejectedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            ClosedRejectedChoiceWindow,
            ClosedRejectedChoiceWindowWindow,
            ClosedRejectedChoiceWindowWindowLookback,
            ClosedRejectedPlan,
            FernApi,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.record_closed_rejected(
            plan=ClosedRejectedPlan(
                choice=ClosedRejectedChoiceWindow(
                    window=ClosedRejectedChoiceWindowWindow(
                        lookback=ClosedRejectedChoiceWindowWindowLookback(
                            days=20,
                        ),
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.record_closed_rejected(plan=plan, request_options=request_options)
        return _response.data

    def record_null_allowed(
        self, *, plan: NullAllowedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : NullAllowedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            FernApi,
            NullAllowedChoiceWindow,
            NullAllowedChoiceWindowWindow,
            NullAllowedPlan,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.record_null_allowed(
            plan=NullAllowedPlan(
                choice=NullAllowedChoiceWindow(
                    window=NullAllowedChoiceWindowWindow(
                        lookback=20,
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.record_null_allowed(plan=plan, request_options=request_options)
        return _response.data

    def record_null_disallowed(
        self, *, plan: NullDisallowedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : NullDisallowedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import (
            FernApi,
            NullDisallowedChoiceWindow,
            NullDisallowedChoiceWindowWindow,
            NullDisallowedPlan,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.record_null_disallowed(
            plan=NullDisallowedPlan(
                choice=NullDisallowedChoiceWindow(
                    window=NullDisallowedChoiceWindowWindow(
                        lookback=20,
                    ),
                ),
            ),
        )
        """
        _response = self._raw_client.record_null_disallowed(plan=plan, request_options=request_options)
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
    base_url : str
        The base url to use for requests from the client.

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

    client = AsyncFernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
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

    async def record_map_accepted(
        self, *, plan: MapAcceptedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : MapAcceptedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            MapAcceptedChoiceWindow,
            MapAcceptedChoiceWindowWindow,
            MapAcceptedPlan,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.record_map_accepted(
                plan=MapAcceptedPlan(
                    choice=MapAcceptedChoiceWindow(
                        window=MapAcceptedChoiceWindowWindow(
                            lookback={"days": 20},
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_map_accepted(plan=plan, request_options=request_options)
        return _response.data

    async def record_map_rejected(
        self, *, plan: MapRejectedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : MapRejectedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            MapRejectedChoiceWindow,
            MapRejectedChoiceWindowWindow,
            MapRejectedPlan,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.record_map_rejected(
                plan=MapRejectedPlan(
                    choice=MapRejectedChoiceWindow(
                        window=MapRejectedChoiceWindowWindow(
                            lookback={"days": 20},
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_map_rejected(plan=plan, request_options=request_options)
        return _response.data

    async def record_closed_accepted(
        self, *, plan: ClosedAcceptedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : ClosedAcceptedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ClosedAcceptedChoiceWindow,
            ClosedAcceptedChoiceWindowWindow,
            ClosedAcceptedChoiceWindowWindowLookback,
            ClosedAcceptedPlan,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.record_closed_accepted(
                plan=ClosedAcceptedPlan(
                    choice=ClosedAcceptedChoiceWindow(
                        window=ClosedAcceptedChoiceWindowWindow(
                            lookback=ClosedAcceptedChoiceWindowWindowLookback(
                                days=20,
                            ),
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_closed_accepted(plan=plan, request_options=request_options)
        return _response.data

    async def record_closed_rejected(
        self, *, plan: ClosedRejectedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : ClosedRejectedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ClosedRejectedChoiceWindow,
            ClosedRejectedChoiceWindowWindow,
            ClosedRejectedChoiceWindowWindowLookback,
            ClosedRejectedPlan,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.record_closed_rejected(
                plan=ClosedRejectedPlan(
                    choice=ClosedRejectedChoiceWindow(
                        window=ClosedRejectedChoiceWindowWindow(
                            lookback=ClosedRejectedChoiceWindowWindowLookback(
                                days=20,
                            ),
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_closed_rejected(plan=plan, request_options=request_options)
        return _response.data

    async def record_null_allowed(
        self, *, plan: NullAllowedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : NullAllowedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            NullAllowedChoiceWindow,
            NullAllowedChoiceWindowWindow,
            NullAllowedPlan,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.record_null_allowed(
                plan=NullAllowedPlan(
                    choice=NullAllowedChoiceWindow(
                        window=NullAllowedChoiceWindowWindow(
                            lookback=20,
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_null_allowed(plan=plan, request_options=request_options)
        return _response.data

    async def record_null_disallowed(
        self, *, plan: NullDisallowedPlan, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        plan : NullDisallowedPlan

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            NullDisallowedChoiceWindow,
            NullDisallowedChoiceWindowWindow,
            NullDisallowedPlan,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.record_null_disallowed(
                plan=NullDisallowedPlan(
                    choice=NullDisallowedChoiceWindow(
                        window=NullDisallowedChoiceWindowWindow(
                            lookback=20,
                        ),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_null_disallowed(plan=plan, request_options=request_options)
        return _response.data
