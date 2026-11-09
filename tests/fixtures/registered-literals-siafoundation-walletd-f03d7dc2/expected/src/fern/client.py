

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .addresses.client import AddressesClient, AsyncAddressesClient
    from .batch.client import AsyncBatchClient, BatchClient
    from .consensus.client import AsyncConsensusClient, ConsensusClient
    from .debug.client import AsyncDebugClient, DebugClient
    from .events.client import AsyncEventsClient, EventsClient
    from .misc.client import AsyncMiscClient, MiscClient
    from .outputs.client import AsyncOutputsClient, OutputsClient
    from .rescan.client import AsyncRescanClient, RescanClient
    from .syncer.client import AsyncSyncerClient, SyncerClient
    from .txpool.client import AsyncTxpoolClient, TxpoolClient
    from .wallets.client import AsyncWalletsClient, WalletsClient


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
        self._misc: typing.Optional[MiscClient] = None
        self._consensus: typing.Optional[ConsensusClient] = None
        self._syncer: typing.Optional[SyncerClient] = None
        self._txpool: typing.Optional[TxpoolClient] = None
        self._addresses: typing.Optional[AddressesClient] = None
        self._batch: typing.Optional[BatchClient] = None
        self._outputs: typing.Optional[OutputsClient] = None
        self._events: typing.Optional[EventsClient] = None
        self._rescan: typing.Optional[RescanClient] = None
        self._wallets: typing.Optional[WalletsClient] = None
        self._debug: typing.Optional[DebugClient] = None

    @property
    def misc(self):
        if self._misc is None:
            from .misc.client import MiscClient

            self._misc = MiscClient(client_wrapper=self._client_wrapper)
        return self._misc

    @property
    def consensus(self):
        if self._consensus is None:
            from .consensus.client import ConsensusClient

            self._consensus = ConsensusClient(client_wrapper=self._client_wrapper)
        return self._consensus

    @property
    def syncer(self):
        if self._syncer is None:
            from .syncer.client import SyncerClient

            self._syncer = SyncerClient(client_wrapper=self._client_wrapper)
        return self._syncer

    @property
    def txpool(self):
        if self._txpool is None:
            from .txpool.client import TxpoolClient

            self._txpool = TxpoolClient(client_wrapper=self._client_wrapper)
        return self._txpool

    @property
    def addresses(self):
        if self._addresses is None:
            from .addresses.client import AddressesClient

            self._addresses = AddressesClient(client_wrapper=self._client_wrapper)
        return self._addresses

    @property
    def batch(self):
        if self._batch is None:
            from .batch.client import BatchClient

            self._batch = BatchClient(client_wrapper=self._client_wrapper)
        return self._batch

    @property
    def outputs(self):
        if self._outputs is None:
            from .outputs.client import OutputsClient

            self._outputs = OutputsClient(client_wrapper=self._client_wrapper)
        return self._outputs

    @property
    def events(self):
        if self._events is None:
            from .events.client import EventsClient

            self._events = EventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def rescan(self):
        if self._rescan is None:
            from .rescan.client import RescanClient

            self._rescan = RescanClient(client_wrapper=self._client_wrapper)
        return self._rescan

    @property
    def wallets(self):
        if self._wallets is None:
            from .wallets.client import WalletsClient

            self._wallets = WalletsClient(client_wrapper=self._client_wrapper)
        return self._wallets

    @property
    def debug(self):
        if self._debug is None:
            from .debug.client import DebugClient

            self._debug = DebugClient(client_wrapper=self._client_wrapper)
        return self._debug


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
        self._misc: typing.Optional[AsyncMiscClient] = None
        self._consensus: typing.Optional[AsyncConsensusClient] = None
        self._syncer: typing.Optional[AsyncSyncerClient] = None
        self._txpool: typing.Optional[AsyncTxpoolClient] = None
        self._addresses: typing.Optional[AsyncAddressesClient] = None
        self._batch: typing.Optional[AsyncBatchClient] = None
        self._outputs: typing.Optional[AsyncOutputsClient] = None
        self._events: typing.Optional[AsyncEventsClient] = None
        self._rescan: typing.Optional[AsyncRescanClient] = None
        self._wallets: typing.Optional[AsyncWalletsClient] = None
        self._debug: typing.Optional[AsyncDebugClient] = None

    @property
    def misc(self):
        if self._misc is None:
            from .misc.client import AsyncMiscClient

            self._misc = AsyncMiscClient(client_wrapper=self._client_wrapper)
        return self._misc

    @property
    def consensus(self):
        if self._consensus is None:
            from .consensus.client import AsyncConsensusClient

            self._consensus = AsyncConsensusClient(client_wrapper=self._client_wrapper)
        return self._consensus

    @property
    def syncer(self):
        if self._syncer is None:
            from .syncer.client import AsyncSyncerClient

            self._syncer = AsyncSyncerClient(client_wrapper=self._client_wrapper)
        return self._syncer

    @property
    def txpool(self):
        if self._txpool is None:
            from .txpool.client import AsyncTxpoolClient

            self._txpool = AsyncTxpoolClient(client_wrapper=self._client_wrapper)
        return self._txpool

    @property
    def addresses(self):
        if self._addresses is None:
            from .addresses.client import AsyncAddressesClient

            self._addresses = AsyncAddressesClient(client_wrapper=self._client_wrapper)
        return self._addresses

    @property
    def batch(self):
        if self._batch is None:
            from .batch.client import AsyncBatchClient

            self._batch = AsyncBatchClient(client_wrapper=self._client_wrapper)
        return self._batch

    @property
    def outputs(self):
        if self._outputs is None:
            from .outputs.client import AsyncOutputsClient

            self._outputs = AsyncOutputsClient(client_wrapper=self._client_wrapper)
        return self._outputs

    @property
    def events(self):
        if self._events is None:
            from .events.client import AsyncEventsClient

            self._events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def rescan(self):
        if self._rescan is None:
            from .rescan.client import AsyncRescanClient

            self._rescan = AsyncRescanClient(client_wrapper=self._client_wrapper)
        return self._rescan

    @property
    def wallets(self):
        if self._wallets is None:
            from .wallets.client import AsyncWalletsClient

            self._wallets = AsyncWalletsClient(client_wrapper=self._client_wrapper)
        return self._wallets

    @property
    def debug(self):
        if self._debug is None:
            from .debug.client import AsyncDebugClient

            self._debug = AsyncDebugClient(client_wrapper=self._client_wrapper)
        return self._debug


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
