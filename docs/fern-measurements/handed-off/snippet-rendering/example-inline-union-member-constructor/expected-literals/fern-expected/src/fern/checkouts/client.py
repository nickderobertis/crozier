

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delivery_choice import DeliveryChoice
from .raw_client import AsyncRawCheckoutsClient, RawCheckoutsClient
from .types.update_checkout_response import UpdateCheckoutResponse


OMIT = typing.cast(typing.Any, ...)


class CheckoutsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCheckoutsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCheckoutsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCheckoutsClient
        """
        return self._raw_client

    def update_checkout(
        self,
        checkout_id: str,
        *,
        deliveries: typing.Sequence[DeliveryChoice],
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCheckoutResponse:
        """
        Parameters
        ----------
        checkout_id : str

        deliveries : typing.Sequence[DeliveryChoice]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCheckoutResponse
            The checkout.

        Examples
        --------
        from fern import DeliveryChoiceZero, FernApi

        client = FernApi()
        client.checkouts.update_checkout(
            checkout_id="checkoutId",
            deliveries=[
                DeliveryChoiceZero(
                    method="locker",
                )
            ],
        )
        """
        _response = self._raw_client.update_checkout(
            checkout_id, deliveries=deliveries, note=note, request_options=request_options
        )
        return _response.data


class AsyncCheckoutsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCheckoutsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCheckoutsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCheckoutsClient
        """
        return self._raw_client

    async def update_checkout(
        self,
        checkout_id: str,
        *,
        deliveries: typing.Sequence[DeliveryChoice],
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCheckoutResponse:
        """
        Parameters
        ----------
        checkout_id : str

        deliveries : typing.Sequence[DeliveryChoice]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCheckoutResponse
            The checkout.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DeliveryChoiceZero

        client = AsyncFernApi()


        async def main() -> None:
            await client.checkouts.update_checkout(
                checkout_id="checkoutId",
                deliveries=[
                    DeliveryChoiceZero(
                        method="locker",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_checkout(
            checkout_id, deliveries=deliveries, note=note, request_options=request_options
        )
        return _response.data
