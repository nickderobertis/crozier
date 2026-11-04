

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .extended_kv_entry_operations.client import (
        AsyncExtendedKvEntryOperationsClient,
        ExtendedKvEntryOperationsClient,
    )
    from .kv_api.client import AsyncKvApiClient, KvApiClient
    from .kv_management_api.client import AsyncKvManagementApiClient, KvManagementApiClient
    from .nats_core_messaging_experimental.client import (
        AsyncNatsCoreMessagingExperimentalClient,
        NatsCoreMessagingExperimentalClient,
    )
    from .object_store_api.client import AsyncObjectStoreApiClient, ObjectStoreApiClient
    from .object_store_entry_operations.client import (
        AsyncObjectStoreEntryOperationsClient,
        ObjectStoreEntryOperationsClient,
    )
    from .object_store_management_api.client import AsyncObjectStoreManagementApiClient, ObjectStoreManagementApiClient


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
        self._kv_api: typing.Optional[KvApiClient] = None
        self._kv_management_api: typing.Optional[KvManagementApiClient] = None
        self._extended_kv_entry_operations: typing.Optional[ExtendedKvEntryOperationsClient] = None
        self._object_store_api: typing.Optional[ObjectStoreApiClient] = None
        self._object_store_management_api: typing.Optional[ObjectStoreManagementApiClient] = None
        self._object_store_entry_operations: typing.Optional[ObjectStoreEntryOperationsClient] = None
        self._nats_core_messaging_experimental: typing.Optional[NatsCoreMessagingExperimentalClient] = None

    @property
    def kv_api(self):
        if self._kv_api is None:
            from .kv_api.client import KvApiClient

            self._kv_api = KvApiClient(client_wrapper=self._client_wrapper)
        return self._kv_api

    @property
    def kv_management_api(self):
        if self._kv_management_api is None:
            from .kv_management_api.client import KvManagementApiClient

            self._kv_management_api = KvManagementApiClient(client_wrapper=self._client_wrapper)
        return self._kv_management_api

    @property
    def extended_kv_entry_operations(self):
        if self._extended_kv_entry_operations is None:
            from .extended_kv_entry_operations.client import ExtendedKvEntryOperationsClient

            self._extended_kv_entry_operations = ExtendedKvEntryOperationsClient(client_wrapper=self._client_wrapper)
        return self._extended_kv_entry_operations

    @property
    def object_store_api(self):
        if self._object_store_api is None:
            from .object_store_api.client import ObjectStoreApiClient

            self._object_store_api = ObjectStoreApiClient(client_wrapper=self._client_wrapper)
        return self._object_store_api

    @property
    def object_store_management_api(self):
        if self._object_store_management_api is None:
            from .object_store_management_api.client import ObjectStoreManagementApiClient

            self._object_store_management_api = ObjectStoreManagementApiClient(client_wrapper=self._client_wrapper)
        return self._object_store_management_api

    @property
    def object_store_entry_operations(self):
        if self._object_store_entry_operations is None:
            from .object_store_entry_operations.client import ObjectStoreEntryOperationsClient

            self._object_store_entry_operations = ObjectStoreEntryOperationsClient(client_wrapper=self._client_wrapper)
        return self._object_store_entry_operations

    @property
    def nats_core_messaging_experimental(self):
        if self._nats_core_messaging_experimental is None:
            from .nats_core_messaging_experimental.client import NatsCoreMessagingExperimentalClient

            self._nats_core_messaging_experimental = NatsCoreMessagingExperimentalClient(
                client_wrapper=self._client_wrapper
            )
        return self._nats_core_messaging_experimental


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
        self._kv_api: typing.Optional[AsyncKvApiClient] = None
        self._kv_management_api: typing.Optional[AsyncKvManagementApiClient] = None
        self._extended_kv_entry_operations: typing.Optional[AsyncExtendedKvEntryOperationsClient] = None
        self._object_store_api: typing.Optional[AsyncObjectStoreApiClient] = None
        self._object_store_management_api: typing.Optional[AsyncObjectStoreManagementApiClient] = None
        self._object_store_entry_operations: typing.Optional[AsyncObjectStoreEntryOperationsClient] = None
        self._nats_core_messaging_experimental: typing.Optional[AsyncNatsCoreMessagingExperimentalClient] = None

    @property
    def kv_api(self):
        if self._kv_api is None:
            from .kv_api.client import AsyncKvApiClient

            self._kv_api = AsyncKvApiClient(client_wrapper=self._client_wrapper)
        return self._kv_api

    @property
    def kv_management_api(self):
        if self._kv_management_api is None:
            from .kv_management_api.client import AsyncKvManagementApiClient

            self._kv_management_api = AsyncKvManagementApiClient(client_wrapper=self._client_wrapper)
        return self._kv_management_api

    @property
    def extended_kv_entry_operations(self):
        if self._extended_kv_entry_operations is None:
            from .extended_kv_entry_operations.client import AsyncExtendedKvEntryOperationsClient

            self._extended_kv_entry_operations = AsyncExtendedKvEntryOperationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._extended_kv_entry_operations

    @property
    def object_store_api(self):
        if self._object_store_api is None:
            from .object_store_api.client import AsyncObjectStoreApiClient

            self._object_store_api = AsyncObjectStoreApiClient(client_wrapper=self._client_wrapper)
        return self._object_store_api

    @property
    def object_store_management_api(self):
        if self._object_store_management_api is None:
            from .object_store_management_api.client import AsyncObjectStoreManagementApiClient

            self._object_store_management_api = AsyncObjectStoreManagementApiClient(client_wrapper=self._client_wrapper)
        return self._object_store_management_api

    @property
    def object_store_entry_operations(self):
        if self._object_store_entry_operations is None:
            from .object_store_entry_operations.client import AsyncObjectStoreEntryOperationsClient

            self._object_store_entry_operations = AsyncObjectStoreEntryOperationsClient(
                client_wrapper=self._client_wrapper
            )
        return self._object_store_entry_operations

    @property
    def nats_core_messaging_experimental(self):
        if self._nats_core_messaging_experimental is None:
            from .nats_core_messaging_experimental.client import AsyncNatsCoreMessagingExperimentalClient

            self._nats_core_messaging_experimental = AsyncNatsCoreMessagingExperimentalClient(
                client_wrapper=self._client_wrapper
            )
        return self._nats_core_messaging_experimental


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
