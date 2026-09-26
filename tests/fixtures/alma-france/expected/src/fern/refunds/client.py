

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.refund import Refund
from .raw_client import AsyncRawRefundsClient, RawRefundsClient


OMIT = typing.cast(typing.Any, ...)


class RefundsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRefundsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRefundsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRefundsClient
        """
        return self._raw_client

    def createrefund(
        self, *, payment_id: str, amount: int, request_options: typing.Optional[RequestOptions] = None
    ) -> Refund:
        """
        Parameters
        ----------
        payment_id : str
            Payment to refund

        amount : int
            Refund amount in cents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Refund
            Refund created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.refunds.createrefund(
            payment_id="payment_id",
            amount=1,
        )
        """
        _response = self._raw_client.createrefund(payment_id=payment_id, amount=amount, request_options=request_options)
        return _response.data


class AsyncRefundsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRefundsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRefundsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRefundsClient
        """
        return self._raw_client

    async def createrefund(
        self, *, payment_id: str, amount: int, request_options: typing.Optional[RequestOptions] = None
    ) -> Refund:
        """
        Parameters
        ----------
        payment_id : str
            Payment to refund

        amount : int
            Refund amount in cents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Refund
            Refund created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.refunds.createrefund(
                payment_id="payment_id",
                amount=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createrefund(
            payment_id=payment_id, amount=amount, request_options=request_options
        )
        return _response.data
