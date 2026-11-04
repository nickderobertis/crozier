

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .accounts.client import AccountsClient, AsyncAccountsClient
    from .alias.client import AliasClient, AsyncAliasClient
    from .api_keys.client import ApiKeysClient, AsyncApiKeysClient
    from .auditing.client import AsyncAuditingClient, AuditingClient
    from .billing.client import AsyncBillingClient, BillingClient
    from .collections.client import AsyncCollectionsClient, CollectionsClient
    from .guids.client import AsyncGuidsClient, GuidsClient
    from .history.client import AsyncHistoryClient, HistoryClient
    from .images.client import AsyncImagesClient, ImagesClient
    from .messaging.client import AsyncMessagingClient, MessagingClient
    from .meta_information.client import AsyncMetaInformationClient, MetaInformationClient
    from .organizations.client import AsyncOrganizationsClient, OrganizationsClient
    from .public_services.client import AsyncPublicServicesClient, PublicServicesClient
    from .routing.client import AsyncRoutingClient, RoutingClient
    from .storage.client import AsyncStorageClient, StorageClient
    from .transfer.client import AsyncTransferClient, TransferClient


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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._accounts: typing.Optional[AccountsClient] = None
        self._api_keys: typing.Optional[ApiKeysClient] = None
        self._billing: typing.Optional[BillingClient] = None
        self._auditing: typing.Optional[AuditingClient] = None
        self._collections: typing.Optional[CollectionsClient] = None
        self._organizations: typing.Optional[OrganizationsClient] = None
        self._storage: typing.Optional[StorageClient] = None
        self._guids: typing.Optional[GuidsClient] = None
        self._history: typing.Optional[HistoryClient] = None
        self._alias: typing.Optional[AliasClient] = None
        self._meta_information: typing.Optional[MetaInformationClient] = None
        self._messaging: typing.Optional[MessagingClient] = None
        self._public_services: typing.Optional[PublicServicesClient] = None
        self._images: typing.Optional[ImagesClient] = None
        self._routing: typing.Optional[RoutingClient] = None
        self._transfer: typing.Optional[TransferClient] = None

    @property
    def accounts(self):
        if self._accounts is None:
            from .accounts.client import AccountsClient

            self._accounts = AccountsClient(client_wrapper=self._client_wrapper)
        return self._accounts

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import ApiKeysClient

            self._api_keys = ApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def billing(self):
        if self._billing is None:
            from .billing.client import BillingClient

            self._billing = BillingClient(client_wrapper=self._client_wrapper)
        return self._billing

    @property
    def auditing(self):
        if self._auditing is None:
            from .auditing.client import AuditingClient

            self._auditing = AuditingClient(client_wrapper=self._client_wrapper)
        return self._auditing

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import CollectionsClient

            self._collections = CollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def organizations(self):
        if self._organizations is None:
            from .organizations.client import OrganizationsClient

            self._organizations = OrganizationsClient(client_wrapper=self._client_wrapper)
        return self._organizations

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import StorageClient

            self._storage = StorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def guids(self):
        if self._guids is None:
            from .guids.client import GuidsClient

            self._guids = GuidsClient(client_wrapper=self._client_wrapper)
        return self._guids

    @property
    def history(self):
        if self._history is None:
            from .history.client import HistoryClient

            self._history = HistoryClient(client_wrapper=self._client_wrapper)
        return self._history

    @property
    def alias(self):
        if self._alias is None:
            from .alias.client import AliasClient

            self._alias = AliasClient(client_wrapper=self._client_wrapper)
        return self._alias

    @property
    def meta_information(self):
        if self._meta_information is None:
            from .meta_information.client import MetaInformationClient

            self._meta_information = MetaInformationClient(client_wrapper=self._client_wrapper)
        return self._meta_information

    @property
    def messaging(self):
        if self._messaging is None:
            from .messaging.client import MessagingClient

            self._messaging = MessagingClient(client_wrapper=self._client_wrapper)
        return self._messaging

    @property
    def public_services(self):
        if self._public_services is None:
            from .public_services.client import PublicServicesClient

            self._public_services = PublicServicesClient(client_wrapper=self._client_wrapper)
        return self._public_services

    @property
    def images(self):
        if self._images is None:
            from .images.client import ImagesClient

            self._images = ImagesClient(client_wrapper=self._client_wrapper)
        return self._images

    @property
    def routing(self):
        if self._routing is None:
            from .routing.client import RoutingClient

            self._routing = RoutingClient(client_wrapper=self._client_wrapper)
        return self._routing

    @property
    def transfer(self):
        if self._transfer is None:
            from .transfer.client import TransferClient

            self._transfer = TransferClient(client_wrapper=self._client_wrapper)
        return self._transfer


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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._accounts: typing.Optional[AsyncAccountsClient] = None
        self._api_keys: typing.Optional[AsyncApiKeysClient] = None
        self._billing: typing.Optional[AsyncBillingClient] = None
        self._auditing: typing.Optional[AsyncAuditingClient] = None
        self._collections: typing.Optional[AsyncCollectionsClient] = None
        self._organizations: typing.Optional[AsyncOrganizationsClient] = None
        self._storage: typing.Optional[AsyncStorageClient] = None
        self._guids: typing.Optional[AsyncGuidsClient] = None
        self._history: typing.Optional[AsyncHistoryClient] = None
        self._alias: typing.Optional[AsyncAliasClient] = None
        self._meta_information: typing.Optional[AsyncMetaInformationClient] = None
        self._messaging: typing.Optional[AsyncMessagingClient] = None
        self._public_services: typing.Optional[AsyncPublicServicesClient] = None
        self._images: typing.Optional[AsyncImagesClient] = None
        self._routing: typing.Optional[AsyncRoutingClient] = None
        self._transfer: typing.Optional[AsyncTransferClient] = None

    @property
    def accounts(self):
        if self._accounts is None:
            from .accounts.client import AsyncAccountsClient

            self._accounts = AsyncAccountsClient(client_wrapper=self._client_wrapper)
        return self._accounts

    @property
    def api_keys(self):
        if self._api_keys is None:
            from .api_keys.client import AsyncApiKeysClient

            self._api_keys = AsyncApiKeysClient(client_wrapper=self._client_wrapper)
        return self._api_keys

    @property
    def billing(self):
        if self._billing is None:
            from .billing.client import AsyncBillingClient

            self._billing = AsyncBillingClient(client_wrapper=self._client_wrapper)
        return self._billing

    @property
    def auditing(self):
        if self._auditing is None:
            from .auditing.client import AsyncAuditingClient

            self._auditing = AsyncAuditingClient(client_wrapper=self._client_wrapper)
        return self._auditing

    @property
    def collections(self):
        if self._collections is None:
            from .collections.client import AsyncCollectionsClient

            self._collections = AsyncCollectionsClient(client_wrapper=self._client_wrapper)
        return self._collections

    @property
    def organizations(self):
        if self._organizations is None:
            from .organizations.client import AsyncOrganizationsClient

            self._organizations = AsyncOrganizationsClient(client_wrapper=self._client_wrapper)
        return self._organizations

    @property
    def storage(self):
        if self._storage is None:
            from .storage.client import AsyncStorageClient

            self._storage = AsyncStorageClient(client_wrapper=self._client_wrapper)
        return self._storage

    @property
    def guids(self):
        if self._guids is None:
            from .guids.client import AsyncGuidsClient

            self._guids = AsyncGuidsClient(client_wrapper=self._client_wrapper)
        return self._guids

    @property
    def history(self):
        if self._history is None:
            from .history.client import AsyncHistoryClient

            self._history = AsyncHistoryClient(client_wrapper=self._client_wrapper)
        return self._history

    @property
    def alias(self):
        if self._alias is None:
            from .alias.client import AsyncAliasClient

            self._alias = AsyncAliasClient(client_wrapper=self._client_wrapper)
        return self._alias

    @property
    def meta_information(self):
        if self._meta_information is None:
            from .meta_information.client import AsyncMetaInformationClient

            self._meta_information = AsyncMetaInformationClient(client_wrapper=self._client_wrapper)
        return self._meta_information

    @property
    def messaging(self):
        if self._messaging is None:
            from .messaging.client import AsyncMessagingClient

            self._messaging = AsyncMessagingClient(client_wrapper=self._client_wrapper)
        return self._messaging

    @property
    def public_services(self):
        if self._public_services is None:
            from .public_services.client import AsyncPublicServicesClient

            self._public_services = AsyncPublicServicesClient(client_wrapper=self._client_wrapper)
        return self._public_services

    @property
    def images(self):
        if self._images is None:
            from .images.client import AsyncImagesClient

            self._images = AsyncImagesClient(client_wrapper=self._client_wrapper)
        return self._images

    @property
    def routing(self):
        if self._routing is None:
            from .routing.client import AsyncRoutingClient

            self._routing = AsyncRoutingClient(client_wrapper=self._client_wrapper)
        return self._routing

    @property
    def transfer(self):
        if self._transfer is None:
            from .transfer.client import AsyncTransferClient

            self._transfer = AsyncTransferClient(client_wrapper=self._client_wrapper)
        return self._transfer


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
