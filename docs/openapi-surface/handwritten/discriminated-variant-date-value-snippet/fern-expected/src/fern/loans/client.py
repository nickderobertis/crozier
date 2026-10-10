

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.due_marker import DueMarker
from .raw_client import AsyncRawLoansClient, RawLoansClient


OMIT = typing.cast(typing.Any, ...)


class LoansClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLoansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLoansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLoansClient
        """
        return self._raw_client

    def set_due(
        self, loan_id: str, *, request: DueMarker, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        loan_id : str

        request : DueMarker

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import DueMarker_Calendar, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.loans.set_due(
            loan_id="loanId",
            request=DueMarker_Calendar(
                value=datetime.date.fromisoformat(
                    "2023-01-15",
                ),
            ),
        )
        """
        _response = self._raw_client.set_due(loan_id, request=request, request_options=request_options)
        return _response.data


class AsyncLoansClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLoansClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLoansClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLoansClient
        """
        return self._raw_client

    async def set_due(
        self, loan_id: str, *, request: DueMarker, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        loan_id : str

        request : DueMarker

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, DueMarker_Calendar

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.loans.set_due(
                loan_id="loanId",
                request=DueMarker_Calendar(
                    value=datetime.date.fromisoformat(
                        "2023-01-15",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_due(loan_id, request=request, request_options=request_options)
        return _response.data
