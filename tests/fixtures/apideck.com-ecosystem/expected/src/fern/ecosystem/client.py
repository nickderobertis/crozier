

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_ecosystem_response import GetEcosystemResponse
from .raw_client import AsyncRawEcosystemClient, RawEcosystemClient


class EcosystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEcosystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEcosystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEcosystemClient
        """
        return self._raw_client

    def ecosystems_one(
        self, ecosystem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEcosystemResponse:
        """
        Get ecosystem

        Parameters
        ----------
        ecosystem_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEcosystemResponse
            Ecosystems

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.ecosystem.ecosystems_one(
            ecosystem_id="ecosystem_id",
        )
        """
        _response = self._raw_client.ecosystems_one(ecosystem_id, request_options=request_options)
        return _response.data


class AsyncEcosystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEcosystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEcosystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEcosystemClient
        """
        return self._raw_client

    async def ecosystems_one(
        self, ecosystem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEcosystemResponse:
        """
        Get ecosystem

        Parameters
        ----------
        ecosystem_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEcosystemResponse
            Ecosystems

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.ecosystem.ecosystems_one(
                ecosystem_id="ecosystem_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ecosystems_one(ecosystem_id, request_options=request_options)
        return _response.data
