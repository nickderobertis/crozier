

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.apple_subscription_response import AppleSubscriptionResponse
from .raw_client import AsyncRawSubscriptionsClient, RawSubscriptionsClient


OMIT = typing.cast(typing.Any, ...)


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

    def create_apple_subscription(
        self, *, signed_transaction: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AppleSubscriptionResponse:
        """
        Parameters
        ----------
        signed_transaction : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppleSubscriptionResponse
            Current account state after durable App Store reconciliation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.subscriptions.create_apple_subscription(
            signed_transaction="signedTransaction",
        )
        """
        _response = self._raw_client.create_apple_subscription(
            signed_transaction=signed_transaction, request_options=request_options
        )
        return _response.data

    def create_apple_subscription_notification(
        self, *, signed_payload: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        signed_payload : str

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
        client.subscriptions.create_apple_subscription_notification(
            signed_payload="signedPayload",
        )
        """
        _response = self._raw_client.create_apple_subscription_notification(
            signed_payload=signed_payload, request_options=request_options
        )
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

    async def create_apple_subscription(
        self, *, signed_transaction: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AppleSubscriptionResponse:
        """
        Parameters
        ----------
        signed_transaction : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppleSubscriptionResponse
            Current account state after durable App Store reconciliation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.subscriptions.create_apple_subscription(
                signed_transaction="signedTransaction",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_apple_subscription(
            signed_transaction=signed_transaction, request_options=request_options
        )
        return _response.data

    async def create_apple_subscription_notification(
        self, *, signed_payload: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        signed_payload : str

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
            await client.subscriptions.create_apple_subscription_notification(
                signed_payload="signedPayload",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_apple_subscription_notification(
            signed_payload=signed_payload, request_options=request_options
        )
        return _response.data
