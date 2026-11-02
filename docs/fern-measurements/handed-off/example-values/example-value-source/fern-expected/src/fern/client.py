

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .beacons.client import AsyncBeaconsClient, BeaconsClient
    from .charts.client import AsyncChartsClient, ChartsClient
    from .drills.client import AsyncDrillsClient, DrillsClient
    from .harbours.client import AsyncHarboursClient, HarboursClient
    from .ledger.client import AsyncLedgerClient, LedgerClient
    from .markers.client import AsyncMarkersClient, MarkersClient
    from .mirrors.client import AsyncMirrorsClient, MirrorsClient
    from .passes.client import AsyncPassesClient, PassesClient
    from .rosters.client import AsyncRostersClient, RostersClient
    from .routes.client import AsyncRoutesClient, RoutesClient
    from .soundings.client import AsyncSoundingsClient, SoundingsClient
    from .stations.client import AsyncStationsClient, StationsClient


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
        self._charts: typing.Optional[ChartsClient] = None
        self._mirrors: typing.Optional[MirrorsClient] = None
        self._harbours: typing.Optional[HarboursClient] = None
        self._markers: typing.Optional[MarkersClient] = None
        self._routes: typing.Optional[RoutesClient] = None
        self._drills: typing.Optional[DrillsClient] = None
        self._stations: typing.Optional[StationsClient] = None
        self._passes: typing.Optional[PassesClient] = None
        self._ledger: typing.Optional[LedgerClient] = None
        self._soundings: typing.Optional[SoundingsClient] = None
        self._rosters: typing.Optional[RostersClient] = None
        self._beacons: typing.Optional[BeaconsClient] = None

    @property
    def charts(self):
        if self._charts is None:
            from .charts.client import ChartsClient

            self._charts = ChartsClient(client_wrapper=self._client_wrapper)
        return self._charts

    @property
    def mirrors(self):
        if self._mirrors is None:
            from .mirrors.client import MirrorsClient

            self._mirrors = MirrorsClient(client_wrapper=self._client_wrapper)
        return self._mirrors

    @property
    def harbours(self):
        if self._harbours is None:
            from .harbours.client import HarboursClient

            self._harbours = HarboursClient(client_wrapper=self._client_wrapper)
        return self._harbours

    @property
    def markers(self):
        if self._markers is None:
            from .markers.client import MarkersClient

            self._markers = MarkersClient(client_wrapper=self._client_wrapper)
        return self._markers

    @property
    def routes(self):
        if self._routes is None:
            from .routes.client import RoutesClient

            self._routes = RoutesClient(client_wrapper=self._client_wrapper)
        return self._routes

    @property
    def drills(self):
        if self._drills is None:
            from .drills.client import DrillsClient

            self._drills = DrillsClient(client_wrapper=self._client_wrapper)
        return self._drills

    @property
    def stations(self):
        if self._stations is None:
            from .stations.client import StationsClient

            self._stations = StationsClient(client_wrapper=self._client_wrapper)
        return self._stations

    @property
    def passes(self):
        if self._passes is None:
            from .passes.client import PassesClient

            self._passes = PassesClient(client_wrapper=self._client_wrapper)
        return self._passes

    @property
    def ledger(self):
        if self._ledger is None:
            from .ledger.client import LedgerClient

            self._ledger = LedgerClient(client_wrapper=self._client_wrapper)
        return self._ledger

    @property
    def soundings(self):
        if self._soundings is None:
            from .soundings.client import SoundingsClient

            self._soundings = SoundingsClient(client_wrapper=self._client_wrapper)
        return self._soundings

    @property
    def rosters(self):
        if self._rosters is None:
            from .rosters.client import RostersClient

            self._rosters = RostersClient(client_wrapper=self._client_wrapper)
        return self._rosters

    @property
    def beacons(self):
        if self._beacons is None:
            from .beacons.client import BeaconsClient

            self._beacons = BeaconsClient(client_wrapper=self._client_wrapper)
        return self._beacons


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
        self._charts: typing.Optional[AsyncChartsClient] = None
        self._mirrors: typing.Optional[AsyncMirrorsClient] = None
        self._harbours: typing.Optional[AsyncHarboursClient] = None
        self._markers: typing.Optional[AsyncMarkersClient] = None
        self._routes: typing.Optional[AsyncRoutesClient] = None
        self._drills: typing.Optional[AsyncDrillsClient] = None
        self._stations: typing.Optional[AsyncStationsClient] = None
        self._passes: typing.Optional[AsyncPassesClient] = None
        self._ledger: typing.Optional[AsyncLedgerClient] = None
        self._soundings: typing.Optional[AsyncSoundingsClient] = None
        self._rosters: typing.Optional[AsyncRostersClient] = None
        self._beacons: typing.Optional[AsyncBeaconsClient] = None

    @property
    def charts(self):
        if self._charts is None:
            from .charts.client import AsyncChartsClient

            self._charts = AsyncChartsClient(client_wrapper=self._client_wrapper)
        return self._charts

    @property
    def mirrors(self):
        if self._mirrors is None:
            from .mirrors.client import AsyncMirrorsClient

            self._mirrors = AsyncMirrorsClient(client_wrapper=self._client_wrapper)
        return self._mirrors

    @property
    def harbours(self):
        if self._harbours is None:
            from .harbours.client import AsyncHarboursClient

            self._harbours = AsyncHarboursClient(client_wrapper=self._client_wrapper)
        return self._harbours

    @property
    def markers(self):
        if self._markers is None:
            from .markers.client import AsyncMarkersClient

            self._markers = AsyncMarkersClient(client_wrapper=self._client_wrapper)
        return self._markers

    @property
    def routes(self):
        if self._routes is None:
            from .routes.client import AsyncRoutesClient

            self._routes = AsyncRoutesClient(client_wrapper=self._client_wrapper)
        return self._routes

    @property
    def drills(self):
        if self._drills is None:
            from .drills.client import AsyncDrillsClient

            self._drills = AsyncDrillsClient(client_wrapper=self._client_wrapper)
        return self._drills

    @property
    def stations(self):
        if self._stations is None:
            from .stations.client import AsyncStationsClient

            self._stations = AsyncStationsClient(client_wrapper=self._client_wrapper)
        return self._stations

    @property
    def passes(self):
        if self._passes is None:
            from .passes.client import AsyncPassesClient

            self._passes = AsyncPassesClient(client_wrapper=self._client_wrapper)
        return self._passes

    @property
    def ledger(self):
        if self._ledger is None:
            from .ledger.client import AsyncLedgerClient

            self._ledger = AsyncLedgerClient(client_wrapper=self._client_wrapper)
        return self._ledger

    @property
    def soundings(self):
        if self._soundings is None:
            from .soundings.client import AsyncSoundingsClient

            self._soundings = AsyncSoundingsClient(client_wrapper=self._client_wrapper)
        return self._soundings

    @property
    def rosters(self):
        if self._rosters is None:
            from .rosters.client import AsyncRostersClient

            self._rosters = AsyncRostersClient(client_wrapper=self._client_wrapper)
        return self._rosters

    @property
    def beacons(self):
        if self._beacons is None:
            from .beacons.client import AsyncBeaconsClient

            self._beacons = AsyncBeaconsClient(client_wrapper=self._client_wrapper)
        return self._beacons
