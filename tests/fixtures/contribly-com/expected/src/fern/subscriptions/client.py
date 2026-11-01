

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.subscription import Subscription
from ..types.subscription_type import SubscriptionType
from .raw_client import AsyncRawSubscriptionsClient, RawSubscriptionsClient


class SubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubscriptionsClient
        """
        return self._raw_client

    def subscription_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SubscriptionType]:
        """
        List available subscription types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SubscriptionType]
            A list of subscription event types

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.subscriptions.subscription_types()
        """
        _response = self._raw_client.subscription_types(request_options=request_options)
        return _response.data

    def list_subscriptions_for_the_authorised_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Subscription]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Subscription]
            A list of notification subscriptions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.subscriptions.list_subscriptions_for_the_authorised_user()
        """
        _response = self._raw_client.list_subscriptions_for_the_authorised_user(request_options=request_options)
        return _response.data

    def delete_a_subscription(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str
            Id of the subscription to delete

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
        client.subscriptions.delete_a_subscription(
            id="id",
        )
        """
        _response = self._raw_client.delete_a_subscription(id, request_options=request_options)
        return _response.data


class AsyncSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubscriptionsClient
        """
        return self._raw_client

    async def subscription_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SubscriptionType]:
        """
        List available subscription types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SubscriptionType]
            A list of subscription event types

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.subscriptions.subscription_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.subscription_types(request_options=request_options)
        return _response.data

    async def list_subscriptions_for_the_authorised_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Subscription]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Subscription]
            A list of notification subscriptions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.subscriptions.list_subscriptions_for_the_authorised_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_subscriptions_for_the_authorised_user(request_options=request_options)
        return _response.data

    async def delete_a_subscription(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str
            Id of the subscription to delete

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
            await client.subscriptions.delete_a_subscription(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_subscription(id, request_options=request_options)
        return _response.data
