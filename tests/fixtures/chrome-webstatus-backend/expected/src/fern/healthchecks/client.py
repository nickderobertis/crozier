

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.healthcheck_response import HealthcheckResponse
from .raw_client import AsyncRawHealthchecksClient, RawHealthchecksClient


class HealthchecksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthchecksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthchecksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthchecksClient
        """
        return self._raw_client

    def get_healthcheck_liveness(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthcheckResponse:
        """
        Returns a 200 OK status to indicate that the service process is alive and responsive.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthcheckResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )
        client.healthchecks.get_healthcheck_liveness()
        """
        _response = self._raw_client.get_healthcheck_liveness(request_options=request_options)
        return _response.data


class AsyncHealthchecksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthchecksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthchecksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthchecksClient
        """
        return self._raw_client

    async def get_healthcheck_liveness(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthcheckResponse:
        """
        Returns a 200 OK status to indicate that the service process is alive and responsive.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthcheckResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            no_auth="YOUR_NO_AUTH",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.healthchecks.get_healthcheck_liveness()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_healthcheck_liveness(request_options=request_options)
        return _response.data
