

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.card_batch_replace_create import CardBatchReplaceCreate
from ..types.card_batch_replace_entry import CardBatchReplaceEntry
from .raw_client import AsyncRawCardBatchReplaceClient, RawCardBatchReplaceClient


OMIT = typing.cast(typing.Any, ...)


class CardBatchReplaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCardBatchReplaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCardBatchReplaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCardBatchReplaceClient
        """
        return self._raw_client

    def create_card_batch_replace_for_user(
        self,
        user_id: int,
        *,
        cards: typing.Sequence[CardBatchReplaceEntry],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardBatchReplaceCreate:
        """
        Used to replace multiple cards in a batch.

        Parameters
        ----------
        user_id : int


        cards : typing.Sequence[CardBatchReplaceEntry]
            The cards that need to be replaced.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardBatchReplaceCreate
            Used to replace multiple cards in a batch.

        Examples
        --------
        from fern import CardBatchReplaceEntry, FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.card_batch_replace.create_card_batch_replace_for_user(
            user_id=1,
            cards=[
                CardBatchReplaceEntry(
                    id=1,
                )
            ],
        )
        """
        _response = self._raw_client.create_card_batch_replace_for_user(
            user_id, cards=cards, request_options=request_options
        )
        return _response.data


class AsyncCardBatchReplaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCardBatchReplaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCardBatchReplaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCardBatchReplaceClient
        """
        return self._raw_client

    async def create_card_batch_replace_for_user(
        self,
        user_id: int,
        *,
        cards: typing.Sequence[CardBatchReplaceEntry],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CardBatchReplaceCreate:
        """
        Used to replace multiple cards in a batch.

        Parameters
        ----------
        user_id : int


        cards : typing.Sequence[CardBatchReplaceEntry]
            The cards that need to be replaced.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CardBatchReplaceCreate
            Used to replace multiple cards in a batch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CardBatchReplaceEntry

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.card_batch_replace.create_card_batch_replace_for_user(
                user_id=1,
                cards=[
                    CardBatchReplaceEntry(
                        id=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_card_batch_replace_for_user(
            user_id, cards=cards, request_options=request_options
        )
        return _response.data
