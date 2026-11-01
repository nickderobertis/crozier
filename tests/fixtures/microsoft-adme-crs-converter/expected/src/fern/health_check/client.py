

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawHealthCheckClient, RawHealthCheckClient


class HealthCheckClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthCheckClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthCheckClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthCheckClient
        """
        return self._raw_client

    def liveness_check(
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
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )
        client.health_check.liveness_check()
        """
        _response = self._raw_client.liveness_check(request_options=request_options)
        return _response.data

    def readiness_check(
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
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )
        client.health_check.readiness_check()
        """
        _response = self._raw_client.readiness_check(request_options=request_options)
        return _response.data


class AsyncHealthCheckClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthCheckClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthCheckClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthCheckClient
        """
        return self._raw_client

    async def liveness_check(
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
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.health_check.liveness_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.liveness_check(request_options=request_options)
        return _response.data

    async def readiness_check(
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
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.health_check.readiness_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.readiness_check(request_options=request_options)
        return _response.data
