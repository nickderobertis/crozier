

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.activity_summary_kid import ActivitySummaryKid
from .raw_client import AsyncRawActivitiesSummaryClient, RawActivitiesSummaryClient


class ActivitiesSummaryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActivitiesSummaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActivitiesSummaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActivitiesSummaryClient
        """
        return self._raw_client

    def get_activities_summary_v3(
        self, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ActivitySummaryKid]:
        """
        Authenticated proxy to the activity service. company_id and school_id are required nonempty strings. This handler does not validate them as UUIDs or apply session company/school equality checks. It forwards the upstream status, Content-Type and body. Local validation and gateway errors are plain text; no pagination or count headers are added. Returns a flat kid-summary array sorted by kid key.

        Parameters
        ----------
        company_id : str
            Required company identifier forwarded to the source.

        school_id : str
            Required school identifier forwarded to the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ActivitySummaryKid]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.activities_summary.get_activities_summary_v3(
            company_id="company_id",
            school_id="school_id",
        )
        """
        _response = self._raw_client.get_activities_summary_v3(
            company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data


class AsyncActivitiesSummaryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActivitiesSummaryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActivitiesSummaryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActivitiesSummaryClient
        """
        return self._raw_client

    async def get_activities_summary_v3(
        self, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ActivitySummaryKid]:
        """
        Authenticated proxy to the activity service. company_id and school_id are required nonempty strings. This handler does not validate them as UUIDs or apply session company/school equality checks. It forwards the upstream status, Content-Type and body. Local validation and gateway errors are plain text; no pagination or count headers are added. Returns a flat kid-summary array sorted by kid key.

        Parameters
        ----------
        company_id : str
            Required company identifier forwarded to the source.

        school_id : str
            Required school identifier forwarded to the source.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ActivitySummaryKid]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.activities_summary.get_activities_summary_v3(
                company_id="company_id",
                school_id="school_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_activities_summary_v3(
            company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data
