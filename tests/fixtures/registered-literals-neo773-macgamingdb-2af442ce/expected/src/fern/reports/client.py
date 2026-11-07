

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawReportsClient, RawReportsClient
from .types.report_create_request_reason import ReportCreateRequestReason
from .types.report_create_response import ReportCreateResponse


OMIT = typing.cast(typing.Any, ...)


class ReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReportsClient
        """
        return self._raw_client

    def report_create(
        self,
        *,
        review_id: str,
        reason: typing.Optional[ReportCreateRequestReason] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportCreateResponse:
        """
        Parameters
        ----------
        review_id : str

        reason : typing.Optional[ReportCreateRequestReason]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportCreateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.reports.report_create(
            review_id="reviewId",
        )
        """
        _response = self._raw_client.report_create(
            review_id=review_id, reason=reason, note=note, request_options=request_options
        )
        return _response.data


class AsyncReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReportsClient
        """
        return self._raw_client

    async def report_create(
        self,
        *,
        review_id: str,
        reason: typing.Optional[ReportCreateRequestReason] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportCreateResponse:
        """
        Parameters
        ----------
        review_id : str

        reason : typing.Optional[ReportCreateRequestReason]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportCreateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reports.report_create(
                review_id="reviewId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.report_create(
            review_id=review_id, reason=reason, note=note, request_options=request_options
        )
        return _response.data
