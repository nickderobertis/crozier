

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.payment_request_source import PaymentRequestSource
from .raw_client import AsyncRawPaymentsClient, RawPaymentsClient
from .types.pay_toll_response import PayTollResponse


OMIT = typing.cast(typing.Any, ...)


class PaymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentsClient
        """
        return self._raw_client

    def pay_toll(
        self, *, lane: int, source: PaymentRequestSource, request_options: typing.Optional[RequestOptions] = None
    ) -> PayTollResponse:
        """
        Parameters
        ----------
        lane : int

        source : PaymentRequestSource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayTollResponse
            Paid.

        Examples
        --------
        from fern import FernApi, PaymentRequestSource_Tag

        client = FernApi()
        client.payments.pay_toll(
            lane=1,
            source=PaymentRequestSource_Tag(
                tag_id="tagId",
            ),
        )
        """
        _response = self._raw_client.pay_toll(lane=lane, source=source, request_options=request_options)
        return _response.data


class AsyncPaymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentsClient
        """
        return self._raw_client

    async def pay_toll(
        self, *, lane: int, source: PaymentRequestSource, request_options: typing.Optional[RequestOptions] = None
    ) -> PayTollResponse:
        """
        Parameters
        ----------
        lane : int

        source : PaymentRequestSource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayTollResponse
            Paid.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PaymentRequestSource_Tag

        client = AsyncFernApi()


        async def main() -> None:
            await client.payments.pay_toll(
                lane=1,
                source=PaymentRequestSource_Tag(
                    tag_id="tagId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pay_toll(lane=lane, source=source, request_options=request_options)
        return _response.data
