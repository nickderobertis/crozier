

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawHarboursClient, RawHarboursClient
from .types.get_berth_response import GetBerthResponse


class HarboursClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHarboursClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHarboursClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHarboursClient
        """
        return self._raw_client

    def get_berth(
        self, harbour_slug: str, berth_ref: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBerthResponse:
        """
        Path parameters beside one declaring an empty schema.

        Parameters
        ----------
        harbour_slug : str

        berth_ref : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBerthResponse
            The berth

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.harbours.get_berth(
            harbour_slug="harbourSlug",
            berth_ref="berthRef",
        )
        """
        _response = self._raw_client.get_berth(harbour_slug, berth_ref, request_options=request_options)
        return _response.data


class AsyncHarboursClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHarboursClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHarboursClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHarboursClient
        """
        return self._raw_client

    async def get_berth(
        self, harbour_slug: str, berth_ref: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBerthResponse:
        """
        Path parameters beside one declaring an empty schema.

        Parameters
        ----------
        harbour_slug : str

        berth_ref : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBerthResponse
            The berth

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.harbours.get_berth(
                harbour_slug="harbourSlug",
                berth_ref="berthRef",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_berth(harbour_slug, berth_ref, request_options=request_options)
        return _response.data
