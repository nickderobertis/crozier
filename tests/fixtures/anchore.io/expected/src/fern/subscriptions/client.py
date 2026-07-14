

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.subscription_list import SubscriptionList
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

    def list_subscriptions(
        self,
        *,
        subscription_key: typing.Optional[str] = None,
        subscription_type: typing.Optional[str] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """
        Parameters
        ----------
        subscription_key : typing.Optional[str]
            filter only subscriptions matching key

        subscription_type : typing.Optional[str]
            filter only subscriptions matching type

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Subscription listing

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptions.list_subscriptions()
        """
        _response = self._raw_client.list_subscriptions(
            subscription_key=subscription_key,
            subscription_type=subscription_type,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    def add_subscription(
        self,
        *,
        anchore_account: typing.Optional[str] = None,
        subscription_key: typing.Optional[str] = OMIT,
        subscription_type: typing.Optional[str] = OMIT,
        subscription_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """
        Create a new subscription to watch a tag and get notifications of changes

        Parameters
        ----------
        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        subscription_key : typing.Optional[str]

        subscription_type : typing.Optional[str]

        subscription_value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Subscription add success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptions.add_subscription()
        """
        _response = self._raw_client.add_subscription(
            anchore_account=anchore_account,
            subscription_key=subscription_key,
            subscription_type=subscription_type,
            subscription_value=subscription_value,
            request_options=request_options,
        )
        return _response.data

    def get_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Filtered subscription list by type

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptions.get_subscription(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.get_subscription(
            subscription_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    def update_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        active: typing.Optional[bool] = OMIT,
        subscription_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        active : typing.Optional[bool]
            Toggle the subscription processing on or off

        subscription_value : typing.Optional[str]
            The new subscription value, e.g. the new tag to be subscribed to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Subscription add success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptions.update_subscription(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.update_subscription(
            subscription_id,
            anchore_account=anchore_account,
            active=active,
            subscription_value=subscription_value,
            request_options=request_options,
        )
        return _response.data

    def delete_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscriptions.delete_subscription(
            subscription_id="subscriptionId",
        )
        """
        _response = self._raw_client.delete_subscription(
            subscription_id, anchore_account=anchore_account, request_options=request_options
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

    async def list_subscriptions(
        self,
        *,
        subscription_key: typing.Optional[str] = None,
        subscription_type: typing.Optional[str] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """
        Parameters
        ----------
        subscription_key : typing.Optional[str]
            filter only subscriptions matching key

        subscription_type : typing.Optional[str]
            filter only subscriptions matching type

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Subscription listing

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptions.list_subscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_subscriptions(
            subscription_key=subscription_key,
            subscription_type=subscription_type,
            anchore_account=anchore_account,
            request_options=request_options,
        )
        return _response.data

    async def add_subscription(
        self,
        *,
        anchore_account: typing.Optional[str] = None,
        subscription_key: typing.Optional[str] = OMIT,
        subscription_type: typing.Optional[str] = OMIT,
        subscription_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """
        Create a new subscription to watch a tag and get notifications of changes

        Parameters
        ----------
        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        subscription_key : typing.Optional[str]

        subscription_type : typing.Optional[str]

        subscription_value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Subscription add success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptions.add_subscription()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_subscription(
            anchore_account=anchore_account,
            subscription_key=subscription_key,
            subscription_type=subscription_type,
            subscription_value=subscription_value,
            request_options=request_options,
        )
        return _response.data

    async def get_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Filtered subscription list by type

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptions.get_subscription(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_subscription(
            subscription_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data

    async def update_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        active: typing.Optional[bool] = OMIT,
        subscription_value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscriptionList:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        active : typing.Optional[bool]
            Toggle the subscription processing on or off

        subscription_value : typing.Optional[str]
            The new subscription value, e.g. the new tag to be subscribed to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscriptionList
            Subscription add success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptions.update_subscription(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_subscription(
            subscription_id,
            anchore_account=anchore_account,
            active=active,
            subscription_value=subscription_value,
            request_options=request_options,
        )
        return _response.data

    async def delete_subscription(
        self,
        subscription_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscriptions.delete_subscription(
                subscription_id="subscriptionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_subscription(
            subscription_id, anchore_account=anchore_account, request_options=request_options
        )
        return _response.data
