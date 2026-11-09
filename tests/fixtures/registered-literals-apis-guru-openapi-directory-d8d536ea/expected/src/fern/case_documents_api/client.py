

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.case_document import CaseDocument
from ..types.case_document_order_callback import CaseDocumentOrderCallback
from ..types.case_document_order_callback_list_response import CaseDocumentOrderCallbackListResponse
from ..types.case_document_order_pacer_options import CaseDocumentOrderPacerOptions
from ..types.case_documents import CaseDocuments
from .raw_client import AsyncRawCaseDocumentsApiClient, RawCaseDocumentsApiClient
from .types.get_case_document_download_by_id_response import GetCaseDocumentDownloadByIdResponse
from .types.get_case_document_order_callbacks_request_status import GetCaseDocumentOrderCallbacksRequestStatus
from .types.get_case_documents_request_sort_by import GetCaseDocumentsRequestSortBy


OMIT = typing.cast(typing.Any, ...)


class CaseDocumentsApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCaseDocumentsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCaseDocumentsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCaseDocumentsApiClient
        """
        return self._raw_client

    def get_case_documents(
        self,
        case_id: str,
        *,
        in_library: typing.Optional[bool] = None,
        after_first_fetch_date: typing.Optional[dt.datetime] = None,
        library_date: typing.Optional[dt.datetime] = None,
        first_fetch_date: typing.Optional[dt.datetime] = None,
        sort_by: typing.Optional[GetCaseDocumentsRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[CaseDocuments]:
        """
        Gets Documents for a requested Case ID.

        Parameters
        ----------
        case_id : str
            Case ID for which you want the data for.

        in_library : typing.Optional[bool]
            Filter all the documents those are added to the UniCourt library.

        after_first_fetch_date : typing.Optional[dt.datetime]
            Get all the documents which were added to the case on or after a specific date.

        library_date : typing.Optional[dt.datetime]
            Sort all the documents based on the date when the document was added to the UniCourt Library.

        first_fetch_date : typing.Optional[dt.datetime]
            Sort all the documents based on the date it was fetched from the source site.

        sort_by : typing.Optional[GetCaseDocumentsRequestSortBy]
            Sort documents with document order.

        page_number : typing.Optional[int]
            The page for which the result should be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CaseDocuments]
            The request is recieved.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_documents_api.get_case_documents(
            case_id="CASEgua4c06e119ea8",
            after_first_fetch_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            library_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            first_fetch_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.get_case_documents(
            case_id,
            in_library=in_library,
            after_first_fetch_date=after_first_fetch_date,
            library_date=library_date,
            first_fetch_date=first_fetch_date,
            sort_by=sort_by,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data

    def get_document_by_id(
        self, case_document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CaseDocument]:
        """
        Gets details for a requested Document ID.

        Parameters
        ----------
        case_document_id : str
            Specific Case Dcoument ID for which you want the data for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CaseDocument]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_documents_api.get_document_by_id(
            case_document_id="CDOCag3e5eba43b870",
        )
        """
        _response = self._raw_client.get_document_by_id(case_document_id, request_options=request_options)
        return _response.data

    def get_case_document_download_by_id(
        self,
        case_document_id: str,
        *,
        is_preview_document: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCaseDocumentDownloadByIdResponse:
        """
        Gets downloadable URL for a requested Document ID.

        Parameters
        ----------
        case_document_id : str
            Document ID which you want to download.

        is_preview_document : typing.Optional[bool]
            If the document you want to download is a preview of a document.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCaseDocumentDownloadByIdResponse
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_documents_api.get_case_document_download_by_id(
            case_document_id="CDOCaqe42a86394f63",
        )
        """
        _response = self._raw_client.get_case_document_download_by_id(
            case_document_id, is_preview_document=is_preview_document, request_options=request_options
        )
        return _response.data

    def order_case_document(
        self,
        *,
        case_document_id: str,
        is_preview_only: bool,
        pacer_options: typing.Optional[CaseDocumentOrderPacerOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseDocumentOrderCallback:
        """
        Add Case Document Order for requested Document Ids.

        Parameters
        ----------
        case_document_id : str
            Document ID which you want to order.

        is_preview_only : bool
            Flag value to determine if the document order is a preview order or no.

        pacer_options : typing.Optional[CaseDocumentOrderPacerOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseDocumentOrderCallback
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_documents_api.order_case_document(
            case_document_id="CDOCcre989d654fa05",
            is_preview_only=False,
        )
        """
        _response = self._raw_client.order_case_document(
            case_document_id=case_document_id,
            is_preview_only=is_preview_only,
            pacer_options=pacer_options,
            request_options=request_options,
        )
        return _response.data

    def get_case_document_order_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseDocumentOrderCallbacksRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseDocumentOrderCallbackListResponse:
        """
        Get Case Document Order Callback list for a requested Date.

        Parameters
        ----------
        date : typing.Optional[dt.datetime]
            Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.

        status : typing.Optional[GetCaseDocumentOrderCallbacksRequestStatus]
            Status of Document Order callbacks. Default status will fetch all callbacks.

        page_number : typing.Optional[int]
            Page to fetch the Case Document Order Callback list.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseDocumentOrderCallbackListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_documents_api.get_case_document_order_callbacks()
        """
        _response = self._raw_client.get_case_document_order_callbacks(
            date=date, status=status, page_number=page_number, request_options=request_options
        )
        return _response.data

    def get_case_document_order_callback_by_id(
        self, case_document_order_callback_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseDocumentOrderCallback:
        """
        Get Case Document Order Callback for a requested Case Document Order Callback Id.

        Parameters
        ----------
        case_document_order_callback_id : str
            Unique Id for the Case Document Order Callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseDocumentOrderCallback
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_documents_api.get_case_document_order_callback_by_id(
            case_document_order_callback_id="CBDOnrb63f4808bjO3",
        )
        """
        _response = self._raw_client.get_case_document_order_callback_by_id(
            case_document_order_callback_id, request_options=request_options
        )
        return _response.data


class AsyncCaseDocumentsApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCaseDocumentsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCaseDocumentsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCaseDocumentsApiClient
        """
        return self._raw_client

    async def get_case_documents(
        self,
        case_id: str,
        *,
        in_library: typing.Optional[bool] = None,
        after_first_fetch_date: typing.Optional[dt.datetime] = None,
        library_date: typing.Optional[dt.datetime] = None,
        first_fetch_date: typing.Optional[dt.datetime] = None,
        sort_by: typing.Optional[GetCaseDocumentsRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[CaseDocuments]:
        """
        Gets Documents for a requested Case ID.

        Parameters
        ----------
        case_id : str
            Case ID for which you want the data for.

        in_library : typing.Optional[bool]
            Filter all the documents those are added to the UniCourt library.

        after_first_fetch_date : typing.Optional[dt.datetime]
            Get all the documents which were added to the case on or after a specific date.

        library_date : typing.Optional[dt.datetime]
            Sort all the documents based on the date when the document was added to the UniCourt Library.

        first_fetch_date : typing.Optional[dt.datetime]
            Sort all the documents based on the date it was fetched from the source site.

        sort_by : typing.Optional[GetCaseDocumentsRequestSortBy]
            Sort documents with document order.

        page_number : typing.Optional[int]
            The page for which the result should be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CaseDocuments]
            The request is recieved.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_documents_api.get_case_documents(
                case_id="CASEgua4c06e119ea8",
                after_first_fetch_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                library_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                first_fetch_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_documents(
            case_id,
            in_library=in_library,
            after_first_fetch_date=after_first_fetch_date,
            library_date=library_date,
            first_fetch_date=first_fetch_date,
            sort_by=sort_by,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data

    async def get_document_by_id(
        self, case_document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CaseDocument]:
        """
        Gets details for a requested Document ID.

        Parameters
        ----------
        case_document_id : str
            Specific Case Dcoument ID for which you want the data for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CaseDocument]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_documents_api.get_document_by_id(
                case_document_id="CDOCag3e5eba43b870",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_document_by_id(case_document_id, request_options=request_options)
        return _response.data

    async def get_case_document_download_by_id(
        self,
        case_document_id: str,
        *,
        is_preview_document: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetCaseDocumentDownloadByIdResponse:
        """
        Gets downloadable URL for a requested Document ID.

        Parameters
        ----------
        case_document_id : str
            Document ID which you want to download.

        is_preview_document : typing.Optional[bool]
            If the document you want to download is a preview of a document.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCaseDocumentDownloadByIdResponse
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_documents_api.get_case_document_download_by_id(
                case_document_id="CDOCaqe42a86394f63",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_document_download_by_id(
            case_document_id, is_preview_document=is_preview_document, request_options=request_options
        )
        return _response.data

    async def order_case_document(
        self,
        *,
        case_document_id: str,
        is_preview_only: bool,
        pacer_options: typing.Optional[CaseDocumentOrderPacerOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseDocumentOrderCallback:
        """
        Add Case Document Order for requested Document Ids.

        Parameters
        ----------
        case_document_id : str
            Document ID which you want to order.

        is_preview_only : bool
            Flag value to determine if the document order is a preview order or no.

        pacer_options : typing.Optional[CaseDocumentOrderPacerOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseDocumentOrderCallback
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_documents_api.order_case_document(
                case_document_id="CDOCcre989d654fa05",
                is_preview_only=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.order_case_document(
            case_document_id=case_document_id,
            is_preview_only=is_preview_only,
            pacer_options=pacer_options,
            request_options=request_options,
        )
        return _response.data

    async def get_case_document_order_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseDocumentOrderCallbacksRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseDocumentOrderCallbackListResponse:
        """
        Get Case Document Order Callback list for a requested Date.

        Parameters
        ----------
        date : typing.Optional[dt.datetime]
            Date for which fetch the Case Document Order Callback list. By default, the date will be set to current date.

        status : typing.Optional[GetCaseDocumentOrderCallbacksRequestStatus]
            Status of Document Order callbacks. Default status will fetch all callbacks.

        page_number : typing.Optional[int]
            Page to fetch the Case Document Order Callback list.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseDocumentOrderCallbackListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_documents_api.get_case_document_order_callbacks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_document_order_callbacks(
            date=date, status=status, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def get_case_document_order_callback_by_id(
        self, case_document_order_callback_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseDocumentOrderCallback:
        """
        Get Case Document Order Callback for a requested Case Document Order Callback Id.

        Parameters
        ----------
        case_document_order_callback_id : str
            Unique Id for the Case Document Order Callback.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseDocumentOrderCallback
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_documents_api.get_case_document_order_callback_by_id(
                case_document_order_callback_id="CBDOnrb63f4808bjO3",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_document_order_callback_by_id(
            case_document_order_callback_id, request_options=request_options
        )
        return _response.data
