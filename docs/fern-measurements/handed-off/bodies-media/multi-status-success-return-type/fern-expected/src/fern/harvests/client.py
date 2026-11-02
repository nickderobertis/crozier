

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.row_harvest import RowHarvest
from .raw_client import AsyncRawHarvestsClient, RawHarvestsClient


OMIT = typing.cast(typing.Any, ...)


class HarvestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHarvestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHarvestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHarvestsClient
        """
        return self._raw_client

    def record_harvests(
        self, *, rows: typing.Sequence[RowHarvest], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        rows : typing.Sequence[RowHarvest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, RowHarvest

        client = FernApi()
        client.harvests.record_harvests(
            rows=[
                RowHarvest(
                    row="row",
                    crates=1,
                )
            ],
        )
        """
        _response = self._raw_client.record_harvests(rows=rows, request_options=request_options)
        return _response.data


class AsyncHarvestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHarvestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHarvestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHarvestsClient
        """
        return self._raw_client

    async def record_harvests(
        self, *, rows: typing.Sequence[RowHarvest], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        rows : typing.Sequence[RowHarvest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RowHarvest

        client = AsyncFernApi()


        async def main() -> None:
            await client.harvests.record_harvests(
                rows=[
                    RowHarvest(
                        row="row",
                        crates=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_harvests(rows=rows, request_options=request_options)
        return _response.data
