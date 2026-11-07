

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unavailable_for_legal_reasons_error import UnavailableForLegalReasonsError
from ..types.case_document import CaseDocument
from ..types.case_document_order_callback import CaseDocumentOrderCallback
from ..types.case_document_order_callback_list_response import CaseDocumentOrderCallbackListResponse
from ..types.case_document_order_pacer_options import CaseDocumentOrderPacerOptions
from ..types.case_documents import CaseDocuments
from ..types.exception import Exception
from .types.get_case_document_download_by_id_response import GetCaseDocumentDownloadByIdResponse
from .types.get_case_document_order_callbacks_request_status import GetCaseDocumentOrderCallbacksRequestStatus
from .types.get_case_documents_request_sort_by import GetCaseDocumentsRequestSortBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCaseDocumentsApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[typing.Optional[CaseDocuments]]:
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
        HttpResponse[typing.Optional[CaseDocuments]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/documents",
            method="GET",
            params={
                "inLibrary": in_library,
                "afterFirstFetchDate": serialize_datetime(after_first_fetch_date)
                if after_first_fetch_date is not None
                else None,
                "libraryDate": serialize_datetime(library_date) if library_date is not None else None,
                "firstFetchDate": serialize_datetime(first_fetch_date) if first_fetch_date is not None else None,
                "sortBy": sort_by,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseDocuments],
                    parse_obj_as(
                        type_=typing.Optional[CaseDocuments],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_document_by_id(
        self, case_document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[CaseDocument]]:
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
        HttpResponse[typing.Optional[CaseDocument]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"caseDocument/{encode_path_param(case_document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseDocument],
                    parse_obj_as(
                        type_=typing.Optional[CaseDocument],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_case_document_download_by_id(
        self,
        case_document_id: str,
        *,
        is_preview_document: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetCaseDocumentDownloadByIdResponse]:
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
        HttpResponse[GetCaseDocumentDownloadByIdResponse]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"caseDocumentDownload/{encode_path_param(case_document_id)}",
            method="GET",
            params={
                "isPreviewDocument": is_preview_document,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCaseDocumentDownloadByIdResponse,
                    parse_obj_as(
                        type_=GetCaseDocumentDownloadByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def order_case_document(
        self,
        *,
        case_document_id: str,
        is_preview_only: bool,
        pacer_options: typing.Optional[CaseDocumentOrderPacerOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseDocumentOrderCallback]:
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
        HttpResponse[CaseDocumentOrderCallback]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "caseDocumentOrder",
            method="PUT",
            json={
                "caseDocumentId": case_document_id,
                "isPreviewOnly": is_preview_only,
                "pacerOptions": convert_and_respect_annotation_metadata(
                    object_=pacer_options, annotation=CaseDocumentOrderPacerOptions, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseDocumentOrderCallback,
                    parse_obj_as(
                        type_=CaseDocumentOrderCallback,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_case_document_order_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseDocumentOrderCallbacksRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseDocumentOrderCallbackListResponse]:
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
        HttpResponse[CaseDocumentOrderCallbackListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "caseDocumentOrder/callbacks",
            method="GET",
            params={
                "date": serialize_datetime(date) if date is not None else None,
                "status": status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseDocumentOrderCallbackListResponse,
                    parse_obj_as(
                        type_=CaseDocumentOrderCallbackListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_case_document_order_callback_by_id(
        self, case_document_order_callback_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CaseDocumentOrderCallback]:
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
        HttpResponse[CaseDocumentOrderCallback]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"caseDocumentOrder/callbacks/{encode_path_param(case_document_order_callback_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseDocumentOrderCallback,
                    parse_obj_as(
                        type_=CaseDocumentOrderCallback,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCaseDocumentsApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[typing.Optional[CaseDocuments]]:
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
        AsyncHttpResponse[typing.Optional[CaseDocuments]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/documents",
            method="GET",
            params={
                "inLibrary": in_library,
                "afterFirstFetchDate": serialize_datetime(after_first_fetch_date)
                if after_first_fetch_date is not None
                else None,
                "libraryDate": serialize_datetime(library_date) if library_date is not None else None,
                "firstFetchDate": serialize_datetime(first_fetch_date) if first_fetch_date is not None else None,
                "sortBy": sort_by,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseDocuments],
                    parse_obj_as(
                        type_=typing.Optional[CaseDocuments],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_document_by_id(
        self, case_document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[CaseDocument]]:
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
        AsyncHttpResponse[typing.Optional[CaseDocument]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"caseDocument/{encode_path_param(case_document_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseDocument],
                    parse_obj_as(
                        type_=typing.Optional[CaseDocument],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_case_document_download_by_id(
        self,
        case_document_id: str,
        *,
        is_preview_document: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetCaseDocumentDownloadByIdResponse]:
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
        AsyncHttpResponse[GetCaseDocumentDownloadByIdResponse]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"caseDocumentDownload/{encode_path_param(case_document_id)}",
            method="GET",
            params={
                "isPreviewDocument": is_preview_document,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCaseDocumentDownloadByIdResponse,
                    parse_obj_as(
                        type_=GetCaseDocumentDownloadByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def order_case_document(
        self,
        *,
        case_document_id: str,
        is_preview_only: bool,
        pacer_options: typing.Optional[CaseDocumentOrderPacerOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseDocumentOrderCallback]:
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
        AsyncHttpResponse[CaseDocumentOrderCallback]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "caseDocumentOrder",
            method="PUT",
            json={
                "caseDocumentId": case_document_id,
                "isPreviewOnly": is_preview_only,
                "pacerOptions": convert_and_respect_annotation_metadata(
                    object_=pacer_options, annotation=CaseDocumentOrderPacerOptions, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseDocumentOrderCallback,
                    parse_obj_as(
                        type_=CaseDocumentOrderCallback,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_case_document_order_callbacks(
        self,
        *,
        date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseDocumentOrderCallbacksRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseDocumentOrderCallbackListResponse]:
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
        AsyncHttpResponse[CaseDocumentOrderCallbackListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "caseDocumentOrder/callbacks",
            method="GET",
            params={
                "date": serialize_datetime(date) if date is not None else None,
                "status": status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseDocumentOrderCallbackListResponse,
                    parse_obj_as(
                        type_=CaseDocumentOrderCallbackListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_case_document_order_callback_by_id(
        self, case_document_order_callback_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CaseDocumentOrderCallback]:
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
        AsyncHttpResponse[CaseDocumentOrderCallback]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"caseDocumentOrder/callbacks/{encode_path_param(case_document_order_callback_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseDocumentOrderCallback,
                    parse_obj_as(
                        type_=CaseDocumentOrderCallback,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
