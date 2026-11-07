

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUserSubscriptionsClient, RawUserSubscriptionsClient


class UserSubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserSubscriptionsClient
        """
        return self._raw_client

    def post_api_v1user_subscriptions(
        self, *, email: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : typing.Optional[str]

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
        client.user_subscriptions.post_api_v1user_subscriptions()
        """
        _response = self._raw_client.post_api_v1user_subscriptions(email=email, request_options=request_options)
        return _response.data

    def delete_api_v1user_subscriptions(
        self, *, email: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : typing.Optional[str]

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
        client.user_subscriptions.delete_api_v1user_subscriptions()
        """
        _response = self._raw_client.delete_api_v1user_subscriptions(email=email, request_options=request_options)
        return _response.data


class AsyncUserSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserSubscriptionsClient
        """
        return self._raw_client

    async def post_api_v1user_subscriptions(
        self, *, email: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : typing.Optional[str]

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
            await client.user_subscriptions.post_api_v1user_subscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1user_subscriptions(email=email, request_options=request_options)
        return _response.data

    async def delete_api_v1user_subscriptions(
        self, *, email: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        email : typing.Optional[str]

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
            await client.user_subscriptions.delete_api_v1user_subscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1user_subscriptions(email=email, request_options=request_options)
        return _response.data
