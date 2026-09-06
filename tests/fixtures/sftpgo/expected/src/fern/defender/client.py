

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.defender_entry import DefenderEntry
from .raw_client import AsyncRawDefenderClient, RawDefenderClient


class DefenderClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDefenderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDefenderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDefenderClient
        """
        return self._raw_client

    def get_defender_hosts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DefenderEntry]:
        """
        Returns hosts that are banned or for which some violations have been detected

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DefenderEntry]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.defender.get_defender_hosts()
        """
        _response = self._raw_client.get_defender_hosts(request_options=request_options)
        return _response.data

    def get_defender_host_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DefenderEntry:
        """
        Returns the host with the given id, if it exists

        Parameters
        ----------
        id : str
            host id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DefenderEntry
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.defender.get_defender_host_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_defender_host_by_id(id, request_options=request_options)
        return _response.data

    def delete_defender_host_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Unbans the specified host or clears its violations

        Parameters
        ----------
        id : str
            host id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.defender.delete_defender_host_by_id(
            id="id",
        )
        """
        _response = self._raw_client.delete_defender_host_by_id(id, request_options=request_options)
        return _response.data


class AsyncDefenderClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDefenderClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDefenderClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDefenderClient
        """
        return self._raw_client

    async def get_defender_hosts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DefenderEntry]:
        """
        Returns hosts that are banned or for which some violations have been detected

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DefenderEntry]
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
            await client.defender.get_defender_hosts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_defender_hosts(request_options=request_options)
        return _response.data

    async def get_defender_host_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DefenderEntry:
        """
        Returns the host with the given id, if it exists

        Parameters
        ----------
        id : str
            host id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DefenderEntry
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
            await client.defender.get_defender_host_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_defender_host_by_id(id, request_options=request_options)
        return _response.data

    async def delete_defender_host_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApiResponse:
        """
        Unbans the specified host or clears its violations

        Parameters
        ----------
        id : str
            host id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
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
            await client.defender.delete_defender_host_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_defender_host_by_id(id, request_options=request_options)
        return _response.data
