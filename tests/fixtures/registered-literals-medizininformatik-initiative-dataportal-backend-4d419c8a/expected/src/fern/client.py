

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger

if typing.TYPE_CHECKING:
    from .codeable_concepts.client import AsyncCodeableConceptsClient, CodeableConceptsClient
    from .dataquery.client import AsyncDataqueryClient, DataqueryClient
    from .dse.client import AsyncDseClient, DseClient
    from .feasibility.client import AsyncFeasibilityClient, FeasibilityClient
    from .intrinsics.client import AsyncIntrinsicsClient, IntrinsicsClient
    from .profile.client import AsyncProfileClient, ProfileClient
    from .terminology.client import AsyncTerminologyClient, TerminologyClient
    from .upgrade.client import AsyncUpgradeClient, UpgradeClient
    from .validation.client import AsyncValidationClient, ValidationClient


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
        self._dataquery: typing.Optional[DataqueryClient] = None
        self._feasibility: typing.Optional[FeasibilityClient] = None
        self._terminology: typing.Optional[TerminologyClient] = None
        self._codeable_concepts: typing.Optional[CodeableConceptsClient] = None
        self._profile: typing.Optional[ProfileClient] = None
        self._dse: typing.Optional[DseClient] = None
        self._validation: typing.Optional[ValidationClient] = None
        self._upgrade: typing.Optional[UpgradeClient] = None
        self._intrinsics: typing.Optional[IntrinsicsClient] = None

    @property
    def dataquery(self):
        if self._dataquery is None:
            from .dataquery.client import DataqueryClient

            self._dataquery = DataqueryClient(client_wrapper=self._client_wrapper)
        return self._dataquery

    @property
    def feasibility(self):
        if self._feasibility is None:
            from .feasibility.client import FeasibilityClient

            self._feasibility = FeasibilityClient(client_wrapper=self._client_wrapper)
        return self._feasibility

    @property
    def terminology(self):
        if self._terminology is None:
            from .terminology.client import TerminologyClient

            self._terminology = TerminologyClient(client_wrapper=self._client_wrapper)
        return self._terminology

    @property
    def codeable_concepts(self):
        if self._codeable_concepts is None:
            from .codeable_concepts.client import CodeableConceptsClient

            self._codeable_concepts = CodeableConceptsClient(client_wrapper=self._client_wrapper)
        return self._codeable_concepts

    @property
    def profile(self):
        if self._profile is None:
            from .profile.client import ProfileClient

            self._profile = ProfileClient(client_wrapper=self._client_wrapper)
        return self._profile

    @property
    def dse(self):
        if self._dse is None:
            from .dse.client import DseClient

            self._dse = DseClient(client_wrapper=self._client_wrapper)
        return self._dse

    @property
    def validation(self):
        if self._validation is None:
            from .validation.client import ValidationClient

            self._validation = ValidationClient(client_wrapper=self._client_wrapper)
        return self._validation

    @property
    def upgrade(self):
        if self._upgrade is None:
            from .upgrade.client import UpgradeClient

            self._upgrade = UpgradeClient(client_wrapper=self._client_wrapper)
        return self._upgrade

    @property
    def intrinsics(self):
        if self._intrinsics is None:
            from .intrinsics.client import IntrinsicsClient

            self._intrinsics = IntrinsicsClient(client_wrapper=self._client_wrapper)
        return self._intrinsics


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
        self._dataquery: typing.Optional[AsyncDataqueryClient] = None
        self._feasibility: typing.Optional[AsyncFeasibilityClient] = None
        self._terminology: typing.Optional[AsyncTerminologyClient] = None
        self._codeable_concepts: typing.Optional[AsyncCodeableConceptsClient] = None
        self._profile: typing.Optional[AsyncProfileClient] = None
        self._dse: typing.Optional[AsyncDseClient] = None
        self._validation: typing.Optional[AsyncValidationClient] = None
        self._upgrade: typing.Optional[AsyncUpgradeClient] = None
        self._intrinsics: typing.Optional[AsyncIntrinsicsClient] = None

    @property
    def dataquery(self):
        if self._dataquery is None:
            from .dataquery.client import AsyncDataqueryClient

            self._dataquery = AsyncDataqueryClient(client_wrapper=self._client_wrapper)
        return self._dataquery

    @property
    def feasibility(self):
        if self._feasibility is None:
            from .feasibility.client import AsyncFeasibilityClient

            self._feasibility = AsyncFeasibilityClient(client_wrapper=self._client_wrapper)
        return self._feasibility

    @property
    def terminology(self):
        if self._terminology is None:
            from .terminology.client import AsyncTerminologyClient

            self._terminology = AsyncTerminologyClient(client_wrapper=self._client_wrapper)
        return self._terminology

    @property
    def codeable_concepts(self):
        if self._codeable_concepts is None:
            from .codeable_concepts.client import AsyncCodeableConceptsClient

            self._codeable_concepts = AsyncCodeableConceptsClient(client_wrapper=self._client_wrapper)
        return self._codeable_concepts

    @property
    def profile(self):
        if self._profile is None:
            from .profile.client import AsyncProfileClient

            self._profile = AsyncProfileClient(client_wrapper=self._client_wrapper)
        return self._profile

    @property
    def dse(self):
        if self._dse is None:
            from .dse.client import AsyncDseClient

            self._dse = AsyncDseClient(client_wrapper=self._client_wrapper)
        return self._dse

    @property
    def validation(self):
        if self._validation is None:
            from .validation.client import AsyncValidationClient

            self._validation = AsyncValidationClient(client_wrapper=self._client_wrapper)
        return self._validation

    @property
    def upgrade(self):
        if self._upgrade is None:
            from .upgrade.client import AsyncUpgradeClient

            self._upgrade = AsyncUpgradeClient(client_wrapper=self._client_wrapper)
        return self._upgrade

    @property
    def intrinsics(self):
        if self._intrinsics is None:
            from .intrinsics.client import AsyncIntrinsicsClient

            self._intrinsics = AsyncIntrinsicsClient(client_wrapper=self._client_wrapper)
        return self._intrinsics
