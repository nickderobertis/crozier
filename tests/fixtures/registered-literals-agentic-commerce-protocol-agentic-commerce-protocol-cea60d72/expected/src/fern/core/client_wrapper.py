

import datetime as dt
import typing

import httpx
from .http_client import AsyncHttpClient, HttpClient
from .logging import LogConfig, Logger


class BaseClientWrapper:
    def __init__(
        self,
        *,
        accept_language: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        signature: typing.Optional[str] = None,
        timestamp: typing.Optional[dt.datetime] = None,
        api_version: str,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        max_retries: int = 2,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        self._accept_language = accept_language
        self._idempotency_key = idempotency_key
        self._request_id = request_id
        self._signature = signature
        self._timestamp = timestamp
        self._api_version = api_version
        self._token = token
        self._headers = headers
        self._base_url = base_url
        self._timeout = timeout
        self._max_retries = max_retries
        self._stream_reconnection_enabled = stream_reconnection_enabled
        self._max_stream_reconnection_attempts = max_stream_reconnection_attempts
        self._logging = logging

    def get_headers(self, *, include_token: bool = True) -> typing.Dict[str, str]:
        import platform

        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-Runtime": f"python/{platform.python_version()}",
            "X-Fern-Platform": f"{platform.system().lower()}/{platform.release()}",
            "X-Fern-SDK-Name": "default_package_name",
            "X-Fern-SDK-Version": "0.0.0",
            **(self.get_custom_headers() or {}),
        }
        if self._accept_language is not None:
            headers["Accept-Language"] = self._accept_language
        if self._idempotency_key is not None:
            headers["Idempotency-Key"] = self._idempotency_key
        if self._request_id is not None:
            headers["Request-Id"] = self._request_id
        if self._signature is not None:
            headers["Signature"] = self._signature
        if self._timestamp is not None:
            headers["Timestamp"] = str(self._timestamp)
        headers["API-Version"] = self._api_version
        if include_token:
            headers["Authorization"] = f"Bearer {self._get_token()}"
        return headers

    def _get_token(self) -> str:
        if isinstance(self._token, str):
            return self._token
        else:
            return self._token()

    def get_custom_headers(self) -> typing.Optional[typing.Dict[str, str]]:
        return self._headers

    def get_base_url(self) -> str:
        return self._base_url

    def get_timeout(self) -> typing.Optional[float]:
        return self._timeout

    def get_max_retries(self) -> int:
        return self._max_retries

    def get_stream_reconnection_enabled(self) -> bool:
        return self._stream_reconnection_enabled if self._stream_reconnection_enabled is not None else True

    def get_max_stream_reconnection_attempts(self) -> typing.Optional[int]:
        return self._max_stream_reconnection_attempts


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        accept_language: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        signature: typing.Optional[str] = None,
        timestamp: typing.Optional[dt.datetime] = None,
        api_version: str,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        max_retries: int = 2,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
        httpx_client: httpx.Client,
    ):
        super().__init__(
            accept_language=accept_language,
            idempotency_key=idempotency_key,
            request_id=request_id,
            signature=signature,
            timestamp=timestamp,
            api_version=api_version,
            token=token,
            headers=headers,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self.httpx_client = HttpClient(
            httpx_client=httpx_client,
            base_headers=self.get_headers,
            base_timeout=self.get_timeout,
            base_url=self.get_base_url,
            base_max_retries=self.get_max_retries(),
            logging_config=self._logging,
        )


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        accept_language: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        signature: typing.Optional[str] = None,
        timestamp: typing.Optional[dt.datetime] = None,
        api_version: str,
        token: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        max_retries: int = 2,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(
            accept_language=accept_language,
            idempotency_key=idempotency_key,
            request_id=request_id,
            signature=signature,
            timestamp=timestamp,
            api_version=api_version,
            token=token,
            headers=headers,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._async_token = async_token
        self.httpx_client = AsyncHttpClient(
            httpx_client=httpx_client,
            base_headers=self.get_headers,
            base_timeout=self.get_timeout,
            base_url=self.get_base_url,
            base_max_retries=self.get_max_retries(),
            async_base_headers=self.async_get_headers,
            logging_config=self._logging,
        )

    async def async_get_headers(self) -> typing.Dict[str, str]:
        headers = self.get_headers(include_token=self._async_token is None)
        if self._async_token is not None:
            token = await self._async_token()
            headers["Authorization"] = f"Bearer {token}"
        return headers
