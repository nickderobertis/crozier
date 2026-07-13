

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.export_statement_create import ExportStatementCreate
from ..types.export_statement_delete import ExportStatementDelete
from ..types.export_statement_listing import ExportStatementListing
from ..types.export_statement_read import ExportStatementRead


OMIT = typing.cast(typing.Any, ...)


class RawCustomerStatementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_customer_statement_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ExportStatementListing]]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ExportStatementListing]]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementListing],
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

    def create_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        date_end: str,
        date_start: str,
        statement_format: str,
        include_attachment: typing.Optional[bool] = OMIT,
        regional_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportStatementCreate]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        date_end : str
            The end date for making statements.

        date_start : str
            The start date for making statements.

        statement_format : str
            The format type of statement. Allowed values: MT940, CSV, PDF.

        include_attachment : typing.Optional[bool]
            Only for PDF exports. Includes attachments to mutations in the export, such as scanned receipts.

        regional_format : typing.Optional[str]
            Required for CSV exports. The regional format of the statement, can be UK_US (comma-separated) or EUROPEAN (semicolon-separated).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportStatementCreate]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement",
            method="POST",
            json={
                "date_end": date_end,
                "date_start": date_start,
                "include_attachment": include_attachment,
                "regional_format": regional_format,
                "statement_format": statement_format,
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
                    ExportStatementCreate,
                    parse_obj_as(
                        type_=ExportStatementCreate,
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

    def read_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportStatementRead]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportStatementRead]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportStatementRead,
                    parse_obj_as(
                        type_=ExportStatementRead,
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

    def delete_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportStatementDelete]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportStatementDelete]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportStatementDelete,
                    parse_obj_as(
                        type_=ExportStatementDelete,
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


class AsyncRawCustomerStatementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_customer_statement_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ExportStatementListing]]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ExportStatementListing]]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ExportStatementListing],
                    parse_obj_as(
                        type_=typing.List[ExportStatementListing],
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

    async def create_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        date_end: str,
        date_start: str,
        statement_format: str,
        include_attachment: typing.Optional[bool] = OMIT,
        regional_format: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportStatementCreate]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        date_end : str
            The end date for making statements.

        date_start : str
            The start date for making statements.

        statement_format : str
            The format type of statement. Allowed values: MT940, CSV, PDF.

        include_attachment : typing.Optional[bool]
            Only for PDF exports. Includes attachments to mutations in the export, such as scanned receipts.

        regional_format : typing.Optional[str]
            Required for CSV exports. The regional format of the statement, can be UK_US (comma-separated) or EUROPEAN (semicolon-separated).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportStatementCreate]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement",
            method="POST",
            json={
                "date_end": date_end,
                "date_start": date_start,
                "include_attachment": include_attachment,
                "regional_format": regional_format,
                "statement_format": statement_format,
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
                    ExportStatementCreate,
                    parse_obj_as(
                        type_=ExportStatementCreate,
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

    async def read_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportStatementRead]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportStatementRead]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportStatementRead,
                    parse_obj_as(
                        type_=ExportStatementRead,
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

    async def delete_customer_statement_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportStatementDelete]:
        """
        Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportStatementDelete]
            Used to create new and read existing statement exports. Statement exports can be created in either CSV, MT940 or PDF file format.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/customer-statement/{jsonable_encoder(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportStatementDelete,
                    parse_obj_as(
                        type_=ExportStatementDelete,
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
