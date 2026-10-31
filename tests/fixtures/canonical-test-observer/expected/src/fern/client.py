

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi

if typing.TYPE_CHECKING:
    from .applications.client import ApplicationsClient, AsyncApplicationsClient
    from .artefact_matching_rules.client import ArtefactMatchingRulesClient, AsyncArtefactMatchingRulesClient
    from .artefacts.client import ArtefactsClient, AsyncArtefactsClient
    from .authentication.client import AsyncAuthenticationClient, AuthenticationClient
    from .environments.client import AsyncEnvironmentsClient, EnvironmentsClient
    from .execution_metadata.client import AsyncExecutionMetadataClient, ExecutionMetadataClient
    from .issues.client import AsyncIssuesClient, IssuesClient
    from .notifications.client import AsyncNotificationsClient, NotificationsClient
    from .permissions.client import AsyncPermissionsClient, PermissionsClient
    from .reports.client import AsyncReportsClient, ReportsClient
    from .teams.client import AsyncTeamsClient, TeamsClient
    from .test_cases.client import AsyncTestCasesClient, TestCasesClient
    from .test_executions.client import AsyncTestExecutionsClient, TestExecutionsClient
    from .test_plans.client import AsyncTestPlansClient, TestPlansClient
    from .test_results.client import AsyncTestResultsClient, TestResultsClient
    from .users.client import AsyncUsersClient, UsersClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    csrf_token : str
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
        csrf_token="YOUR_CSRF_TOKEN",
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        csrf_token: str,
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
            csrf_token=csrf_token,
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
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._test_executions: typing.Optional[TestExecutionsClient] = None
        self._artefacts: typing.Optional[ArtefactsClient] = None
        self._reports: typing.Optional[ReportsClient] = None
        self._test_cases: typing.Optional[TestCasesClient] = None
        self._environments: typing.Optional[EnvironmentsClient] = None
        self._test_plans: typing.Optional[TestPlansClient] = None
        self._issues: typing.Optional[IssuesClient] = None
        self._test_results: typing.Optional[TestResultsClient] = None
        self._execution_metadata: typing.Optional[ExecutionMetadataClient] = None
        self._authentication: typing.Optional[AuthenticationClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._teams: typing.Optional[TeamsClient] = None
        self._permissions: typing.Optional[PermissionsClient] = None
        self._applications: typing.Optional[ApplicationsClient] = None
        self._notifications: typing.Optional[NotificationsClient] = None
        self._artefact_matching_rules: typing.Optional[ArtefactMatchingRulesClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_version_v1version_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_version_v1version_get()
        """
        _response = self._raw_client.get_version_v1version_get(request_options=request_options)
        return _response.data

    def live_health_live_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        Liveness probe.

        Returns 200 OK if the application process is running and responding to requests.
        Does not check external dependencies like the database.

        Use this probe with container orchestration to determine if the process should be restarted.
        Note that this should only be accessible internally (e.g. from the host container)
        and not accessible over the public API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.live_health_live_get()
        """
        _response = self._raw_client.live_health_live_get(request_options=request_options)
        return _response.data

    def ready_health_ready_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Readiness probe.

        Returns 200 OK if the application is ready to serve traffic, including database connectivity.
        Performs a simple database query to verify the connection is valid.

        Use this probe with container orchestration to determine if traffic should be routed to this pod.
        Note that this should only be accessible internally (e.g. from the host container)
        and not accessible over the public API.
        Returns 503 if the database is unavailable.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.ready_health_ready_get()
        """
        _response = self._raw_client.ready_health_ready_get(request_options=request_options)
        return _response.data

    def root_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.root_get()
        """
        _response = self._raw_client.root_get(request_options=request_options)
        return _response.data

    def trigger_error_sentry_debug_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.trigger_error_sentry_debug_get()
        """
        _response = self._raw_client.trigger_error_sentry_debug_get(request_options=request_options)
        return _response.data

    @property
    def test_executions(self):
        if self._test_executions is None:
            from .test_executions.client import TestExecutionsClient

            self._test_executions = TestExecutionsClient(client_wrapper=self._client_wrapper)
        return self._test_executions

    @property
    def artefacts(self):
        if self._artefacts is None:
            from .artefacts.client import ArtefactsClient

            self._artefacts = ArtefactsClient(client_wrapper=self._client_wrapper)
        return self._artefacts

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import ReportsClient

            self._reports = ReportsClient(client_wrapper=self._client_wrapper)
        return self._reports

    @property
    def test_cases(self):
        if self._test_cases is None:
            from .test_cases.client import TestCasesClient

            self._test_cases = TestCasesClient(client_wrapper=self._client_wrapper)
        return self._test_cases

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import EnvironmentsClient

            self._environments = EnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def test_plans(self):
        if self._test_plans is None:
            from .test_plans.client import TestPlansClient

            self._test_plans = TestPlansClient(client_wrapper=self._client_wrapper)
        return self._test_plans

    @property
    def issues(self):
        if self._issues is None:
            from .issues.client import IssuesClient

            self._issues = IssuesClient(client_wrapper=self._client_wrapper)
        return self._issues

    @property
    def test_results(self):
        if self._test_results is None:
            from .test_results.client import TestResultsClient

            self._test_results = TestResultsClient(client_wrapper=self._client_wrapper)
        return self._test_results

    @property
    def execution_metadata(self):
        if self._execution_metadata is None:
            from .execution_metadata.client import ExecutionMetadataClient

            self._execution_metadata = ExecutionMetadataClient(client_wrapper=self._client_wrapper)
        return self._execution_metadata

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AuthenticationClient

            self._authentication = AuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def teams(self):
        if self._teams is None:
            from .teams.client import TeamsClient

            self._teams = TeamsClient(client_wrapper=self._client_wrapper)
        return self._teams

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import PermissionsClient

            self._permissions = PermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def applications(self):
        if self._applications is None:
            from .applications.client import ApplicationsClient

            self._applications = ApplicationsClient(client_wrapper=self._client_wrapper)
        return self._applications

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import NotificationsClient

            self._notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def artefact_matching_rules(self):
        if self._artefact_matching_rules is None:
            from .artefact_matching_rules.client import ArtefactMatchingRulesClient

            self._artefact_matching_rules = ArtefactMatchingRulesClient(client_wrapper=self._client_wrapper)
        return self._artefact_matching_rules


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

    csrf_token : str
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
        csrf_token="YOUR_CSRF_TOKEN",
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        csrf_token: str,
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
            csrf_token=csrf_token,
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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._test_executions: typing.Optional[AsyncTestExecutionsClient] = None
        self._artefacts: typing.Optional[AsyncArtefactsClient] = None
        self._reports: typing.Optional[AsyncReportsClient] = None
        self._test_cases: typing.Optional[AsyncTestCasesClient] = None
        self._environments: typing.Optional[AsyncEnvironmentsClient] = None
        self._test_plans: typing.Optional[AsyncTestPlansClient] = None
        self._issues: typing.Optional[AsyncIssuesClient] = None
        self._test_results: typing.Optional[AsyncTestResultsClient] = None
        self._execution_metadata: typing.Optional[AsyncExecutionMetadataClient] = None
        self._authentication: typing.Optional[AsyncAuthenticationClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._teams: typing.Optional[AsyncTeamsClient] = None
        self._permissions: typing.Optional[AsyncPermissionsClient] = None
        self._applications: typing.Optional[AsyncApplicationsClient] = None
        self._notifications: typing.Optional[AsyncNotificationsClient] = None
        self._artefact_matching_rules: typing.Optional[AsyncArtefactMatchingRulesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_version_v1version_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_version_v1version_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_version_v1version_get(request_options=request_options)
        return _response.data

    async def live_health_live_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Liveness probe.

        Returns 200 OK if the application process is running and responding to requests.
        Does not check external dependencies like the database.

        Use this probe with container orchestration to determine if the process should be restarted.
        Note that this should only be accessible internally (e.g. from the host container)
        and not accessible over the public API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.live_health_live_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.live_health_live_get(request_options=request_options)
        return _response.data

    async def ready_health_ready_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Readiness probe.

        Returns 200 OK if the application is ready to serve traffic, including database connectivity.
        Performs a simple database query to verify the connection is valid.

        Use this probe with container orchestration to determine if traffic should be routed to this pod.
        Note that this should only be accessible internally (e.g. from the host container)
        and not accessible over the public API.
        Returns 503 if the database is unavailable.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ready_health_ready_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.ready_health_ready_get(request_options=request_options)
        return _response.data

    async def root_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.root_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.root_get(request_options=request_options)
        return _response.data

    async def trigger_error_sentry_debug_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.trigger_error_sentry_debug_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.trigger_error_sentry_debug_get(request_options=request_options)
        return _response.data

    @property
    def test_executions(self):
        if self._test_executions is None:
            from .test_executions.client import AsyncTestExecutionsClient

            self._test_executions = AsyncTestExecutionsClient(client_wrapper=self._client_wrapper)
        return self._test_executions

    @property
    def artefacts(self):
        if self._artefacts is None:
            from .artefacts.client import AsyncArtefactsClient

            self._artefacts = AsyncArtefactsClient(client_wrapper=self._client_wrapper)
        return self._artefacts

    @property
    def reports(self):
        if self._reports is None:
            from .reports.client import AsyncReportsClient

            self._reports = AsyncReportsClient(client_wrapper=self._client_wrapper)
        return self._reports

    @property
    def test_cases(self):
        if self._test_cases is None:
            from .test_cases.client import AsyncTestCasesClient

            self._test_cases = AsyncTestCasesClient(client_wrapper=self._client_wrapper)
        return self._test_cases

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import AsyncEnvironmentsClient

            self._environments = AsyncEnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def test_plans(self):
        if self._test_plans is None:
            from .test_plans.client import AsyncTestPlansClient

            self._test_plans = AsyncTestPlansClient(client_wrapper=self._client_wrapper)
        return self._test_plans

    @property
    def issues(self):
        if self._issues is None:
            from .issues.client import AsyncIssuesClient

            self._issues = AsyncIssuesClient(client_wrapper=self._client_wrapper)
        return self._issues

    @property
    def test_results(self):
        if self._test_results is None:
            from .test_results.client import AsyncTestResultsClient

            self._test_results = AsyncTestResultsClient(client_wrapper=self._client_wrapper)
        return self._test_results

    @property
    def execution_metadata(self):
        if self._execution_metadata is None:
            from .execution_metadata.client import AsyncExecutionMetadataClient

            self._execution_metadata = AsyncExecutionMetadataClient(client_wrapper=self._client_wrapper)
        return self._execution_metadata

    @property
    def authentication(self):
        if self._authentication is None:
            from .authentication.client import AsyncAuthenticationClient

            self._authentication = AsyncAuthenticationClient(client_wrapper=self._client_wrapper)
        return self._authentication

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def teams(self):
        if self._teams is None:
            from .teams.client import AsyncTeamsClient

            self._teams = AsyncTeamsClient(client_wrapper=self._client_wrapper)
        return self._teams

    @property
    def permissions(self):
        if self._permissions is None:
            from .permissions.client import AsyncPermissionsClient

            self._permissions = AsyncPermissionsClient(client_wrapper=self._client_wrapper)
        return self._permissions

    @property
    def applications(self):
        if self._applications is None:
            from .applications.client import AsyncApplicationsClient

            self._applications = AsyncApplicationsClient(client_wrapper=self._client_wrapper)
        return self._applications

    @property
    def notifications(self):
        if self._notifications is None:
            from .notifications.client import AsyncNotificationsClient

            self._notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        return self._notifications

    @property
    def artefact_matching_rules(self):
        if self._artefact_matching_rules is None:
            from .artefact_matching_rules.client import AsyncArtefactMatchingRulesClient

            self._artefact_matching_rules = AsyncArtefactMatchingRulesClient(client_wrapper=self._client_wrapper)
        return self._artefact_matching_rules
