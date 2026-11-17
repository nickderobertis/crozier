

import datetime as dt
import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.get_status_response import GetStatusResponse
from .types.institution import Institution
from .types.job import Job


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

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def get_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        The application root

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
        client.get_root()
        """
        _response = self._raw_client.get_root(request_options=request_options)
        return _response.data

    def get_admin(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        A single-page application where users can manage institutions and their associated harvest jobs

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The admin interface

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_admin()
        """
        _response = self._raw_client.get_admin(request_options=request_options)
        return _response.data

    def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetStatusResponse:
        """
        A response indicating the current status of the application. This may include information about the health of the server, details about which configuration options are engaged, and other things.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStatusResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_status()
        """
        _response = self._raw_client.get_status(request_options=request_options)
        return _response.data

    def list_institutions(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Institution]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Institution]
            A list of institutions

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_institutions()
        """
        _response = self._raw_client.list_institutions(request_options=request_options)
        return _response.data

    def add_institutions(
        self, *, request: typing.Sequence[Institution], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Institution]:
        """
        The endpoint for adding new institutions

        Parameters
        ----------
        request : typing.Sequence[Institution]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Institution]
            A list of institutions

        Examples
        --------
        from fern import FernApi, Institution

        client = FernApi()
        client.add_institutions(
            request=[
                Institution(
                    name="name",
                    description="description",
                    location="location",
                    website="website",
                )
            ],
        )
        """
        _response = self._raw_client.add_institutions(request=request, request_options=request_options)
        return _response.data

    def get_institution(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Institution:
        """
        Parameters
        ----------
        id : int
            The institution's unique identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Institution
            An institution

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_institution(
            id=1,
        )
        """
        _response = self._raw_client.get_institution(id, request_options=request_options)
        return _response.data

    def update_institution(
        self,
        id_: int,
        *,
        name: str,
        description: str,
        location: str,
        website: str,
        id: typing.Optional[int] = OMIT,
        email: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        web_contact: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Institution:
        """
        The endpoint for updating an institution

        Parameters
        ----------
        id_ : int
            The institution's unique identifier

        name : str

        description : str

        location : str

        website : str

        id : typing.Optional[int]
            The institution's unique identifier

        email : typing.Optional[str]

        phone : typing.Optional[str]

        web_contact : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Institution
            An institution

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.update_institution(
            id_=1,
            name="name",
            description="description",
            location="location",
            website="website",
        )
        """
        _response = self._raw_client.update_institution(
            id_,
            name=name,
            description=description,
            location=location,
            website=website,
            id=id,
            email=email,
            phone=phone,
            web_contact=web_contact,
            request_options=request_options,
        )
        return _response.data

    def remove_institution(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            The institution's unique identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.remove_institution(
            id=1,
        )
        """
        _response = self._raw_client.remove_institution(id, request_options=request_options)
        return _response.data

    def list_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Job]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Job]
            A list of jobs

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.list_jobs()
        """
        _response = self._raw_client.list_jobs(request_options=request_options)
        return _response.data

    def add_jobs(
        self, *, request: typing.Sequence[Job], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Job]:
        """
        The endpoint for adding new jobs

        Parameters
        ----------
        request : typing.Sequence[Job]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Job]
            A list of jobs

        Examples
        --------
        from fern import FernApi, Job

        client = FernApi()
        client.add_jobs(
            request=[
                Job(
                    institution_id=1,
                    repository_base_url="repositoryBaseURL",
                    metadata_prefix="metadataPrefix",
                    sets=["sets"],
                    schedule_cron_expression="0 5 * * 1",
                )
            ],
        )
        """
        _response = self._raw_client.add_jobs(request=request, request_options=request_options)
        return _response.data

    def get_job(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Parameters
        ----------
        id : int
            The job's unique identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            A job

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_job(
            id=1,
        )
        """
        _response = self._raw_client.get_job(id, request_options=request_options)
        return _response.data

    def update_job(
        self,
        id_: int,
        *,
        institution_id: int,
        repository_base_url: str,
        metadata_prefix: str,
        sets: typing.Sequence[str],
        schedule_cron_expression: str,
        id: typing.Optional[int] = OMIT,
        last_successful_run: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
        """
        The endpoint for updating a job

        Parameters
        ----------
        id_ : int
            The job's unique identifier

        institution_id : int

        repository_base_url : str

        metadata_prefix : str

        sets : typing.Sequence[str]

        schedule_cron_expression : str

        id : typing.Optional[int]
            The job's unique identifier

        last_successful_run : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            A job

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.update_job(
            id_=1,
            institution_id=1,
            repository_base_url="repositoryBaseURL",
            metadata_prefix="metadataPrefix",
            sets=["sets"],
            schedule_cron_expression="0 5 * * 1",
        )
        """
        _response = self._raw_client.update_job(
            id_,
            institution_id=institution_id,
            repository_base_url=repository_base_url,
            metadata_prefix=metadata_prefix,
            sets=sets,
            schedule_cron_expression=schedule_cron_expression,
            id=id,
            last_successful_run=last_successful_run,
            request_options=request_options,
        )
        return _response.data

    def remove_job(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            The job's unique identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.remove_job(
            id=1,
        )
        """
        _response = self._raw_client.remove_job(id, request_options=request_options)
        return _response.data


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

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def get_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        The application root

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
            await client.get_root()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_root(request_options=request_options)
        return _response.data

    async def get_admin(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        A single-page application where users can manage institutions and their associated harvest jobs

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The admin interface

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_admin()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin(request_options=request_options)
        return _response.data

    async def get_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetStatusResponse:
        """
        A response indicating the current status of the application. This may include information about the health of the server, details about which configuration options are engaged, and other things.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStatusResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status(request_options=request_options)
        return _response.data

    async def list_institutions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Institution]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Institution]
            A list of institutions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_institutions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_institutions(request_options=request_options)
        return _response.data

    async def add_institutions(
        self, *, request: typing.Sequence[Institution], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Institution]:
        """
        The endpoint for adding new institutions

        Parameters
        ----------
        request : typing.Sequence[Institution]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Institution]
            A list of institutions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Institution

        client = AsyncFernApi()


        async def main() -> None:
            await client.add_institutions(
                request=[
                    Institution(
                        name="name",
                        description="description",
                        location="location",
                        website="website",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_institutions(request=request, request_options=request_options)
        return _response.data

    async def get_institution(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Institution:
        """
        Parameters
        ----------
        id : int
            The institution's unique identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Institution
            An institution

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_institution(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_institution(id, request_options=request_options)
        return _response.data

    async def update_institution(
        self,
        id_: int,
        *,
        name: str,
        description: str,
        location: str,
        website: str,
        id: typing.Optional[int] = OMIT,
        email: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        web_contact: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Institution:
        """
        The endpoint for updating an institution

        Parameters
        ----------
        id_ : int
            The institution's unique identifier

        name : str

        description : str

        location : str

        website : str

        id : typing.Optional[int]
            The institution's unique identifier

        email : typing.Optional[str]

        phone : typing.Optional[str]

        web_contact : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Institution
            An institution

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.update_institution(
                id_=1,
                name="name",
                description="description",
                location="location",
                website="website",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_institution(
            id_,
            name=name,
            description=description,
            location=location,
            website=website,
            id=id,
            email=email,
            phone=phone,
            web_contact=web_contact,
            request_options=request_options,
        )
        return _response.data

    async def remove_institution(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            The institution's unique identifier

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
            await client.remove_institution(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_institution(id, request_options=request_options)
        return _response.data

    async def list_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Job]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Job]
            A list of jobs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.list_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_jobs(request_options=request_options)
        return _response.data

    async def add_jobs(
        self, *, request: typing.Sequence[Job], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Job]:
        """
        The endpoint for adding new jobs

        Parameters
        ----------
        request : typing.Sequence[Job]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Job]
            A list of jobs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Job

        client = AsyncFernApi()


        async def main() -> None:
            await client.add_jobs(
                request=[
                    Job(
                        institution_id=1,
                        repository_base_url="repositoryBaseURL",
                        metadata_prefix="metadataPrefix",
                        sets=["sets"],
                        schedule_cron_expression="0 5 * * 1",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_jobs(request=request, request_options=request_options)
        return _response.data

    async def get_job(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Parameters
        ----------
        id : int
            The job's unique identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            A job

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_job(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job(id, request_options=request_options)
        return _response.data

    async def update_job(
        self,
        id_: int,
        *,
        institution_id: int,
        repository_base_url: str,
        metadata_prefix: str,
        sets: typing.Sequence[str],
        schedule_cron_expression: str,
        id: typing.Optional[int] = OMIT,
        last_successful_run: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
        """
        The endpoint for updating a job

        Parameters
        ----------
        id_ : int
            The job's unique identifier

        institution_id : int

        repository_base_url : str

        metadata_prefix : str

        sets : typing.Sequence[str]

        schedule_cron_expression : str

        id : typing.Optional[int]
            The job's unique identifier

        last_successful_run : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            A job

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.update_job(
                id_=1,
                institution_id=1,
                repository_base_url="repositoryBaseURL",
                metadata_prefix="metadataPrefix",
                sets=["sets"],
                schedule_cron_expression="0 5 * * 1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_job(
            id_,
            institution_id=institution_id,
            repository_base_url=repository_base_url,
            metadata_prefix=metadata_prefix,
            sets=sets,
            schedule_cron_expression=schedule_cron_expression,
            id=id,
            last_successful_run=last_successful_run,
            request_options=request_options,
        )
        return _response.data

    async def remove_job(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            The job's unique identifier

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
            await client.remove_job(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_job(id, request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
