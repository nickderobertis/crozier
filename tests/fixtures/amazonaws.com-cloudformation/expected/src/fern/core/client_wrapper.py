

import typing

import httpx
from .http_client import AsyncHttpClient, HttpClient


class BaseClientWrapper:
    def __init__(
        self,
        *,
        amz_content_sha256: typing.Optional[str] = None,
        amz_date: typing.Optional[str] = None,
        amz_algorithm: typing.Optional[str] = None,
        amz_credential: typing.Optional[str] = None,
        amz_security_token: typing.Optional[str] = None,
        amz_signature: typing.Optional[str] = None,
        amz_signed_headers: typing.Optional[str] = None,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
    ):
        self._amz_content_sha256 = amz_content_sha256
        self._amz_date = amz_date
        self._amz_algorithm = amz_algorithm
        self._amz_credential = amz_credential
        self._amz_security_token = amz_security_token
        self._amz_signature = amz_signature
        self._amz_signed_headers = amz_signed_headers
        self.api_key = api_key
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
        if self._amz_content_sha256 is not None:
            headers["X-Amz-Content-Sha256"] = self._amz_content_sha256
        if self._amz_date is not None:
            headers["X-Amz-Date"] = self._amz_date
        if self._amz_algorithm is not None:
            headers["X-Amz-Algorithm"] = self._amz_algorithm
        if self._amz_credential is not None:
            headers["X-Amz-Credential"] = self._amz_credential
        if self._amz_security_token is not None:
            headers["X-Amz-Security-Token"] = self._amz_security_token
        if self._amz_signature is not None:
            headers["X-Amz-Signature"] = self._amz_signature
        if self._amz_signed_headers is not None:
            headers["X-Amz-SignedHeaders"] = self._amz_signed_headers
        headers["Authorization"] = self.api_key
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
        amz_content_sha256: typing.Optional[str] = None,
        amz_date: typing.Optional[str] = None,
        amz_algorithm: typing.Optional[str] = None,
        amz_credential: typing.Optional[str] = None,
        amz_security_token: typing.Optional[str] = None,
        amz_signature: typing.Optional[str] = None,
        amz_signed_headers: typing.Optional[str] = None,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.Client,
    ):
        super().__init__(
            amz_content_sha256=amz_content_sha256,
            amz_date=amz_date,
            amz_algorithm=amz_algorithm,
            amz_credential=amz_credential,
            amz_security_token=amz_security_token,
            amz_signature=amz_signature,
            amz_signed_headers=amz_signed_headers,
            api_key=api_key,
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
        amz_content_sha256: typing.Optional[str] = None,
        amz_date: typing.Optional[str] = None,
        amz_algorithm: typing.Optional[str] = None,
        amz_credential: typing.Optional[str] = None,
        amz_security_token: typing.Optional[str] = None,
        amz_signature: typing.Optional[str] = None,
        amz_signed_headers: typing.Optional[str] = None,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        base_url: str,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(
            amz_content_sha256=amz_content_sha256,
            amz_date=amz_date,
            amz_algorithm=amz_algorithm,
            amz_credential=amz_credential,
            amz_security_token=amz_security_token,
            amz_signature=amz_signature,
            amz_signed_headers=amz_signed_headers,
            api_key=api_key,
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
