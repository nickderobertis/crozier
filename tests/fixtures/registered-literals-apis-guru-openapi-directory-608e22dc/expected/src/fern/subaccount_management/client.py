

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.subaccount_create_response import SubaccountCreateResponse
from ..types.subaccount_response import SubaccountResponse
from ..types.subaccounts_all_response import SubaccountsAllResponse
from .raw_client import AsyncRawSubaccountManagementClient, RawSubaccountManagementClient


OMIT = typing.cast(typing.Any, ...)


class SubaccountManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubaccountManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubaccountManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubaccountManagementClient
        """
        return self._raw_client

    def retrieve_subaccounts_list(
        self, api_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubaccountsAllResponse:
        """
        Get the information of all the subaccounts owned by the primary account.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubaccountsAllResponse
            Subaccounts response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.subaccount_management.retrieve_subaccounts_list(
            api_key="api_key",
        )
        """
        _response = self._raw_client.retrieve_subaccounts_list(api_key, request_options=request_options)
        return _response.data

    def create_sub_account(
        self,
        api_key: str,
        *,
        name: str,
        secret: typing.Optional[str] = OMIT,
        use_primary_account_balance: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubaccountCreateResponse:
        """
        Create a subaccount for a given primary account.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        name : str

        secret : typing.Optional[str]

        use_primary_account_balance : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubaccountCreateResponse
            Subaccount response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.subaccount_management.create_sub_account(
            api_key="api_key",
            name="Subaccount department A",
        )
        """
        _response = self._raw_client.create_sub_account(
            api_key,
            name=name,
            secret=secret,
            use_primary_account_balance=use_primary_account_balance,
            request_options=request_options,
        )
        return _response.data

    def retrieve_subaccount(
        self, api_key: str, subaccount_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubaccountResponse:
        """
        Get the information of a subaccount specified with its API key.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        subaccount_key : str
            ID of the subaccount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubaccountResponse
            Subaccount response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.subaccount_management.retrieve_subaccount(
            api_key="api_key",
            subaccount_key="subaccount_key",
        )
        """
        _response = self._raw_client.retrieve_subaccount(api_key, subaccount_key, request_options=request_options)
        return _response.data

    def modify_subaccount(
        self,
        api_key: str,
        subaccount_key: str,
        *,
        name: typing.Optional[str] = OMIT,
        suspended: typing.Optional[bool] = OMIT,
        use_primary_account_balance: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubaccountResponse:
        """
        Change one or more properties of a subaccount.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        subaccount_key : str
            ID of the subaccount

        name : typing.Optional[str]

        suspended : typing.Optional[bool]

        use_primary_account_balance : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubaccountResponse
            Subaccount response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.subaccount_management.modify_subaccount(
            api_key="api_key",
            subaccount_key="subaccount_key",
        )
        """
        _response = self._raw_client.modify_subaccount(
            api_key,
            subaccount_key,
            name=name,
            suspended=suspended,
            use_primary_account_balance=use_primary_account_balance,
            request_options=request_options,
        )
        return _response.data


class AsyncSubaccountManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubaccountManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubaccountManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubaccountManagementClient
        """
        return self._raw_client

    async def retrieve_subaccounts_list(
        self, api_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubaccountsAllResponse:
        """
        Get the information of all the subaccounts owned by the primary account.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubaccountsAllResponse
            Subaccounts response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.subaccount_management.retrieve_subaccounts_list(
                api_key="api_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_subaccounts_list(api_key, request_options=request_options)
        return _response.data

    async def create_sub_account(
        self,
        api_key: str,
        *,
        name: str,
        secret: typing.Optional[str] = OMIT,
        use_primary_account_balance: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubaccountCreateResponse:
        """
        Create a subaccount for a given primary account.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        name : str

        secret : typing.Optional[str]

        use_primary_account_balance : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubaccountCreateResponse
            Subaccount response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.subaccount_management.create_sub_account(
                api_key="api_key",
                name="Subaccount department A",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_sub_account(
            api_key,
            name=name,
            secret=secret,
            use_primary_account_balance=use_primary_account_balance,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_subaccount(
        self, api_key: str, subaccount_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubaccountResponse:
        """
        Get the information of a subaccount specified with its API key.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        subaccount_key : str
            ID of the subaccount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubaccountResponse
            Subaccount response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.subaccount_management.retrieve_subaccount(
                api_key="api_key",
                subaccount_key="subaccount_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_subaccount(api_key, subaccount_key, request_options=request_options)
        return _response.data

    async def modify_subaccount(
        self,
        api_key: str,
        subaccount_key: str,
        *,
        name: typing.Optional[str] = OMIT,
        suspended: typing.Optional[bool] = OMIT,
        use_primary_account_balance: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubaccountResponse:
        """
        Change one or more properties of a subaccount.

        Parameters
        ----------
        api_key : str
            ID of the primary account

        subaccount_key : str
            ID of the subaccount

        name : typing.Optional[str]

        suspended : typing.Optional[bool]

        use_primary_account_balance : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubaccountResponse
            Subaccount response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.subaccount_management.modify_subaccount(
                api_key="api_key",
                subaccount_key="subaccount_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_subaccount(
            api_key,
            subaccount_key,
            name=name,
            suspended=suspended,
            use_primary_account_balance=use_primary_account_balance,
            request_options=request_options,
        )
        return _response.data
