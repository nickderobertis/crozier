

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.grant_account import GrantAccount
from .raw_client import AsyncRawGrantAccountsClient, RawGrantAccountsClient


class GrantAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGrantAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGrantAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGrantAccountsClient
        """
        return self._raw_client

    def get_grant_accounts_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GrantAccount:
        """
        Returns the details of the specified grant account. This account tracks existing grants in your marketplace or platform.

        Parameters
        ----------
        id : str
            The unique identifier of the grant account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrantAccount
            OK - The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.grant_accounts.get_grant_accounts_id(
            id="id",
        )
        """
        _response = self._raw_client.get_grant_accounts_id(id, request_options=request_options)
        return _response.data


class AsyncGrantAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGrantAccountsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGrantAccountsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGrantAccountsClient
        """
        return self._raw_client

    async def get_grant_accounts_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GrantAccount:
        """
        Returns the details of the specified grant account. This account tracks existing grants in your marketplace or platform.

        Parameters
        ----------
        id : str
            The unique identifier of the grant account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GrantAccount
            OK - The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.grant_accounts.get_grant_accounts_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_grant_accounts_id(id, request_options=request_options)
        return _response.data
