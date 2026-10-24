

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.data import Data
from .types.data_types import DataTypes
from .types.field_value import FieldValue
from .types.raw_messages import RawMessages
from .types.seconds import Seconds
from .types.templates import Templates


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

    def get_all_messages_of_all_circuits(
        self,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Data:
        """
        Parameters
        ----------
        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Data
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_all_messages_of_all_circuits(
            since=1493483370,
        )
        """
        _response = self._raw_client.get_all_messages_of_all_circuits(
            since=since,
            poll=poll,
            verbose=verbose,
            indexed=indexed,
            numeric=numeric,
            valuename=valuename,
            full=full,
            required=required,
            write=write,
            raw=raw,
            def_=def_,
            user=user,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def get_all_messages_of_a_particular_circuit(
        self,
        circuit: str,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        exact: typing.Optional[bool] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Data:
        """
        Parameters
        ----------
        circuit : str

        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        exact : typing.Optional[bool]
            exact search for circuit/message name.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Data
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_all_messages_of_a_particular_circuit(
            circuit="circuit",
            since=1493483370,
        )
        """
        _response = self._raw_client.get_all_messages_of_a_particular_circuit(
            circuit,
            since=since,
            poll=poll,
            exact=exact,
            verbose=verbose,
            indexed=indexed,
            numeric=numeric,
            valuename=valuename,
            full=full,
            required=required,
            write=write,
            raw=raw,
            def_=def_,
            user=user,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def get_a_particular_message_of_a_particular_circuit(
        self,
        circuit: str,
        message: str,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        exact: typing.Optional[bool] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        define: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Data:
        """
        Parameters
        ----------
        circuit : str

        message : str

        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        exact : typing.Optional[bool]
            exact search for circuit/message name.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        define : typing.Optional[str]
            update/replace a message definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Data
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_a_particular_message_of_a_particular_circuit(
            circuit="circuit",
            message="message",
            since=1493483370,
        )
        """
        _response = self._raw_client.get_a_particular_message_of_a_particular_circuit(
            circuit,
            message,
            since=since,
            poll=poll,
            exact=exact,
            verbose=verbose,
            indexed=indexed,
            numeric=numeric,
            valuename=valuename,
            full=full,
            required=required,
            write=write,
            raw=raw,
            def_=def_,
            define=define,
            user=user,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    def get_all_known_field_data_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> DataTypes:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataTypes
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_all_known_field_data_types()
        """
        _response = self._raw_client.get_all_known_field_data_types(request_options=request_options)
        return _response.data

    def get_all_known_field_templates_for_the_root(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Templates:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Templates
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_all_known_field_templates_for_the_root()
        """
        _response = self._raw_client.get_all_known_field_templates_for_the_root(request_options=request_options)
        return _response.data

    def get_all_known_field_templates_for_the_path(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Templates:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Templates
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.get_all_known_field_templates_for_the_path(
            path="path",
        )
        """
        _response = self._raw_client.get_all_known_field_templates_for_the_path(path, request_options=request_options)
        return _response.data

    def retrieve_raw_data_from_grabbed_and_or_decoded_messages(
        self, *, since: typing.Optional[Seconds] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> RawMessages:
        """
        Parameters
        ----------
        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RawMessages
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.retrieve_raw_data_from_grabbed_and_or_decoded_messages(
            since=1493483370,
        )
        """
        _response = self._raw_client.retrieve_raw_data_from_grabbed_and_or_decoded_messages(
            since=since, request_options=request_options
        )
        return _response.data

    def decode_raw_data_with_the_specified_field_defintion(
        self, *, def_: str, raw: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[FieldValue]:
        """
        Parameters
        ----------
        def_ : str
            the field definition (starting with type).

        raw : str
            the raw symbols to decode as hex sequence.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FieldValue]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.decode_raw_data_with_the_specified_field_defintion(
            def_="def",
            raw="raw",
        )
        """
        _response = self._raw_client.decode_raw_data_with_the_specified_field_defintion(
            def_=def_, raw=raw, request_options=request_options
        )
        return _response.data

    def retrieve_a_particular_file(
        self, file: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        file : str
            the file to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.retrieve_a_particular_file(
            file="file",
        )
        """
        with self._raw_client.retrieve_a_particular_file(file, request_options=request_options) as r:
            yield from r.data


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

    async def get_all_messages_of_all_circuits(
        self,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Data:
        """
        Parameters
        ----------
        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Data
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_all_messages_of_all_circuits(
                since=1493483370,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_messages_of_all_circuits(
            since=since,
            poll=poll,
            verbose=verbose,
            indexed=indexed,
            numeric=numeric,
            valuename=valuename,
            full=full,
            required=required,
            write=write,
            raw=raw,
            def_=def_,
            user=user,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def get_all_messages_of_a_particular_circuit(
        self,
        circuit: str,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        exact: typing.Optional[bool] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Data:
        """
        Parameters
        ----------
        circuit : str

        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        exact : typing.Optional[bool]
            exact search for circuit/message name.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Data
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_all_messages_of_a_particular_circuit(
                circuit="circuit",
                since=1493483370,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_messages_of_a_particular_circuit(
            circuit,
            since=since,
            poll=poll,
            exact=exact,
            verbose=verbose,
            indexed=indexed,
            numeric=numeric,
            valuename=valuename,
            full=full,
            required=required,
            write=write,
            raw=raw,
            def_=def_,
            user=user,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def get_a_particular_message_of_a_particular_circuit(
        self,
        circuit: str,
        message: str,
        *,
        since: typing.Optional[Seconds] = None,
        poll: typing.Optional[int] = None,
        exact: typing.Optional[bool] = None,
        verbose: typing.Optional[bool] = None,
        indexed: typing.Optional[bool] = None,
        numeric: typing.Optional[bool] = None,
        valuename: typing.Optional[bool] = None,
        full: typing.Optional[bool] = None,
        required: typing.Optional[bool] = None,
        write: typing.Optional[bool] = None,
        raw: typing.Optional[bool] = None,
        def_: typing.Optional[bool] = None,
        define: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Data:
        """
        Parameters
        ----------
        circuit : str

        message : str

        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        poll : typing.Optional[int]
            set the poll priority of matching message(s) to prio.

        exact : typing.Optional[bool]
            exact search for circuit/message name.

        verbose : typing.Optional[bool]
            include comments and field units.

        indexed : typing.Optional[bool]
            always return field indexes instead of names.

        numeric : typing.Optional[bool]
            return numeric values of value list entries.

        valuename : typing.Optional[bool]
            include value and name for named values.

        full : typing.Optional[bool]
            include all available attributes.

        required : typing.Optional[bool]
            retrieve the data from the bus if not yet cached.

        write : typing.Optional[bool]
            retrieve write messages in addition to read/poll messages.

        raw : typing.Optional[bool]
            include raw master/slave data.

        def_ : typing.Optional[bool]
            include message and field definition.

        define : typing.Optional[str]
            update/replace a message definition.

        user : typing.Optional[str]
            authenticate with user name.

        secret : typing.Optional[str]
            authenticate with user secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Data
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_a_particular_message_of_a_particular_circuit(
                circuit="circuit",
                message="message",
                since=1493483370,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_particular_message_of_a_particular_circuit(
            circuit,
            message,
            since=since,
            poll=poll,
            exact=exact,
            verbose=verbose,
            indexed=indexed,
            numeric=numeric,
            valuename=valuename,
            full=full,
            required=required,
            write=write,
            raw=raw,
            def_=def_,
            define=define,
            user=user,
            secret=secret,
            request_options=request_options,
        )
        return _response.data

    async def get_all_known_field_data_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DataTypes:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataTypes
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_all_known_field_data_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_known_field_data_types(request_options=request_options)
        return _response.data

    async def get_all_known_field_templates_for_the_root(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Templates:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Templates
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_all_known_field_templates_for_the_root()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_known_field_templates_for_the_root(request_options=request_options)
        return _response.data

    async def get_all_known_field_templates_for_the_path(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Templates:
        """
        Parameters
        ----------
        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Templates
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.get_all_known_field_templates_for_the_path(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_known_field_templates_for_the_path(
            path, request_options=request_options
        )
        return _response.data

    async def retrieve_raw_data_from_grabbed_and_or_decoded_messages(
        self, *, since: typing.Optional[Seconds] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> RawMessages:
        """
        Parameters
        ----------
        since : typing.Optional[Seconds]
            limit to messages that have changed since the specified UTC seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RawMessages
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.retrieve_raw_data_from_grabbed_and_or_decoded_messages(
                since=1493483370,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_raw_data_from_grabbed_and_or_decoded_messages(
            since=since, request_options=request_options
        )
        return _response.data

    async def decode_raw_data_with_the_specified_field_defintion(
        self, *, def_: str, raw: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[FieldValue]:
        """
        Parameters
        ----------
        def_ : str
            the field definition (starting with type).

        raw : str
            the raw symbols to decode as hex sequence.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[FieldValue]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.decode_raw_data_with_the_specified_field_defintion(
                def_="def",
                raw="raw",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.decode_raw_data_with_the_specified_field_defintion(
            def_=def_, raw=raw, request_options=request_options
        )
        return _response.data

    async def retrieve_a_particular_file(
        self, file: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        file : str
            the file to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.retrieve_a_particular_file(
                file="file",
            )


        asyncio.run(main())
        """
        async with self._raw_client.retrieve_a_particular_file(file, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
