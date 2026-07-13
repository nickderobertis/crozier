

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from ..types.card_country_permission import CardCountryPermission
from ..types.card_listing import CardListing
from ..types.card_pin_assignment import CardPinAssignment
from ..types.card_primary_account_number import CardPrimaryAccountNumber
from ..types.card_read import CardRead
from ..types.card_update import CardUpdate
from .raw_client import AsyncRawCardClient, RawCardClient


OMIT = typing.cast(typing.Any, ...)


class CardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCardClient
        """
        return self._raw_client

    def list_all_card_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CardListing]:
        """
        Return all the cards available to the user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CardListing]
            Endpoint for retrieving details for the cards the user has access to.

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
        client.card.list_all_card_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_card_for_user(user_id, request_options=request_options)
        return _response.data

    def read_card_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CardRead:
        """
        Return the details of a specific card.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardRead
            Endpoint for retrieving details for the cards the user has access to.

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
        client.card.read_card_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_card_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    def update_card_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        activation_code: typing.Optional[str] = OMIT,
        card_limit: typing.Optional[Amount] = OMIT,
        card_limit_atm: typing.Optional[Amount] = OMIT,
        country_permission: typing.Optional[typing.Sequence[CardCountryPermission]] = OMIT,
        monetary_account_id_fallback: typing.Optional[int] = OMIT,
        order_status: typing.Optional[str] = OMIT,
        pin_code: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        primary_account_numbers: typing.Optional[typing.Sequence[CardPrimaryAccountNumber]] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardUpdate:
        """
        Update the card details. Allow to change pin code, status, limits, country permissions and the monetary account connected to the card. When the card has been received, it can be also activated through this endpoint.

        Parameters
        ----------
        user_id : int


        item_id : int


        activation_code : typing.Optional[str]
            DEPRECATED: Activate a card by setting status to ACTIVE when the order_status is ACCEPTED_FOR_PRODUCTION.

        card_limit : typing.Optional[Amount]
            The spending limit for the card.

        card_limit_atm : typing.Optional[Amount]
            The ATM spending limit for the card.

        country_permission : typing.Optional[typing.Sequence[CardCountryPermission]]
            The countries for which to grant (temporary) permissions to use the card.

        monetary_account_id_fallback : typing.Optional[int]
            ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.

        order_status : typing.Optional[str]
            The order status to set for the card. Set to CARD_REQUEST_PENDING to get a virtual card produced.

        pin_code : typing.Optional[str]
            The plaintext pin code. Requests require encryption to be enabled.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        primary_account_numbers : typing.Optional[typing.Sequence[CardPrimaryAccountNumber]]
            Array of PANs and their attributes.

        status : typing.Optional[str]
            The status to set for the card. Can be ACTIVE, DEACTIVATED, LOST, STOLEN or CANCELLED, and can only be set to LOST/STOLEN/CANCELLED when order status is ACCEPTED_FOR_PRODUCTION/DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Can only be set to DEACTIVATED after initial activation, i.e. order_status is DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Mind that all the possible choices (apart from ACTIVE and DEACTIVATED) are permanent and cannot be changed after.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardUpdate
            Endpoint for retrieving details for the cards the user has access to.

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
        client.card.update_card_for_user(
            user_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_card_for_user(
            user_id,
            item_id,
            activation_code=activation_code,
            card_limit=card_limit,
            card_limit_atm=card_limit_atm,
            country_permission=country_permission,
            monetary_account_id_fallback=monetary_account_id_fallback,
            order_status=order_status,
            pin_code=pin_code,
            pin_code_assignment=pin_code_assignment,
            primary_account_numbers=primary_account_numbers,
            status=status,
            request_options=request_options,
        )
        return _response.data


class AsyncCardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCardClient
        """
        return self._raw_client

    async def list_all_card_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CardListing]:
        """
        Return all the cards available to the user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CardListing]
            Endpoint for retrieving details for the cards the user has access to.

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
            await client.card.list_all_card_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_card_for_user(user_id, request_options=request_options)
        return _response.data

    async def read_card_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CardRead:
        """
        Return the details of a specific card.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardRead
            Endpoint for retrieving details for the cards the user has access to.

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
            await client.card.read_card_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_card_for_user(user_id, item_id, request_options=request_options)
        return _response.data

    async def update_card_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        activation_code: typing.Optional[str] = OMIT,
        card_limit: typing.Optional[Amount] = OMIT,
        card_limit_atm: typing.Optional[Amount] = OMIT,
        country_permission: typing.Optional[typing.Sequence[CardCountryPermission]] = OMIT,
        monetary_account_id_fallback: typing.Optional[int] = OMIT,
        order_status: typing.Optional[str] = OMIT,
        pin_code: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        primary_account_numbers: typing.Optional[typing.Sequence[CardPrimaryAccountNumber]] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardUpdate:
        """
        Update the card details. Allow to change pin code, status, limits, country permissions and the monetary account connected to the card. When the card has been received, it can be also activated through this endpoint.

        Parameters
        ----------
        user_id : int


        item_id : int


        activation_code : typing.Optional[str]
            DEPRECATED: Activate a card by setting status to ACTIVE when the order_status is ACCEPTED_FOR_PRODUCTION.

        card_limit : typing.Optional[Amount]
            The spending limit for the card.

        card_limit_atm : typing.Optional[Amount]
            The ATM spending limit for the card.

        country_permission : typing.Optional[typing.Sequence[CardCountryPermission]]
            The countries for which to grant (temporary) permissions to use the card.

        monetary_account_id_fallback : typing.Optional[int]
            ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.

        order_status : typing.Optional[str]
            The order status to set for the card. Set to CARD_REQUEST_PENDING to get a virtual card produced.

        pin_code : typing.Optional[str]
            The plaintext pin code. Requests require encryption to be enabled.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        primary_account_numbers : typing.Optional[typing.Sequence[CardPrimaryAccountNumber]]
            Array of PANs and their attributes.

        status : typing.Optional[str]
            The status to set for the card. Can be ACTIVE, DEACTIVATED, LOST, STOLEN or CANCELLED, and can only be set to LOST/STOLEN/CANCELLED when order status is ACCEPTED_FOR_PRODUCTION/DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Can only be set to DEACTIVATED after initial activation, i.e. order_status is DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Mind that all the possible choices (apart from ACTIVE and DEACTIVATED) are permanent and cannot be changed after.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardUpdate
            Endpoint for retrieving details for the cards the user has access to.

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
            await client.card.update_card_for_user(
                user_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_card_for_user(
            user_id,
            item_id,
            activation_code=activation_code,
            card_limit=card_limit,
            card_limit_atm=card_limit_atm,
            country_permission=country_permission,
            monetary_account_id_fallback=monetary_account_id_fallback,
            order_status=order_status,
            pin_code=pin_code,
            pin_code_assignment=pin_code_assignment,
            primary_account_numbers=primary_account_numbers,
            status=status,
            request_options=request_options,
        )
        return _response.data
