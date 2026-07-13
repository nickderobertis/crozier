

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bunq_me_fundraiser_result_read import BunqMeFundraiserResultRead
from .raw_client import AsyncRawBunqmeFundraiserResultClient, RawBunqmeFundraiserResultClient


class BunqmeFundraiserResultClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBunqmeFundraiserResultClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBunqmeFundraiserResultClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBunqmeFundraiserResultClient
        """
        return self._raw_client

    def read_bunqme_fundraiser_result_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BunqMeFundraiserResultRead:
        """
        bunq.me fundraiser result containing all payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeFundraiserResultRead
            bunq.me fundraiser result containing all payments.

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
        client.bunqme_fundraiser_result.read_bunqme_fundraiser_result_for_user_monetary_account(
            user_id=1,
            monetary_account_id=1,
            item_id=1,
        )
        """
        _response = self._raw_client.read_bunqme_fundraiser_result_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data


class AsyncBunqmeFundraiserResultClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBunqmeFundraiserResultClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBunqmeFundraiserResultClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBunqmeFundraiserResultClient
        """
        return self._raw_client

    async def read_bunqme_fundraiser_result_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BunqMeFundraiserResultRead:
        """
        bunq.me fundraiser result containing all payments.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BunqMeFundraiserResultRead
            bunq.me fundraiser result containing all payments.

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
            await client.bunqme_fundraiser_result.read_bunqme_fundraiser_result_for_user_monetary_account(
                user_id=1,
                monetary_account_id=1,
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_bunqme_fundraiser_result_for_user_monetary_account(
            user_id, monetary_account_id, item_id, request_options=request_options
        )
        return _response.data
