

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.eligibility_response import EligibilityResponse
from .raw_client import AsyncRawEligibilityClient, RawEligibilityClient


OMIT = typing.cast(typing.Any, ...)


class EligibilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEligibilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEligibilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEligibilityClient
        """
        return self._raw_client

    def checkpurchaseeligibility(
        self,
        *,
        purchase_amount: int,
        installments_counts: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EligibilityResponse:
        """
        Parameters
        ----------
        purchase_amount : int
            Purchase amount in cents

        installments_counts : typing.Optional[typing.Sequence[int]]
            List of installment counts to check eligibility for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EligibilityResponse
            Eligibility result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.eligibility.checkpurchaseeligibility(
            purchase_amount=1,
        )
        """
        _response = self._raw_client.checkpurchaseeligibility(
            purchase_amount=purchase_amount, installments_counts=installments_counts, request_options=request_options
        )
        return _response.data


class AsyncEligibilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEligibilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEligibilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEligibilityClient
        """
        return self._raw_client

    async def checkpurchaseeligibility(
        self,
        *,
        purchase_amount: int,
        installments_counts: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EligibilityResponse:
        """
        Parameters
        ----------
        purchase_amount : int
            Purchase amount in cents

        installments_counts : typing.Optional[typing.Sequence[int]]
            List of installment counts to check eligibility for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EligibilityResponse
            Eligibility result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.eligibility.checkpurchaseeligibility(
                purchase_amount=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.checkpurchaseeligibility(
            purchase_amount=purchase_amount, installments_counts=installments_counts, request_options=request_options
        )
        return _response.data
