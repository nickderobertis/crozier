

import typing

import httpx
from .http_client import AsyncHttpClient, HttpClient


class BaseClientWrapper:
    def __init__(
        self,
        *,
        cache_control: typing.Optional[str] = None,
        bunq_language: typing.Optional[str] = None,
        bunq_region: typing.Optional[str] = None,
        bunq_client_request_id: typing.Optional[str] = None,
        bunq_geolocation: typing.Optional[str] = None,
        bunq_client_authentication: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
    ):
        self._cache_control = cache_control
        self._bunq_language = bunq_language
        self._bunq_region = bunq_region
        self._bunq_client_request_id = bunq_client_request_id
        self._bunq_geolocation = bunq_geolocation
        self._bunq_client_authentication = bunq_client_authentication
        self._headers = headers
        self._base_url = base_url
        self._timeout = timeout

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "default_package_name",
            "X-Fern-SDK-Version": "0.0.0",
            **(self.get_custom_headers() or {}),
        }
        if self._cache_control is not None:
            headers["Cache-Control"] = self._cache_control
        if self._bunq_language is not None:
            headers["X-Bunq-Language"] = self._bunq_language
        if self._bunq_region is not None:
            headers["X-Bunq-Region"] = self._bunq_region
        if self._bunq_client_request_id is not None:
            headers["X-Bunq-Client-Request-Id"] = self._bunq_client_request_id
        if self._bunq_geolocation is not None:
            headers["X-Bunq-Geolocation"] = self._bunq_geolocation
        headers["X-Bunq-Client-Authentication"] = self._bunq_client_authentication
        return headers

    def get_custom_headers(self) -> typing.Optional[typing.Dict[str, str]]:
        return self._headers

    def get_base_url(self) -> str:
        return self._base_url

    def get_timeout(self) -> typing.Optional[float]:
        return self._timeout


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        cache_control: typing.Optional[str] = None,
        bunq_language: typing.Optional[str] = None,
        bunq_region: typing.Optional[str] = None,
        bunq_client_request_id: typing.Optional[str] = None,
        bunq_geolocation: typing.Optional[str] = None,
        bunq_client_authentication: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.Client,
    ):
        super().__init__(
            cache_control=cache_control,
            bunq_language=bunq_language,
            bunq_region=bunq_region,
            bunq_client_request_id=bunq_client_request_id,
            bunq_geolocation=bunq_geolocation,
            bunq_client_authentication=bunq_client_authentication,
            headers=headers,
            base_url=base_url,
            timeout=timeout,
        )
        self.httpx_client = HttpClient(
            httpx_client=httpx_client,
            base_headers=self.get_headers,
            base_timeout=self.get_timeout,
            base_url=self.get_base_url,
        )


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        cache_control: typing.Optional[str] = None,
        bunq_language: typing.Optional[str] = None,
        bunq_region: typing.Optional[str] = None,
        bunq_client_request_id: typing.Optional[str] = None,
        bunq_geolocation: typing.Optional[str] = None,
        bunq_client_authentication: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(
            cache_control=cache_control,
            bunq_language=bunq_language,
            bunq_region=bunq_region,
            bunq_client_request_id=bunq_client_request_id,
            bunq_geolocation=bunq_geolocation,
            bunq_client_authentication=bunq_client_authentication,
            headers=headers,
            base_url=base_url,
            timeout=timeout,
        )
        self.httpx_client = AsyncHttpClient(
            httpx_client=httpx_client,
            base_headers=self.get_headers,
            base_timeout=self.get_timeout,
            base_url=self.get_base_url,
        )
