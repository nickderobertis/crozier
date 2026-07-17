

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.active import Active
from ..types.bad_request_response import BadRequestResponse
from ..types.create_invoice_item_response import CreateInvoiceItemResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.delete_tax_rate_response import DeleteTaxRateResponse
from ..types.get_invoice_item_response import GetInvoiceItemResponse
from ..types.get_invoice_items_response import GetInvoiceItemsResponse
from ..types.invoice_item_purchase_details import InvoiceItemPurchaseDetails
from ..types.invoice_item_sales_details import InvoiceItemSalesDetails
from ..types.invoice_item_type import InvoiceItemType
from ..types.invoice_items_filter import InvoiceItemsFilter
from ..types.linked_ledger_account import LinkedLedgerAccount
from ..types.not_found_response import NotFoundResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.quantity import Quantity
from ..types.row_version import RowVersion
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unit_price import UnitPrice
from ..types.unprocessable_response import UnprocessableResponse
from ..types.update_invoice_items_response import UpdateInvoiceItemsResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInvoiceItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[InvoiceItemsFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetInvoiceItemsResponse]:
        """
        List Invoice Items

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[InvoiceItemsFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetInvoiceItemsResponse]
            InvoiceItems
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/invoice-items",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=InvoiceItemsFilter, direction="write"
                ),
                "pass_through": convert_and_respect_annotation_metadata(
                    object_=pass_through, annotation=PassThroughQuery, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInvoiceItemsResponse,
                    parse_obj_as(
                        type_=GetInvoiceItemsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[Active] = OMIT,
        asset_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        expense_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        id: typing.Optional[str] = OMIT,
        income_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        inventory_date: typing.Optional[dt.date] = OMIT,
        name: typing.Optional[str] = OMIT,
        purchase_details: typing.Optional[InvoiceItemPurchaseDetails] = OMIT,
        purchased: typing.Optional[bool] = OMIT,
        quantity: typing.Optional[Quantity] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        sales_details: typing.Optional[InvoiceItemSalesDetails] = OMIT,
        sold: typing.Optional[bool] = OMIT,
        taxable: typing.Optional[bool] = OMIT,
        tracked: typing.Optional[bool] = OMIT,
        type: typing.Optional[InvoiceItemType] = OMIT,
        unit_price: typing.Optional[UnitPrice] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateInvoiceItemResponse]:
        """
        Create Invoice Item

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[Active]

        asset_account : typing.Optional[LinkedLedgerAccount]

        code : typing.Optional[str]
            User defined item code

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            A short description of the item

        expense_account : typing.Optional[LinkedLedgerAccount]

        id : typing.Optional[str]
            The ID of the item.

        income_account : typing.Optional[LinkedLedgerAccount]

        inventory_date : typing.Optional[dt.date]
            The date of opening balance if inventory item is tracked - YYYY-MM-DD.

        name : typing.Optional[str]
            Item name

        purchase_details : typing.Optional[InvoiceItemPurchaseDetails]

        purchased : typing.Optional[bool]
            Item is available for purchase transactions

        quantity : typing.Optional[Quantity]

        row_version : typing.Optional[RowVersion]

        sales_details : typing.Optional[InvoiceItemSalesDetails]

        sold : typing.Optional[bool]
            Item will be available on sales transactions

        taxable : typing.Optional[bool]
            If true, transactions for this item are taxable

        tracked : typing.Optional[bool]
            Item is inventoried

        type : typing.Optional[InvoiceItemType]
            Item type

        unit_price : typing.Optional[UnitPrice]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateInvoiceItemResponse]
            InvoiceItems
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/invoice-items",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "asset_account": convert_and_respect_annotation_metadata(
                    object_=asset_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "expense_account": convert_and_respect_annotation_metadata(
                    object_=expense_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "id": id,
                "income_account": convert_and_respect_annotation_metadata(
                    object_=income_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "inventory_date": inventory_date,
                "name": name,
                "purchase_details": convert_and_respect_annotation_metadata(
                    object_=purchase_details, annotation=InvoiceItemPurchaseDetails, direction="write"
                ),
                "purchased": purchased,
                "quantity": quantity,
                "row_version": row_version,
                "sales_details": convert_and_respect_annotation_metadata(
                    object_=sales_details, annotation=InvoiceItemSalesDetails, direction="write"
                ),
                "sold": sold,
                "taxable": taxable,
                "tracked": tracked,
                "type": type,
                "unit_price": unit_price,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
                    CreateInvoiceItemResponse,
                    parse_obj_as(
                        type_=CreateInvoiceItemResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetInvoiceItemResponse]:
        """
        Get Invoice Item

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetInvoiceItemResponse]
            InvoiceItems
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/invoice-items/{encode_path_param(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInvoiceItemResponse,
                    parse_obj_as(
                        type_=GetInvoiceItemResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteTaxRateResponse]:
        """
        Delete Invoice Item

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteTaxRateResponse]
            InvoiceItems
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/invoice-items/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteTaxRateResponse,
                    parse_obj_as(
                        type_=DeleteTaxRateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[Active] = OMIT,
        asset_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        expense_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        id: typing.Optional[str] = OMIT,
        income_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        inventory_date: typing.Optional[dt.date] = OMIT,
        name: typing.Optional[str] = OMIT,
        purchase_details: typing.Optional[InvoiceItemPurchaseDetails] = OMIT,
        purchased: typing.Optional[bool] = OMIT,
        quantity: typing.Optional[Quantity] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        sales_details: typing.Optional[InvoiceItemSalesDetails] = OMIT,
        sold: typing.Optional[bool] = OMIT,
        taxable: typing.Optional[bool] = OMIT,
        tracked: typing.Optional[bool] = OMIT,
        type: typing.Optional[InvoiceItemType] = OMIT,
        unit_price: typing.Optional[UnitPrice] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateInvoiceItemsResponse]:
        """
        Update Invoice Item

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[Active]

        asset_account : typing.Optional[LinkedLedgerAccount]

        code : typing.Optional[str]
            User defined item code

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            A short description of the item

        expense_account : typing.Optional[LinkedLedgerAccount]

        id : typing.Optional[str]
            The ID of the item.

        income_account : typing.Optional[LinkedLedgerAccount]

        inventory_date : typing.Optional[dt.date]
            The date of opening balance if inventory item is tracked - YYYY-MM-DD.

        name : typing.Optional[str]
            Item name

        purchase_details : typing.Optional[InvoiceItemPurchaseDetails]

        purchased : typing.Optional[bool]
            Item is available for purchase transactions

        quantity : typing.Optional[Quantity]

        row_version : typing.Optional[RowVersion]

        sales_details : typing.Optional[InvoiceItemSalesDetails]

        sold : typing.Optional[bool]
            Item will be available on sales transactions

        taxable : typing.Optional[bool]
            If true, transactions for this item are taxable

        tracked : typing.Optional[bool]
            Item is inventoried

        type : typing.Optional[InvoiceItemType]
            Item type

        unit_price : typing.Optional[UnitPrice]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateInvoiceItemsResponse]
            InvoiceItems
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/invoice-items/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "asset_account": convert_and_respect_annotation_metadata(
                    object_=asset_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "expense_account": convert_and_respect_annotation_metadata(
                    object_=expense_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "id": id,
                "income_account": convert_and_respect_annotation_metadata(
                    object_=income_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "inventory_date": inventory_date,
                "name": name,
                "purchase_details": convert_and_respect_annotation_metadata(
                    object_=purchase_details, annotation=InvoiceItemPurchaseDetails, direction="write"
                ),
                "purchased": purchased,
                "quantity": quantity,
                "row_version": row_version,
                "sales_details": convert_and_respect_annotation_metadata(
                    object_=sales_details, annotation=InvoiceItemSalesDetails, direction="write"
                ),
                "sold": sold,
                "taxable": taxable,
                "tracked": tracked,
                "type": type,
                "unit_price": unit_price,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
                    UpdateInvoiceItemsResponse,
                    parse_obj_as(
                        type_=UpdateInvoiceItemsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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


class AsyncRawInvoiceItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[InvoiceItemsFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetInvoiceItemsResponse]:
        """
        List Invoice Items

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        filter : typing.Optional[InvoiceItemsFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetInvoiceItemsResponse]
            InvoiceItems
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/invoice-items",
            method="GET",
            params={
                "raw": raw,
                "cursor": cursor,
                "limit": limit,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=InvoiceItemsFilter, direction="write"
                ),
                "pass_through": convert_and_respect_annotation_metadata(
                    object_=pass_through, annotation=PassThroughQuery, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInvoiceItemsResponse,
                    parse_obj_as(
                        type_=GetInvoiceItemsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[Active] = OMIT,
        asset_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        expense_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        id: typing.Optional[str] = OMIT,
        income_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        inventory_date: typing.Optional[dt.date] = OMIT,
        name: typing.Optional[str] = OMIT,
        purchase_details: typing.Optional[InvoiceItemPurchaseDetails] = OMIT,
        purchased: typing.Optional[bool] = OMIT,
        quantity: typing.Optional[Quantity] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        sales_details: typing.Optional[InvoiceItemSalesDetails] = OMIT,
        sold: typing.Optional[bool] = OMIT,
        taxable: typing.Optional[bool] = OMIT,
        tracked: typing.Optional[bool] = OMIT,
        type: typing.Optional[InvoiceItemType] = OMIT,
        unit_price: typing.Optional[UnitPrice] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateInvoiceItemResponse]:
        """
        Create Invoice Item

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[Active]

        asset_account : typing.Optional[LinkedLedgerAccount]

        code : typing.Optional[str]
            User defined item code

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            A short description of the item

        expense_account : typing.Optional[LinkedLedgerAccount]

        id : typing.Optional[str]
            The ID of the item.

        income_account : typing.Optional[LinkedLedgerAccount]

        inventory_date : typing.Optional[dt.date]
            The date of opening balance if inventory item is tracked - YYYY-MM-DD.

        name : typing.Optional[str]
            Item name

        purchase_details : typing.Optional[InvoiceItemPurchaseDetails]

        purchased : typing.Optional[bool]
            Item is available for purchase transactions

        quantity : typing.Optional[Quantity]

        row_version : typing.Optional[RowVersion]

        sales_details : typing.Optional[InvoiceItemSalesDetails]

        sold : typing.Optional[bool]
            Item will be available on sales transactions

        taxable : typing.Optional[bool]
            If true, transactions for this item are taxable

        tracked : typing.Optional[bool]
            Item is inventoried

        type : typing.Optional[InvoiceItemType]
            Item type

        unit_price : typing.Optional[UnitPrice]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateInvoiceItemResponse]
            InvoiceItems
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/invoice-items",
            method="POST",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "asset_account": convert_and_respect_annotation_metadata(
                    object_=asset_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "expense_account": convert_and_respect_annotation_metadata(
                    object_=expense_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "id": id,
                "income_account": convert_and_respect_annotation_metadata(
                    object_=income_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "inventory_date": inventory_date,
                "name": name,
                "purchase_details": convert_and_respect_annotation_metadata(
                    object_=purchase_details, annotation=InvoiceItemPurchaseDetails, direction="write"
                ),
                "purchased": purchased,
                "quantity": quantity,
                "row_version": row_version,
                "sales_details": convert_and_respect_annotation_metadata(
                    object_=sales_details, annotation=InvoiceItemSalesDetails, direction="write"
                ),
                "sold": sold,
                "taxable": taxable,
                "tracked": tracked,
                "type": type,
                "unit_price": unit_price,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
                    CreateInvoiceItemResponse,
                    parse_obj_as(
                        type_=CreateInvoiceItemResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetInvoiceItemResponse]:
        """
        Get Invoice Item

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetInvoiceItemResponse]
            InvoiceItems
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/invoice-items/{encode_path_param(id)}",
            method="GET",
            params={
                "raw": raw,
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetInvoiceItemResponse,
                    parse_obj_as(
                        type_=GetInvoiceItemResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteTaxRateResponse]:
        """
        Delete Invoice Item

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteTaxRateResponse]
            InvoiceItems
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/invoice-items/{encode_path_param(id)}",
            method="DELETE",
            params={
                "raw": raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteTaxRateResponse,
                    parse_obj_as(
                        type_=DeleteTaxRateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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

    async def update(
        self,
        id_: str,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[Active] = OMIT,
        asset_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        description: typing.Optional[str] = OMIT,
        expense_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        id: typing.Optional[str] = OMIT,
        income_account: typing.Optional[LinkedLedgerAccount] = OMIT,
        inventory_date: typing.Optional[dt.date] = OMIT,
        name: typing.Optional[str] = OMIT,
        purchase_details: typing.Optional[InvoiceItemPurchaseDetails] = OMIT,
        purchased: typing.Optional[bool] = OMIT,
        quantity: typing.Optional[Quantity] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        sales_details: typing.Optional[InvoiceItemSalesDetails] = OMIT,
        sold: typing.Optional[bool] = OMIT,
        taxable: typing.Optional[bool] = OMIT,
        tracked: typing.Optional[bool] = OMIT,
        type: typing.Optional[InvoiceItemType] = OMIT,
        unit_price: typing.Optional[UnitPrice] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateInvoiceItemsResponse]:
        """
        Update Invoice Item

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[Active]

        asset_account : typing.Optional[LinkedLedgerAccount]

        code : typing.Optional[str]
            User defined item code

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        description : typing.Optional[str]
            A short description of the item

        expense_account : typing.Optional[LinkedLedgerAccount]

        id : typing.Optional[str]
            The ID of the item.

        income_account : typing.Optional[LinkedLedgerAccount]

        inventory_date : typing.Optional[dt.date]
            The date of opening balance if inventory item is tracked - YYYY-MM-DD.

        name : typing.Optional[str]
            Item name

        purchase_details : typing.Optional[InvoiceItemPurchaseDetails]

        purchased : typing.Optional[bool]
            Item is available for purchase transactions

        quantity : typing.Optional[Quantity]

        row_version : typing.Optional[RowVersion]

        sales_details : typing.Optional[InvoiceItemSalesDetails]

        sold : typing.Optional[bool]
            Item will be available on sales transactions

        taxable : typing.Optional[bool]
            If true, transactions for this item are taxable

        tracked : typing.Optional[bool]
            Item is inventoried

        type : typing.Optional[InvoiceItemType]
            Item type

        unit_price : typing.Optional[UnitPrice]

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateInvoiceItemsResponse]
            InvoiceItems
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/invoice-items/{encode_path_param(id_)}",
            method="PATCH",
            params={
                "raw": raw,
            },
            json={
                "active": active,
                "asset_account": convert_and_respect_annotation_metadata(
                    object_=asset_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "code": code,
                "created_at": created_at,
                "created_by": created_by,
                "description": description,
                "expense_account": convert_and_respect_annotation_metadata(
                    object_=expense_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "id": id,
                "income_account": convert_and_respect_annotation_metadata(
                    object_=income_account, annotation=typing.Optional[LinkedLedgerAccount], direction="write"
                ),
                "inventory_date": inventory_date,
                "name": name,
                "purchase_details": convert_and_respect_annotation_metadata(
                    object_=purchase_details, annotation=InvoiceItemPurchaseDetails, direction="write"
                ),
                "purchased": purchased,
                "quantity": quantity,
                "row_version": row_version,
                "sales_details": convert_and_respect_annotation_metadata(
                    object_=sales_details, annotation=InvoiceItemSalesDetails, direction="write"
                ),
                "sold": sold,
                "taxable": taxable,
                "tracked": tracked,
                "type": type,
                "unit_price": unit_price,
                "updated_at": updated_at,
                "updated_by": updated_by,
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
                    UpdateInvoiceItemsResponse,
                    parse_obj_as(
                        type_=UpdateInvoiceItemsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
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
