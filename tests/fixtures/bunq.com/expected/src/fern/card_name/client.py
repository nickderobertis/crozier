

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.card_name_listing import CardNameListing
from .raw_client import AsyncRawCardNameClient, RawCardNameClient


class CardNameClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCardNameClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCardNameClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCardNameClient
        """
        return self._raw_client

    def list_all_card_name_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CardNameListing]:
        """
        Return all the accepted card names for a specific user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CardNameListing]
            Endpoint for getting all the accepted card names for a user. As bunq do not allow total freedom in choosing the name that is going to be printed on the card, the following formats are accepted: Name Surname, N. Surname, N Surname or Surname.

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
        client.card_name.list_all_card_name_for_user(
            user_id=1,
        )
        """
        _response = self._raw_client.list_all_card_name_for_user(user_id, request_options=request_options)
        return _response.data


class AsyncCardNameClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCardNameClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCardNameClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCardNameClient
        """
        return self._raw_client

    async def list_all_card_name_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CardNameListing]:
        """
        Return all the accepted card names for a specific user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CardNameListing]
            Endpoint for getting all the accepted card names for a user. As bunq do not allow total freedom in choosing the name that is going to be printed on the card, the following formats are accepted: Name Surname, N. Surname, N Surname or Surname.

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
            await client.card_name.list_all_card_name_for_user(
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_card_name_for_user(user_id, request_options=request_options)
        return _response.data
