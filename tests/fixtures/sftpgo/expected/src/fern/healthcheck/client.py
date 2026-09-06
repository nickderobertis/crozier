

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawHealthcheckClient, RawHealthcheckClient


class HealthcheckClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthcheckClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthcheckClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthcheckClient
        """
        return self._raw_client

    def healthz(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        This endpoint can be used to check if the application is running and responding to requests

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.healthcheck.healthz()
        """
        _response = self._raw_client.healthz(request_options=request_options)
        return _response.data


class AsyncHealthcheckClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthcheckClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthcheckClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthcheckClient
        """
        return self._raw_client

    async def healthz(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        This endpoint can be used to check if the application is running and responding to requests

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.healthcheck.healthz()


        asyncio.run(main())
        """
        _response = await self._raw_client.healthz(request_options=request_options)
        return _response.data
