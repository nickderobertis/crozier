

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.subscription import Subscription
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

    def create(self, *, callback_url: str, request_options: typing.Optional[RequestOptions] = None) -> Subscription:
        """
        Parameters
        ----------
        callback_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subscription


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.subscriptions.create(
            callback_url="callbackUrl",
        )
        """
        _response = self._raw_client.create(callback_url=callback_url, request_options=request_options)
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

    async def create(
        self, *, callback_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Subscription:
        """
        Parameters
        ----------
        callback_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subscription


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.subscriptions.create(
                callback_url="callbackUrl",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(callback_url=callback_url, request_options=request_options)
        return _response.data
