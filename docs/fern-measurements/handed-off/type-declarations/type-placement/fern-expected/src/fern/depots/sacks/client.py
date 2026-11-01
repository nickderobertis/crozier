

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawSacksClient, RawSacksClient
from .types.list_sacks_request_priority import ListSacksRequestPriority


class SacksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSacksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSacksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSacksClient
        """
        return self._raw_client

    def list(
        self,
        depot_id: str,
        *,
        priority: typing.Optional[ListSacksRequestPriority] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        depot_id : str

        priority : typing.Optional[ListSacksRequestPriority]
            Sorting priority.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The sacks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.depots.sacks.list(
            depot_id="depotId",
        )
        """
        _response = self._raw_client.list(depot_id, priority=priority, request_options=request_options)
        return _response.data


class AsyncSacksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSacksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSacksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSacksClient
        """
        return self._raw_client

    async def list(
        self,
        depot_id: str,
        *,
        priority: typing.Optional[ListSacksRequestPriority] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        depot_id : str

        priority : typing.Optional[ListSacksRequestPriority]
            Sorting priority.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            The sacks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.depots.sacks.list(
                depot_id="depotId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(depot_id, priority=priority, request_options=request_options)
        return _response.data
