

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .adgs_filter_extension.client import AdgsFilterExtensionClient, AsyncAdgsFilterExtensionClient
    from .adgs_stations.client import AdgsStationsClient, AsyncAdgsStationsClient
    from .authentication.client import AsyncAuthenticationClient, AuthenticationClient
    from .cadip_filter_extension.client import AsyncCadipFilterExtensionClient, CadipFilterExtensionClient
    from .cadip_stations.client import AsyncCadipStationsClient, CadipStationsClient
    from .catalog.client import AsyncCatalogClient, CatalogClient
    from .catalog_bulk_transaction_extension.client import (
        AsyncCatalogBulkTransactionExtensionClient,
        CatalogBulkTransactionExtensionClient,
    )
    from .catalog_filter_extension.client import AsyncCatalogFilterExtensionClient, CatalogFilterExtensionClient
    from .catalog_liveliness_readiness.client import (
        AsyncCatalogLivelinessReadinessClient,
        CatalogLivelinessReadinessClient,
    )
    from .catalog_transaction_extension.client import (
        AsyncCatalogTransactionExtensionClient,
        CatalogTransactionExtensionClient,
    )
    from .osam_service.client import AsyncOsamServiceClient, OsamServiceClient
    from .prip_filter_extension.client import AsyncPripFilterExtensionClient, PripFilterExtensionClient
    from .prip_stations.client import AsyncPripStationsClient, PripStationsClient
    from .processing_service.client import AsyncProcessingServiceClient, ProcessingServiceClient
    from .sort_extension.client import AsyncSortExtensionClient, SortExtensionClient
    from .staging_service.client import AsyncStagingServiceClient, StagingServiceClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    api_key : str
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
        api_key="YOUR_API_KEY",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        api_key: str,
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
            api_key=api_key,
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
        self._sort_extension: typing.Optional[SortExtensionClient] = None
        self._adgs_filter_extension: typing.Optional[AdgsFilterExtensionClient] = None
        self._adgs_stations: typing.Optional[AdgsStationsClient] = None
        self._authentication: typing.Optional[AuthenticationClient] = None
        self._cadip_filter_extension: typing.Optional[CadipFilterExtensionClient] = None
        self._cadip_stations: typing.Optional[CadipStationsClient] = None
        self._prip_filter_extension: typing.Optional[PripFilterExtensionClient] = None
        self._prip_stations: typing.Optional[PripStationsClient] = None
        self._osam_service: typing.Optional[OsamServiceClient] = None
        self._catalog: typing.Optional[CatalogClient] = None
        self._catalog_transaction_extension: typing.Optional[CatalogTransactionExtensionClient] = None
        self._catalog_filter_extension: typing.Optional[CatalogFilterExtensionClient] = None
        self._catalog_bulk_transaction_extension: typing.Optional[CatalogBulkTransactionExtensionClient] = None
        self._catalog_liveliness_readiness: typing.Optional[CatalogLivelinessReadinessClient] = None
        self._staging_service: typing.Optional[StagingServiceClient] = None
        self._processing_service: typing.Optional[ProcessingServiceClient] = None

    @property
    def sort_extension(self):
        if self._sort_extension is None:
            from .sort_extension.client import SortExtensionClient

            self._sort_extension = SortExtensionClient(client_wrapper=self._client_wrapper)
        return self._sort_extension

    @property
    def adgs_filter_extension(self):
        if self._adgs_filter_extension is None:
            from .adgs_filter_extension.client import AdgsFilterExtensionClient

            self._adgs_filter_extension = AdgsFilterExtensionClient(client_wrapper=self._client_wrapper)
        return self._adgs_filter_extension

    @property
    def adgs_stations(self):
        if self._adgs_stations is None:
            from .adgs_stations.client import AdgsStationsClient

            self._adgs_stations = AdgsStationsClient(client_wrapper=self._client_wrapper)
        return self._adgs_stations

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AuthenticationClient

            self._authentication = AuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def cadip_filter_extension(self):
        if self._cadip_filter_extension is None:
            from .cadip_filter_extension.client import CadipFilterExtensionClient

            self._cadip_filter_extension = CadipFilterExtensionClient(client_wrapper=self._client_wrapper)
        return self._cadip_filter_extension

    @property
    def cadip_stations(self):
        if self._cadip_stations is None:
            from .cadip_stations.client import CadipStationsClient

            self._cadip_stations = CadipStationsClient(client_wrapper=self._client_wrapper)
        return self._cadip_stations

    @property
    def prip_filter_extension(self):
        if self._prip_filter_extension is None:
            from .prip_filter_extension.client import PripFilterExtensionClient

            self._prip_filter_extension = PripFilterExtensionClient(client_wrapper=self._client_wrapper)
        return self._prip_filter_extension

    @property
    def prip_stations(self):
        if self._prip_stations is None:
            from .prip_stations.client import PripStationsClient

            self._prip_stations = PripStationsClient(client_wrapper=self._client_wrapper)
        return self._prip_stations

    @property
    def osam_service(self):
        if self._osam_service is None:
            from .osam_service.client import OsamServiceClient

            self._osam_service = OsamServiceClient(client_wrapper=self._client_wrapper)
        return self._osam_service

    @property
    def catalog(self):
        if self._catalog is None:
            from .catalog.client import CatalogClient

            self._catalog = CatalogClient(client_wrapper=self._client_wrapper)
        return self._catalog

    @property
    def catalog_transaction_extension(self):
        if self._catalog_transaction_extension is None:
            from .catalog_transaction_extension.client import CatalogTransactionExtensionClient

            self._catalog_transaction_extension = CatalogTransactionExtensionClient(client_wrapper=self._client_wrapper)
        return self._catalog_transaction_extension

    @property
    def catalog_filter_extension(self):
        if self._catalog_filter_extension is None:
            from .catalog_filter_extension.client import CatalogFilterExtensionClient

            self._catalog_filter_extension = CatalogFilterExtensionClient(client_wrapper=self._client_wrapper)
        return self._catalog_filter_extension

    @property
    def catalog_bulk_transaction_extension(self):
        if self._catalog_bulk_transaction_extension is None:
            from .catalog_bulk_transaction_extension.client import CatalogBulkTransactionExtensionClient

            self._catalog_bulk_transaction_extension = CatalogBulkTransactionExtensionClient(
                client_wrapper=self._client_wrapper
            )
        return self._catalog_bulk_transaction_extension

    @property
    def catalog_liveliness_readiness(self):
        if self._catalog_liveliness_readiness is None:
            from .catalog_liveliness_readiness.client import CatalogLivelinessReadinessClient

            self._catalog_liveliness_readiness = CatalogLivelinessReadinessClient(client_wrapper=self._client_wrapper)
        return self._catalog_liveliness_readiness

    @property
    def staging_service(self):
        if self._staging_service is None:
            from .staging_service.client import StagingServiceClient

            self._staging_service = StagingServiceClient(client_wrapper=self._client_wrapper)
        return self._staging_service

    @property
    def processing_service(self):
        if self._processing_service is None:
            from .processing_service.client import ProcessingServiceClient

            self._processing_service = ProcessingServiceClient(client_wrapper=self._client_wrapper)
        return self._processing_service


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

    api_key : str
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
        api_key="YOUR_API_KEY",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        api_key: str,
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
            api_key=api_key,
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
        self._sort_extension: typing.Optional[AsyncSortExtensionClient] = None
        self._adgs_filter_extension: typing.Optional[AsyncAdgsFilterExtensionClient] = None
        self._adgs_stations: typing.Optional[AsyncAdgsStationsClient] = None
        self._authentication: typing.Optional[AsyncAuthenticationClient] = None
        self._cadip_filter_extension: typing.Optional[AsyncCadipFilterExtensionClient] = None
        self._cadip_stations: typing.Optional[AsyncCadipStationsClient] = None
        self._prip_filter_extension: typing.Optional[AsyncPripFilterExtensionClient] = None
        self._prip_stations: typing.Optional[AsyncPripStationsClient] = None
        self._osam_service: typing.Optional[AsyncOsamServiceClient] = None
        self._catalog: typing.Optional[AsyncCatalogClient] = None
        self._catalog_transaction_extension: typing.Optional[AsyncCatalogTransactionExtensionClient] = None
        self._catalog_filter_extension: typing.Optional[AsyncCatalogFilterExtensionClient] = None
        self._catalog_bulk_transaction_extension: typing.Optional[AsyncCatalogBulkTransactionExtensionClient] = None
        self._catalog_liveliness_readiness: typing.Optional[AsyncCatalogLivelinessReadinessClient] = None
        self._staging_service: typing.Optional[AsyncStagingServiceClient] = None
        self._processing_service: typing.Optional[AsyncProcessingServiceClient] = None

    @property
    def sort_extension(self):
        if self._sort_extension is None:
            from .sort_extension.client import AsyncSortExtensionClient

            self._sort_extension = AsyncSortExtensionClient(client_wrapper=self._client_wrapper)
        return self._sort_extension

    @property
    def adgs_filter_extension(self):
        if self._adgs_filter_extension is None:
            from .adgs_filter_extension.client import AsyncAdgsFilterExtensionClient

            self._adgs_filter_extension = AsyncAdgsFilterExtensionClient(client_wrapper=self._client_wrapper)
        return self._adgs_filter_extension

    @property
    def adgs_stations(self):
        if self._adgs_stations is None:
            from .adgs_stations.client import AsyncAdgsStationsClient

            self._adgs_stations = AsyncAdgsStationsClient(client_wrapper=self._client_wrapper)
        return self._adgs_stations

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AsyncAuthenticationClient

            self._authentication = AsyncAuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def cadip_filter_extension(self):
        if self._cadip_filter_extension is None:
            from .cadip_filter_extension.client import AsyncCadipFilterExtensionClient

            self._cadip_filter_extension = AsyncCadipFilterExtensionClient(client_wrapper=self._client_wrapper)
        return self._cadip_filter_extension

    @property
    def cadip_stations(self):
        if self._cadip_stations is None:
            from .cadip_stations.client import AsyncCadipStationsClient

            self._cadip_stations = AsyncCadipStationsClient(client_wrapper=self._client_wrapper)
        return self._cadip_stations

    @property
    def prip_filter_extension(self):
        if self._prip_filter_extension is None:
            from .prip_filter_extension.client import AsyncPripFilterExtensionClient

            self._prip_filter_extension = AsyncPripFilterExtensionClient(client_wrapper=self._client_wrapper)
        return self._prip_filter_extension

    @property
    def prip_stations(self):
        if self._prip_stations is None:
            from .prip_stations.client import AsyncPripStationsClient

            self._prip_stations = AsyncPripStationsClient(client_wrapper=self._client_wrapper)
        return self._prip_stations

    @property
    def osam_service(self):
        if self._osam_service is None:
            from .osam_service.client import AsyncOsamServiceClient

            self._osam_service = AsyncOsamServiceClient(client_wrapper=self._client_wrapper)
        return self._osam_service

    @property
    def catalog(self):
        if self._catalog is None:
            from .catalog.client import AsyncCatalogClient

            self._catalog = AsyncCatalogClient(client_wrapper=self._client_wrapper)
        return self._catalog

    @property
    def catalog_transaction_extension(self):
        if self._catalog_transaction_extension is None:
            from .catalog_transaction_extension.client import AsyncCatalogTransactionExtensionClient

            self._catalog_transaction_extension = AsyncCatalogTransactionExtensionClient(
                client_wrapper=self._client_wrapper
            )
        return self._catalog_transaction_extension

    @property
    def catalog_filter_extension(self):
        if self._catalog_filter_extension is None:
            from .catalog_filter_extension.client import AsyncCatalogFilterExtensionClient

            self._catalog_filter_extension = AsyncCatalogFilterExtensionClient(client_wrapper=self._client_wrapper)
        return self._catalog_filter_extension

    @property
    def catalog_bulk_transaction_extension(self):
        if self._catalog_bulk_transaction_extension is None:
            from .catalog_bulk_transaction_extension.client import (
                AsyncCatalogBulkTransactionExtensionClient,
            )

            self._catalog_bulk_transaction_extension = AsyncCatalogBulkTransactionExtensionClient(
                client_wrapper=self._client_wrapper
            )
        return self._catalog_bulk_transaction_extension

    @property
    def catalog_liveliness_readiness(self):
        if self._catalog_liveliness_readiness is None:
            from .catalog_liveliness_readiness.client import AsyncCatalogLivelinessReadinessClient

            self._catalog_liveliness_readiness = AsyncCatalogLivelinessReadinessClient(
                client_wrapper=self._client_wrapper
            )
        return self._catalog_liveliness_readiness

    @property
    def staging_service(self):
        if self._staging_service is None:
            from .staging_service.client import AsyncStagingServiceClient

            self._staging_service = AsyncStagingServiceClient(client_wrapper=self._client_wrapper)
        return self._staging_service

    @property
    def processing_service(self):
        if self._processing_service is None:
            from .processing_service.client import AsyncProcessingServiceClient

            self._processing_service = AsyncProcessingServiceClient(client_wrapper=self._client_wrapper)
        return self._processing_service
