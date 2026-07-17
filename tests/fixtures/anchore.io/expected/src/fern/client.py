

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.file_content_search_list import FileContentSearchList
from .types.retrieved_file_list import RetrievedFileList
from .types.secret_search_list import SecretSearchList
from .types.service_version import ServiceVersion
from .types.token_response import TokenResponse

if typing.TYPE_CHECKING:
    from .archives.client import ArchivesClient, AsyncArchivesClient
    from .events.client import AsyncEventsClient, EventsClient
    from .identity.client import AsyncIdentityClient, IdentityClient
    from .images.client import AsyncImagesClient, ImagesClient
    from .import_.client import AsyncImportClient, ImportClient
    from .imports.client import AsyncImportsClient, ImportsClient
    from .policies.client import AsyncPoliciesClient, PoliciesClient
    from .query.client import AsyncQueryClient, QueryClient
    from .registries.client import AsyncRegistriesClient, RegistriesClient
    from .repository_credentials.client import AsyncRepositoryCredentialsClient, RepositoryCredentialsClient
    from .subscriptions.client import AsyncSubscriptionsClient, SubscriptionsClient
    from .summaries.client import AsyncSummariesClient, SummariesClient
    from .system.client import AsyncSystemClient, SystemClient
    from .user_management.client import AsyncUserManagementClient, UserManagementClient

OMIT = typing.cast(typing.Any, ...)


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
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._identity: typing.Optional[IdentityClient] = None
        self._user_management: typing.Optional[UserManagementClient] = None
        self._archives: typing.Optional[ArchivesClient] = None
        self._events: typing.Optional[EventsClient] = None
        self._images: typing.Optional[ImagesClient] = None
        self._import_: typing.Optional[ImportClient] = None
        self._imports: typing.Optional[ImportsClient] = None
        self._policies: typing.Optional[PoliciesClient] = None
        self._query: typing.Optional[QueryClient] = None
        self._registries: typing.Optional[RegistriesClient] = None
        self._repository_credentials: typing.Optional[RepositoryCredentialsClient] = None
        self._system: typing.Optional[SystemClient] = None
        self._subscriptions: typing.Optional[SubscriptionsClient] = None
        self._summaries: typing.Optional[SummariesClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Simple status check

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Version check response, returns the api version prefix (e.g. 'v1')

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ping()
        """
        _response = self._raw_client.ping(request_options=request_options)
        return _response.data

    def health_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Health check, returns 200 and no body if service is running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.health_check()
        """
        _response = self._raw_client.health_check(request_options=request_options)
        return _response.data

    def list_file_content_search_results(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FileContentSearchList:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileContentSearchList
            List of file metadata objects

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_file_content_search_results(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.list_file_content_search_results(image_digest, request_options=request_options)
        return _response.data

    def list_retrieved_files(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrievedFileList:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrievedFileList
            List of file metadata objects

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_retrieved_files(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.list_retrieved_files(image_digest, request_options=request_options)
        return _response.data

    def list_secret_search_results(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SecretSearchList:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SecretSearchList
            List of file metadata objects

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_secret_search_results(
            image_digest="imageDigest",
        )
        """
        _response = self._raw_client.list_secret_search_results(image_digest, request_options=request_options)
        return _response.data

    def get_oauth_token(
        self,
        *,
        client_id: typing.Optional[str] = OMIT,
        grant_type: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Request a jwt token for subsequent operations, this request is authenticated with normal HTTP auth

        Parameters
        ----------
        client_id : typing.Optional[str]
            The type of client used for the OAuth token

        grant_type : typing.Optional[str]
            OAuth Grant type for token

        password : typing.Optional[str]
            Password for corresponding user

        username : typing.Optional[str]
            User to assign OAuth token to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Resulting JWT token

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_oauth_token()
        """
        _response = self._raw_client.get_oauth_token(
            client_id=client_id,
            grant_type=grant_type,
            password=password,
            username=username,
            request_options=request_options,
        )
        return _response.data

    def version_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServiceVersion:
        """
        Returns the version object for the service, including db schema version info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceVersion
            Version object describing version state

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.version_check()
        """
        _response = self._raw_client.version_check(request_options=request_options)
        return _response.data

    @property
    def identity(self):
        if self._identity is None:
            from .identity.client import IdentityClient

            self._identity = IdentityClient(client_wrapper=self._client_wrapper)
        return self._identity

    @property
    def user_management(self):
        if self._user_management is None:
            from .user_management.client import UserManagementClient

            self._user_management = UserManagementClient(client_wrapper=self._client_wrapper)
        return self._user_management

    @property
    def archives(self):
        if self._archives is None:
            from .archives.client import ArchivesClient

            self._archives = ArchivesClient(client_wrapper=self._client_wrapper)
        return self._archives

    @property
    def events(self):
        if self._events is None:
            from .events.client import EventsClient

            self._events = EventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def images(self):
        if self._images is None:
            from .images.client import ImagesClient

            self._images = ImagesClient(client_wrapper=self._client_wrapper)
        return self._images

    @property
    def import_(self):
        if self._import_ is None:
            from .import_.client import ImportClient

            self._import_ = ImportClient(client_wrapper=self._client_wrapper)
        return self._import_

    @property
    def imports(self):
        if self._imports is None:
            from .imports.client import ImportsClient

            self._imports = ImportsClient(client_wrapper=self._client_wrapper)
        return self._imports

    @property
    def policies(self):
        if self._policies is None:
            from .policies.client import PoliciesClient

            self._policies = PoliciesClient(client_wrapper=self._client_wrapper)
        return self._policies

    @property
    def query(self):
        if self._query is None:
            from .query.client import QueryClient

            self._query = QueryClient(client_wrapper=self._client_wrapper)
        return self._query

    @property
    def registries(self):
        if self._registries is None:
            from .registries.client import RegistriesClient

            self._registries = RegistriesClient(client_wrapper=self._client_wrapper)
        return self._registries

    @property
    def repository_credentials(self):
        if self._repository_credentials is None:
            from .repository_credentials.client import RepositoryCredentialsClient

            self._repository_credentials = RepositoryCredentialsClient(client_wrapper=self._client_wrapper)
        return self._repository_credentials

    @property
    def system(self):
        if self._system is None:
            from .system.client import SystemClient

            self._system = SystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def subscriptions(self):
        if self._subscriptions is None:
            from .subscriptions.client import SubscriptionsClient

            self._subscriptions = SubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._subscriptions

    @property
    def summaries(self):
        if self._summaries is None:
            from .summaries.client import SummariesClient

            self._summaries = SummariesClient(client_wrapper=self._client_wrapper)
        return self._summaries


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
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._identity: typing.Optional[AsyncIdentityClient] = None
        self._user_management: typing.Optional[AsyncUserManagementClient] = None
        self._archives: typing.Optional[AsyncArchivesClient] = None
        self._events: typing.Optional[AsyncEventsClient] = None
        self._images: typing.Optional[AsyncImagesClient] = None
        self._import_: typing.Optional[AsyncImportClient] = None
        self._imports: typing.Optional[AsyncImportsClient] = None
        self._policies: typing.Optional[AsyncPoliciesClient] = None
        self._query: typing.Optional[AsyncQueryClient] = None
        self._registries: typing.Optional[AsyncRegistriesClient] = None
        self._repository_credentials: typing.Optional[AsyncRepositoryCredentialsClient] = None
        self._system: typing.Optional[AsyncSystemClient] = None
        self._subscriptions: typing.Optional[AsyncSubscriptionsClient] = None
        self._summaries: typing.Optional[AsyncSummariesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Simple status check

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Version check response, returns the api version prefix (e.g. 'v1')

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping(request_options=request_options)
        return _response.data

    async def health_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Health check, returns 200 and no body if service is running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.health_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.health_check(request_options=request_options)
        return _response.data

    async def list_file_content_search_results(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FileContentSearchList:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileContentSearchList
            List of file metadata objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_file_content_search_results(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_file_content_search_results(
            image_digest, request_options=request_options
        )
        return _response.data

    async def list_retrieved_files(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrievedFileList:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrievedFileList
            List of file metadata objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_retrieved_files(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_retrieved_files(image_digest, request_options=request_options)
        return _response.data

    async def list_secret_search_results(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SecretSearchList:
        """
        Parameters
        ----------
        image_digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SecretSearchList
            List of file metadata objects

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_secret_search_results(
                image_digest="imageDigest",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_secret_search_results(image_digest, request_options=request_options)
        return _response.data

    async def get_oauth_token(
        self,
        *,
        client_id: typing.Optional[str] = OMIT,
        grant_type: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokenResponse:
        """
        Request a jwt token for subsequent operations, this request is authenticated with normal HTTP auth

        Parameters
        ----------
        client_id : typing.Optional[str]
            The type of client used for the OAuth token

        grant_type : typing.Optional[str]
            OAuth Grant type for token

        password : typing.Optional[str]
            Password for corresponding user

        username : typing.Optional[str]
            User to assign OAuth token to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponse
            Resulting JWT token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_oauth_token()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_oauth_token(
            client_id=client_id,
            grant_type=grant_type,
            password=password,
            username=username,
            request_options=request_options,
        )
        return _response.data

    async def version_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> ServiceVersion:
        """
        Returns the version object for the service, including db schema version info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceVersion
            Version object describing version state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.version_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.version_check(request_options=request_options)
        return _response.data

    @property
    def identity(self):
        if self._identity is None:
            from .identity.client import AsyncIdentityClient

            self._identity = AsyncIdentityClient(client_wrapper=self._client_wrapper)
        return self._identity

    @property
    def user_management(self):
        if self._user_management is None:
            from .user_management.client import AsyncUserManagementClient

            self._user_management = AsyncUserManagementClient(client_wrapper=self._client_wrapper)
        return self._user_management

    @property
    def archives(self):
        if self._archives is None:
            from .archives.client import AsyncArchivesClient

            self._archives = AsyncArchivesClient(client_wrapper=self._client_wrapper)
        return self._archives

    @property
    def events(self):
        if self._events is None:
            from .events.client import AsyncEventsClient

            self._events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        return self._events

    @property
    def images(self):
        if self._images is None:
            from .images.client import AsyncImagesClient

            self._images = AsyncImagesClient(client_wrapper=self._client_wrapper)
        return self._images

    @property
    def import_(self):
        if self._import_ is None:
            from .import_.client import AsyncImportClient

            self._import_ = AsyncImportClient(client_wrapper=self._client_wrapper)
        return self._import_

    @property
    def imports(self):
        if self._imports is None:
            from .imports.client import AsyncImportsClient

            self._imports = AsyncImportsClient(client_wrapper=self._client_wrapper)
        return self._imports

    @property
    def policies(self):
        if self._policies is None:
            from .policies.client import AsyncPoliciesClient

            self._policies = AsyncPoliciesClient(client_wrapper=self._client_wrapper)
        return self._policies

    @property
    def query(self):
        if self._query is None:
            from .query.client import AsyncQueryClient

            self._query = AsyncQueryClient(client_wrapper=self._client_wrapper)
        return self._query

    @property
    def registries(self):
        if self._registries is None:
            from .registries.client import AsyncRegistriesClient

            self._registries = AsyncRegistriesClient(client_wrapper=self._client_wrapper)
        return self._registries

    @property
    def repository_credentials(self):
        if self._repository_credentials is None:
            from .repository_credentials.client import AsyncRepositoryCredentialsClient

            self._repository_credentials = AsyncRepositoryCredentialsClient(client_wrapper=self._client_wrapper)
        return self._repository_credentials

    @property
    def system(self):
        if self._system is None:
            from .system.client import AsyncSystemClient

            self._system = AsyncSystemClient(client_wrapper=self._client_wrapper)
        return self._system

    @property
    def subscriptions(self):
        if self._subscriptions is None:
            from .subscriptions.client import AsyncSubscriptionsClient

            self._subscriptions = AsyncSubscriptionsClient(client_wrapper=self._client_wrapper)
        return self._subscriptions

    @property
    def summaries(self):
        if self._summaries is None:
            from .summaries.client import AsyncSummariesClient

            self._summaries = AsyncSummariesClient(client_wrapper=self._client_wrapper)
        return self._summaries


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
