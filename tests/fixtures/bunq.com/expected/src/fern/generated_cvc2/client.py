

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.card_generated_cvc2create import CardGeneratedCvc2Create
from ..types.card_generated_cvc2listing import CardGeneratedCvc2Listing
from ..types.card_generated_cvc2read import CardGeneratedCvc2Read
from ..types.card_generated_cvc2update import CardGeneratedCvc2Update
from .raw_client import AsyncRawGeneratedCvc2Client, RawGeneratedCvc2Client


OMIT = typing.cast(typing.Any, ...)


class GeneratedCvc2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGeneratedCvc2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGeneratedCvc2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGeneratedCvc2Client
        """
        return self._raw_client

    def list_all_generated_cvc2for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CardGeneratedCvc2Listing]:
        """
        Get all generated CVC2 codes for a card.

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CardGeneratedCvc2Listing]
            Endpoint for generating and retrieving a new CVC2 code.

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
        client.generated_cvc2.list_all_generated_cvc2for_user_card(
            user_id=1,
            card_id=1,
        )
        """
        _response = self._raw_client.list_all_generated_cvc2for_user_card(
            user_id, card_id, request_options=request_options
        )
        return _response.data

    def create_generated_cvc2for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardGeneratedCvc2Create:
        """
        Generate a new CVC2 code for a card.

        Parameters
        ----------
        user_id : int


        card_id : int


        type : typing.Optional[str]
            The type of generated cvc2. Can be STATIC or GENERATED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardGeneratedCvc2Create
            Endpoint for generating and retrieving a new CVC2 code.

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
        client.generated_cvc2.create_generated_cvc2for_user_card(
            user_id=1,
            card_id=1,
        )
        """
        _response = self._raw_client.create_generated_cvc2for_user_card(
            user_id, card_id, type=type, request_options=request_options
        )
        return _response.data

    def read_generated_cvc2for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CardGeneratedCvc2Read:
        """
        Get the details for a specific generated CVC2 code.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardGeneratedCvc2Read
            Endpoint for generating and retrieving a new CVC2 code.

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
        client.generated_cvc2.read_generated_cvc2for_user_card(
            user_id=1,
            card_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_generated_cvc2for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data

    def update_generated_cvc2for_user_card(
        self,
        user_id: int,
        card_id: int,
        item_id: int,
        *,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardGeneratedCvc2Update:
        """
        Endpoint for generating and retrieving a new CVC2 code.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        type : typing.Optional[str]
            The type of generated cvc2. Can be STATIC or GENERATED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardGeneratedCvc2Update
            Endpoint for generating and retrieving a new CVC2 code.

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
        client.generated_cvc2.update_generated_cvc2for_user_card(
            user_id=1,
            card_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.update_generated_cvc2for_user_card(
            user_id, card_id, item_id, type=type, request_options=request_options
        )
        return _response.data


class AsyncGeneratedCvc2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGeneratedCvc2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGeneratedCvc2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGeneratedCvc2Client
        """
        return self._raw_client

    async def list_all_generated_cvc2for_user_card(
        self, user_id: int, card_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CardGeneratedCvc2Listing]:
        """
        Get all generated CVC2 codes for a card.

        Parameters
        ----------
        user_id : int


        card_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CardGeneratedCvc2Listing]
            Endpoint for generating and retrieving a new CVC2 code.

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
            await client.generated_cvc2.list_all_generated_cvc2for_user_card(
                user_id=1,
                card_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_generated_cvc2for_user_card(
            user_id, card_id, request_options=request_options
        )
        return _response.data

    async def create_generated_cvc2for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardGeneratedCvc2Create:
        """
        Generate a new CVC2 code for a card.

        Parameters
        ----------
        user_id : int


        card_id : int


        type : typing.Optional[str]
            The type of generated cvc2. Can be STATIC or GENERATED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardGeneratedCvc2Create
            Endpoint for generating and retrieving a new CVC2 code.

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
            await client.generated_cvc2.create_generated_cvc2for_user_card(
                user_id=1,
                card_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_generated_cvc2for_user_card(
            user_id, card_id, type=type, request_options=request_options
        )
        return _response.data

    async def read_generated_cvc2for_user_card(
        self, user_id: int, card_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CardGeneratedCvc2Read:
        """
        Get the details for a specific generated CVC2 code.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardGeneratedCvc2Read
            Endpoint for generating and retrieving a new CVC2 code.

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
            await client.generated_cvc2.read_generated_cvc2for_user_card(
                user_id=1,
                card_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_generated_cvc2for_user_card(
            user_id, card_id, item_id, request_options=request_options
        )
        return _response.data

    async def update_generated_cvc2for_user_card(
        self,
        user_id: int,
        card_id: int,
        item_id: int,
        *,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardGeneratedCvc2Update:
        """
        Endpoint for generating and retrieving a new CVC2 code.

        Parameters
        ----------
        user_id : int


        card_id : int


        item_id : int


        type : typing.Optional[str]
            The type of generated cvc2. Can be STATIC or GENERATED.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardGeneratedCvc2Update
            Endpoint for generating and retrieving a new CVC2 code.

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
            await client.generated_cvc2.update_generated_cvc2for_user_card(
                user_id=1,
                card_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_generated_cvc2for_user_card(
            user_id, card_id, item_id, type=type, request_options=request_options
        )
        return _response.data
