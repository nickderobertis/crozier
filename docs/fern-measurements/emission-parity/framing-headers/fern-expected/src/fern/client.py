

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.parcel import Parcel


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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

    def send_lower(
        self,
        *,
        forwarded_proto: str,
        forwarded_host: str,
        forwarded_port: str,
        forwarded: str,
        real_ip: str,
        host: str,
        connection: str,
        transfer_encoding: str,
        te: str,
        trailer: str,
        upgrade: str,
        via: str,
        keep_alive: str,
        expect: str,
        date: str,
        accept: str,
        accept_encoding: str,
        accept_charset: str,
        accept_language: str,
        referer: str,
        content_encoding: str,
        content_md5: str,
        content_language: str,
        cache_control: str,
        pragma: str,
        proxy_authorization: str,
        dnt: str,
        sec_fetch_mode: str,
        request_id: str,
        if_match: str,
        range: str,
        authorization: str,
        csrf_token: str,
        http_method_override: str,
        set_cookie: str,
        forwarded_server: str,
        client_ip: str,
        true_client_ip: str,
        original_forwarded_for: str,
        content_range: str,
        idempotency_key: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Parcel:
        """
        Parameters
        ----------
        forwarded_proto : str

        forwarded_host : str

        forwarded_port : str

        forwarded : str

        real_ip : str

        host : str

        connection : str

        transfer_encoding : str

        te : str

        trailer : str

        upgrade : str

        via : str

        keep_alive : str

        expect : str

        date : str

        accept : str

        accept_encoding : str

        accept_charset : str

        accept_language : str

        referer : str

        content_encoding : str

        content_md5 : str

        content_language : str

        cache_control : str

        pragma : str

        proxy_authorization : str

        dnt : str

        sec_fetch_mode : str

        request_id : str

        if_match : str

        range : str

        authorization : str

        csrf_token : str

        http_method_override : str

        set_cookie : str

        forwarded_server : str

        client_ip : str

        true_client_ip : str

        original_forwarded_for : str

        content_range : str

        idempotency_key : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Parcel
            Accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.send_lower(
            forwarded_proto="v2",
            forwarded_host="v3",
            forwarded_port="v4",
            forwarded="v5",
            real_ip="v6",
            host="v7",
            connection="v8",
            transfer_encoding="v9",
            te="v10",
            trailer="v11",
            upgrade="v12",
            via="v13",
            keep_alive="v14",
            expect="v15",
            date="v16",
            accept="v17",
            accept_encoding="v18",
            accept_charset="v19",
            accept_language="v20",
            referer="v21",
            content_encoding="v22",
            content_md5="v23",
            content_language="v24",
            cache_control="v25",
            pragma="v26",
            proxy_authorization="v27",
            dnt="v28",
            sec_fetch_mode="v29",
            request_id="v30",
            if_match="v31",
            range="v32",
            authorization="v33",
            csrf_token="v34",
            http_method_override="v35",
            set_cookie="v40",
            forwarded_server="v41",
            client_ip="v42",
            true_client_ip="v43",
            original_forwarded_for="v44",
            content_range="v45",
            idempotency_key="v47",
            label="crate",
        )
        """
        _response = self._raw_client.send_lower(
            forwarded_proto=forwarded_proto,
            forwarded_host=forwarded_host,
            forwarded_port=forwarded_port,
            forwarded=forwarded,
            real_ip=real_ip,
            host=host,
            connection=connection,
            transfer_encoding=transfer_encoding,
            te=te,
            trailer=trailer,
            upgrade=upgrade,
            via=via,
            keep_alive=keep_alive,
            expect=expect,
            date=date,
            accept=accept,
            accept_encoding=accept_encoding,
            accept_charset=accept_charset,
            accept_language=accept_language,
            referer=referer,
            content_encoding=content_encoding,
            content_md5=content_md5,
            content_language=content_language,
            cache_control=cache_control,
            pragma=pragma,
            proxy_authorization=proxy_authorization,
            dnt=dnt,
            sec_fetch_mode=sec_fetch_mode,
            request_id=request_id,
            if_match=if_match,
            range=range,
            authorization=authorization,
            csrf_token=csrf_token,
            http_method_override=http_method_override,
            set_cookie=set_cookie,
            forwarded_server=forwarded_server,
            client_ip=client_ip,
            true_client_ip=true_client_ip,
            original_forwarded_for=original_forwarded_for,
            content_range=content_range,
            idempotency_key=idempotency_key,
            label=label,
            request_options=request_options,
        )
        return _response.data

    def send_canonical(
        self,
        *,
        forwarded_proto: str,
        forwarded_host: str,
        forwarded_port: str,
        forwarded: str,
        real_ip: str,
        host: str,
        connection: str,
        transfer_encoding: str,
        te: str,
        trailer: str,
        upgrade: str,
        via: str,
        keep_alive: str,
        expect: str,
        date: str,
        accept: str,
        accept_encoding: str,
        accept_charset: str,
        accept_language: str,
        referer: str,
        content_encoding: str,
        content_md5: str,
        content_language: str,
        cache_control: str,
        pragma: str,
        proxy_authorization: str,
        dnt: str,
        sec_fetch_mode: str,
        request_id: str,
        if_match: str,
        range: str,
        authorization: str,
        csrf_token: str,
        http_method_override: str,
        set_cookie: str,
        forwarded_server: str,
        client_ip: str,
        true_client_ip: str,
        original_forwarded_for: str,
        content_range: str,
        idempotency_key: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Parcel:
        """
        Parameters
        ----------
        forwarded_proto : str

        forwarded_host : str

        forwarded_port : str

        forwarded : str

        real_ip : str

        host : str

        connection : str

        transfer_encoding : str

        te : str

        trailer : str

        upgrade : str

        via : str

        keep_alive : str

        expect : str

        date : str

        accept : str

        accept_encoding : str

        accept_charset : str

        accept_language : str

        referer : str

        content_encoding : str

        content_md5 : str

        content_language : str

        cache_control : str

        pragma : str

        proxy_authorization : str

        dnt : str

        sec_fetch_mode : str

        request_id : str

        if_match : str

        range : str

        authorization : str

        csrf_token : str

        http_method_override : str

        set_cookie : str

        forwarded_server : str

        client_ip : str

        true_client_ip : str

        original_forwarded_for : str

        content_range : str

        idempotency_key : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Parcel
            Accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.send_canonical(
            forwarded_proto="c2",
            forwarded_host="c3",
            forwarded_port="c4",
            forwarded="c5",
            real_ip="c6",
            host="c7",
            connection="c8",
            transfer_encoding="c9",
            te="c10",
            trailer="c11",
            upgrade="c12",
            via="c13",
            keep_alive="c14",
            expect="c15",
            date="c16",
            accept="c17",
            accept_encoding="c18",
            accept_charset="c19",
            accept_language="c20",
            referer="c21",
            content_encoding="c22",
            content_md5="c23",
            content_language="c24",
            cache_control="c25",
            pragma="c26",
            proxy_authorization="c27",
            dnt="c28",
            sec_fetch_mode="c29",
            request_id="c30",
            if_match="c31",
            range="c32",
            authorization="c33",
            csrf_token="c34",
            http_method_override="c35",
            set_cookie="c40",
            forwarded_server="c41",
            client_ip="c42",
            true_client_ip="c43",
            original_forwarded_for="c44",
            content_range="c45",
            idempotency_key="c47",
            label="crate",
        )
        """
        _response = self._raw_client.send_canonical(
            forwarded_proto=forwarded_proto,
            forwarded_host=forwarded_host,
            forwarded_port=forwarded_port,
            forwarded=forwarded,
            real_ip=real_ip,
            host=host,
            connection=connection,
            transfer_encoding=transfer_encoding,
            te=te,
            trailer=trailer,
            upgrade=upgrade,
            via=via,
            keep_alive=keep_alive,
            expect=expect,
            date=date,
            accept=accept,
            accept_encoding=accept_encoding,
            accept_charset=accept_charset,
            accept_language=accept_language,
            referer=referer,
            content_encoding=content_encoding,
            content_md5=content_md5,
            content_language=content_language,
            cache_control=cache_control,
            pragma=pragma,
            proxy_authorization=proxy_authorization,
            dnt=dnt,
            sec_fetch_mode=sec_fetch_mode,
            request_id=request_id,
            if_match=if_match,
            range=range,
            authorization=authorization,
            csrf_token=csrf_token,
            http_method_override=http_method_override,
            set_cookie=set_cookie,
            forwarded_server=forwarded_server,
            client_ip=client_ip,
            true_client_ip=true_client_ip,
            original_forwarded_for=original_forwarded_for,
            content_range=content_range,
            idempotency_key=idempotency_key,
            label=label,
            request_options=request_options,
        )
        return _response.data

    def send_optional(
        self,
        *,
        label: str,
        forwarded_proto: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        transfer_encoding: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Parcel:
        """
        Parameters
        ----------
        label : str

        forwarded_proto : typing.Optional[str]

        host : typing.Optional[str]

        transfer_encoding : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Parcel
            Accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.send_optional(
            forwarded_proto="o2",
            host="o3",
            transfer_encoding="o4",
            label="crate",
        )
        """
        _response = self._raw_client.send_optional(
            label=label,
            forwarded_proto=forwarded_proto,
            host=host,
            transfer_encoding=transfer_encoding,
            request_options=request_options,
        )
        return _response.data

    def list_relays(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Parcel]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Parcel]
            The relays

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_relays()
        """
        _response = self._raw_client.list_relays(request_options=request_options)
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
    base_url : str
        The base url to use for requests from the client.

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
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
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
            base_url=base_url,
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

    async def send_lower(
        self,
        *,
        forwarded_proto: str,
        forwarded_host: str,
        forwarded_port: str,
        forwarded: str,
        real_ip: str,
        host: str,
        connection: str,
        transfer_encoding: str,
        te: str,
        trailer: str,
        upgrade: str,
        via: str,
        keep_alive: str,
        expect: str,
        date: str,
        accept: str,
        accept_encoding: str,
        accept_charset: str,
        accept_language: str,
        referer: str,
        content_encoding: str,
        content_md5: str,
        content_language: str,
        cache_control: str,
        pragma: str,
        proxy_authorization: str,
        dnt: str,
        sec_fetch_mode: str,
        request_id: str,
        if_match: str,
        range: str,
        authorization: str,
        csrf_token: str,
        http_method_override: str,
        set_cookie: str,
        forwarded_server: str,
        client_ip: str,
        true_client_ip: str,
        original_forwarded_for: str,
        content_range: str,
        idempotency_key: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Parcel:
        """
        Parameters
        ----------
        forwarded_proto : str

        forwarded_host : str

        forwarded_port : str

        forwarded : str

        real_ip : str

        host : str

        connection : str

        transfer_encoding : str

        te : str

        trailer : str

        upgrade : str

        via : str

        keep_alive : str

        expect : str

        date : str

        accept : str

        accept_encoding : str

        accept_charset : str

        accept_language : str

        referer : str

        content_encoding : str

        content_md5 : str

        content_language : str

        cache_control : str

        pragma : str

        proxy_authorization : str

        dnt : str

        sec_fetch_mode : str

        request_id : str

        if_match : str

        range : str

        authorization : str

        csrf_token : str

        http_method_override : str

        set_cookie : str

        forwarded_server : str

        client_ip : str

        true_client_ip : str

        original_forwarded_for : str

        content_range : str

        idempotency_key : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Parcel
            Accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.send_lower(
                forwarded_proto="v2",
                forwarded_host="v3",
                forwarded_port="v4",
                forwarded="v5",
                real_ip="v6",
                host="v7",
                connection="v8",
                transfer_encoding="v9",
                te="v10",
                trailer="v11",
                upgrade="v12",
                via="v13",
                keep_alive="v14",
                expect="v15",
                date="v16",
                accept="v17",
                accept_encoding="v18",
                accept_charset="v19",
                accept_language="v20",
                referer="v21",
                content_encoding="v22",
                content_md5="v23",
                content_language="v24",
                cache_control="v25",
                pragma="v26",
                proxy_authorization="v27",
                dnt="v28",
                sec_fetch_mode="v29",
                request_id="v30",
                if_match="v31",
                range="v32",
                authorization="v33",
                csrf_token="v34",
                http_method_override="v35",
                set_cookie="v40",
                forwarded_server="v41",
                client_ip="v42",
                true_client_ip="v43",
                original_forwarded_for="v44",
                content_range="v45",
                idempotency_key="v47",
                label="crate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_lower(
            forwarded_proto=forwarded_proto,
            forwarded_host=forwarded_host,
            forwarded_port=forwarded_port,
            forwarded=forwarded,
            real_ip=real_ip,
            host=host,
            connection=connection,
            transfer_encoding=transfer_encoding,
            te=te,
            trailer=trailer,
            upgrade=upgrade,
            via=via,
            keep_alive=keep_alive,
            expect=expect,
            date=date,
            accept=accept,
            accept_encoding=accept_encoding,
            accept_charset=accept_charset,
            accept_language=accept_language,
            referer=referer,
            content_encoding=content_encoding,
            content_md5=content_md5,
            content_language=content_language,
            cache_control=cache_control,
            pragma=pragma,
            proxy_authorization=proxy_authorization,
            dnt=dnt,
            sec_fetch_mode=sec_fetch_mode,
            request_id=request_id,
            if_match=if_match,
            range=range,
            authorization=authorization,
            csrf_token=csrf_token,
            http_method_override=http_method_override,
            set_cookie=set_cookie,
            forwarded_server=forwarded_server,
            client_ip=client_ip,
            true_client_ip=true_client_ip,
            original_forwarded_for=original_forwarded_for,
            content_range=content_range,
            idempotency_key=idempotency_key,
            label=label,
            request_options=request_options,
        )
        return _response.data

    async def send_canonical(
        self,
        *,
        forwarded_proto: str,
        forwarded_host: str,
        forwarded_port: str,
        forwarded: str,
        real_ip: str,
        host: str,
        connection: str,
        transfer_encoding: str,
        te: str,
        trailer: str,
        upgrade: str,
        via: str,
        keep_alive: str,
        expect: str,
        date: str,
        accept: str,
        accept_encoding: str,
        accept_charset: str,
        accept_language: str,
        referer: str,
        content_encoding: str,
        content_md5: str,
        content_language: str,
        cache_control: str,
        pragma: str,
        proxy_authorization: str,
        dnt: str,
        sec_fetch_mode: str,
        request_id: str,
        if_match: str,
        range: str,
        authorization: str,
        csrf_token: str,
        http_method_override: str,
        set_cookie: str,
        forwarded_server: str,
        client_ip: str,
        true_client_ip: str,
        original_forwarded_for: str,
        content_range: str,
        idempotency_key: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Parcel:
        """
        Parameters
        ----------
        forwarded_proto : str

        forwarded_host : str

        forwarded_port : str

        forwarded : str

        real_ip : str

        host : str

        connection : str

        transfer_encoding : str

        te : str

        trailer : str

        upgrade : str

        via : str

        keep_alive : str

        expect : str

        date : str

        accept : str

        accept_encoding : str

        accept_charset : str

        accept_language : str

        referer : str

        content_encoding : str

        content_md5 : str

        content_language : str

        cache_control : str

        pragma : str

        proxy_authorization : str

        dnt : str

        sec_fetch_mode : str

        request_id : str

        if_match : str

        range : str

        authorization : str

        csrf_token : str

        http_method_override : str

        set_cookie : str

        forwarded_server : str

        client_ip : str

        true_client_ip : str

        original_forwarded_for : str

        content_range : str

        idempotency_key : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Parcel
            Accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.send_canonical(
                forwarded_proto="c2",
                forwarded_host="c3",
                forwarded_port="c4",
                forwarded="c5",
                real_ip="c6",
                host="c7",
                connection="c8",
                transfer_encoding="c9",
                te="c10",
                trailer="c11",
                upgrade="c12",
                via="c13",
                keep_alive="c14",
                expect="c15",
                date="c16",
                accept="c17",
                accept_encoding="c18",
                accept_charset="c19",
                accept_language="c20",
                referer="c21",
                content_encoding="c22",
                content_md5="c23",
                content_language="c24",
                cache_control="c25",
                pragma="c26",
                proxy_authorization="c27",
                dnt="c28",
                sec_fetch_mode="c29",
                request_id="c30",
                if_match="c31",
                range="c32",
                authorization="c33",
                csrf_token="c34",
                http_method_override="c35",
                set_cookie="c40",
                forwarded_server="c41",
                client_ip="c42",
                true_client_ip="c43",
                original_forwarded_for="c44",
                content_range="c45",
                idempotency_key="c47",
                label="crate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_canonical(
            forwarded_proto=forwarded_proto,
            forwarded_host=forwarded_host,
            forwarded_port=forwarded_port,
            forwarded=forwarded,
            real_ip=real_ip,
            host=host,
            connection=connection,
            transfer_encoding=transfer_encoding,
            te=te,
            trailer=trailer,
            upgrade=upgrade,
            via=via,
            keep_alive=keep_alive,
            expect=expect,
            date=date,
            accept=accept,
            accept_encoding=accept_encoding,
            accept_charset=accept_charset,
            accept_language=accept_language,
            referer=referer,
            content_encoding=content_encoding,
            content_md5=content_md5,
            content_language=content_language,
            cache_control=cache_control,
            pragma=pragma,
            proxy_authorization=proxy_authorization,
            dnt=dnt,
            sec_fetch_mode=sec_fetch_mode,
            request_id=request_id,
            if_match=if_match,
            range=range,
            authorization=authorization,
            csrf_token=csrf_token,
            http_method_override=http_method_override,
            set_cookie=set_cookie,
            forwarded_server=forwarded_server,
            client_ip=client_ip,
            true_client_ip=true_client_ip,
            original_forwarded_for=original_forwarded_for,
            content_range=content_range,
            idempotency_key=idempotency_key,
            label=label,
            request_options=request_options,
        )
        return _response.data

    async def send_optional(
        self,
        *,
        label: str,
        forwarded_proto: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        transfer_encoding: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Parcel:
        """
        Parameters
        ----------
        label : str

        forwarded_proto : typing.Optional[str]

        host : typing.Optional[str]

        transfer_encoding : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Parcel
            Accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.send_optional(
                forwarded_proto="o2",
                host="o3",
                transfer_encoding="o4",
                label="crate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_optional(
            label=label,
            forwarded_proto=forwarded_proto,
            host=host,
            transfer_encoding=transfer_encoding,
            request_options=request_options,
        )
        return _response.data

    async def list_relays(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Parcel]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Parcel]
            The relays

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_relays()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_relays(request_options=request_options)
        return _response.data
