

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .checkouts.client import AsyncCheckoutsClient, CheckoutsClient
    from .customers.client import AsyncCustomersClient, CustomersClient
    from .members.client import AsyncMembersClient, MembersClient
    from .memberships.client import AsyncMembershipsClient, MembershipsClient
    from .merchants.client import AsyncMerchantsClient, MerchantsClient
    from .payouts.client import AsyncPayoutsClient, PayoutsClient
    from .readers.client import AsyncReadersClient, ReadersClient
    from .receipts.client import AsyncReceiptsClient, ReceiptsClient
    from .roles.client import AsyncRolesClient, RolesClient
    from .transactions.client import AsyncTransactionsClient, TransactionsClient


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
        self._checkouts: typing.Optional[CheckoutsClient] = None
        self._customers: typing.Optional[CustomersClient] = None
        self._transactions: typing.Optional[TransactionsClient] = None
        self._payouts: typing.Optional[PayoutsClient] = None
        self._receipts: typing.Optional[ReceiptsClient] = None
        self._readers: typing.Optional[ReadersClient] = None
        self._memberships: typing.Optional[MembershipsClient] = None
        self._members: typing.Optional[MembersClient] = None
        self._roles: typing.Optional[RolesClient] = None
        self._merchants: typing.Optional[MerchantsClient] = None

    @property
    def checkouts(self):
        if self._checkouts is None:
            from .checkouts.client import CheckoutsClient

            self._checkouts = CheckoutsClient(client_wrapper=self._client_wrapper)
        return self._checkouts

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import CustomersClient

            self._customers = CustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def transactions(self):
        if self._transactions is None:
            from .transactions.client import TransactionsClient

            self._transactions = TransactionsClient(client_wrapper=self._client_wrapper)
        return self._transactions

    @property
    def payouts(self):
        if self._payouts is None:
            from .payouts.client import PayoutsClient

            self._payouts = PayoutsClient(client_wrapper=self._client_wrapper)
        return self._payouts

    @property
    def receipts(self):
        if self._receipts is None:
            from .receipts.client import ReceiptsClient

            self._receipts = ReceiptsClient(client_wrapper=self._client_wrapper)
        return self._receipts

    @property
    def readers(self):
        if self._readers is None:
            from .readers.client import ReadersClient

            self._readers = ReadersClient(client_wrapper=self._client_wrapper)
        return self._readers

    @property
    def memberships(self):
        if self._memberships is None:
            from .memberships.client import MembershipsClient

            self._memberships = MembershipsClient(client_wrapper=self._client_wrapper)
        return self._memberships

    @property
    def members(self):
        if self._members is None:
            from .members.client import MembersClient

            self._members = MembersClient(client_wrapper=self._client_wrapper)
        return self._members

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import RolesClient

            self._roles = RolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def merchants(self):
        if self._merchants is None:
            from .merchants.client import MerchantsClient

            self._merchants = MerchantsClient(client_wrapper=self._client_wrapper)
        return self._merchants


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
        self._checkouts: typing.Optional[AsyncCheckoutsClient] = None
        self._customers: typing.Optional[AsyncCustomersClient] = None
        self._transactions: typing.Optional[AsyncTransactionsClient] = None
        self._payouts: typing.Optional[AsyncPayoutsClient] = None
        self._receipts: typing.Optional[AsyncReceiptsClient] = None
        self._readers: typing.Optional[AsyncReadersClient] = None
        self._memberships: typing.Optional[AsyncMembershipsClient] = None
        self._members: typing.Optional[AsyncMembersClient] = None
        self._roles: typing.Optional[AsyncRolesClient] = None
        self._merchants: typing.Optional[AsyncMerchantsClient] = None

    @property
    def checkouts(self):
        if self._checkouts is None:
            from .checkouts.client import AsyncCheckoutsClient

            self._checkouts = AsyncCheckoutsClient(client_wrapper=self._client_wrapper)
        return self._checkouts

    @property
    def customers(self):
        if self._customers is None:
            from .customers.client import AsyncCustomersClient

            self._customers = AsyncCustomersClient(client_wrapper=self._client_wrapper)
        return self._customers

    @property
    def transactions(self):
        if self._transactions is None:
            from .transactions.client import AsyncTransactionsClient

            self._transactions = AsyncTransactionsClient(client_wrapper=self._client_wrapper)
        return self._transactions

    @property
    def payouts(self):
        if self._payouts is None:
            from .payouts.client import AsyncPayoutsClient

            self._payouts = AsyncPayoutsClient(client_wrapper=self._client_wrapper)
        return self._payouts

    @property
    def receipts(self):
        if self._receipts is None:
            from .receipts.client import AsyncReceiptsClient

            self._receipts = AsyncReceiptsClient(client_wrapper=self._client_wrapper)
        return self._receipts

    @property
    def readers(self):
        if self._readers is None:
            from .readers.client import AsyncReadersClient

            self._readers = AsyncReadersClient(client_wrapper=self._client_wrapper)
        return self._readers

    @property
    def memberships(self):
        if self._memberships is None:
            from .memberships.client import AsyncMembershipsClient

            self._memberships = AsyncMembershipsClient(client_wrapper=self._client_wrapper)
        return self._memberships

    @property
    def members(self):
        if self._members is None:
            from .members.client import AsyncMembersClient

            self._members = AsyncMembersClient(client_wrapper=self._client_wrapper)
        return self._members

    @property
    def roles(self):
        if self._roles is None:
            from .roles.client import AsyncRolesClient

            self._roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
        return self._roles

    @property
    def merchants(self):
        if self._merchants is None:
            from .merchants.client import AsyncMerchantsClient

            self._merchants = AsyncMerchantsClient(client_wrapper=self._client_wrapper)
        return self._merchants


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
