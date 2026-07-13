

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.export_statement_card_pdf_create import ExportStatementCardPdfCreate
from ..types.export_statement_card_pdf_delete import ExportStatementCardPdfDelete
from ..types.export_statement_card_pdf_listing import ExportStatementCardPdfListing
from ..types.export_statement_card_pdf_read import ExportStatementCardPdfRead


OMIT = typing.cast(typing.Any, ...)


class RawExportStatementCardPdfClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ExportStatementCardPdfListing]]:
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
        HttpResponse[typing.List[ExportStatementCardPdfListing]]
            Used to serialize ExportStatementCardPdf
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card-pdf",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementCardPdfListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementCardPdfListing],
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

    def create_export_statement_card_pdf_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        date_end: str,
        date_start: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportStatementCardPdfCreate]:
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
        HttpResponse[ExportStatementCardPdfCreate]
            Used to serialize ExportStatementCardPdf
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card-pdf",
            method="POST",
            json={
                "date_end": date_end,
                "date_start": date_start,
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
                    ExportStatementCardPdfCreate,
                    parse_obj_as(
                        type_=ExportStatementCardPdfCreate,
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

    def read_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ExportStatementCardPdfRead]:
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
        HttpResponse[ExportStatementCardPdfRead]
            Used to serialize ExportStatementCardPdf
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card-pdf/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportStatementCardPdfRead,
                    parse_obj_as(
                        type_=ExportStatementCardPdfRead,
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

    def delete_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ExportStatementCardPdfDelete]:
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
        HttpResponse[ExportStatementCardPdfDelete]
            Used to serialize ExportStatementCardPdf
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card-pdf/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportStatementCardPdfDelete,
                    parse_obj_as(
                        type_=ExportStatementCardPdfDelete,
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


class AsyncRawExportStatementCardPdfClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ExportStatementCardPdfListing]]:
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
        AsyncHttpResponse[typing.List[ExportStatementCardPdfListing]]
            Used to serialize ExportStatementCardPdf
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card-pdf",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementCardPdfListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementCardPdfListing],
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

    async def create_export_statement_card_pdf_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        date_end: str,
        date_start: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportStatementCardPdfCreate]:
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
        AsyncHttpResponse[ExportStatementCardPdfCreate]
            Used to serialize ExportStatementCardPdf
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card-pdf",
            method="POST",
            json={
                "date_end": date_end,
                "date_start": date_start,
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
                    ExportStatementCardPdfCreate,
                    parse_obj_as(
                        type_=ExportStatementCardPdfCreate,
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

    async def read_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ExportStatementCardPdfRead]:
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
        AsyncHttpResponse[ExportStatementCardPdfRead]
            Used to serialize ExportStatementCardPdf
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card-pdf/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportStatementCardPdfRead,
                    parse_obj_as(
                        type_=ExportStatementCardPdfRead,
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

    async def delete_export_statement_card_pdf_for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ExportStatementCardPdfDelete]:
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
        AsyncHttpResponse[ExportStatementCardPdfDelete]
            Used to serialize ExportStatementCardPdf
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/export-statement-card-pdf/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportStatementCardPdfDelete,
                    parse_obj_as(
                        type_=ExportStatementCardPdfDelete,
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
