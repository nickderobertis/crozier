

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account_category import AccountCategory
from ..types.categories import Categories
from ..types.categorised_account import CategorisedAccount
from ..types.categorised_accounts import CategorisedAccounts
from .raw_client import AsyncRawCategoriesClient, RawCategoriesClient
from .types.confirm_categories_categories_item import ConfirmCategoriesCategoriesItem


OMIT = typing.cast(typing.Any, ...)


class CategoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCategoriesClient
        """
        return self._raw_client

    def list_available_account_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Categories:
        """
        Lists available account categories Codat's categorisation engine can provide.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Categories
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.categories.list_available_account_categories()
        """
        _response = self._raw_client.list_available_account_categories(request_options=request_options)
        return _response.data

    def list_accounts_categories(
        self,
        company_id: str,
        connection_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CategorisedAccounts:
        """
        Lists suggested and confirmed chart of account categories for the given company and data connection.

        Parameters
        ----------
        company_id : str

        connection_id : str

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        order_by : typing.Optional[str]
            Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CategorisedAccounts
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.categories.list_accounts_categories(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            page=1,
            page_size=100,
            order_by="-modifiedDate",
        )
        """
        _response = self._raw_client.list_accounts_categories(
            company_id,
            connection_id,
            page=page,
            page_size=page_size,
            query=query,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def update_accounts_categories(
        self,
        company_id: str,
        connection_id: str,
        *,
        categories: typing.Optional[typing.Sequence[ConfirmCategoriesCategoriesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CategorisedAccount]:
        """
        Comfirms the categories for all or a batch of accounts for a specific connection.

        Parameters
        ----------
        company_id : str

        connection_id : str

        categories : typing.Optional[typing.Sequence[ConfirmCategoriesCategoriesItem]]
            List of confirmed account categories set manually by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CategorisedAccount]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.categories.update_accounts_categories(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
        )
        """
        _response = self._raw_client.update_accounts_categories(
            company_id, connection_id, categories=categories, request_options=request_options
        )
        return _response.data

    def get_account_category(
        self,
        company_id: str,
        connection_id: str,
        account_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CategorisedAccount:
        """
        Get category for specific nominal account.

        Parameters
        ----------
        company_id : str

        connection_id : str

        account_id : str
            Nominal account id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CategorisedAccount
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.categories.get_account_category(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            account_id="accountId",
        )
        """
        _response = self._raw_client.get_account_category(
            company_id, connection_id, account_id, request_options=request_options
        )
        return _response.data

    def update_account_category(
        self,
        company_id: str,
        connection_id: str,
        account_id: str,
        *,
        confirmed: AccountCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CategorisedAccount:
        """
        Update category for a specific nominal account

        Parameters
        ----------
        company_id : str

        connection_id : str

        account_id : str
            Nominal account id

        confirmed : AccountCategory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CategorisedAccount
            OK

        Examples
        --------
        from fern import AccountCategory, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.categories.update_account_category(
            company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
            connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            account_id="accountId",
            confirmed=AccountCategory(
                detail_type="Cash",
                subtype="Current",
                type="Asset",
            ),
        )
        """
        _response = self._raw_client.update_account_category(
            company_id, connection_id, account_id, confirmed=confirmed, request_options=request_options
        )
        return _response.data


class AsyncCategoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCategoriesClient
        """
        return self._raw_client

    async def list_available_account_categories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Categories:
        """
        Lists available account categories Codat's categorisation engine can provide.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Categories
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.categories.list_available_account_categories()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_available_account_categories(request_options=request_options)
        return _response.data

    async def list_accounts_categories(
        self,
        company_id: str,
        connection_id: str,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CategorisedAccounts:
        """
        Lists suggested and confirmed chart of account categories for the given company and data connection.

        Parameters
        ----------
        company_id : str

        connection_id : str

        page : int
            Page number. [Read more](https://docs.codat.io/using-the-api/paging).

        page_size : typing.Optional[int]
            Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).

        query : typing.Optional[str]
            Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).

        order_by : typing.Optional[str]
            Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CategorisedAccounts
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.categories.list_accounts_categories(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                page=1,
                page_size=100,
                order_by="-modifiedDate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_accounts_categories(
            company_id,
            connection_id,
            page=page,
            page_size=page_size,
            query=query,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def update_accounts_categories(
        self,
        company_id: str,
        connection_id: str,
        *,
        categories: typing.Optional[typing.Sequence[ConfirmCategoriesCategoriesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CategorisedAccount]:
        """
        Comfirms the categories for all or a batch of accounts for a specific connection.

        Parameters
        ----------
        company_id : str

        connection_id : str

        categories : typing.Optional[typing.Sequence[ConfirmCategoriesCategoriesItem]]
            List of confirmed account categories set manually by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CategorisedAccount]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.categories.update_accounts_categories(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_accounts_categories(
            company_id, connection_id, categories=categories, request_options=request_options
        )
        return _response.data

    async def get_account_category(
        self,
        company_id: str,
        connection_id: str,
        account_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CategorisedAccount:
        """
        Get category for specific nominal account.

        Parameters
        ----------
        company_id : str

        connection_id : str

        account_id : str
            Nominal account id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CategorisedAccount
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.categories.get_account_category(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                account_id="accountId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_category(
            company_id, connection_id, account_id, request_options=request_options
        )
        return _response.data

    async def update_account_category(
        self,
        company_id: str,
        connection_id: str,
        account_id: str,
        *,
        confirmed: AccountCategory,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CategorisedAccount:
        """
        Update category for a specific nominal account

        Parameters
        ----------
        company_id : str

        connection_id : str

        account_id : str
            Nominal account id

        confirmed : AccountCategory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CategorisedAccount
            OK

        Examples
        --------
        import asyncio

        from fern import AccountCategory, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.categories.update_account_category(
                company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
                connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
                account_id="accountId",
                confirmed=AccountCategory(
                    detail_type="Cash",
                    subtype="Current",
                    type="Asset",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_account_category(
            company_id, connection_id, account_id, confirmed=confirmed, request_options=request_options
        )
        return _response.data
