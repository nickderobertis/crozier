

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.active import Active
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
from ..types.pass_through_query import PassThroughQuery
from ..types.quantity import Quantity
from ..types.row_version import RowVersion
from ..types.unit_price import UnitPrice
from ..types.update_invoice_items_response import UpdateInvoiceItemsResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawInvoiceItemsClient, RawInvoiceItemsClient


OMIT = typing.cast(typing.Any, ...)


class InvoiceItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInvoiceItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInvoiceItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInvoiceItemsClient
        """
        return self._raw_client

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
    ) -> GetInvoiceItemsResponse:
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
        GetInvoiceItemsResponse
            InvoiceItems

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.invoice_items.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CreateInvoiceItemResponse:
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
        CreateInvoiceItemResponse
            InvoiceItems

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.invoice_items.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            active=active,
            asset_account=asset_account,
            code=code,
            created_at=created_at,
            created_by=created_by,
            description=description,
            expense_account=expense_account,
            id=id,
            income_account=income_account,
            inventory_date=inventory_date,
            name=name,
            purchase_details=purchase_details,
            purchased=purchased,
            quantity=quantity,
            row_version=row_version,
            sales_details=sales_details,
            sold=sold,
            taxable=taxable,
            tracked=tracked,
            type=type,
            unit_price=unit_price,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetInvoiceItemResponse:
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
        GetInvoiceItemResponse
            InvoiceItems

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.invoice_items.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTaxRateResponse:
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
        DeleteTaxRateResponse
            InvoiceItems

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.invoice_items.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

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
    ) -> UpdateInvoiceItemsResponse:
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
        UpdateInvoiceItemsResponse
            InvoiceItems

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.invoice_items.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            active=active,
            asset_account=asset_account,
            code=code,
            created_at=created_at,
            created_by=created_by,
            description=description,
            expense_account=expense_account,
            id=id,
            income_account=income_account,
            inventory_date=inventory_date,
            name=name,
            purchase_details=purchase_details,
            purchased=purchased,
            quantity=quantity,
            row_version=row_version,
            sales_details=sales_details,
            sold=sold,
            taxable=taxable,
            tracked=tracked,
            type=type,
            unit_price=unit_price,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data


class AsyncInvoiceItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInvoiceItemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInvoiceItemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInvoiceItemsClient
        """
        return self._raw_client

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
    ) -> GetInvoiceItemsResponse:
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
        GetInvoiceItemsResponse
            InvoiceItems

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.invoice_items.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            filter=filter,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CreateInvoiceItemResponse:
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
        CreateInvoiceItemResponse
            InvoiceItems

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.invoice_items.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            active=active,
            asset_account=asset_account,
            code=code,
            created_at=created_at,
            created_by=created_by,
            description=description,
            expense_account=expense_account,
            id=id,
            income_account=income_account,
            inventory_date=inventory_date,
            name=name,
            purchase_details=purchase_details,
            purchased=purchased,
            quantity=quantity,
            row_version=row_version,
            sales_details=sales_details,
            sold=sold,
            taxable=taxable,
            tracked=tracked,
            type=type,
            unit_price=unit_price,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetInvoiceItemResponse:
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
        GetInvoiceItemResponse
            InvoiceItems

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.invoice_items.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteTaxRateResponse:
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
        DeleteTaxRateResponse
            InvoiceItems

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.invoice_items.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

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
    ) -> UpdateInvoiceItemsResponse:
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
        UpdateInvoiceItemsResponse
            InvoiceItems

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.invoice_items.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            active=active,
            asset_account=asset_account,
            code=code,
            created_at=created_at,
            created_by=created_by,
            description=description,
            expense_account=expense_account,
            id=id,
            income_account=income_account,
            inventory_date=inventory_date,
            name=name,
            purchase_details=purchase_details,
            purchased=purchased,
            quantity=quantity,
            row_version=row_version,
            sales_details=sales_details,
            sold=sold,
            taxable=taxable,
            tracked=tracked,
            type=type,
            unit_price=unit_price,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
