

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.graph_ql_response import GraphQlResponse

if typing.TYPE_CHECKING:
    from .service_credential.client import AsyncServiceCredentialClient, ServiceCredentialClient
    from .service_credential_type.client import AsyncServiceCredentialTypeClient, ServiceCredentialTypeClient
    from .service_instance.client import AsyncServiceInstanceClient, ServiceInstanceClient
    from .service_inventory.client import AsyncServiceInventoryClient, ServiceInventoryClient
    from .service_offering.client import AsyncServiceOfferingClient, ServiceOfferingClient
    from .service_offering_node.client import AsyncServiceOfferingNodeClient, ServiceOfferingNodeClient
    from .service_plan.client import AsyncServicePlanClient, ServicePlanClient
    from .source.client import AsyncSourceClient, SourceClient
    from .tags.client import AsyncTagsClient, TagsClient
    from .task.client import AsyncTaskClient, TaskClient

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



    base_path : typing.Optional[str]
        Server URL variable for 'basePath'. Defaults to '/api/catalog-inventory/v1.0'.

    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        base_path: typing.Optional[str] = None,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
        if base_path is not None:
            _base_path = base_path if base_path is not None else "/api/catalog-inventory/v1.0"
            base_url = "https://cloud.redhat.com/{basePath}".format(basePath=_base_path)
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            username=username,
            password=password,
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
        self._service_credential_type: typing.Optional[ServiceCredentialTypeClient] = None
        self._service_credential: typing.Optional[ServiceCredentialClient] = None
        self._service_instance: typing.Optional[ServiceInstanceClient] = None
        self._service_inventory: typing.Optional[ServiceInventoryClient] = None
        self._service_offering_node: typing.Optional[ServiceOfferingNodeClient] = None
        self._service_offering: typing.Optional[ServiceOfferingClient] = None
        self._service_plan: typing.Optional[ServicePlanClient] = None
        self._source: typing.Optional[SourceClient] = None
        self._tags: typing.Optional[TagsClient] = None
        self._task: typing.Optional[TaskClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def post_graph_ql(
        self,
        *,
        query: str,
        operation_name: typing.Optional[str] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GraphQlResponse:
        """
        Performs a GraphQL Query

        Parameters
        ----------
        query : str
            The GraphQL query

        operation_name : typing.Optional[str]
            If the Query contains several named operations, the operationName controls which one should be executed

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Optional Query variables

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GraphQlResponse
            GraphQL Query Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.post_graph_ql(
            query="query",
        )
        """
        _response = self._raw_client.post_graph_ql(
            query=query, operation_name=operation_name, variables=variables, request_options=request_options
        )
        return _response.data

    def get_documentation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The API document for this version of the API

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.get_documentation()
        """
        _response = self._raw_client.get_documentation(request_options=request_options)
        return _response.data

    @property
    def service_credential_type(self):
        if self._service_credential_type is None:
            from .service_credential_type.client import ServiceCredentialTypeClient

            self._service_credential_type = ServiceCredentialTypeClient(client_wrapper=self._client_wrapper)
        return self._service_credential_type

    @property
    def service_credential(self):
        if self._service_credential is None:
            from .service_credential.client import ServiceCredentialClient

            self._service_credential = ServiceCredentialClient(client_wrapper=self._client_wrapper)
        return self._service_credential

    @property
    def service_instance(self):
        if self._service_instance is None:
            from .service_instance.client import ServiceInstanceClient

            self._service_instance = ServiceInstanceClient(client_wrapper=self._client_wrapper)
        return self._service_instance

    @property
    def service_inventory(self):
        if self._service_inventory is None:
            from .service_inventory.client import ServiceInventoryClient

            self._service_inventory = ServiceInventoryClient(client_wrapper=self._client_wrapper)
        return self._service_inventory

    @property
    def service_offering_node(self):
        if self._service_offering_node is None:
            from .service_offering_node.client import ServiceOfferingNodeClient

            self._service_offering_node = ServiceOfferingNodeClient(client_wrapper=self._client_wrapper)
        return self._service_offering_node

    @property
    def service_offering(self):
        if self._service_offering is None:
            from .service_offering.client import ServiceOfferingClient

            self._service_offering = ServiceOfferingClient(client_wrapper=self._client_wrapper)
        return self._service_offering

    @property
    def service_plan(self):
        if self._service_plan is None:
            from .service_plan.client import ServicePlanClient

            self._service_plan = ServicePlanClient(client_wrapper=self._client_wrapper)
        return self._service_plan

    @property
    def source(self):
        if self._source is None:
            from .source.client import SourceClient

            self._source = SourceClient(client_wrapper=self._client_wrapper)
        return self._source

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import TagsClient

            self._tags = TagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def task(self):
        if self._task is None:
            from .task.client import TaskClient

            self._task = TaskClient(client_wrapper=self._client_wrapper)
        return self._task


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



    base_path : typing.Optional[str]
        Server URL variable for 'basePath'. Defaults to '/api/catalog-inventory/v1.0'.

    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        base_path: typing.Optional[str] = None,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
        if base_path is not None:
            _base_path = base_path if base_path is not None else "/api/catalog-inventory/v1.0"
            base_url = "https://cloud.redhat.com/{basePath}".format(basePath=_base_path)
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            username=username,
            password=password,
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
        self._service_credential_type: typing.Optional[AsyncServiceCredentialTypeClient] = None
        self._service_credential: typing.Optional[AsyncServiceCredentialClient] = None
        self._service_instance: typing.Optional[AsyncServiceInstanceClient] = None
        self._service_inventory: typing.Optional[AsyncServiceInventoryClient] = None
        self._service_offering_node: typing.Optional[AsyncServiceOfferingNodeClient] = None
        self._service_offering: typing.Optional[AsyncServiceOfferingClient] = None
        self._service_plan: typing.Optional[AsyncServicePlanClient] = None
        self._source: typing.Optional[AsyncSourceClient] = None
        self._tags: typing.Optional[AsyncTagsClient] = None
        self._task: typing.Optional[AsyncTaskClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def post_graph_ql(
        self,
        *,
        query: str,
        operation_name: typing.Optional[str] = OMIT,
        variables: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GraphQlResponse:
        """
        Performs a GraphQL Query

        Parameters
        ----------
        query : str
            The GraphQL query

        operation_name : typing.Optional[str]
            If the Query contains several named operations, the operationName controls which one should be executed

        variables : typing.Optional[typing.Dict[str, typing.Any]]
            Optional Query variables

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GraphQlResponse
            GraphQL Query Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.post_graph_ql(
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_graph_ql(
            query=query, operation_name=operation_name, variables=variables, request_options=request_options
        )
        return _response.data

    async def get_documentation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            The API document for this version of the API

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.get_documentation()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_documentation(request_options=request_options)
        return _response.data

    @property
    def service_credential_type(self):
        if self._service_credential_type is None:
            from .service_credential_type.client import AsyncServiceCredentialTypeClient

            self._service_credential_type = AsyncServiceCredentialTypeClient(client_wrapper=self._client_wrapper)
        return self._service_credential_type

    @property
    def service_credential(self):
        if self._service_credential is None:
            from .service_credential.client import AsyncServiceCredentialClient

            self._service_credential = AsyncServiceCredentialClient(client_wrapper=self._client_wrapper)
        return self._service_credential

    @property
    def service_instance(self):
        if self._service_instance is None:
            from .service_instance.client import AsyncServiceInstanceClient

            self._service_instance = AsyncServiceInstanceClient(client_wrapper=self._client_wrapper)
        return self._service_instance

    @property
    def service_inventory(self):
        if self._service_inventory is None:
            from .service_inventory.client import AsyncServiceInventoryClient

            self._service_inventory = AsyncServiceInventoryClient(client_wrapper=self._client_wrapper)
        return self._service_inventory

    @property
    def service_offering_node(self):
        if self._service_offering_node is None:
            from .service_offering_node.client import AsyncServiceOfferingNodeClient

            self._service_offering_node = AsyncServiceOfferingNodeClient(client_wrapper=self._client_wrapper)
        return self._service_offering_node

    @property
    def service_offering(self):
        if self._service_offering is None:
            from .service_offering.client import AsyncServiceOfferingClient

            self._service_offering = AsyncServiceOfferingClient(client_wrapper=self._client_wrapper)
        return self._service_offering

    @property
    def service_plan(self):
        if self._service_plan is None:
            from .service_plan.client import AsyncServicePlanClient

            self._service_plan = AsyncServicePlanClient(client_wrapper=self._client_wrapper)
        return self._service_plan

    @property
    def source(self):
        if self._source is None:
            from .source.client import AsyncSourceClient

            self._source = AsyncSourceClient(client_wrapper=self._client_wrapper)
        return self._source

    @property
    def tags(self):
        if self._tags is None:
            from .tags.client import AsyncTagsClient

            self._tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        return self._tags

    @property
    def task(self):
        if self._task is None:
            from .task.client import AsyncTaskClient

            self._task = AsyncTaskClient(client_wrapper=self._client_wrapper)
        return self._task


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
