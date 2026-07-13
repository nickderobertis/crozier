

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.invoice_export_pdf_content_listing import InvoiceExportPdfContentListing
from .raw_client import AsyncRawPdfContentClient, RawPdfContentClient


class PdfContentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPdfContentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPdfContentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPdfContentClient
        """
        return self._raw_client

    def list_all_pdf_content_for_user_invoice(
        self, user_id: int, invoice_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InvoiceExportPdfContentListing]:
        """
        Get a PDF export of an invoice.

        Parameters
        ----------
        user_id : int


        invoice_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InvoiceExportPdfContentListing]
            Get a PDF export of an invoice.

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
        client.pdf_content.list_all_pdf_content_for_user_invoice(
            user_id=1,
            invoice_id=1,
        )
        """
        _response = self._raw_client.list_all_pdf_content_for_user_invoice(
            user_id, invoice_id, request_options=request_options
        )
        return _response.data


class AsyncPdfContentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPdfContentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPdfContentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPdfContentClient
        """
        return self._raw_client

    async def list_all_pdf_content_for_user_invoice(
        self, user_id: int, invoice_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[InvoiceExportPdfContentListing]:
        """
        Get a PDF export of an invoice.

        Parameters
        ----------
        user_id : int


        invoice_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[InvoiceExportPdfContentListing]
            Get a PDF export of an invoice.

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
            await client.pdf_content.list_all_pdf_content_for_user_invoice(
                user_id=1,
                invoice_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_pdf_content_for_user_invoice(
            user_id, invoice_id, request_options=request_options
        )
        return _response.data
