

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.daily_activity import DailyActivity
from .raw_client import AsyncRawActivityDetailsClient, RawActivityDetailsClient


class ActivityDetailsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActivityDetailsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActivityDetailsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActivityDetailsClient
        """
        return self._raw_client

    def get_activity_details_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        kid_id: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Optional[typing.List[DailyActivity]]]:
        """
        Authenticated proxy to the activity service. company_id and school_id are required nonempty strings. This handler does not validate them as UUIDs or apply session company/school equality checks. It forwards the upstream status, Content-Type and body. Local validation and gateway errors are plain text; no pagination or count headers are added. Returns an array of per-kid activity arrays, not a flat activity array. Kids are sorted by key when kid_id is omitted. A missing kid may produce a null inner array; filtering with since can produce an empty array.

        Parameters
        ----------
        company_id : str
            Required company identifier forwarded to the source.

        school_id : str
            Required school identifier forwarded to the source.

        kid_id : typing.Optional[str]
            Optional kid UUID. If absent, returns activity lists for all kids in the school.

        since : typing.Optional[dt.datetime]
            Optional RFC3339 timestamp to filter activities.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Optional[typing.List[DailyActivity]]]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.activity_details.get_activity_details_v3(
            company_id="company_id",
            school_id="school_id",
        )
        """
        _response = self._raw_client.get_activity_details_v3(
            company_id=company_id, school_id=school_id, kid_id=kid_id, since=since, request_options=request_options
        )
        return _response.data


class AsyncActivityDetailsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActivityDetailsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActivityDetailsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActivityDetailsClient
        """
        return self._raw_client

    async def get_activity_details_v3(
        self,
        *,
        company_id: str,
        school_id: str,
        kid_id: typing.Optional[str] = None,
        since: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Optional[typing.List[DailyActivity]]]:
        """
        Authenticated proxy to the activity service. company_id and school_id are required nonempty strings. This handler does not validate them as UUIDs or apply session company/school equality checks. It forwards the upstream status, Content-Type and body. Local validation and gateway errors are plain text; no pagination or count headers are added. Returns an array of per-kid activity arrays, not a flat activity array. Kids are sorted by key when kid_id is omitted. A missing kid may produce a null inner array; filtering with since can produce an empty array.

        Parameters
        ----------
        company_id : str
            Required company identifier forwarded to the source.

        school_id : str
            Required school identifier forwarded to the source.

        kid_id : typing.Optional[str]
            Optional kid UUID. If absent, returns activity lists for all kids in the school.

        since : typing.Optional[dt.datetime]
            Optional RFC3339 timestamp to filter activities.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Optional[typing.List[DailyActivity]]]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.activity_details.get_activity_details_v3(
                company_id="company_id",
                school_id="school_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_activity_details_v3(
            company_id=company_id, school_id=school_id, kid_id=kid_id, since=since, request_options=request_options
        )
        return _response.data
