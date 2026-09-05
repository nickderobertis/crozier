

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1alpha1metrics import V1Alpha1Metrics
from ..types.v1alpha1system_status import V1Alpha1SystemStatus
from .raw_client import AsyncRawHealthClient, RawHealthClient


class HealthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthClient
        """
        return self._raw_client

    def status(self, *, request_options: typing.Optional[RequestOptions] = None) -> V1Alpha1SystemStatus:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1SystemStatus
            System info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.health.status()
        """
        _response = self._raw_client.status(request_options=request_options)
        return _response.data

    def metrics(
        self,
        *,
        name: typing.Optional[str] = None,
        start_time: typing.Optional[dt.datetime] = None,
        end_time: typing.Optional[dt.datetime] = None,
        max_length: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1Metrics:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        start_time : typing.Optional[dt.datetime]

        end_time : typing.Optional[dt.datetime]

        max_length : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1Metrics
            System metrics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )
        client.health.metrics()
        """
        _response = self._raw_client.metrics(
            name=name, start_time=start_time, end_time=end_time, max_length=max_length, request_options=request_options
        )
        return _response.data


class AsyncHealthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthClient
        """
        return self._raw_client

    async def status(self, *, request_options: typing.Optional[RequestOptions] = None) -> V1Alpha1SystemStatus:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1SystemStatus
            System info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health.status()


        asyncio.run(main())
        """
        _response = await self._raw_client.status(request_options=request_options)
        return _response.data

    async def metrics(
        self,
        *,
        name: typing.Optional[str] = None,
        start_time: typing.Optional[dt.datetime] = None,
        end_time: typing.Optional[dt.datetime] = None,
        max_length: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1Alpha1Metrics:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        start_time : typing.Optional[dt.datetime]

        end_time : typing.Optional[dt.datetime]

        max_length : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1Alpha1Metrics
            System metrics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_version="YOUR_API_VERSION",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health.metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.metrics(
            name=name, start_time=start_time, end_time=end_time, max_length=max_length, request_options=request_options
        )
        return _response.data
