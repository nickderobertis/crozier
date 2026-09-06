

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tachiyomi_read_progress_dto import TachiyomiReadProgressDto
from ..types.tachiyomi_read_progress_v2dto import TachiyomiReadProgressV2Dto
from .raw_client import AsyncRawMihonClient, RawMihonClient


OMIT = typing.cast(typing.Any, ...)


class MihonClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMihonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMihonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMihonClient
        """
        return self._raw_client

    def get_mihon_read_progress_by_read_list_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TachiyomiReadProgressDto:
        """
        Mihon specific, due to how read progress is handled in Mihon.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TachiyomiReadProgressDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.mihon.get_mihon_read_progress_by_read_list_id(
            id="id",
        )
        """
        _response = self._raw_client.get_mihon_read_progress_by_read_list_id(id, request_options=request_options)
        return _response.data

    def update_mihon_read_progress_by_read_list_id(
        self, id: str, *, last_book_read: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mihon specific, due to how read progress is handled in Mihon.

        Parameters
        ----------
        id : str

        last_book_read : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.mihon.update_mihon_read_progress_by_read_list_id(
            id="id",
            last_book_read=1,
        )
        """
        _response = self._raw_client.update_mihon_read_progress_by_read_list_id(
            id, last_book_read=last_book_read, request_options=request_options
        )
        return _response.data

    def get_mihon_read_progress_by_series_id(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TachiyomiReadProgressV2Dto:
        """
        Mihon specific, due to how read progress is handled in Mihon.

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TachiyomiReadProgressV2Dto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.mihon.get_mihon_read_progress_by_series_id(
            series_id="seriesId",
        )
        """
        _response = self._raw_client.get_mihon_read_progress_by_series_id(series_id, request_options=request_options)
        return _response.data

    def update_mihon_read_progress_by_series_id(
        self,
        series_id: str,
        *,
        last_book_number_sort_read: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Mihon specific, due to how read progress is handled in Mihon.

        Parameters
        ----------
        series_id : str

        last_book_number_sort_read : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.mihon.update_mihon_read_progress_by_series_id(
            series_id="seriesId",
            last_book_number_sort_read=1.1,
        )
        """
        _response = self._raw_client.update_mihon_read_progress_by_series_id(
            series_id, last_book_number_sort_read=last_book_number_sort_read, request_options=request_options
        )
        return _response.data


class AsyncMihonClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMihonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMihonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMihonClient
        """
        return self._raw_client

    async def get_mihon_read_progress_by_read_list_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TachiyomiReadProgressDto:
        """
        Mihon specific, due to how read progress is handled in Mihon.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TachiyomiReadProgressDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.mihon.get_mihon_read_progress_by_read_list_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mihon_read_progress_by_read_list_id(id, request_options=request_options)
        return _response.data

    async def update_mihon_read_progress_by_read_list_id(
        self, id: str, *, last_book_read: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mihon specific, due to how read progress is handled in Mihon.

        Parameters
        ----------
        id : str

        last_book_read : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.mihon.update_mihon_read_progress_by_read_list_id(
                id="id",
                last_book_read=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_mihon_read_progress_by_read_list_id(
            id, last_book_read=last_book_read, request_options=request_options
        )
        return _response.data

    async def get_mihon_read_progress_by_series_id(
        self, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TachiyomiReadProgressV2Dto:
        """
        Mihon specific, due to how read progress is handled in Mihon.

        Parameters
        ----------
        series_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TachiyomiReadProgressV2Dto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.mihon.get_mihon_read_progress_by_series_id(
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mihon_read_progress_by_series_id(
            series_id, request_options=request_options
        )
        return _response.data

    async def update_mihon_read_progress_by_series_id(
        self,
        series_id: str,
        *,
        last_book_number_sort_read: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Mihon specific, due to how read progress is handled in Mihon.

        Parameters
        ----------
        series_id : str

        last_book_number_sort_read : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.mihon.update_mihon_read_progress_by_series_id(
                series_id="seriesId",
                last_book_number_sort_read=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_mihon_read_progress_by_series_id(
            series_id, last_book_number_sort_read=last_book_number_sort_read, request_options=request_options
        )
        return _response.data
