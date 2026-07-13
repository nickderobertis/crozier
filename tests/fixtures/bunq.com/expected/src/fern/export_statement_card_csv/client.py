

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_statement_card_csv_create import ExportStatementCardCsvCreate
from ..types.export_statement_card_csv_delete import ExportStatementCardCsvDelete
from ..types.export_statement_card_csv_listing import ExportStatementCardCsvListing
from ..types.export_statement_card_csv_read import ExportStatementCardCsvRead
from .raw_client import AsyncRawExportStatementCardCsvClient, RawExportStatementCardCsvClient


OMIT = typing.cast(typing.Any, ...)


class ExportStatementCardCsvClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExportStatementCardCsvClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExportStatementCardCsvClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExportStatementCardCsvClient
        """
        return self._raw_client

    def list_all_export_statement_card_csv_for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportStatementCardCsvListing]:
        """
        Used to serialize ExportStatementCardCsv

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementCardCsvListing]
            Used to serialize ExportStatementCardCsv

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.export_statement_card_csv.list_all_export_statement_card_csv_for_user_card(
            user_id=1,
            card_id=1,
        )
        """
        _response = self._raw_client.list_all_export_statement_card_csv_for_user_card(
            user_id, card_id, request_options=request_options
        )
        return _response.data

    def create_export_statement_card_csv_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        date_end: str,
        date_start: str,
        regional_format: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementCardCsvCreate:
        """
        Used to serialize ExportStatementCardCsv

        Parameters
        ----------
        user_id : int


        card_id : int


        date_end : str
            The end date for making statements.

        date_start : str
            The start date for making statements.

        regional_format : str
            Required for CSV exports. The regional format of the statement, can be UK_US (comma-separated) or EUROPEAN (semicolon-separated).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardCsvCreate
            Used to serialize ExportStatementCardCsv

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.export_statement_card_csv.create_export_statement_card_csv_for_user_card(
            user_id=1,
            card_id=1,
            date_end="date_end",
            date_start="date_start",
            regional_format="regional_format",
        )
        """
        _response = self._raw_client.create_export_statement_card_csv_for_user_card(
            user_id,
            card_id,
            date_end=date_end,
            date_start=date_start,
            regional_format=regional_format,
            request_options=request_options,
        )
        return _response.data

    def read_export_statement_card_csv_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardCsvRead:
        """
        Used to serialize ExportStatementCardCsv

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardCsvRead
            Used to serialize ExportStatementCardCsv

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.export_statement_card_csv.read_export_statement_card_csv_for_user_card(
            user_id=1,
            card_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_export_statement_card_csv_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data

    def delete_export_statement_card_csv_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardCsvDelete:
        """
        Used to serialize ExportStatementCardCsv

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardCsvDelete
            Used to serialize ExportStatementCardCsv

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.export_statement_card_csv.delete_export_statement_card_csv_for_user_card(
            user_id=1,
            card_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_export_statement_card_csv_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncExportStatementCardCsvClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExportStatementCardCsvClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExportStatementCardCsvClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExportStatementCardCsvClient
        """
        return self._raw_client

    async def list_all_export_statement_card_csv_for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportStatementCardCsvListing]:
        """
        Used to serialize ExportStatementCardCsv

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementCardCsvListing]
            Used to serialize ExportStatementCardCsv

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.export_statement_card_csv.list_all_export_statement_card_csv_for_user_card(
                user_id=1,
                card_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_export_statement_card_csv_for_user_card(
            user_id, card_id, request_options=request_options
        )
        return _response.data

    async def create_export_statement_card_csv_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        date_end: str,
        date_start: str,
        regional_format: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementCardCsvCreate:
        """
        Used to serialize ExportStatementCardCsv

        Parameters
        ----------
        user_id : int


        card_id : int


        date_end : str
            The end date for making statements.

        date_start : str
            The start date for making statements.

        regional_format : str
            Required for CSV exports. The regional format of the statement, can be UK_US (comma-separated) or EUROPEAN (semicolon-separated).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardCsvCreate
            Used to serialize ExportStatementCardCsv

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.export_statement_card_csv.create_export_statement_card_csv_for_user_card(
                user_id=1,
                card_id=1,
                date_end="date_end",
                date_start="date_start",
                regional_format="regional_format",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_export_statement_card_csv_for_user_card(
            user_id,
            card_id,
            date_end=date_end,
            date_start=date_start,
            regional_format=regional_format,
            request_options=request_options,
        )
        return _response.data

    async def read_export_statement_card_csv_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardCsvRead:
        """
        Used to serialize ExportStatementCardCsv

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardCsvRead
            Used to serialize ExportStatementCardCsv

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.export_statement_card_csv.read_export_statement_card_csv_for_user_card(
                user_id=1,
                card_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_export_statement_card_csv_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data

    async def delete_export_statement_card_csv_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardCsvDelete:
        """
        Used to serialize ExportStatementCardCsv

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardCsvDelete
            Used to serialize ExportStatementCardCsv

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.export_statement_card_csv.delete_export_statement_card_csv_for_user_card(
                user_id=1,
                card_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_export_statement_card_csv_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data
