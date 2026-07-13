

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_statement_card_pdf_create import ExportStatementCardPdfCreate
from ..types.export_statement_card_pdf_delete import ExportStatementCardPdfDelete
from ..types.export_statement_card_pdf_listing import ExportStatementCardPdfListing
from ..types.export_statement_card_pdf_read import ExportStatementCardPdfRead
from .raw_client import AsyncRawExportStatementCardPdfClient, RawExportStatementCardPdfClient


OMIT = typing.cast(typing.Any, ...)


class ExportStatementCardPdfClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExportStatementCardPdfClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExportStatementCardPdfClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExportStatementCardPdfClient
        """
        return self._raw_client

    def list_all_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportStatementCardPdfListing]:
        """
        Used to serialize ExportStatementCardPdf

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementCardPdfListing]
            Used to serialize ExportStatementCardPdf

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
        client.export_statement_card_pdf.list_all_export_statement_card_pdf_for_user_card(
            user_id=1,
            card_id=1,
        )
        """
        _response = self._raw_client.list_all_export_statement_card_pdf_for_user_card(
            user_id, card_id, request_options=request_options
        )
        return _response.data

    def create_export_statement_card_pdf_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        date_end: str,
        date_start: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementCardPdfCreate:
        """
        Used to serialize ExportStatementCardPdf

        Parameters
        ----------
        user_id : int


        card_id : int


        date_end : str
            The end date for making statements.

        date_start : str
            The start date for making statements.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardPdfCreate
            Used to serialize ExportStatementCardPdf

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
        client.export_statement_card_pdf.create_export_statement_card_pdf_for_user_card(
            user_id=1,
            card_id=1,
            date_end="date_end",
            date_start="date_start",
        )
        """
        _response = self._raw_client.create_export_statement_card_pdf_for_user_card(
            user_id, card_id, date_end=date_end, date_start=date_start, request_options=request_options
        )
        return _response.data

    def read_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardPdfRead:
        """
        Used to serialize ExportStatementCardPdf

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardPdfRead
            Used to serialize ExportStatementCardPdf

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
        client.export_statement_card_pdf.read_export_statement_card_pdf_for_user_card(
            user_id=1,
            card_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_export_statement_card_pdf_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data

    def delete_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardPdfDelete:
        """
        Used to serialize ExportStatementCardPdf

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardPdfDelete
            Used to serialize ExportStatementCardPdf

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
        client.export_statement_card_pdf.delete_export_statement_card_pdf_for_user_card(
            user_id=1,
            card_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.delete_export_statement_card_pdf_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncExportStatementCardPdfClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExportStatementCardPdfClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExportStatementCardPdfClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExportStatementCardPdfClient
        """
        return self._raw_client

    async def list_all_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ExportStatementCardPdfListing]:
        """
        Used to serialize ExportStatementCardPdf

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ExportStatementCardPdfListing]
            Used to serialize ExportStatementCardPdf

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
            await client.export_statement_card_pdf.list_all_export_statement_card_pdf_for_user_card(
                user_id=1,
                card_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_export_statement_card_pdf_for_user_card(
            user_id, card_id, request_options=request_options
        )
        return _response.data

    async def create_export_statement_card_pdf_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        date_end: str,
        date_start: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportStatementCardPdfCreate:
        """
        Used to serialize ExportStatementCardPdf

        Parameters
        ----------
        user_id : int


        card_id : int


        date_end : str
            The end date for making statements.

        date_start : str
            The start date for making statements.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardPdfCreate
            Used to serialize ExportStatementCardPdf

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
            await client.export_statement_card_pdf.create_export_statement_card_pdf_for_user_card(
                user_id=1,
                card_id=1,
                date_end="date_end",
                date_start="date_start",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_export_statement_card_pdf_for_user_card(
            user_id, card_id, date_end=date_end, date_start=date_start, request_options=request_options
        )
        return _response.data

    async def read_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardPdfRead:
        """
        Used to serialize ExportStatementCardPdf

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardPdfRead
            Used to serialize ExportStatementCardPdf

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
            await client.export_statement_card_pdf.read_export_statement_card_pdf_for_user_card(
                user_id=1,
                card_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_export_statement_card_pdf_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data

    async def delete_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportStatementCardPdfDelete:
        """
        Used to serialize ExportStatementCardPdf

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportStatementCardPdfDelete
            Used to serialize ExportStatementCardPdf

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
            await client.export_statement_card_pdf.delete_export_statement_card_pdf_for_user_card(
                user_id=1,
                card_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_export_statement_card_pdf_for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data
