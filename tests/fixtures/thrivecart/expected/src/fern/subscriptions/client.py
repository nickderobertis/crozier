

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSubscriptionsClient, RawSubscriptionsClient
from .types.cancel_subscription_response import CancelSubscriptionResponse
from .types.pause_subscription_response import PauseSubscriptionResponse
from .types.resume_subscription_response import ResumeSubscriptionResponse


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

    def cancel_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelSubscriptionResponse:
        """
        Cancel an active subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelSubscriptionResponse
            Cancellation result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.subscriptions.cancel_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.cancel_subscription(subscription_id, request_options=request_options)
        return _response.data

    def pause_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PauseSubscriptionResponse:
        """
        Pause an active subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PauseSubscriptionResponse
            Pause result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.subscriptions.pause_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.pause_subscription(subscription_id, request_options=request_options)
        return _response.data

    def resume_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResumeSubscriptionResponse:
        """
        Resume a paused subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResumeSubscriptionResponse
            Resume result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.subscriptions.resume_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.resume_subscription(subscription_id, request_options=request_options)
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

    async def cancel_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelSubscriptionResponse:
        """
        Cancel an active subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelSubscriptionResponse
            Cancellation result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.subscriptions.cancel_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_subscription(subscription_id, request_options=request_options)
        return _response.data

    async def pause_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PauseSubscriptionResponse:
        """
        Pause an active subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PauseSubscriptionResponse
            Pause result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.subscriptions.pause_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pause_subscription(subscription_id, request_options=request_options)
        return _response.data

    async def resume_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResumeSubscriptionResponse:
        """
        Resume a paused subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResumeSubscriptionResponse
            Resume result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.subscriptions.resume_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume_subscription(subscription_id, request_options=request_options)
        return _response.data
