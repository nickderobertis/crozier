

from __future__ import annotations

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.loan import Loan
from .raw_client import AsyncRawLoansClient, RawLoansClient

if typing.TYPE_CHECKING:
    from .renewals.client import AsyncRenewalsClient, RenewalsClient


class LoansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLoansClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._renewals: typing.Optional[RenewalsClient] = None

    @property
    def with_raw_response(self) -> RawLoansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLoansClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Loan]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Loan]
            Loans.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.library.loans.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    @property
    def renewals(self):
        if self._renewals is None:
            from .renewals.client import RenewalsClient

            self._renewals = RenewalsClient(client_wrapper=self._client_wrapper)
        return self._renewals


class AsyncLoansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLoansClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._renewals: typing.Optional[AsyncRenewalsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawLoansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLoansClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Loan]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Loan]
            Loans.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.library.loans.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    @property
    def renewals(self):
        if self._renewals is None:
            from .renewals.client import AsyncRenewalsClient

            self._renewals = AsyncRenewalsClient(client_wrapper=self._client_wrapper)
        return self._renewals
