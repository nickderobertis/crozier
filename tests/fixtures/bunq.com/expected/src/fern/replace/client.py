

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.card_pin_assignment import CardPinAssignment
from ..types.card_replace_create import CardReplaceCreate
from .raw_client import AsyncRawReplaceClient, RawReplaceClient


OMIT = typing.cast(typing.Any, ...)


class ReplaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReplaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReplaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReplaceClient
        """
        return self._raw_client

    def create_replace_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        name_on_card: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        preferred_name_on_card: typing.Optional[str] = OMIT,
        second_line: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardReplaceCreate:
        """
        Request a card replacement.

        Parameters
        ----------
        user_id : int


        card_id : int


        name_on_card : typing.Optional[str]
            The user's name as it will be on the card. Check 'card-name' for the available card names for a user.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        preferred_name_on_card : typing.Optional[str]
            The user's preferred name that can be put on the card.

        second_line : typing.Optional[str]
            The second line on the card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardReplaceCreate
            It is possible to order a card replacement with the bunq API.<br/><br/>You can order up to one free card replacement per year. Additional replacement requests will be billed.<br/><br/>The card replacement will have the same expiry date and the same pricing as the old card, but it will have a new card number. You can change the description and optional the PIN through the card replacement endpoint.

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
        client.replace.create_replace_for_user_card(
            user_id=1,
            card_id=1,
        )
        """
        _response = self._raw_client.create_replace_for_user_card(
            user_id,
            card_id,
            name_on_card=name_on_card,
            pin_code_assignment=pin_code_assignment,
            preferred_name_on_card=preferred_name_on_card,
            second_line=second_line,
            request_options=request_options,
        )
        return _response.data


class AsyncReplaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReplaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReplaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReplaceClient
        """
        return self._raw_client

    async def create_replace_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        name_on_card: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        preferred_name_on_card: typing.Optional[str] = OMIT,
        second_line: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardReplaceCreate:
        """
        Request a card replacement.

        Parameters
        ----------
        user_id : int


        card_id : int


        name_on_card : typing.Optional[str]
            The user's name as it will be on the card. Check 'card-name' for the available card names for a user.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        preferred_name_on_card : typing.Optional[str]
            The user's preferred name that can be put on the card.

        second_line : typing.Optional[str]
            The second line on the card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardReplaceCreate
            It is possible to order a card replacement with the bunq API.<br/><br/>You can order up to one free card replacement per year. Additional replacement requests will be billed.<br/><br/>The card replacement will have the same expiry date and the same pricing as the old card, but it will have a new card number. You can change the description and optional the PIN through the card replacement endpoint.

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
            await client.replace.create_replace_for_user_card(
                user_id=1,
                card_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_replace_for_user_card(
            user_id,
            card_id,
            name_on_card=name_on_card,
            pin_code_assignment=pin_code_assignment,
            preferred_name_on_card=preferred_name_on_card,
            second_line=second_line,
            request_options=request_options,
        )
        return _response.data
