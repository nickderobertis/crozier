

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account_list_response import AccountListResponse
from ..types.account_response import AccountResponse
from .raw_client import AsyncRawAccountsClient, RawAccountsClient
from .types.account_create_request_data import AccountCreateRequestData
from .types.account_update_request_data import AccountUpdateRequestData


OMIT = typing.cast(typing.Any, ...)


class AccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountsClient
        """
        return self._raw_client

    def list_accounts(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountListResponse:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

        sort : typing.Optional[str]
            Sort field (prefix with - for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.list_accounts()
        """
        _response = self._raw_client.list_accounts(
            page_offset=page_offset, page_limit=page_limit, sort=sort, request_options=request_options
        )
        return _response.data

    def create_account(
        self,
        *,
        data: typing.Optional[AccountCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountResponse:
        """
        Parameters
        ----------
        data : typing.Optional[AccountCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            Account created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.create_account()
        """
        _response = self._raw_client.create_account(data=data, request_options=request_options)
        return _response.data

    def get_account(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AccountResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.get_account(
            id=1,
        )
        """
        _response = self._raw_client.get_account(id, request_options=request_options)
        return _response.data

    def delete_account(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.delete_account(
            id=1,
        )
        """
        _response = self._raw_client.delete_account(id, request_options=request_options)
        return _response.data

    def update_account(
        self,
        id: int,
        *,
        data: typing.Optional[AccountUpdateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        data : typing.Optional[AccountUpdateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            Account updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.accounts.update_account(
            id=1,
        )
        """
        _response = self._raw_client.update_account(id, data=data, request_options=request_options)
        return _response.data


class AsyncAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountsClient
        """
        return self._raw_client

    async def list_accounts(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountListResponse:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

        sort : typing.Optional[str]
            Sort field (prefix with - for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.list_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_accounts(
            page_offset=page_offset, page_limit=page_limit, sort=sort, request_options=request_options
        )
        return _response.data

    async def create_account(
        self,
        *,
        data: typing.Optional[AccountCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountResponse:
        """
        Parameters
        ----------
        data : typing.Optional[AccountCreateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            Account created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.create_account()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_account(data=data, request_options=request_options)
        return _response.data

    async def get_account(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AccountResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.get_account(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account(id, request_options=request_options)
        return _response.data

    async def delete_account(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : int
            Resource ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.delete_account(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_account(id, request_options=request_options)
        return _response.data

    async def update_account(
        self,
        id: int,
        *,
        data: typing.Optional[AccountUpdateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountResponse:
        """
        Parameters
        ----------
        id : int
            Resource ID

        data : typing.Optional[AccountUpdateRequestData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            Account updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.accounts.update_account(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_account(id, data=data, request_options=request_options)
        return _response.data
