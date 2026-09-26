

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .alias_operations_v2.client import AliasOperationsV2Client, AsyncAliasOperationsV2Client
    from .collection_operations_v2.client import AsyncCollectionOperationsV2Client, CollectionOperationsV2Client
    from .index_operations_v2.client import AsyncIndexOperationsV2Client, IndexOperationsV2Client
    from .partition_operations_v2.client import AsyncPartitionOperationsV2Client, PartitionOperationsV2Client
    from .role_operations_v2.client import AsyncRoleOperationsV2Client, RoleOperationsV2Client
    from .user_operations_v2.client import AsyncUserOperationsV2Client, UserOperationsV2Client
    from .vector_operations_v2.client import AsyncVectorOperationsV2Client, VectorOperationsV2Client


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    request_timeout : typing.Optional[int]
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
        request_timeout="YOUR_REQUEST_TIMEOUT",
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        request_timeout: typing.Optional[int] = None,
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
            request_timeout=request_timeout,
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
        self._vector_operations_v2: typing.Optional[VectorOperationsV2Client] = None
        self._collection_operations_v2: typing.Optional[CollectionOperationsV2Client] = None
        self._partition_operations_v2: typing.Optional[PartitionOperationsV2Client] = None
        self._user_operations_v2: typing.Optional[UserOperationsV2Client] = None
        self._role_operations_v2: typing.Optional[RoleOperationsV2Client] = None
        self._index_operations_v2: typing.Optional[IndexOperationsV2Client] = None
        self._alias_operations_v2: typing.Optional[AliasOperationsV2Client] = None

    @property
    def vector_operations_v2(self):
        if self._vector_operations_v2 is None:
            from .vector_operations_v2.client import VectorOperationsV2Client

            self._vector_operations_v2 = VectorOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._vector_operations_v2

    @property
    def collection_operations_v2(self):
        if self._collection_operations_v2 is None:
            from .collection_operations_v2.client import CollectionOperationsV2Client

            self._collection_operations_v2 = CollectionOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._collection_operations_v2

    @property
    def partition_operations_v2(self):
        if self._partition_operations_v2 is None:
            from .partition_operations_v2.client import PartitionOperationsV2Client

            self._partition_operations_v2 = PartitionOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._partition_operations_v2

    @property
    def user_operations_v2(self):
        if self._user_operations_v2 is None:
            from .user_operations_v2.client import UserOperationsV2Client

            self._user_operations_v2 = UserOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._user_operations_v2

    @property
    def role_operations_v2(self):
        if self._role_operations_v2 is None:
            from .role_operations_v2.client import RoleOperationsV2Client

            self._role_operations_v2 = RoleOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._role_operations_v2

    @property
    def index_operations_v2(self):
        if self._index_operations_v2 is None:
            from .index_operations_v2.client import IndexOperationsV2Client

            self._index_operations_v2 = IndexOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._index_operations_v2

    @property
    def alias_operations_v2(self):
        if self._alias_operations_v2 is None:
            from .alias_operations_v2.client import AliasOperationsV2Client

            self._alias_operations_v2 = AliasOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._alias_operations_v2


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

    request_timeout : typing.Optional[int]
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
        request_timeout="YOUR_REQUEST_TIMEOUT",
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        request_timeout: typing.Optional[int] = None,
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
            request_timeout=request_timeout,
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
        self._vector_operations_v2: typing.Optional[AsyncVectorOperationsV2Client] = None
        self._collection_operations_v2: typing.Optional[AsyncCollectionOperationsV2Client] = None
        self._partition_operations_v2: typing.Optional[AsyncPartitionOperationsV2Client] = None
        self._user_operations_v2: typing.Optional[AsyncUserOperationsV2Client] = None
        self._role_operations_v2: typing.Optional[AsyncRoleOperationsV2Client] = None
        self._index_operations_v2: typing.Optional[AsyncIndexOperationsV2Client] = None
        self._alias_operations_v2: typing.Optional[AsyncAliasOperationsV2Client] = None

    @property
    def vector_operations_v2(self):
        if self._vector_operations_v2 is None:
            from .vector_operations_v2.client import AsyncVectorOperationsV2Client

            self._vector_operations_v2 = AsyncVectorOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._vector_operations_v2

    @property
    def collection_operations_v2(self):
        if self._collection_operations_v2 is None:
            from .collection_operations_v2.client import AsyncCollectionOperationsV2Client

            self._collection_operations_v2 = AsyncCollectionOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._collection_operations_v2

    @property
    def partition_operations_v2(self):
        if self._partition_operations_v2 is None:
            from .partition_operations_v2.client import AsyncPartitionOperationsV2Client

            self._partition_operations_v2 = AsyncPartitionOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._partition_operations_v2

    @property
    def user_operations_v2(self):
        if self._user_operations_v2 is None:
            from .user_operations_v2.client import AsyncUserOperationsV2Client

            self._user_operations_v2 = AsyncUserOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._user_operations_v2

    @property
    def role_operations_v2(self):
        if self._role_operations_v2 is None:
            from .role_operations_v2.client import AsyncRoleOperationsV2Client

            self._role_operations_v2 = AsyncRoleOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._role_operations_v2

    @property
    def index_operations_v2(self):
        if self._index_operations_v2 is None:
            from .index_operations_v2.client import AsyncIndexOperationsV2Client

            self._index_operations_v2 = AsyncIndexOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._index_operations_v2

    @property
    def alias_operations_v2(self):
        if self._alias_operations_v2 is None:
            from .alias_operations_v2.client import AsyncAliasOperationsV2Client

            self._alias_operations_v2 = AsyncAliasOperationsV2Client(client_wrapper=self._client_wrapper)
        return self._alias_operations_v2
