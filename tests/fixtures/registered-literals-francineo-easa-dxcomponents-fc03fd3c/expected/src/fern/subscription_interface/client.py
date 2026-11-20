

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSubscriptionInterfaceClient, RawSubscriptionInterfaceClient


OMIT = typing.cast(typing.Any, ...)


class SubscriptionInterfaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubscriptionInterfaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubscriptionInterfaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubscriptionInterfaceClient
        """
        return self._raw_client

    def get_uas_zones_updates_subscription(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Only subscriptions belonging to the caller are returned. This endpoint would be used if a data consumer lost track of subscriptions they had created and/or wanted to resolve an error indicating that they had too many existing subscriptions in an area.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Subscriptions were retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.subscription_interface.get_uas_zones_updates_subscription()
        """
        _response = self._raw_client.get_uas_zones_updates_subscription(request_options=request_options)
        return _response.data

    def subscribe_to_uas_zones_updates(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This operation creates a subscription for the user, with "PAUSED" state. The operation creates also a publication resource (i.e. queue) at the provider infrastructure, where all information updates related to the subscription will be delivered.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Subscriptions request received successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.subscription_interface.subscribe_to_uas_zones_updates(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.subscribe_to_uas_zones_updates(request=request, request_options=request_options)
        return _response.data


class AsyncSubscriptionInterfaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubscriptionInterfaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubscriptionInterfaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubscriptionInterfaceClient
        """
        return self._raw_client

    async def get_uas_zones_updates_subscription(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Only subscriptions belonging to the caller are returned. This endpoint would be used if a data consumer lost track of subscriptions they had created and/or wanted to resolve an error indicating that they had too many existing subscriptions in an area.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Subscriptions were retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.subscription_interface.get_uas_zones_updates_subscription()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_uas_zones_updates_subscription(request_options=request_options)
        return _response.data

    async def subscribe_to_uas_zones_updates(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This operation creates a subscription for the user, with "PAUSED" state. The operation creates also a publication resource (i.e. queue) at the provider infrastructure, where all information updates related to the subscription will be delivered.

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Subscriptions request received successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.subscription_interface.subscribe_to_uas_zones_updates(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subscribe_to_uas_zones_updates(
            request=request, request_options=request_options
        )
        return _response.data
