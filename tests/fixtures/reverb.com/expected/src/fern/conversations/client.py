

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawConversationsClient, RawConversationsClient


OMIT = typing.cast(typing.Any, ...)


class ConversationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConversationsClient
        """
        return self._raw_client

    def make_an_offer_to_the_other_participant_in_the_conversation(
        self,
        id: str,
        *,
        price: str,
        message: typing.Optional[str] = OMIT,
        shipping_price: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Make an offer to the other participant in the conversation

        Parameters
        ----------
        id : str

        price : str
            Offer price

        message : typing.Optional[str]
            Message to include with counter offer

        shipping_price : typing.Optional[str]
            Shipping price (sellers only)

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
        client.conversations.make_an_offer_to_the_other_participant_in_the_conversation(
            id="id",
            price="price",
        )
        """
        _response = self._raw_client.make_an_offer_to_the_other_participant_in_the_conversation(
            id, price=price, message=message, shipping_price=shipping_price, request_options=request_options
        )
        return _response.data


class AsyncConversationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConversationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConversationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConversationsClient
        """
        return self._raw_client

    async def make_an_offer_to_the_other_participant_in_the_conversation(
        self,
        id: str,
        *,
        price: str,
        message: typing.Optional[str] = OMIT,
        shipping_price: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Make an offer to the other participant in the conversation

        Parameters
        ----------
        id : str

        price : str
            Offer price

        message : typing.Optional[str]
            Message to include with counter offer

        shipping_price : typing.Optional[str]
            Shipping price (sellers only)

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
            await client.conversations.make_an_offer_to_the_other_participant_in_the_conversation(
                id="id",
                price="price",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.make_an_offer_to_the_other_participant_in_the_conversation(
            id, price=price, message=message, shipping_price=shipping_price, request_options=request_options
        )
        return _response.data
