

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_row_request_picker import GetRowRequestPicker
from .raw_client import AsyncRawRowsClient, RawRowsClient
from .types.get_row_request_row import GetRowRequestRow
from .types.get_row_request_season import GetRowRequestSeason
from .types.get_row_request_x_orchard_block import GetRowRequestXOrchardBlock


class RowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRowsClient
        """
        return self._raw_client

    def get_row(
        self,
        row: GetRowRequestRow,
        *,
        season: GetRowRequestSeason,
        picker: typing.Optional[GetRowRequestPicker] = None,
        orchard_block: typing.Optional[GetRowRequestXOrchardBlock] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        row : GetRowRequestRow

        season : GetRowRequestSeason

        picker : typing.Optional[GetRowRequestPicker]

        orchard_block : typing.Optional[GetRowRequestXOrchardBlock]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One orchard row.

        Examples
        --------
        from fern import FernApi, GetRowRequestPickerZero

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.rows.get_row(
            row="row",
            season="season",
            picker=GetRowRequestPickerZero.MORNING,
        )
        """
        _response = self._raw_client.get_row(
            row, season=season, picker=picker, orchard_block=orchard_block, request_options=request_options
        )
        return _response.data


class AsyncRowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRowsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRowsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRowsClient
        """
        return self._raw_client

    async def get_row(
        self,
        row: GetRowRequestRow,
        *,
        season: GetRowRequestSeason,
        picker: typing.Optional[GetRowRequestPicker] = None,
        orchard_block: typing.Optional[GetRowRequestXOrchardBlock] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        row : GetRowRequestRow

        season : GetRowRequestSeason

        picker : typing.Optional[GetRowRequestPicker]

        orchard_block : typing.Optional[GetRowRequestXOrchardBlock]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One orchard row.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GetRowRequestPickerZero

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rows.get_row(
                row="row",
                season="season",
                picker=GetRowRequestPickerZero.MORNING,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_row(
            row, season=season, picker=picker, orchard_block=orchard_block, request_options=request_options
        )
        return _response.data
