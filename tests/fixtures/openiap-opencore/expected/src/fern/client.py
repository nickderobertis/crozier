

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.collection import Collection
from .types.create_collection_options_timeseries import CreateCollectionOptionsTimeseries
from .types.i_record_of_any import IRecordOfAny
from .types.i_string_to_string_dictionary import IStringToStringDictionary
from .types.query_params_sort import QueryParamsSort
from .types.user import User
from .types.workflow import Workflow


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

    def me(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[User]:
        """
        Returns the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.me()
        """
        _response = self._raw_client.me(request_options=request_options)
        return _response.data

    def get_users(
        self,
        *,
        limit: typing.Optional[float] = None,
        projection: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[User]:
        """
        Return a list of users ( max 100 by default)
        each users properties are limited to name, username, email, lastseen, Ude GetUser with _id to get all properties

        Parameters
        ----------
        limit : typing.Optional[float]

        projection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_users()
        """
        _response = self._raw_client.get_users(limit=limit, projection=projection, request_options=request_options)
        return _response.data

    def create_user(
        self,
        *,
        name: str,
        email: str,
        username: str,
        newpassword: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        name : str

        email : str

        username : str

        newpassword : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_user(
            name="name",
            email="email",
            username="username",
            newpassword="newpassword",
        )
        """
        _response = self._raw_client.create_user(
            name=name, email=email, username=username, newpassword=newpassword, request_options=request_options
        )
        return _response.data

    def get_user(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Return a user by _id

        Parameters
        ----------
        id : str
            _id of user to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_user(
            id="id",
        )
        """
        _response = self._raw_client.get_user(id, request_options=request_options)
        return _response.data

    def delete_user(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_user(
            id="id",
        )
        """
        _response = self._raw_client.delete_user(id, request_options=request_options)
        return _response.data

    def get_openrpaworkflows(
        self,
        *,
        limit: typing.Optional[float] = None,
        projection: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Workflow]:
        """
        Parameters
        ----------
        limit : typing.Optional[float]

        projection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Workflow]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_openrpaworkflows()
        """
        _response = self._raw_client.get_openrpaworkflows(
            limit=limit, projection=projection, request_options=request_options
        )
        return _response.data

    def create_open_rpa_workflow(
        self,
        *,
        name: str,
        background: bool,
        serializable: bool,
        filename: str,
        projectandname: str,
        xaml: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Workflow:
        """
        Parameters
        ----------
        name : str

        background : bool

        serializable : bool

        filename : str

        projectandname : str

        xaml : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workflow
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_open_rpa_workflow(
            name="name",
            background=True,
            serializable=True,
            filename="Filename",
            projectandname="projectandname",
            xaml="Xaml",
        )
        """
        _response = self._raw_client.create_open_rpa_workflow(
            name=name,
            background=background,
            serializable=serializable,
            filename=filename,
            projectandname=projectandname,
            xaml=xaml,
            request_options=request_options,
        )
        return _response.data

    def get_open_rpa_workflow(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Workflow:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workflow
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_open_rpa_workflow(
            id="id",
        )
        """
        _response = self._raw_client.get_open_rpa_workflow(id, request_options=request_options)
        return _response.data

    def delete_open_rpa_workflow(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.delete_open_rpa_workflow(
            id="id",
        )
        """
        _response = self._raw_client.delete_open_rpa_workflow(id, request_options=request_options)
        return _response.data

    def get_collections(
        self, *, includesystem: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Collection]:
        """
        Parameters
        ----------
        includesystem : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Collection]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_collections()
        """
        _response = self._raw_client.get_collections(includesystem=includesystem, request_options=request_options)
        return _response.data

    def create_collection(
        self,
        *,
        name: str,
        timeseries: typing.Optional[CreateCollectionOptionsTimeseries] = OMIT,
        expire_after_seconds: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collection:
        """
        Parameters
        ----------
        name : str

        timeseries : typing.Optional[CreateCollectionOptionsTimeseries]

        expire_after_seconds : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_collection(
            name="name",
        )
        """
        _response = self._raw_client.create_collection(
            name=name, timeseries=timeseries, expire_after_seconds=expire_after_seconds, request_options=request_options
        )
        return _response.data

    def get_collection(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Collection:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_collection(
            collectionname="collectionname",
        )
        """
        _response = self._raw_client.get_collection(collectionname, request_options=request_options)
        return _response.data

    def drop_collection(self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.drop_collection(
            collectionname="collectionname",
        )
        """
        _response = self._raw_client.drop_collection(collectionname, request_options=request_options)
        return _response.data

    def get_indexes(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.get_indexes(
            collectionname="collectionname",
        )
        """
        _response = self._raw_client.get_indexes(collectionname, request_options=request_options)
        return _response.data

    def create_index(
        self,
        collectionname: str,
        *,
        keypath: IRecordOfAny,
        name: typing.Optional[str] = OMIT,
        options: typing.Optional[IRecordOfAny] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        collectionname : str

        keypath : IRecordOfAny

        name : typing.Optional[str]

        options : typing.Optional[IRecordOfAny]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.create_index(
            collectionname="collectionname",
            keypath={"key": "value"},
        )
        """
        _response = self._raw_client.create_index(
            collectionname, keypath=keypath, name=name, options=options, request_options=request_options
        )
        return _response.data

    def drop_index(
        self, collectionname: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        collectionname : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.drop_index(
            collectionname="collectionname",
            name="name",
        )
        """
        _response = self._raw_client.drop_index(collectionname, name, request_options=request_options)
        return _response.data

    def query(
        self,
        collectionname: str,
        *,
        query: typing.Any,
        explain: typing.Optional[bool] = OMIT,
        queryas: typing.Optional[str] = OMIT,
        sort: typing.Optional[QueryParamsSort] = OMIT,
        skip: typing.Optional[float] = OMIT,
        top: typing.Optional[float] = OMIT,
        projection: typing.Optional[IStringToStringDictionary] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        collectionname : str

        query : typing.Any

        explain : typing.Optional[bool]

        queryas : typing.Optional[str]

        sort : typing.Optional[QueryParamsSort]

        skip : typing.Optional[float]

        top : typing.Optional[float]

        projection : typing.Optional[IStringToStringDictionary]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.query(
            collectionname="collectionname",
            query={"key": "value"},
        )
        """
        _response = self._raw_client.query(
            collectionname,
            query=query,
            explain=explain,
            queryas=queryas,
            sort=sort,
            skip=skip,
            top=top,
            projection=projection,
            request_options=request_options,
        )
        return _response.data

    def count(
        self,
        collectionname: str,
        *,
        query: typing.Any,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> float:
        """
        Parameters
        ----------
        collectionname : str

        query : typing.Any

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.count(
            collectionname="collectionname",
            query={"key": "value"},
        )
        """
        _response = self._raw_client.count(
            collectionname, query=query, queryas=queryas, request_options=request_options
        )
        return _response.data

    def distinct(
        self,
        collectionname: str,
        *,
        field: str,
        query: typing.Any,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        collectionname : str

        field : str

        query : typing.Any

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.distinct(
            collectionname="collectionname",
            field="field",
            query={"key": "value"},
        )
        """
        _response = self._raw_client.distinct(
            collectionname, field=field, query=query, queryas=queryas, request_options=request_options
        )
        return _response.data

    def aggregate(
        self,
        collectionname: str,
        *,
        pipeline: typing.Any,
        explain: typing.Optional[bool] = OMIT,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        collectionname : str

        pipeline : typing.Any

        explain : typing.Optional[bool]

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.aggregate(
            collectionname="collectionname",
            pipeline={"key": "value"},
        )
        """
        _response = self._raw_client.aggregate(
            collectionname, pipeline=pipeline, explain=explain, queryas=queryas, request_options=request_options
        )
        return _response.data

    def run_open_rpa_workflow(
        self,
        robotname: str,
        *,
        rpc: bool,
        workflowid: str,
        parameters: typing.Optional[IRecordOfAny] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IRecordOfAny:
        """
        Parameters
        ----------
        robotname : str

        rpc : bool

        workflowid : str

        parameters : typing.Optional[IRecordOfAny]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IRecordOfAny
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.run_open_rpa_workflow(
            robotname="robotname",
            rpc=True,
            workflowid="workflowid",
        )
        """
        _response = self._raw_client.run_open_rpa_workflow(
            robotname, rpc=rpc, workflowid=workflowid, parameters=parameters, request_options=request_options
        )
        return _response.data

    def queue_message(
        self, queuename: str, *, rpc: bool, payload: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> IRecordOfAny:
        """
        Parameters
        ----------
        queuename : str

        rpc : bool

        payload : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IRecordOfAny
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.queue_message(
            queuename="queuename",
            rpc=True,
            payload={"key": "value"},
        )
        """
        _response = self._raw_client.queue_message(queuename, rpc=rpc, payload=payload, request_options=request_options)
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

    async def me(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[User]:
        """
        Returns the current user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.me()


        asyncio.run(main())
        """
        _response = await self._raw_client.me(request_options=request_options)
        return _response.data

    async def get_users(
        self,
        *,
        limit: typing.Optional[float] = None,
        projection: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[User]:
        """
        Return a list of users ( max 100 by default)
        each users properties are limited to name, username, email, lastseen, Ude GetUser with _id to get all properties

        Parameters
        ----------
        limit : typing.Optional[float]

        projection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[User]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users(
            limit=limit, projection=projection, request_options=request_options
        )
        return _response.data

    async def create_user(
        self,
        *,
        name: str,
        email: str,
        username: str,
        newpassword: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> User:
        """
        Parameters
        ----------
        name : str

        email : str

        username : str

        newpassword : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_user(
                name="name",
                email="email",
                username="username",
                newpassword="newpassword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_user(
            name=name, email=email, username=username, newpassword=newpassword, request_options=request_options
        )
        return _response.data

    async def get_user(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> User:
        """
        Return a user by _id

        Parameters
        ----------
        id : str
            _id of user to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        User
            User

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_user(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(id, request_options=request_options)
        return _response.data

    async def delete_user(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_user(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user(id, request_options=request_options)
        return _response.data

    async def get_openrpaworkflows(
        self,
        *,
        limit: typing.Optional[float] = None,
        projection: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Workflow]:
        """
        Parameters
        ----------
        limit : typing.Optional[float]

        projection : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Workflow]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_openrpaworkflows()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_openrpaworkflows(
            limit=limit, projection=projection, request_options=request_options
        )
        return _response.data

    async def create_open_rpa_workflow(
        self,
        *,
        name: str,
        background: bool,
        serializable: bool,
        filename: str,
        projectandname: str,
        xaml: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Workflow:
        """
        Parameters
        ----------
        name : str

        background : bool

        serializable : bool

        filename : str

        projectandname : str

        xaml : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workflow
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_open_rpa_workflow(
                name="name",
                background=True,
                serializable=True,
                filename="Filename",
                projectandname="projectandname",
                xaml="Xaml",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_open_rpa_workflow(
            name=name,
            background=background,
            serializable=serializable,
            filename=filename,
            projectandname=projectandname,
            xaml=xaml,
            request_options=request_options,
        )
        return _response.data

    async def get_open_rpa_workflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Workflow:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Workflow
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_open_rpa_workflow(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_open_rpa_workflow(id, request_options=request_options)
        return _response.data

    async def delete_open_rpa_workflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_open_rpa_workflow(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_open_rpa_workflow(id, request_options=request_options)
        return _response.data

    async def get_collections(
        self, *, includesystem: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Collection]:
        """
        Parameters
        ----------
        includesystem : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Collection]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collections(includesystem=includesystem, request_options=request_options)
        return _response.data

    async def create_collection(
        self,
        *,
        name: str,
        timeseries: typing.Optional[CreateCollectionOptionsTimeseries] = OMIT,
        expire_after_seconds: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collection:
        """
        Parameters
        ----------
        name : str

        timeseries : typing.Optional[CreateCollectionOptionsTimeseries]

        expire_after_seconds : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_collection(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_collection(
            name=name, timeseries=timeseries, expire_after_seconds=expire_after_seconds, request_options=request_options
        )
        return _response.data

    async def get_collection(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Collection:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_collection(
                collectionname="collectionname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_collection(collectionname, request_options=request_options)
        return _response.data

    async def drop_collection(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.drop_collection(
                collectionname="collectionname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drop_collection(collectionname, request_options=request_options)
        return _response.data

    async def get_indexes(
        self, collectionname: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        collectionname : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_indexes(
                collectionname="collectionname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_indexes(collectionname, request_options=request_options)
        return _response.data

    async def create_index(
        self,
        collectionname: str,
        *,
        keypath: IRecordOfAny,
        name: typing.Optional[str] = OMIT,
        options: typing.Optional[IRecordOfAny] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        collectionname : str

        keypath : IRecordOfAny

        name : typing.Optional[str]

        options : typing.Optional[IRecordOfAny]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.create_index(
                collectionname="collectionname",
                keypath={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_index(
            collectionname, keypath=keypath, name=name, options=options, request_options=request_options
        )
        return _response.data

    async def drop_index(
        self, collectionname: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        collectionname : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.drop_index(
                collectionname="collectionname",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drop_index(collectionname, name, request_options=request_options)
        return _response.data

    async def query(
        self,
        collectionname: str,
        *,
        query: typing.Any,
        explain: typing.Optional[bool] = OMIT,
        queryas: typing.Optional[str] = OMIT,
        sort: typing.Optional[QueryParamsSort] = OMIT,
        skip: typing.Optional[float] = OMIT,
        top: typing.Optional[float] = OMIT,
        projection: typing.Optional[IStringToStringDictionary] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        collectionname : str

        query : typing.Any

        explain : typing.Optional[bool]

        queryas : typing.Optional[str]

        sort : typing.Optional[QueryParamsSort]

        skip : typing.Optional[float]

        top : typing.Optional[float]

        projection : typing.Optional[IStringToStringDictionary]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.query(
                collectionname="collectionname",
                query={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query(
            collectionname,
            query=query,
            explain=explain,
            queryas=queryas,
            sort=sort,
            skip=skip,
            top=top,
            projection=projection,
            request_options=request_options,
        )
        return _response.data

    async def count(
        self,
        collectionname: str,
        *,
        query: typing.Any,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> float:
        """
        Parameters
        ----------
        collectionname : str

        query : typing.Any

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.count(
                collectionname="collectionname",
                query={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.count(
            collectionname, query=query, queryas=queryas, request_options=request_options
        )
        return _response.data

    async def distinct(
        self,
        collectionname: str,
        *,
        field: str,
        query: typing.Any,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        collectionname : str

        field : str

        query : typing.Any

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.distinct(
                collectionname="collectionname",
                field="field",
                query={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.distinct(
            collectionname, field=field, query=query, queryas=queryas, request_options=request_options
        )
        return _response.data

    async def aggregate(
        self,
        collectionname: str,
        *,
        pipeline: typing.Any,
        explain: typing.Optional[bool] = OMIT,
        queryas: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Parameters
        ----------
        collectionname : str

        pipeline : typing.Any

        explain : typing.Optional[bool]

        queryas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Any]
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.aggregate(
                collectionname="collectionname",
                pipeline={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregate(
            collectionname, pipeline=pipeline, explain=explain, queryas=queryas, request_options=request_options
        )
        return _response.data

    async def run_open_rpa_workflow(
        self,
        robotname: str,
        *,
        rpc: bool,
        workflowid: str,
        parameters: typing.Optional[IRecordOfAny] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IRecordOfAny:
        """
        Parameters
        ----------
        robotname : str

        rpc : bool

        workflowid : str

        parameters : typing.Optional[IRecordOfAny]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IRecordOfAny
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.run_open_rpa_workflow(
                robotname="robotname",
                rpc=True,
                workflowid="workflowid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_open_rpa_workflow(
            robotname, rpc=rpc, workflowid=workflowid, parameters=parameters, request_options=request_options
        )
        return _response.data

    async def queue_message(
        self, queuename: str, *, rpc: bool, payload: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> IRecordOfAny:
        """
        Parameters
        ----------
        queuename : str

        rpc : bool

        payload : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IRecordOfAny
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.queue_message(
                queuename="queuename",
                rpc=True,
                payload={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.queue_message(
            queuename, rpc=rpc, payload=payload, request_options=request_options
        )
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
