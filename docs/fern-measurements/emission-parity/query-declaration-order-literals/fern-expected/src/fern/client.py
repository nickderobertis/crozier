

import typing

import httpx
from . import core
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.logbook_entry import LogbookEntry
from .types.reading import Reading


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

    def list_readings(
        self,
        lamp_id: str,
        *,
        unit: str,
        shift: str,
        since: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Reading]:
        """
        Parameters
        ----------
        lamp_id : str

        unit : str
            Unit the readings are reported in.

        shift : str

        since : typing.Optional[str]
            Earliest reading to include.

        page : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Reading]
            The readings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_readings(
            lamp_id="north-tower",
            since="2024-03-01",
            unit="lumen",
            limit=25,
            shift="shift",
        )
        """
        _response = self._raw_client.list_readings(
            lamp_id, unit=unit, shift=shift, since=since, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    def write_logbook(
        self,
        lamp_id: str,
        *,
        tide: str,
        keeper_id: str,
        text: str,
        draft: typing.Optional[bool] = None,
        watch_note: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogbookEntry:
        """
        Parameters
        ----------
        lamp_id : str

        tide : str

        keeper_id : str

        text : str

        draft : typing.Optional[bool]

        watch_note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogbookEntry
            Written

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.write_logbook(
            lamp_id="north-tower",
            watch_note="calm seas",
            keeper_id="keeper-7",
            draft=True,
            tide="high",
            text="Fog rolled in at six.",
        )
        """
        _response = self._raw_client.write_logbook(
            lamp_id,
            tide=tide,
            keeper_id=keeper_id,
            text=text,
            draft=draft,
            watch_note=watch_note,
            request_options=request_options,
        )
        return _response.data

    def upload_photo(
        self,
        lamp_id: str,
        *,
        album: str,
        photo: core.File,
        caption: typing.Optional[str] = None,
        camera: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        lamp_id : str

        album : str

        photo : core.File
            See core.File for more documentation

        caption : typing.Optional[str]

        camera : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.upload_photo(
            lamp_id="lampId",
            camera="brass-lens",
            caption="dusk",
            album="winter",
        )
        """
        _response = self._raw_client.upload_photo(
            lamp_id, album=album, photo=photo, caption=caption, camera=camera, request_options=request_options
        )
        return _response.data

    def list_lamps(
        self, *, region: str, lit: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        region : str

        lit : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The lamps

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_lamps(
            region="coast",
            lit=False,
        )
        """
        _response = self._raw_client.list_lamps(region=region, lit=lit, request_options=request_options)
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

    async def list_readings(
        self,
        lamp_id: str,
        *,
        unit: str,
        shift: str,
        since: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Reading]:
        """
        Parameters
        ----------
        lamp_id : str

        unit : str
            Unit the readings are reported in.

        shift : str

        since : typing.Optional[str]
            Earliest reading to include.

        page : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Reading]
            The readings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_readings(
                lamp_id="north-tower",
                since="2024-03-01",
                unit="lumen",
                limit=25,
                shift="shift",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_readings(
            lamp_id, unit=unit, shift=shift, since=since, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    async def write_logbook(
        self,
        lamp_id: str,
        *,
        tide: str,
        keeper_id: str,
        text: str,
        draft: typing.Optional[bool] = None,
        watch_note: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LogbookEntry:
        """
        Parameters
        ----------
        lamp_id : str

        tide : str

        keeper_id : str

        text : str

        draft : typing.Optional[bool]

        watch_note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LogbookEntry
            Written

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.write_logbook(
                lamp_id="north-tower",
                watch_note="calm seas",
                keeper_id="keeper-7",
                draft=True,
                tide="high",
                text="Fog rolled in at six.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.write_logbook(
            lamp_id,
            tide=tide,
            keeper_id=keeper_id,
            text=text,
            draft=draft,
            watch_note=watch_note,
            request_options=request_options,
        )
        return _response.data

    async def upload_photo(
        self,
        lamp_id: str,
        *,
        album: str,
        photo: core.File,
        caption: typing.Optional[str] = None,
        camera: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        lamp_id : str

        album : str

        photo : core.File
            See core.File for more documentation

        caption : typing.Optional[str]

        camera : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.upload_photo(
                lamp_id="lampId",
                camera="brass-lens",
                caption="dusk",
                album="winter",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_photo(
            lamp_id, album=album, photo=photo, caption=caption, camera=camera, request_options=request_options
        )
        return _response.data

    async def list_lamps(
        self, *, region: str, lit: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        region : str

        lit : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The lamps

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_lamps(
                region="coast",
                lit=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_lamps(region=region, lit=lit, request_options=request_options)
        return _response.data
