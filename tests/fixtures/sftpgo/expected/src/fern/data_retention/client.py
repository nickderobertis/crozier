

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.retention_check import RetentionCheck
from .raw_client import AsyncRawDataRetentionClient, RawDataRetentionClient


class DataRetentionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataRetentionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataRetentionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataRetentionClient
        """
        return self._raw_client

    def get_users_retention_checks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RetentionCheck]:
        """
        Returns the active retention checks

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RetentionCheck]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.data_retention.get_users_retention_checks()
        """
        _response = self._raw_client.get_users_retention_checks(request_options=request_options)
        return _response.data


class AsyncDataRetentionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataRetentionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataRetentionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataRetentionClient
        """
        return self._raw_client

    async def get_users_retention_checks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RetentionCheck]:
        """
        Returns the active retention checks

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RetentionCheck]
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
            await client.data_retention.get_users_retention_checks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_users_retention_checks(request_options=request_options)
        return _response.data
