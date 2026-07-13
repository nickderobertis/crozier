

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.invoice_export_pdf_content_listing import InvoiceExportPdfContentListing


class RawPdfContentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_pdf_content_for_user_invoice(
        self, user_id: int, invoice_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[InvoiceExportPdfContentListing]]:
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
        HttpResponse[typing.List[InvoiceExportPdfContentListing]]
            Get a PDF export of an invoice.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/invoice/{jsonable_encoder(invoice_id)}/pdf-content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[InvoiceExportPdfContentListing],
                    parse_obj_as(
                        type_=typing.List[InvoiceExportPdfContentListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPdfContentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_pdf_content_for_user_invoice(
        self, user_id: int, invoice_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[InvoiceExportPdfContentListing]]:
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
        AsyncHttpResponse[typing.List[InvoiceExportPdfContentListing]]
            Get a PDF export of an invoice.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/invoice/{jsonable_encoder(invoice_id)}/pdf-content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[InvoiceExportPdfContentListing],
                    parse_obj_as(
                        type_=typing.List[InvoiceExportPdfContentListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
