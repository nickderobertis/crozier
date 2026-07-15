

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bank_account import BankAccount
from ..types.create_ledger_account_response import CreateLedgerAccountResponse
from ..types.created_at import CreatedAt
from ..types.created_by import CreatedBy
from ..types.currency import Currency
from ..types.delete_ledger_account_response import DeleteLedgerAccountResponse
from ..types.get_ledger_account_response import GetLedgerAccountResponse
from ..types.get_ledger_accounts_response import GetLedgerAccountsResponse
from ..types.id import Id
from ..types.ledger_account_categories_item import LedgerAccountCategoriesItem
from ..types.ledger_account_classification import LedgerAccountClassification
from ..types.ledger_account_parent_account import LedgerAccountParentAccount
from ..types.ledger_account_status import LedgerAccountStatus
from ..types.ledger_account_sub_accounts_item import LedgerAccountSubAccountsItem
from ..types.ledger_account_type import LedgerAccountType
from ..types.linked_tax_rate import LinkedTaxRate
from ..types.pass_through_query import PassThroughQuery
from ..types.row_version import RowVersion
from ..types.update_ledger_account_response import UpdateLedgerAccountResponse
from ..types.updated_at import UpdatedAt
from ..types.updated_by import UpdatedBy
from .raw_client import AsyncRawLedgerAccountsClient, RawLedgerAccountsClient


OMIT = typing.cast(typing.Any, ...)


class LedgerAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLedgerAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLedgerAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLedgerAccountsClient
        """
        return self._raw_client

    def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLedgerAccountsResponse:
        """
        List Ledger Accounts

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLedgerAccountsResponse
            LedgerAccounts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.ledger_accounts.all_(
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        bank_account: typing.Optional[BankAccount] = OMIT,
        categories: typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]] = OMIT,
        classification: typing.Optional[LedgerAccountClassification] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        fully_qualified_name: typing.Optional[str] = OMIT,
        header: typing.Optional[bool] = OMIT,
        id: typing.Optional[Id] = OMIT,
        last_reconciliation_date: typing.Optional[dt.date] = OMIT,
        level: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        nominal_code: typing.Optional[str] = OMIT,
        opening_balance: typing.Optional[float] = OMIT,
        parent_account: typing.Optional[LedgerAccountParentAccount] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[LedgerAccountStatus] = OMIT,
        sub_account: typing.Optional[bool] = OMIT,
        sub_accounts: typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        tax_type: typing.Optional[str] = OMIT,
        type: typing.Optional[LedgerAccountType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateLedgerAccountResponse:
        """
        Create Ledger Account

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]
            Whether the account is active or not.

        bank_account : typing.Optional[BankAccount]

        categories : typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]
            The categories of the account.

        classification : typing.Optional[LedgerAccountClassification]
            The classification of account.

        code : typing.Optional[str]
            The code assigned to the account.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        current_balance : typing.Optional[float]
            The current balance of the account.

        description : typing.Optional[str]
            The description of the account.

        display_id : typing.Optional[str]
            The human readable display ID used when displaying the account

        fully_qualified_name : typing.Optional[str]
            The fully qualified name of the account.

        header : typing.Optional[bool]
            Whether the account is a header or not.

        id : typing.Optional[Id]

        last_reconciliation_date : typing.Optional[dt.date]
            Reconciliation Date means the last calendar day of each Reconciliation Period.

        level : typing.Optional[float]

        name : typing.Optional[str]
            The name of the account.

        nominal_code : typing.Optional[str]
            The nominal code of the ledger account.

        opening_balance : typing.Optional[float]
            The opening balance of the account.

        parent_account : typing.Optional[LedgerAccountParentAccount]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[LedgerAccountStatus]
            The status of the account.

        sub_account : typing.Optional[bool]
            Whether the account is a sub account or not.

        sub_accounts : typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]
            The sub accounts of the account.

        sub_type : typing.Optional[str]
            The sub type of account.

        tax_rate : typing.Optional[LinkedTaxRate]

        tax_type : typing.Optional[str]
            The tax type of the account.

        type : typing.Optional[LedgerAccountType]
            The type of account.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLedgerAccountResponse
            LedgerAccount created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.ledger_accounts.add()
        """
        _response = self._raw_client.add(
            raw=raw,
            active=active,
            bank_account=bank_account,
            categories=categories,
            classification=classification,
            code=code,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            current_balance=current_balance,
            description=description,
            display_id=display_id,
            fully_qualified_name=fully_qualified_name,
            header=header,
            id=id,
            last_reconciliation_date=last_reconciliation_date,
            level=level,
            name=name,
            nominal_code=nominal_code,
            opening_balance=opening_balance,
            parent_account=parent_account,
            row_version=row_version,
            status=status,
            sub_account=sub_account,
            sub_accounts=sub_accounts,
            sub_type=sub_type,
            tax_rate=tax_rate,
            tax_type=tax_type,
            type=type,
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
    ) -> GetLedgerAccountResponse:
        """
        Get Ledger Account

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
        GetLedgerAccountResponse
            LedgerAccount

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.ledger_accounts.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLedgerAccountResponse:
        """
        Delete Ledger Account

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
        DeleteLedgerAccountResponse
            LedgerAccount deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.ledger_accounts.delete(
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
        active: typing.Optional[bool] = OMIT,
        bank_account: typing.Optional[BankAccount] = OMIT,
        categories: typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]] = OMIT,
        classification: typing.Optional[LedgerAccountClassification] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        fully_qualified_name: typing.Optional[str] = OMIT,
        header: typing.Optional[bool] = OMIT,
        id: typing.Optional[Id] = OMIT,
        last_reconciliation_date: typing.Optional[dt.date] = OMIT,
        level: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        nominal_code: typing.Optional[str] = OMIT,
        opening_balance: typing.Optional[float] = OMIT,
        parent_account: typing.Optional[LedgerAccountParentAccount] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[LedgerAccountStatus] = OMIT,
        sub_account: typing.Optional[bool] = OMIT,
        sub_accounts: typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        tax_type: typing.Optional[str] = OMIT,
        type: typing.Optional[LedgerAccountType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateLedgerAccountResponse:
        """
        Update Ledger Account

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]
            Whether the account is active or not.

        bank_account : typing.Optional[BankAccount]

        categories : typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]
            The categories of the account.

        classification : typing.Optional[LedgerAccountClassification]
            The classification of account.

        code : typing.Optional[str]
            The code assigned to the account.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        current_balance : typing.Optional[float]
            The current balance of the account.

        description : typing.Optional[str]
            The description of the account.

        display_id : typing.Optional[str]
            The human readable display ID used when displaying the account

        fully_qualified_name : typing.Optional[str]
            The fully qualified name of the account.

        header : typing.Optional[bool]
            Whether the account is a header or not.

        id : typing.Optional[Id]

        last_reconciliation_date : typing.Optional[dt.date]
            Reconciliation Date means the last calendar day of each Reconciliation Period.

        level : typing.Optional[float]

        name : typing.Optional[str]
            The name of the account.

        nominal_code : typing.Optional[str]
            The nominal code of the ledger account.

        opening_balance : typing.Optional[float]
            The opening balance of the account.

        parent_account : typing.Optional[LedgerAccountParentAccount]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[LedgerAccountStatus]
            The status of the account.

        sub_account : typing.Optional[bool]
            Whether the account is a sub account or not.

        sub_accounts : typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]
            The sub accounts of the account.

        sub_type : typing.Optional[str]
            The sub type of account.

        tax_rate : typing.Optional[LinkedTaxRate]

        tax_type : typing.Optional[str]
            The tax type of the account.

        type : typing.Optional[LedgerAccountType]
            The type of account.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLedgerAccountResponse
            LedgerAccount updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.ledger_accounts.update(
            id_="id",
        )
        """
        _response = self._raw_client.update(
            id_,
            raw=raw,
            active=active,
            bank_account=bank_account,
            categories=categories,
            classification=classification,
            code=code,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            current_balance=current_balance,
            description=description,
            display_id=display_id,
            fully_qualified_name=fully_qualified_name,
            header=header,
            id=id,
            last_reconciliation_date=last_reconciliation_date,
            level=level,
            name=name,
            nominal_code=nominal_code,
            opening_balance=opening_balance,
            parent_account=parent_account,
            row_version=row_version,
            status=status,
            sub_account=sub_account,
            sub_accounts=sub_accounts,
            sub_type=sub_type,
            tax_rate=tax_rate,
            tax_type=tax_type,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data


class AsyncLedgerAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLedgerAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLedgerAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLedgerAccountsClient
        """
        return self._raw_client

    async def all_(
        self,
        *,
        raw: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLedgerAccountsResponse:
        """
        List Ledger Accounts

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        cursor : typing.Optional[str]
            Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.

        limit : typing.Optional[int]
            Number of results to return. Minimum 1, Maximum 200, Default 20

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLedgerAccountsResponse
            LedgerAccounts

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
            await client.ledger_accounts.all_(
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(
            raw=raw,
            cursor=cursor,
            limit=limit,
            pass_through=pass_through,
            fields=fields,
            request_options=request_options,
        )
        return _response.data

    async def add(
        self,
        *,
        raw: typing.Optional[bool] = None,
        active: typing.Optional[bool] = OMIT,
        bank_account: typing.Optional[BankAccount] = OMIT,
        categories: typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]] = OMIT,
        classification: typing.Optional[LedgerAccountClassification] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        fully_qualified_name: typing.Optional[str] = OMIT,
        header: typing.Optional[bool] = OMIT,
        id: typing.Optional[Id] = OMIT,
        last_reconciliation_date: typing.Optional[dt.date] = OMIT,
        level: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        nominal_code: typing.Optional[str] = OMIT,
        opening_balance: typing.Optional[float] = OMIT,
        parent_account: typing.Optional[LedgerAccountParentAccount] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[LedgerAccountStatus] = OMIT,
        sub_account: typing.Optional[bool] = OMIT,
        sub_accounts: typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        tax_type: typing.Optional[str] = OMIT,
        type: typing.Optional[LedgerAccountType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateLedgerAccountResponse:
        """
        Create Ledger Account

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]
            Whether the account is active or not.

        bank_account : typing.Optional[BankAccount]

        categories : typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]
            The categories of the account.

        classification : typing.Optional[LedgerAccountClassification]
            The classification of account.

        code : typing.Optional[str]
            The code assigned to the account.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        current_balance : typing.Optional[float]
            The current balance of the account.

        description : typing.Optional[str]
            The description of the account.

        display_id : typing.Optional[str]
            The human readable display ID used when displaying the account

        fully_qualified_name : typing.Optional[str]
            The fully qualified name of the account.

        header : typing.Optional[bool]
            Whether the account is a header or not.

        id : typing.Optional[Id]

        last_reconciliation_date : typing.Optional[dt.date]
            Reconciliation Date means the last calendar day of each Reconciliation Period.

        level : typing.Optional[float]

        name : typing.Optional[str]
            The name of the account.

        nominal_code : typing.Optional[str]
            The nominal code of the ledger account.

        opening_balance : typing.Optional[float]
            The opening balance of the account.

        parent_account : typing.Optional[LedgerAccountParentAccount]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[LedgerAccountStatus]
            The status of the account.

        sub_account : typing.Optional[bool]
            Whether the account is a sub account or not.

        sub_accounts : typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]
            The sub accounts of the account.

        sub_type : typing.Optional[str]
            The sub type of account.

        tax_rate : typing.Optional[LinkedTaxRate]

        tax_type : typing.Optional[str]
            The tax type of the account.

        type : typing.Optional[LedgerAccountType]
            The type of account.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLedgerAccountResponse
            LedgerAccount created

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
            await client.ledger_accounts.add()


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            raw=raw,
            active=active,
            bank_account=bank_account,
            categories=categories,
            classification=classification,
            code=code,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            current_balance=current_balance,
            description=description,
            display_id=display_id,
            fully_qualified_name=fully_qualified_name,
            header=header,
            id=id,
            last_reconciliation_date=last_reconciliation_date,
            level=level,
            name=name,
            nominal_code=nominal_code,
            opening_balance=opening_balance,
            parent_account=parent_account,
            row_version=row_version,
            status=status,
            sub_account=sub_account,
            sub_accounts=sub_accounts,
            sub_type=sub_type,
            tax_rate=tax_rate,
            tax_type=tax_type,
            type=type,
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
    ) -> GetLedgerAccountResponse:
        """
        Get Ledger Account

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
        GetLedgerAccountResponse
            LedgerAccount

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
            await client.ledger_accounts.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLedgerAccountResponse:
        """
        Delete Ledger Account

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
        DeleteLedgerAccountResponse
            LedgerAccount deleted

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
            await client.ledger_accounts.delete(
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
        active: typing.Optional[bool] = OMIT,
        bank_account: typing.Optional[BankAccount] = OMIT,
        categories: typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]] = OMIT,
        classification: typing.Optional[LedgerAccountClassification] = OMIT,
        code: typing.Optional[str] = OMIT,
        created_at: typing.Optional[CreatedAt] = OMIT,
        created_by: typing.Optional[CreatedBy] = OMIT,
        currency: typing.Optional[Currency] = OMIT,
        current_balance: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        display_id: typing.Optional[str] = OMIT,
        fully_qualified_name: typing.Optional[str] = OMIT,
        header: typing.Optional[bool] = OMIT,
        id: typing.Optional[Id] = OMIT,
        last_reconciliation_date: typing.Optional[dt.date] = OMIT,
        level: typing.Optional[float] = OMIT,
        name: typing.Optional[str] = OMIT,
        nominal_code: typing.Optional[str] = OMIT,
        opening_balance: typing.Optional[float] = OMIT,
        parent_account: typing.Optional[LedgerAccountParentAccount] = OMIT,
        row_version: typing.Optional[RowVersion] = OMIT,
        status: typing.Optional[LedgerAccountStatus] = OMIT,
        sub_account: typing.Optional[bool] = OMIT,
        sub_accounts: typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]] = OMIT,
        sub_type: typing.Optional[str] = OMIT,
        tax_rate: typing.Optional[LinkedTaxRate] = OMIT,
        tax_type: typing.Optional[str] = OMIT,
        type: typing.Optional[LedgerAccountType] = OMIT,
        updated_at: typing.Optional[UpdatedAt] = OMIT,
        updated_by: typing.Optional[UpdatedBy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateLedgerAccountResponse:
        """
        Update Ledger Account

        Parameters
        ----------
        id_ : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        active : typing.Optional[bool]
            Whether the account is active or not.

        bank_account : typing.Optional[BankAccount]

        categories : typing.Optional[typing.Sequence[LedgerAccountCategoriesItem]]
            The categories of the account.

        classification : typing.Optional[LedgerAccountClassification]
            The classification of account.

        code : typing.Optional[str]
            The code assigned to the account.

        created_at : typing.Optional[CreatedAt]

        created_by : typing.Optional[CreatedBy]

        currency : typing.Optional[Currency]

        current_balance : typing.Optional[float]
            The current balance of the account.

        description : typing.Optional[str]
            The description of the account.

        display_id : typing.Optional[str]
            The human readable display ID used when displaying the account

        fully_qualified_name : typing.Optional[str]
            The fully qualified name of the account.

        header : typing.Optional[bool]
            Whether the account is a header or not.

        id : typing.Optional[Id]

        last_reconciliation_date : typing.Optional[dt.date]
            Reconciliation Date means the last calendar day of each Reconciliation Period.

        level : typing.Optional[float]

        name : typing.Optional[str]
            The name of the account.

        nominal_code : typing.Optional[str]
            The nominal code of the ledger account.

        opening_balance : typing.Optional[float]
            The opening balance of the account.

        parent_account : typing.Optional[LedgerAccountParentAccount]

        row_version : typing.Optional[RowVersion]

        status : typing.Optional[LedgerAccountStatus]
            The status of the account.

        sub_account : typing.Optional[bool]
            Whether the account is a sub account or not.

        sub_accounts : typing.Optional[typing.Sequence[LedgerAccountSubAccountsItem]]
            The sub accounts of the account.

        sub_type : typing.Optional[str]
            The sub type of account.

        tax_rate : typing.Optional[LinkedTaxRate]

        tax_type : typing.Optional[str]
            The tax type of the account.

        type : typing.Optional[LedgerAccountType]
            The type of account.

        updated_at : typing.Optional[UpdatedAt]

        updated_by : typing.Optional[UpdatedBy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLedgerAccountResponse
            LedgerAccount updated

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
            await client.ledger_accounts.update(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_,
            raw=raw,
            active=active,
            bank_account=bank_account,
            categories=categories,
            classification=classification,
            code=code,
            created_at=created_at,
            created_by=created_by,
            currency=currency,
            current_balance=current_balance,
            description=description,
            display_id=display_id,
            fully_qualified_name=fully_qualified_name,
            header=header,
            id=id,
            last_reconciliation_date=last_reconciliation_date,
            level=level,
            name=name,
            nominal_code=nominal_code,
            opening_balance=opening_balance,
            parent_account=parent_account,
            row_version=row_version,
            status=status,
            sub_account=sub_account,
            sub_accounts=sub_accounts,
            sub_type=sub_type,
            tax_rate=tax_rate,
            tax_type=tax_type,
            type=type,
            updated_at=updated_at,
            updated_by=updated_by,
            request_options=request_options,
        )
        return _response.data
