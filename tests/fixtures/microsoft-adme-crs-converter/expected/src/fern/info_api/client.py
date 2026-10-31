

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.version_info import VersionInfo
from .raw_client import AsyncRawInfoApiClient, RawInfoApiClient


class InfoApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInfoApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInfoApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInfoApiClient
        """
        return self._raw_client

    def info(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )
        client.info_api.info()
        """
        _response = self._raw_client.info(request_options=request_options)
        return _response.data

    def info1(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )
        client.info_api.info1()
        """
        _response = self._raw_client.info1(request_options=request_options)
        return _response.data


class AsyncInfoApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInfoApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInfoApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInfoApiClient
        """
        return self._raw_client

    async def info(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
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
            await client.info_api.info()


        asyncio.run(main())
        """
        _response = await self._raw_client.info(request_options=request_options)
        return _response.data

    async def info1(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
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
            await client.info_api.info1()


        asyncio.run(main())
        """
        _response = await self._raw_client.info1(request_options=request_options)
        return _response.data
