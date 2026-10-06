

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.bridge_status import BridgeStatus
from .types.delete_recording_result import DeleteRecordingResult
from .types.download_ticket import DownloadTicket
from .types.recording_capabilities import RecordingCapabilities
from .types.recording_list import RecordingList
from .types.recording_result import RecordingResult
from .types.transport_key_delete_result import TransportKeyDeleteResult
from .types.transport_key_result import TransportKeyResult
from .types.transport_mode_request_mode import TransportModeRequestMode
from .types.transport_snapshot import TransportSnapshot
from .types.unlock_result import UnlockResult


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            token=token,
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

    def get_recordings(self, *, request_options: typing.Optional[RequestOptions] = None) -> RecordingList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordingList
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_recordings()
        """
        _response = self._raw_client.get_recordings(request_options=request_options)
        return _response.data

    def start_recording(
        self, *, source: str, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordingResult:
        """
        Parameters
        ----------
        source : str

        title : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordingResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.start_recording(
            source="source",
            title="title",
        )
        """
        _response = self._raw_client.start_recording(source=source, title=title, request_options=request_options)
        return _response.data

    def get_recording_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordingCapabilities:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordingCapabilities
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_recording_capabilities()
        """
        _response = self._raw_client.get_recording_capabilities(request_options=request_options)
        return _response.data

    def delete_recording(
        self, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteRecordingResult:
        """
        Parameters
        ----------
        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRecordingResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_recording(
            recording_id="recording_id",
        )
        """
        _response = self._raw_client.delete_recording(recording_id, request_options=request_options)
        return _response.data

    def create_recording_download_ticket(
        self, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DownloadTicket:
        """
        Parameters
        ----------
        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DownloadTicket
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_recording_download_ticket(
            recording_id="recording_id",
        )
        """
        _response = self._raw_client.create_recording_download_ticket(recording_id, request_options=request_options)
        return _response.data

    def download_recording(
        self, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.download_recording(
            recording_id="recording_id",
        )
        """
        with self._raw_client.download_recording(recording_id, request_options=request_options) as r:
            yield from r.data

    def stop_recording(
        self, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordingResult:
        """
        Parameters
        ----------
        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordingResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.stop_recording(
            recording_id="recording_id",
        )
        """
        _response = self._raw_client.stop_recording(recording_id, request_options=request_options)
        return _response.data

    def get_transport(self, *, request_options: typing.Optional[RequestOptions] = None) -> TransportSnapshot:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransportSnapshot
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_transport()
        """
        _response = self._raw_client.get_transport(request_options=request_options)
        return _response.data

    def put_transport_key(
        self, key_id: str, *, psk: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TransportKeyResult:
        """
        Parameters
        ----------
        key_id : str

        psk : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransportKeyResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.put_transport_key(
            key_id="key_id",
            psk="psk",
        )
        """
        _response = self._raw_client.put_transport_key(key_id, psk=psk, request_options=request_options)
        return _response.data

    def delete_transport_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransportKeyDeleteResult:
        """
        Parameters
        ----------
        key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransportKeyDeleteResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_transport_key(
            key_id="key_id",
        )
        """
        _response = self._raw_client.delete_transport_key(key_id, request_options=request_options)
        return _response.data

    def set_transport_mode(
        self, *, mode: TransportModeRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> TransportSnapshot:
        """
        Parameters
        ----------
        mode : TransportModeRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransportSnapshot
            Successful Response

        Examples
        --------
        from fern import FernApi, TransportModeRequestMode

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.set_transport_mode(
            mode=TransportModeRequestMode.CLEARTEXT,
        )
        """
        _response = self._raw_client.set_transport_mode(mode=mode, request_options=request_options)
        return _response.data

    def unlock_bridge(self, *, request_options: typing.Optional[RequestOptions] = None) -> UnlockResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnlockResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.unlock_bridge()
        """
        _response = self._raw_client.unlock_bridge(request_options=request_options)
        return _response.data

    def get_bridge_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_bridge_health()
        """
        _response = self._raw_client.get_bridge_health(request_options=request_options)
        return _response.data

    def get_bridge_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> BridgeStatus:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BridgeStatus
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_bridge_status()
        """
        _response = self._raw_client.get_bridge_status(request_options=request_options)
        return _response.data

    def stream_wav(
        self, *, source: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        source : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.stream_wav()
        """
        with self._raw_client.stream_wav(source=source, request_options=request_options) as r:
            yield from r.data


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

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

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
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
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
            token=token,
            headers=headers,
            async_token=async_token,
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

    async def get_recordings(self, *, request_options: typing.Optional[RequestOptions] = None) -> RecordingList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordingList
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_recordings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_recordings(request_options=request_options)
        return _response.data

    async def start_recording(
        self, *, source: str, title: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordingResult:
        """
        Parameters
        ----------
        source : str

        title : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordingResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.start_recording(
                source="source",
                title="title",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_recording(source=source, title=title, request_options=request_options)
        return _response.data

    async def get_recording_capabilities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordingCapabilities:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordingCapabilities
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_recording_capabilities()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_recording_capabilities(request_options=request_options)
        return _response.data

    async def delete_recording(
        self, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteRecordingResult:
        """
        Parameters
        ----------
        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRecordingResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_recording(
                recording_id="recording_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_recording(recording_id, request_options=request_options)
        return _response.data

    async def create_recording_download_ticket(
        self, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DownloadTicket:
        """
        Parameters
        ----------
        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DownloadTicket
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_recording_download_ticket(
                recording_id="recording_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_recording_download_ticket(
            recording_id, request_options=request_options
        )
        return _response.data

    async def download_recording(
        self, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.download_recording(
                recording_id="recording_id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.download_recording(recording_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def stop_recording(
        self, recording_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordingResult:
        """
        Parameters
        ----------
        recording_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordingResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stop_recording(
                recording_id="recording_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_recording(recording_id, request_options=request_options)
        return _response.data

    async def get_transport(self, *, request_options: typing.Optional[RequestOptions] = None) -> TransportSnapshot:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransportSnapshot
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_transport()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_transport(request_options=request_options)
        return _response.data

    async def put_transport_key(
        self, key_id: str, *, psk: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TransportKeyResult:
        """
        Parameters
        ----------
        key_id : str

        psk : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransportKeyResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.put_transport_key(
                key_id="key_id",
                psk="psk",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_transport_key(key_id, psk=psk, request_options=request_options)
        return _response.data

    async def delete_transport_key(
        self, key_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TransportKeyDeleteResult:
        """
        Parameters
        ----------
        key_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransportKeyDeleteResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_transport_key(
                key_id="key_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_transport_key(key_id, request_options=request_options)
        return _response.data

    async def set_transport_mode(
        self, *, mode: TransportModeRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> TransportSnapshot:
        """
        Parameters
        ----------
        mode : TransportModeRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransportSnapshot
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TransportModeRequestMode

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.set_transport_mode(
                mode=TransportModeRequestMode.CLEARTEXT,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_transport_mode(mode=mode, request_options=request_options)
        return _response.data

    async def unlock_bridge(self, *, request_options: typing.Optional[RequestOptions] = None) -> UnlockResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnlockResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.unlock_bridge()


        asyncio.run(main())
        """
        _response = await self._raw_client.unlock_bridge(request_options=request_options)
        return _response.data

    async def get_bridge_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_bridge_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bridge_health(request_options=request_options)
        return _response.data

    async def get_bridge_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> BridgeStatus:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BridgeStatus
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_bridge_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bridge_status(request_options=request_options)
        return _response.data

    async def stream_wav(
        self, *, source: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        source : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stream_wav()


        asyncio.run(main())
        """
        async with self._raw_client.stream_wav(source=source, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
