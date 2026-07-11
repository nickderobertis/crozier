

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account import Account
from .raw_client import AsyncRawAccountsClient, RawAccountsClient


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

    def createaccount(
        self,
        *,
        username: str,
        password: str,
        age: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Account:
        """
        Parameters
        ----------
        username : str

        password : str

        age : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.accounts.createaccount(
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.createaccount(
            username=username, password=password, age=age, request_options=request_options
        )
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

    async def createaccount(
        self,
        *,
        username: str,
        password: str,
        age: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Account:
        """
        Parameters
        ----------
        username : str

        password : str

        age : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Account


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.accounts.createaccount(
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createaccount(
            username=username, password=password, age=age, request_options=request_options
        )
        return _response.data
