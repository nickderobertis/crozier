

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .channels.client import AsyncChannelsClient, ChannelsClient
    from .invoices.client import AsyncInvoicesClient, InvoicesClient
    from .on_chain.client import AsyncOnChainClient, OnChainClient
    from .other.client import AsyncOtherClient, OtherClient
    from .payments.client import AsyncPaymentsClient, PaymentsClient
    from .peers.client import AsyncPeersClient, PeersClient
    from .rgb.client import AsyncRgbClient, RgbClient
    from .swaps.client import AsyncSwapsClient, SwapsClient


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



    token : typing.Union[str, typing.Callable[[], str]]
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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        token: typing.Union[str, typing.Callable[[], str]],
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
        self._on_chain: typing.Optional[OnChainClient] = None
        self._rgb: typing.Optional[RgbClient] = None
        self._other: typing.Optional[OtherClient] = None
        self._channels: typing.Optional[ChannelsClient] = None
        self._peers: typing.Optional[PeersClient] = None
        self._invoices: typing.Optional[InvoicesClient] = None
        self._swaps: typing.Optional[SwapsClient] = None
        self._payments: typing.Optional[PaymentsClient] = None

    @property
    def on_chain(self):
        if self._on_chain is None:
            from .on_chain.client import OnChainClient

            self._on_chain = OnChainClient(client_wrapper=self._client_wrapper)
        return self._on_chain

    @property
    def rgb(self):
        if self._rgb is None:
            from .rgb.client import RgbClient

            self._rgb = RgbClient(client_wrapper=self._client_wrapper)
        return self._rgb

    @property
    def other(self):
        if self._other is None:
            from .other.client import OtherClient

            self._other = OtherClient(client_wrapper=self._client_wrapper)
        return self._other

    @property
    def channels(self):
        if self._channels is None:
            from .channels.client import ChannelsClient

            self._channels = ChannelsClient(client_wrapper=self._client_wrapper)
        return self._channels

    @property
    def peers(self):
        if self._peers is None:
            from .peers.client import PeersClient

            self._peers = PeersClient(client_wrapper=self._client_wrapper)
        return self._peers

    @property
    def invoices(self):
        if self._invoices is None:
            from .invoices.client import InvoicesClient

            self._invoices = InvoicesClient(client_wrapper=self._client_wrapper)
        return self._invoices

    @property
    def swaps(self):
        if self._swaps is None:
            from .swaps.client import SwapsClient

            self._swaps = SwapsClient(client_wrapper=self._client_wrapper)
        return self._swaps

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import PaymentsClient

            self._payments = PaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments


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



    token : typing.Union[str, typing.Callable[[], str]]
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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        token: typing.Union[str, typing.Callable[[], str]],
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._on_chain: typing.Optional[AsyncOnChainClient] = None
        self._rgb: typing.Optional[AsyncRgbClient] = None
        self._other: typing.Optional[AsyncOtherClient] = None
        self._channels: typing.Optional[AsyncChannelsClient] = None
        self._peers: typing.Optional[AsyncPeersClient] = None
        self._invoices: typing.Optional[AsyncInvoicesClient] = None
        self._swaps: typing.Optional[AsyncSwapsClient] = None
        self._payments: typing.Optional[AsyncPaymentsClient] = None

    @property
    def on_chain(self):
        if self._on_chain is None:
            from .on_chain.client import AsyncOnChainClient

            self._on_chain = AsyncOnChainClient(client_wrapper=self._client_wrapper)
        return self._on_chain

    @property
    def rgb(self):
        if self._rgb is None:
            from .rgb.client import AsyncRgbClient

            self._rgb = AsyncRgbClient(client_wrapper=self._client_wrapper)
        return self._rgb

    @property
    def other(self):
        if self._other is None:
            from .other.client import AsyncOtherClient

            self._other = AsyncOtherClient(client_wrapper=self._client_wrapper)
        return self._other

    @property
    def channels(self):
        if self._channels is None:
            from .channels.client import AsyncChannelsClient

            self._channels = AsyncChannelsClient(client_wrapper=self._client_wrapper)
        return self._channels

    @property
    def peers(self):
        if self._peers is None:
            from .peers.client import AsyncPeersClient

            self._peers = AsyncPeersClient(client_wrapper=self._client_wrapper)
        return self._peers

    @property
    def invoices(self):
        if self._invoices is None:
            from .invoices.client import AsyncInvoicesClient

            self._invoices = AsyncInvoicesClient(client_wrapper=self._client_wrapper)
        return self._invoices

    @property
    def swaps(self):
        if self._swaps is None:
            from .swaps.client import AsyncSwapsClient

            self._swaps = AsyncSwapsClient(client_wrapper=self._client_wrapper)
        return self._swaps

    @property
    def payments(self):
        if self._payments is None:
            from .payments.client import AsyncPaymentsClient

            self._payments = AsyncPaymentsClient(client_wrapper=self._client_wrapper)
        return self._payments


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
