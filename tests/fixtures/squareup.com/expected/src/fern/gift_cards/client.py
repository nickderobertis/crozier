

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_gift_card_response import CreateGiftCardResponse
from ..types.gift_card import GiftCard
from ..types.link_customer_to_gift_card_response import LinkCustomerToGiftCardResponse
from ..types.list_gift_cards_response import ListGiftCardsResponse
from ..types.retrieve_gift_card_from_gan_response import RetrieveGiftCardFromGanResponse
from ..types.retrieve_gift_card_from_nonce_response import RetrieveGiftCardFromNonceResponse
from ..types.retrieve_gift_card_response import RetrieveGiftCardResponse
from ..types.unlink_customer_from_gift_card_response import UnlinkCustomerFromGiftCardResponse
from .raw_client import AsyncRawGiftCardsClient, RawGiftCardsClient


OMIT = typing.cast(typing.Any, ...)


class GiftCardsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGiftCardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGiftCardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGiftCardsClient
        """
        return self._raw_client

    def list_gift_cards(
        self,
        *,
        type: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListGiftCardsResponse:
        """
        Lists all gift cards. You can specify optional filters to retrieve
        a subset of the gift cards.

        Parameters
        ----------
        type : typing.Optional[str]
            If a type is provided, gift cards of this type are returned
            (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)).
            If no type is provided, it returns gift cards of all types.

        state : typing.Optional[str]
            If the state is provided, it returns the gift cards in the specified state
            (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)).
            Otherwise, it returns the gift cards of all states.

        limit : typing.Optional[int]
            If a value is provided, it returns only that number of results per page.
            The maximum number of results allowed per page is 50. The default value is 30.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            If a cursor is not provided, it returns the first page of the results.
            For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination).

        customer_id : typing.Optional[str]
            If a value is provided, returns only the gift cards linked to the specified customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGiftCardsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.gift_cards.list_gift_cards()
        """
        _response = self._raw_client.list_gift_cards(
            type=type, state=state, limit=limit, cursor=cursor, customer_id=customer_id, request_options=request_options
        )
        return _response.data

    def create_gift_card(
        self,
        *,
        gift_card: GiftCard,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateGiftCardResponse:
        """
        Creates a digital gift card or registers a physical (plastic) gift card. You must activate the gift card before
        it can be used for payment. For more information, see
        [Selling gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#selling-square-gift-cards).

        Parameters
        ----------
        gift_card : GiftCard

        idempotency_key : str
            A unique string that identifies the `CreateGiftCard` request.

        location_id : str
            The location ID where the gift card that will be created should be registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGiftCardResponse
            Success

        Examples
        --------
        from fern import FernApi, GiftCard

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.gift_cards.create_gift_card(
            gift_card=GiftCard(
                type={"key": "value"},
            ),
            idempotency_key="x",
            location_id="x",
        )
        """
        _response = self._raw_client.create_gift_card(
            gift_card=gift_card,
            idempotency_key=idempotency_key,
            location_id=location_id,
            request_options=request_options,
        )
        return _response.data

    def retrieve_gift_card_from_gan(
        self, *, gan: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveGiftCardFromGanResponse:
        """
        Retrieves a gift card using the gift card account number (GAN).

        Parameters
        ----------
        gan : str
            The gift card account number (GAN) of the gift card to retrieve.
            The maximum length of a GAN is 255 digits to account for third-party GANs that have been imported.
            Square-issued gift cards have 16-digit GANs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveGiftCardFromGanResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.gift_cards.retrieve_gift_card_from_gan(
            gan="gan",
        )
        """
        _response = self._raw_client.retrieve_gift_card_from_gan(gan=gan, request_options=request_options)
        return _response.data

    def retrieve_gift_card_from_nonce(
        self, *, nonce: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveGiftCardFromNonceResponse:
        """
        Retrieves a gift card using a nonce (a secure token) that represents the gift card.

        Parameters
        ----------
        nonce : str
            The nonce of the gift card to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveGiftCardFromNonceResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.gift_cards.retrieve_gift_card_from_nonce(
            nonce="nonce",
        )
        """
        _response = self._raw_client.retrieve_gift_card_from_nonce(nonce=nonce, request_options=request_options)
        return _response.data

    def link_customer_to_gift_card(
        self, gift_card_id: str, *, customer_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LinkCustomerToGiftCardResponse:
        """
        Links a customer to a gift card

        Parameters
        ----------
        gift_card_id : str
            The ID of the gift card to link.

        customer_id : str
            The ID of the customer to be linked.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkCustomerToGiftCardResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.gift_cards.link_customer_to_gift_card(
            gift_card_id="gift_card_id",
            customer_id="customer_id",
        )
        """
        _response = self._raw_client.link_customer_to_gift_card(
            gift_card_id, customer_id=customer_id, request_options=request_options
        )
        return _response.data

    def unlink_customer_from_gift_card(
        self, gift_card_id: str, *, customer_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UnlinkCustomerFromGiftCardResponse:
        """
        Unlinks a customer from a gift card

        Parameters
        ----------
        gift_card_id : str


        customer_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnlinkCustomerFromGiftCardResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.gift_cards.unlink_customer_from_gift_card(
            gift_card_id="gift_card_id",
            customer_id="customer_id",
        )
        """
        _response = self._raw_client.unlink_customer_from_gift_card(
            gift_card_id, customer_id=customer_id, request_options=request_options
        )
        return _response.data

    def retrieve_gift_card(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveGiftCardResponse:
        """
        Retrieves a gift card using its ID.

        Parameters
        ----------
        id : str
            The ID of the gift card to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveGiftCardResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.gift_cards.retrieve_gift_card(
            id="id",
        )
        """
        _response = self._raw_client.retrieve_gift_card(id, request_options=request_options)
        return _response.data


class AsyncGiftCardsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGiftCardsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGiftCardsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGiftCardsClient
        """
        return self._raw_client

    async def list_gift_cards(
        self,
        *,
        type: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListGiftCardsResponse:
        """
        Lists all gift cards. You can specify optional filters to retrieve
        a subset of the gift cards.

        Parameters
        ----------
        type : typing.Optional[str]
            If a type is provided, gift cards of this type are returned
            (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)).
            If no type is provided, it returns gift cards of all types.

        state : typing.Optional[str]
            If the state is provided, it returns the gift cards in the specified state
            (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)).
            Otherwise, it returns the gift cards of all states.

        limit : typing.Optional[int]
            If a value is provided, it returns only that number of results per page.
            The maximum number of results allowed per page is 50. The default value is 30.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            If a cursor is not provided, it returns the first page of the results.
            For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination).

        customer_id : typing.Optional[str]
            If a value is provided, returns only the gift cards linked to the specified customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGiftCardsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gift_cards.list_gift_cards()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_gift_cards(
            type=type, state=state, limit=limit, cursor=cursor, customer_id=customer_id, request_options=request_options
        )
        return _response.data

    async def create_gift_card(
        self,
        *,
        gift_card: GiftCard,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateGiftCardResponse:
        """
        Creates a digital gift card or registers a physical (plastic) gift card. You must activate the gift card before
        it can be used for payment. For more information, see
        [Selling gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#selling-square-gift-cards).

        Parameters
        ----------
        gift_card : GiftCard

        idempotency_key : str
            A unique string that identifies the `CreateGiftCard` request.

        location_id : str
            The location ID where the gift card that will be created should be registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGiftCardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GiftCard

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gift_cards.create_gift_card(
                gift_card=GiftCard(
                    type={"key": "value"},
                ),
                idempotency_key="x",
                location_id="x",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_gift_card(
            gift_card=gift_card,
            idempotency_key=idempotency_key,
            location_id=location_id,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_gift_card_from_gan(
        self, *, gan: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveGiftCardFromGanResponse:
        """
        Retrieves a gift card using the gift card account number (GAN).

        Parameters
        ----------
        gan : str
            The gift card account number (GAN) of the gift card to retrieve.
            The maximum length of a GAN is 255 digits to account for third-party GANs that have been imported.
            Square-issued gift cards have 16-digit GANs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveGiftCardFromGanResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gift_cards.retrieve_gift_card_from_gan(
                gan="gan",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_gift_card_from_gan(gan=gan, request_options=request_options)
        return _response.data

    async def retrieve_gift_card_from_nonce(
        self, *, nonce: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveGiftCardFromNonceResponse:
        """
        Retrieves a gift card using a nonce (a secure token) that represents the gift card.

        Parameters
        ----------
        nonce : str
            The nonce of the gift card to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveGiftCardFromNonceResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gift_cards.retrieve_gift_card_from_nonce(
                nonce="nonce",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_gift_card_from_nonce(nonce=nonce, request_options=request_options)
        return _response.data

    async def link_customer_to_gift_card(
        self, gift_card_id: str, *, customer_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LinkCustomerToGiftCardResponse:
        """
        Links a customer to a gift card

        Parameters
        ----------
        gift_card_id : str
            The ID of the gift card to link.

        customer_id : str
            The ID of the customer to be linked.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkCustomerToGiftCardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gift_cards.link_customer_to_gift_card(
                gift_card_id="gift_card_id",
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link_customer_to_gift_card(
            gift_card_id, customer_id=customer_id, request_options=request_options
        )
        return _response.data

    async def unlink_customer_from_gift_card(
        self, gift_card_id: str, *, customer_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UnlinkCustomerFromGiftCardResponse:
        """
        Unlinks a customer from a gift card

        Parameters
        ----------
        gift_card_id : str


        customer_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnlinkCustomerFromGiftCardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gift_cards.unlink_customer_from_gift_card(
                gift_card_id="gift_card_id",
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unlink_customer_from_gift_card(
            gift_card_id, customer_id=customer_id, request_options=request_options
        )
        return _response.data

    async def retrieve_gift_card(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveGiftCardResponse:
        """
        Retrieves a gift card using its ID.

        Parameters
        ----------
        id : str
            The ID of the gift card to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveGiftCardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gift_cards.retrieve_gift_card(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_gift_card(id, request_options=request_options)
        return _response.data
