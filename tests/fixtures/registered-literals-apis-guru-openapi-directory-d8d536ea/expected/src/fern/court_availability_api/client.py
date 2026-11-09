

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.court_coverage import CourtCoverage
from .raw_client import AsyncRawCourtAvailabilityApiClient, RawCourtAvailabilityApiClient


class CourtAvailabilityApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCourtAvailabilityApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCourtAvailabilityApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCourtAvailabilityApiClient
        """
        return self._raw_client

    def get_court_coverage(
        self, court_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CourtCoverage]:
        """
        Determine whether the specified court is covered by UniCourt.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CourtCoverage]
            The request is received.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_availability_api.get_court_coverage(
            court_id="CORTV4vCEaKrhystBz",
        )
        """
        _response = self._raw_client.get_court_coverage(court_id, request_options=request_options)
        return _response.data


class AsyncCourtAvailabilityApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCourtAvailabilityApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCourtAvailabilityApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCourtAvailabilityApiClient
        """
        return self._raw_client

    async def get_court_coverage(
        self, court_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CourtCoverage]:
        """
        Determine whether the specified court is covered by UniCourt.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CourtCoverage]
            The request is received.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_availability_api.get_court_coverage(
                court_id="CORTV4vCEaKrhystBz",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court_coverage(court_id, request_options=request_options)
        return _response.data
