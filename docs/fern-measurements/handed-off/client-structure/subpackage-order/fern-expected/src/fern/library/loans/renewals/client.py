

import typing

from ....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ....core.request_options import RequestOptions
from ....types.loan import Loan
from .raw_client import AsyncRawRenewalsClient, RawRenewalsClient


class RenewalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRenewalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRenewalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRenewalsClient
        """
        return self._raw_client

    def create(self, loan_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Loan:
        """
        Parameters
        ----------
        loan_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Loan
            The renewal.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.library.loans.renewals.create(
            loan_id="loanId",
        )
        """
        _response = self._raw_client.create(loan_id, request_options=request_options)
        return _response.data


class AsyncRenewalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRenewalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRenewalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRenewalsClient
        """
        return self._raw_client

    async def create(self, loan_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Loan:
        """
        Parameters
        ----------
        loan_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Loan
            The renewal.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.library.loans.renewals.create(
                loan_id="loanId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(loan_id, request_options=request_options)
        return _response.data
