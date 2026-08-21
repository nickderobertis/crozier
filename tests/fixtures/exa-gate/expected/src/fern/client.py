

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.key_batch_action import KeyBatchAction
from .types.key_create import KeyCreate


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



    admin_session_id : str
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
        admin_session_id="YOUR_ADMIN_SESSION_ID",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        admin_session_id: str,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
            admin_session_id=admin_session_id,
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

    def get_proxy_live(
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
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_live()
        """
        _response = self._raw_client.get_proxy_live(request_options=request_options)
        return _response.data

    def get_proxy_ready(
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
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_ready()
        """
        _response = self._raw_client.get_proxy_ready(request_options=request_options)
        return _response.data

    def get_proxy_openapi_json(
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
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_openapi_json()
        """
        _response = self._raw_client.get_proxy_openapi_json(request_options=request_options)
        return _response.data

    def post_proxy_session(
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
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_session()
        """
        _response = self._raw_client.post_proxy_session(request_options=request_options)
        return _response.data

    def delete_proxy_session(
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
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.delete_proxy_session()
        """
        _response = self._raw_client.delete_proxy_session(request_options=request_options)
        return _response.data

    def get_proxy_health(
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
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_health()
        """
        _response = self._raw_client.get_proxy_health(request_options=request_options)
        return _response.data

    def get_proxy_config_summary(
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
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_config_summary()
        """
        _response = self._raw_client.get_proxy_config_summary(request_options=request_options)
        return _response.data

    def get_proxy_events(
        self,
        *,
        session_id: typing.Optional[str] = None,
        once: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[str]:
        """
        Parameters
        ----------
        session_id : typing.Optional[str]

        once : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            Server-sent events

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        response = client.get_proxy_events()
        for chunk in response:
            yield chunk
        """
        with self._raw_client.get_proxy_events(session_id=session_id, once=once, request_options=request_options) as r:
            yield from r.data

    def get_proxy_keys(
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
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_keys()
        """
        _response = self._raw_client.get_proxy_keys(request_options=request_options)
        return _response.data

    def post_proxy_keys(
        self,
        *,
        id: str,
        value: str,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        value : str

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_keys(
            id="id",
            value="value",
        )
        """
        _response = self._raw_client.post_proxy_keys(id=id, value=value, weight=weight, request_options=request_options)
        return _response.data

    def put_proxy_keys_id(
        self,
        id: str,
        *,
        value: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        value : typing.Optional[str]

        weight : typing.Optional[int]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.put_proxy_keys_id(
            id="id",
        )
        """
        _response = self._raw_client.put_proxy_keys_id(
            id, value=value, weight=weight, enabled=enabled, request_options=request_options
        )
        return _response.data

    def delete_proxy_keys_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.delete_proxy_keys_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_proxy_keys_id(id, request_options=request_options)
        return _response.data

    def post_proxy_keys_id_test(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_keys_id_test(
            id="id",
        )
        """
        _response = self._raw_client.post_proxy_keys_id_test(id, request_options=request_options)
        return _response.data

    def post_proxy_keys_id_disable(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_keys_id_disable(
            id="id",
        )
        """
        _response = self._raw_client.post_proxy_keys_id_disable(id, request_options=request_options)
        return _response.data

    def post_proxy_keys_id_enable(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_keys_id_enable(
            id="id",
        )
        """
        _response = self._raw_client.post_proxy_keys_id_enable(id, request_options=request_options)
        return _response.data

    def post_proxy_keys_id_reset_circuit(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_keys_id_reset_circuit(
            id="id",
        )
        """
        _response = self._raw_client.post_proxy_keys_id_reset_circuit(id, request_options=request_options)
        return _response.data

    def post_proxy_keys_id_secret(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_keys_id_secret(
            id="id",
        )
        """
        _response = self._raw_client.post_proxy_keys_id_secret(id, request_options=request_options)
        return _response.data

    def get_proxy_keys_id_failures(
        self, id: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_keys_id_failures(
            id="id",
        )
        """
        _response = self._raw_client.get_proxy_keys_id_failures(id, limit=limit, request_options=request_options)
        return _response.data

    def post_proxy_keys_batch(
        self,
        *,
        ids: typing.Sequence[str],
        action: KeyBatchAction,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        ids : typing.Sequence[str]

        action : KeyBatchAction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi, KeyBatchAction

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_keys_batch(
            ids=["ids"],
            action=KeyBatchAction.DISABLE,
        )
        """
        _response = self._raw_client.post_proxy_keys_batch(ids=ids, action=action, request_options=request_options)
        return _response.data

    def post_proxy_keys_import(
        self, *, keys: typing.Sequence[KeyCreate], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        keys : typing.Sequence[KeyCreate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi, KeyCreate

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_keys_import(
            keys=[
                KeyCreate(
                    id="id",
                    value="value",
                )
            ],
        )
        """
        _response = self._raw_client.post_proxy_keys_import(keys=keys, request_options=request_options)
        return _response.data

    def get_proxy_logs(
        self,
        *,
        limit: typing.Optional[int] = None,
        key_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        error_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        key_id : typing.Optional[str]

        path : typing.Optional[str]

        status : typing.Optional[str]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        error_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_logs()
        """
        _response = self._raw_client.get_proxy_logs(
            limit=limit,
            key_id=key_id,
            path=path,
            status=status,
            from_=from_,
            to=to,
            error_only=error_only,
            request_options=request_options,
        )
        return _response.data

    def get_proxy_logs_trace_request_id(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_logs_trace_request_id(
            request_id="requestId",
        )
        """
        _response = self._raw_client.get_proxy_logs_trace_request_id(request_id, request_options=request_options)
        return _response.data

    def get_proxy_logs_export(
        self,
        *,
        limit: typing.Optional[int] = None,
        key_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        error_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        key_id : typing.Optional[str]

        path : typing.Optional[str]

        status : typing.Optional[str]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        error_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSV export

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_logs_export()
        """
        _response = self._raw_client.get_proxy_logs_export(
            limit=limit,
            key_id=key_id,
            path=path,
            status=status,
            from_=from_,
            to=to,
            error_only=error_only,
            request_options=request_options,
        )
        return _response.data

    def post_proxy_logs_prune(
        self,
        *,
        older_than_ms: typing.Optional[int] = OMIT,
        days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        older_than_ms : typing.Optional[int]

        days : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_logs_prune()
        """
        _response = self._raw_client.post_proxy_logs_prune(
            older_than_ms=older_than_ms, days=days, request_options=request_options
        )
        return _response.data

    def get_proxy_observability(
        self, *, hours: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        hours : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_observability()
        """
        _response = self._raw_client.get_proxy_observability(hours=hours, request_options=request_options)
        return _response.data

    def get_proxy_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Prometheus exposition

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_metrics()
        """
        _response = self._raw_client.get_proxy_metrics(request_options=request_options)
        return _response.data

    def get_proxy_audit(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_audit()
        """
        _response = self._raw_client.get_proxy_audit(limit=limit, request_options=request_options)
        return _response.data

    def get_proxy_audit_export(
        self,
        *,
        limit: typing.Optional[int] = None,
        action: typing.Optional[str] = None,
        success: typing.Optional[bool] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        action : typing.Optional[str]

        success : typing.Optional[bool]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSV export

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.get_proxy_audit_export()
        """
        _response = self._raw_client.get_proxy_audit_export(
            limit=limit, action=action, success=success, from_=from_, to=to, request_options=request_options
        )
        return _response.data

    def post_proxy_alerts_webhook_test(
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
            JSON response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )
        client.post_proxy_alerts_webhook_test()
        """
        _response = self._raw_client.post_proxy_alerts_webhook_test(request_options=request_options)
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



    admin_session_id : str
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
        admin_session_id="YOUR_ADMIN_SESSION_ID",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        admin_session_id: str,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
            admin_session_id=admin_session_id,
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

    async def get_proxy_live(
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
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_live()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_live(request_options=request_options)
        return _response.data

    async def get_proxy_ready(
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
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_ready()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_ready(request_options=request_options)
        return _response.data

    async def get_proxy_openapi_json(
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
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_openapi_json()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_openapi_json(request_options=request_options)
        return _response.data

    async def post_proxy_session(
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
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_session(request_options=request_options)
        return _response.data

    async def delete_proxy_session(
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
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_proxy_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_proxy_session(request_options=request_options)
        return _response.data

    async def get_proxy_health(
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
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_health(request_options=request_options)
        return _response.data

    async def get_proxy_config_summary(
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
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_config_summary()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_config_summary(request_options=request_options)
        return _response.data

    async def get_proxy_events(
        self,
        *,
        session_id: typing.Optional[str] = None,
        once: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[str]:
        """
        Parameters
        ----------
        session_id : typing.Optional[str]

        once : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            Server-sent events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.get_proxy_events()
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.get_proxy_events(
            session_id=session_id, once=once, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_proxy_keys(
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
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_keys(request_options=request_options)
        return _response.data

    async def post_proxy_keys(
        self,
        *,
        id: str,
        value: str,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        value : str

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_keys(
                id="id",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_keys(
            id=id, value=value, weight=weight, request_options=request_options
        )
        return _response.data

    async def put_proxy_keys_id(
        self,
        id: str,
        *,
        value: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        value : typing.Optional[str]

        weight : typing.Optional[int]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.put_proxy_keys_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_proxy_keys_id(
            id, value=value, weight=weight, enabled=enabled, request_options=request_options
        )
        return _response.data

    async def delete_proxy_keys_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.delete_proxy_keys_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_proxy_keys_id(id, request_options=request_options)
        return _response.data

    async def post_proxy_keys_id_test(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_keys_id_test(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_keys_id_test(id, request_options=request_options)
        return _response.data

    async def post_proxy_keys_id_disable(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_keys_id_disable(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_keys_id_disable(id, request_options=request_options)
        return _response.data

    async def post_proxy_keys_id_enable(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_keys_id_enable(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_keys_id_enable(id, request_options=request_options)
        return _response.data

    async def post_proxy_keys_id_reset_circuit(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_keys_id_reset_circuit(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_keys_id_reset_circuit(id, request_options=request_options)
        return _response.data

    async def post_proxy_keys_id_secret(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_keys_id_secret(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_keys_id_secret(id, request_options=request_options)
        return _response.data

    async def get_proxy_keys_id_failures(
        self, id: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_keys_id_failures(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_keys_id_failures(id, limit=limit, request_options=request_options)
        return _response.data

    async def post_proxy_keys_batch(
        self,
        *,
        ids: typing.Sequence[str],
        action: KeyBatchAction,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        ids : typing.Sequence[str]

        action : KeyBatchAction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, KeyBatchAction

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_keys_batch(
                ids=["ids"],
                action=KeyBatchAction.DISABLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_keys_batch(
            ids=ids, action=action, request_options=request_options
        )
        return _response.data

    async def post_proxy_keys_import(
        self, *, keys: typing.Sequence[KeyCreate], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        keys : typing.Sequence[KeyCreate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, KeyCreate

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_keys_import(
                keys=[
                    KeyCreate(
                        id="id",
                        value="value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_keys_import(keys=keys, request_options=request_options)
        return _response.data

    async def get_proxy_logs(
        self,
        *,
        limit: typing.Optional[int] = None,
        key_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        error_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        key_id : typing.Optional[str]

        path : typing.Optional[str]

        status : typing.Optional[str]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        error_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_logs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_logs(
            limit=limit,
            key_id=key_id,
            path=path,
            status=status,
            from_=from_,
            to=to,
            error_only=error_only,
            request_options=request_options,
        )
        return _response.data

    async def get_proxy_logs_trace_request_id(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_logs_trace_request_id(
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_logs_trace_request_id(request_id, request_options=request_options)
        return _response.data

    async def get_proxy_logs_export(
        self,
        *,
        limit: typing.Optional[int] = None,
        key_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        error_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        key_id : typing.Optional[str]

        path : typing.Optional[str]

        status : typing.Optional[str]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        error_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSV export

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_logs_export()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_logs_export(
            limit=limit,
            key_id=key_id,
            path=path,
            status=status,
            from_=from_,
            to=to,
            error_only=error_only,
            request_options=request_options,
        )
        return _response.data

    async def post_proxy_logs_prune(
        self,
        *,
        older_than_ms: typing.Optional[int] = OMIT,
        days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        older_than_ms : typing.Optional[int]

        days : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_logs_prune()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_logs_prune(
            older_than_ms=older_than_ms, days=days, request_options=request_options
        )
        return _response.data

    async def get_proxy_observability(
        self, *, hours: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        hours : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_observability()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_observability(hours=hours, request_options=request_options)
        return _response.data

    async def get_proxy_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Prometheus exposition

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_metrics(request_options=request_options)
        return _response.data

    async def get_proxy_audit(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_audit()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_audit(limit=limit, request_options=request_options)
        return _response.data

    async def get_proxy_audit_export(
        self,
        *,
        limit: typing.Optional[int] = None,
        action: typing.Optional[str] = None,
        success: typing.Optional[bool] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        action : typing.Optional[str]

        success : typing.Optional[bool]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            CSV export

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.get_proxy_audit_export()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_proxy_audit_export(
            limit=limit, action=action, success=success, from_=from_, to=to, request_options=request_options
        )
        return _response.data

    async def post_proxy_alerts_webhook_test(
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
            JSON response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            admin_session_id="YOUR_ADMIN_SESSION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.post_proxy_alerts_webhook_test()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_proxy_alerts_webhook_test(request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
