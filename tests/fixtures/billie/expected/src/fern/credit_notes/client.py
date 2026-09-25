

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.amount import Amount
from .raw_client import AsyncRawCreditNotesClient, RawCreditNotesClient


OMIT = typing.cast(typing.Any, ...)


class CreditNotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCreditNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCreditNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCreditNotesClient
        """
        return self._raw_client

    def createcreditnote(
        self,
        capture_id: str,
        *,
        amount: Amount,
        external_code: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        capture_id : str

        amount : Amount

        external_code : typing.Optional[str]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import Amount, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.credit_notes.createcreditnote(
            capture_id="captureId",
            amount=Amount(
                net=1.1,
                gross=1.1,
                tax=1.1,
            ),
        )
        """
        _response = self._raw_client.createcreditnote(
            capture_id, amount=amount, external_code=external_code, comment=comment, request_options=request_options
        )
        return _response.data


class AsyncCreditNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCreditNotesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCreditNotesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCreditNotesClient
        """
        return self._raw_client

    async def createcreditnote(
        self,
        capture_id: str,
        *,
        amount: Amount,
        external_code: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        capture_id : str

        amount : Amount

        external_code : typing.Optional[str]

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.credit_notes.createcreditnote(
                capture_id="captureId",
                amount=Amount(
                    net=1.1,
                    gross=1.1,
                    tax=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createcreditnote(
            capture_id, amount=amount, external_code=external_code, comment=comment, request_options=request_options
        )
        return _response.data
