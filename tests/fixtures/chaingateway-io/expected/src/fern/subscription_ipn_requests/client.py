

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_failed_ip_ns import ListFailedIpNs
from ..types.list_subscribed_addresses import ListSubscribedAddresses
from ..types.resend_failed_ipn import ResendFailedIpn
from ..types.subscribe_address import SubscribeAddress
from ..types.unsubscribe_address import UnsubscribeAddress
from .raw_client import AsyncRawSubscriptionIpnRequestsClient, RawSubscriptionIpnRequestsClient


OMIT = typing.cast(typing.Any, ...)


class SubscriptionIpnRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubscriptionIpnRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubscriptionIpnRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubscriptionIpnRequestsClient
        """
        return self._raw_client

    def list_failed_ip_ns(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFailedIpNs:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFailedIpNs


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscription_ipn_requests.list_failed_ip_ns(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
        )
        """
        _response = self._raw_client.list_failed_ip_ns(authorization=authorization, request_options=request_options)
        return _response.data

    def list_subscribed_addresses(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListSubscribedAddresses:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSubscribedAddresses


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscription_ipn_requests.list_subscribed_addresses(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
        )
        """
        _response = self._raw_client.list_subscribed_addresses(
            authorization=authorization, request_options=request_options
        )
        return _response.data

    def resend_failed_ipn(
        self, *, authorization: str, id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ResendFailedIpn:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResendFailedIpn


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscription_ipn_requests.resend_failed_ipn(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            id=17766,
        )
        """
        _response = self._raw_client.resend_failed_ipn(
            authorization=authorization, id=id, request_options=request_options
        )
        return _response.data

    def subscribe_address(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribeAddress:
        """
        Creates a new subscription/IPN for the given address (and contractaddress). You will receive a notification to the given url every time a deposit is received. Unsubscribe the address before sending tokens/ETH from it or you won't get reliable notifications anymore.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscription_ipn_requests.subscribe_address(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            contractaddress="0x514910771af9ca656af840dff83e8264ecf986ca",
            ethereumaddress="0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974",
            url="https://yoururl.com/ipnreceiver.php",
        )
        """
        _response = self._raw_client.subscribe_address(
            authorization=authorization,
            contractaddress=contractaddress,
            ethereumaddress=ethereumaddress,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def unsubscribe_address(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnsubscribeAddress:
        """
        Deletes an existing subscription/IPN for the given address (and contractaddress).

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnsubscribeAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.subscription_ipn_requests.unsubscribe_address(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            contractaddress="0x514910771af9ca656af840dff83e8264ecf986ca",
            ethereumaddress="0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974",
            url="https://yoururl.com/ipnreceiver.php",
        )
        """
        _response = self._raw_client.unsubscribe_address(
            authorization=authorization,
            contractaddress=contractaddress,
            ethereumaddress=ethereumaddress,
            url=url,
            request_options=request_options,
        )
        return _response.data


class AsyncSubscriptionIpnRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubscriptionIpnRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubscriptionIpnRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubscriptionIpnRequestsClient
        """
        return self._raw_client

    async def list_failed_ip_ns(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListFailedIpNs:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListFailedIpNs


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscription_ipn_requests.list_failed_ip_ns(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_failed_ip_ns(
            authorization=authorization, request_options=request_options
        )
        return _response.data

    async def list_subscribed_addresses(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ListSubscribedAddresses:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSubscribedAddresses


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscription_ipn_requests.list_subscribed_addresses(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_subscribed_addresses(
            authorization=authorization, request_options=request_options
        )
        return _response.data

    async def resend_failed_ipn(
        self, *, authorization: str, id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ResendFailedIpn:
        """
        Returns all subscriptions/IPNs created with an account.

        Parameters
        ----------
        authorization : str
            API Key

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResendFailedIpn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscription_ipn_requests.resend_failed_ipn(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                id=17766,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resend_failed_ipn(
            authorization=authorization, id=id, request_options=request_options
        )
        return _response.data

    async def subscribe_address(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribeAddress:
        """
        Creates a new subscription/IPN for the given address (and contractaddress). You will receive a notification to the given url every time a deposit is received. Unsubscribe the address before sending tokens/ETH from it or you won't get reliable notifications anymore.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscription_ipn_requests.subscribe_address(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                contractaddress="0x514910771af9ca656af840dff83e8264ecf986ca",
                ethereumaddress="0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974",
                url="https://yoururl.com/ipnreceiver.php",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subscribe_address(
            authorization=authorization,
            contractaddress=contractaddress,
            ethereumaddress=ethereumaddress,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def unsubscribe_address(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnsubscribeAddress:
        """
        Deletes an existing subscription/IPN for the given address (and contractaddress).

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnsubscribeAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.subscription_ipn_requests.unsubscribe_address(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                contractaddress="0x514910771af9ca656af840dff83e8264ecf986ca",
                ethereumaddress="0xa2107fa5b38d9bbd2c461d6edf11b11a50f6b974",
                url="https://yoururl.com/ipnreceiver.php",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unsubscribe_address(
            authorization=authorization,
            contractaddress=contractaddress,
            ethereumaddress=ethereumaddress,
            url=url,
            request_options=request_options,
        )
        return _response.data
