

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPayoutsClient, RawPayoutsClient
from .types.create_payout_response import CreatePayoutResponse


OMIT = typing.cast(typing.Any, ...)


class PayoutsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPayoutsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPayoutsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPayoutsClient
        """
        return self._raw_client

    def create_payout(
        self, *, amount: int, request_options: typing.Optional[RequestOptions] = None
    ) -> CreatePayoutResponse:
        """
        Parameters
        ----------
        amount : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePayoutResponse
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.payouts.create_payout(
            amount=1,
        )
        """
        _response = self._raw_client.create_payout(amount=amount, request_options=request_options)
        return _response.data


class AsyncPayoutsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPayoutsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPayoutsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPayoutsClient
        """
        return self._raw_client

    async def create_payout(
        self, *, amount: int, request_options: typing.Optional[RequestOptions] = None
    ) -> CreatePayoutResponse:
        """
        Parameters
        ----------
        amount : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePayoutResponse
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.payouts.create_payout(
                amount=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_payout(amount=amount, request_options=request_options)
        return _response.data
