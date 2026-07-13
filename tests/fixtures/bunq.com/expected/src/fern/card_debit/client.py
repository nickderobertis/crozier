

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.card_debit_create import CardDebitCreate
from ..types.card_pin_assignment import CardPinAssignment
from ..types.pointer import Pointer
from .raw_client import AsyncRawCardDebitClient, RawCardDebitClient


OMIT = typing.cast(typing.Any, ...)


class CardDebitClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCardDebitClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCardDebitClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCardDebitClient
        """
        return self._raw_client

    def create_card_debit_for_user(
        self,
        user_id: int,
        *,
        name_on_card: str,
        product_type: str,
        second_line: str,
        type: str,
        alias: typing.Optional[Pointer] = OMIT,
        monetary_account_id_fallback: typing.Optional[int] = OMIT,
        order_status: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        preferred_name_on_card: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardDebitCreate:
        """
        Create a new debit card request.

        Parameters
        ----------
        user_id : int


        name_on_card : str
            The user's name as it will be on the card. Check 'card-name' for the available card names for a user.

        product_type : str
            The product type of the card to order.

        second_line : str
            The second line of text on the card, used as name/description for it. It can contain at most 17 characters and it can be empty.

        type : str
            The type of card to order. Can be MAESTRO or MASTERCARD.

        alias : typing.Optional[Pointer]
            The pointer to the monetary account that will be connected at first with the card. Its IBAN code is also the one that will be printed on the card itself. The pointer must be of type IBAN.

        monetary_account_id_fallback : typing.Optional[int]
            ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.

        order_status : typing.Optional[str]
            The order status of this card. Can be CARD_REQUEST_PENDING or VIRTUAL_DELIVERY.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        preferred_name_on_card : typing.Optional[str]
            The user's preferred name that can be put on the card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardDebitCreate
            With bunq it is possible to order debit cards that can then be connected with each one of the monetary accounts the user has access to (including connected accounts).

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.card_debit.create_card_debit_for_user(
            user_id=1,
            name_on_card="name_on_card",
            product_type="product_type",
            second_line="second_line",
            type="type",
        )
        """
        _response = self._raw_client.create_card_debit_for_user(
            user_id,
            name_on_card=name_on_card,
            product_type=product_type,
            second_line=second_line,
            type=type,
            alias=alias,
            monetary_account_id_fallback=monetary_account_id_fallback,
            order_status=order_status,
            pin_code_assignment=pin_code_assignment,
            preferred_name_on_card=preferred_name_on_card,
            request_options=request_options,
        )
        return _response.data


class AsyncCardDebitClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCardDebitClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCardDebitClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCardDebitClient
        """
        return self._raw_client

    async def create_card_debit_for_user(
        self,
        user_id: int,
        *,
        name_on_card: str,
        product_type: str,
        second_line: str,
        type: str,
        alias: typing.Optional[Pointer] = OMIT,
        monetary_account_id_fallback: typing.Optional[int] = OMIT,
        order_status: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        preferred_name_on_card: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardDebitCreate:
        """
        Create a new debit card request.

        Parameters
        ----------
        user_id : int


        name_on_card : str
            The user's name as it will be on the card. Check 'card-name' for the available card names for a user.

        product_type : str
            The product type of the card to order.

        second_line : str
            The second line of text on the card, used as name/description for it. It can contain at most 17 characters and it can be empty.

        type : str
            The type of card to order. Can be MAESTRO or MASTERCARD.

        alias : typing.Optional[Pointer]
            The pointer to the monetary account that will be connected at first with the card. Its IBAN code is also the one that will be printed on the card itself. The pointer must be of type IBAN.

        monetary_account_id_fallback : typing.Optional[int]
            ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.

        order_status : typing.Optional[str]
            The order status of this card. Can be CARD_REQUEST_PENDING or VIRTUAL_DELIVERY.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        preferred_name_on_card : typing.Optional[str]
            The user's preferred name that can be put on the card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardDebitCreate
            With bunq it is possible to order debit cards that can then be connected with each one of the monetary accounts the user has access to (including connected accounts).

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.card_debit.create_card_debit_for_user(
                user_id=1,
                name_on_card="name_on_card",
                product_type="product_type",
                second_line="second_line",
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_card_debit_for_user(
            user_id,
            name_on_card=name_on_card,
            product_type=product_type,
            second_line=second_line,
            type=type,
            alias=alias,
            monetary_account_id_fallback=monetary_account_id_fallback,
            order_status=order_status,
            pin_code_assignment=pin_code_assignment,
            preferred_name_on_card=preferred_name_on_card,
            request_options=request_options,
        )
        return _response.data
