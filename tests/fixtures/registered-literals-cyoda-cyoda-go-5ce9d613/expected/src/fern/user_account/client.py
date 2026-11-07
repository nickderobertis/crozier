

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.subscriptions_response_dto import SubscriptionsResponseDto
from ..types.user_account_info_response_dto import UserAccountInfoResponseDto
from .raw_client import AsyncRawUserAccountClient, RawUserAccountClient


class UserAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserAccountClient
        """
        return self._raw_client

    def account_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserAccountInfoResponseDto:
        """
        Fetch information related to the current user's account, such as legal entity, roles, and current subscription.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserAccountInfoResponseDto
            Current user's account information with current subscription details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_account.account_get()
        """
        _response = self._raw_client.account_get(request_options=request_options)
        return _response.data

    def account_subscriptions_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscriptionsResponseDto:
        """
        Fetch all subscription details associated with the legal entity of the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionsResponseDto
            Collection of all subscriptions for the user's legal entity

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_account.account_subscriptions_get()
        """
        _response = self._raw_client.account_subscriptions_get(request_options=request_options)
        return _response.data


class AsyncUserAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserAccountClient
        """
        return self._raw_client

    async def account_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserAccountInfoResponseDto:
        """
        Fetch information related to the current user's account, such as legal entity, roles, and current subscription.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserAccountInfoResponseDto
            Current user's account information with current subscription details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_account.account_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.account_get(request_options=request_options)
        return _response.data

    async def account_subscriptions_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SubscriptionsResponseDto:
        """
        Fetch all subscription details associated with the legal entity of the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionsResponseDto
            Collection of all subscriptions for the user's legal entity

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_account.account_subscriptions_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.account_subscriptions_get(request_options=request_options)
        return _response.data
