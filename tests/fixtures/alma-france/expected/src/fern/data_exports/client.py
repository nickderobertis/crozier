

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.data_export import DataExport
from .raw_client import AsyncRawDataExportsClient, RawDataExportsClient


OMIT = typing.cast(typing.Any, ...)


class DataExportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataExportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataExportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataExportsClient
        """
        return self._raw_client

    def createdataexport(
        self,
        *,
        type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[dt.date] = OMIT,
        end_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataExport:
        """
        Parameters
        ----------
        type : typing.Optional[str]
            Type of data to export

        start_date : typing.Optional[dt.date]
            Start date for export range

        end_date : typing.Optional[dt.date]
            End date for export range

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExport
            Data export created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_exports.createdataexport()
        """
        _response = self._raw_client.createdataexport(
            type=type, start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data

    def getdataexport(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DataExport:
        """
        Parameters
        ----------
        id : str
            Data export identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExport
            Data export details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.data_exports.getdataexport(
            id="id",
        )
        """
        _response = self._raw_client.getdataexport(id, request_options=request_options)
        return _response.data


class AsyncDataExportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataExportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataExportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataExportsClient
        """
        return self._raw_client

    async def createdataexport(
        self,
        *,
        type: typing.Optional[str] = OMIT,
        start_date: typing.Optional[dt.date] = OMIT,
        end_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataExport:
        """
        Parameters
        ----------
        type : typing.Optional[str]
            Type of data to export

        start_date : typing.Optional[dt.date]
            Start date for export range

        end_date : typing.Optional[dt.date]
            End date for export range

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExport
            Data export created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_exports.createdataexport()


        asyncio.run(main())
        """
        _response = await self._raw_client.createdataexport(
            type=type, start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data

    async def getdataexport(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DataExport:
        """
        Parameters
        ----------
        id : str
            Data export identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataExport
            Data export details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.data_exports.getdataexport(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getdataexport(id, request_options=request_options)
        return _response.data
