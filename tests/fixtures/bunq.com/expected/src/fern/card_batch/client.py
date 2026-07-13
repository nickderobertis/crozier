

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.card_batch_create import CardBatchCreate
from ..types.card_batch_entry import CardBatchEntry
from .raw_client import AsyncRawCardBatchClient, RawCardBatchClient


OMIT = typing.cast(typing.Any, ...)


class CardBatchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCardBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCardBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCardBatchClient
        """
        return self._raw_client

    def create_card_batch_for_user(
        self,
        user_id: int,
        *,
        cards: typing.Sequence[CardBatchEntry],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardBatchCreate:
        """
        Used to update multiple cards in a batch.

        Parameters
        ----------
        user_id : int


        cards : typing.Sequence[CardBatchEntry]
            The cards that need to be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardBatchCreate
            Used to update multiple cards in a batch.

        Examples
        --------
        from fern import CardBatchEntry, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.card_batch.create_card_batch_for_user(
            user_id=1,
            cards=[
                CardBatchEntry(
                    id=1,
                )
            ],
        )
        """
        _response = self._raw_client.create_card_batch_for_user(user_id, cards=cards, request_options=request_options)
        return _response.data


class AsyncCardBatchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCardBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCardBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCardBatchClient
        """
        return self._raw_client

    async def create_card_batch_for_user(
        self,
        user_id: int,
        *,
        cards: typing.Sequence[CardBatchEntry],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardBatchCreate:
        """
        Used to update multiple cards in a batch.

        Parameters
        ----------
        user_id : int


        cards : typing.Sequence[CardBatchEntry]
            The cards that need to be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardBatchCreate
            Used to update multiple cards in a batch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CardBatchEntry

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.card_batch.create_card_batch_for_user(
                user_id=1,
                cards=[
                    CardBatchEntry(
                        id=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_card_batch_for_user(
            user_id, cards=cards, request_options=request_options
        )
        return _response.data
