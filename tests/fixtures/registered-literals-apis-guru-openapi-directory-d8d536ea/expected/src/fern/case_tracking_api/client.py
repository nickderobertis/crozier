

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.case_track import CaseTrack
from ..types.case_track_list_response import CaseTrackListResponse
from ..types.case_track_schedule import CaseTrackSchedule
from ..types.case_update_request import CaseUpdateRequest
from ..types.success import Success
from .raw_client import AsyncRawCaseTrackingApiClient, RawCaseTrackingApiClient


OMIT = typing.cast(typing.Any, ...)


class CaseTrackingApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCaseTrackingApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCaseTrackingApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCaseTrackingApiClient
        """
        return self._raw_client

    def track_case(
        self,
        *,
        case_track_params: CaseUpdateRequest,
        schedule: CaseTrackSchedule,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Success:
        """
        Track the specified case.

        Parameters
        ----------
        case_track_params : CaseUpdateRequest

        schedule : CaseTrackSchedule

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        from fern import (
            CaseTrackSchedule,
            CaseTrackScheduleType,
            CaseUpdateRequest,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_tracking_api.track_case(
            case_track_params=CaseUpdateRequest(
                case_id="CASEak470fff73ba4e",
            ),
            schedule=CaseTrackSchedule(
                days=[1, 3, 5],
                type=CaseTrackScheduleType.DAILY,
            ),
        )
        """
        _response = self._raw_client.track_case(
            case_track_params=case_track_params, schedule=schedule, request_options=request_options
        )
        return _response.data

    def get_case_track_by_id(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseTrack:
        """
        Retrieve case tracking information for the specified caseId value.

        Parameters
        ----------
        case_id : str
            The caseId value for which case tracking information is to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseTrack
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_tracking_api.get_case_track_by_id(
            case_id="CASEak99a698ea5413",
        )
        """
        _response = self._raw_client.get_case_track_by_id(case_id, request_options=request_options)
        return _response.data

    def remove_case_track_by_id(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Success:
        """
        Remove Case Track for a specific Case Id.

        Parameters
        ----------
        case_id : str
            The caseId value for which case tracking information is to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_tracking_api.remove_case_track_by_id(
            case_id="CASEak99a698ea5413",
        )
        """
        _response = self._raw_client.remove_case_track_by_id(case_id, request_options=request_options)
        return _response.data

    def get_case_tracks(
        self,
        *,
        last_fetch_date: typing.Optional[dt.datetime] = None,
        last_fetch_date_with_updates: typing.Optional[dt.datetime] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseTrackListResponse:
        """
        Retrieve a list of all tracked cases.

        Parameters
        ----------
        last_fetch_date : typing.Optional[dt.datetime]
            The lastFetchDate value of the tracked case. The date value should be entered in the format YYYY-MM-DDTHH:MM:SS+ZZ:zz.

        last_fetch_date_with_updates : typing.Optional[dt.datetime]
            The date on which changes were last found in the case information.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseTrackListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_tracking_api.get_case_tracks(
            page_number=1,
        )
        """
        _response = self._raw_client.get_case_tracks(
            last_fetch_date=last_fetch_date,
            last_fetch_date_with_updates=last_fetch_date_with_updates,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data


class AsyncCaseTrackingApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCaseTrackingApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCaseTrackingApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCaseTrackingApiClient
        """
        return self._raw_client

    async def track_case(
        self,
        *,
        case_track_params: CaseUpdateRequest,
        schedule: CaseTrackSchedule,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Success:
        """
        Track the specified case.

        Parameters
        ----------
        case_track_params : CaseUpdateRequest

        schedule : CaseTrackSchedule

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            CaseTrackSchedule,
            CaseTrackScheduleType,
            CaseUpdateRequest,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_tracking_api.track_case(
                case_track_params=CaseUpdateRequest(
                    case_id="CASEak470fff73ba4e",
                ),
                schedule=CaseTrackSchedule(
                    days=[1, 3, 5],
                    type=CaseTrackScheduleType.DAILY,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.track_case(
            case_track_params=case_track_params, schedule=schedule, request_options=request_options
        )
        return _response.data

    async def get_case_track_by_id(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseTrack:
        """
        Retrieve case tracking information for the specified caseId value.

        Parameters
        ----------
        case_id : str
            The caseId value for which case tracking information is to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseTrack
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_tracking_api.get_case_track_by_id(
                case_id="CASEak99a698ea5413",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_track_by_id(case_id, request_options=request_options)
        return _response.data

    async def remove_case_track_by_id(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Success:
        """
        Remove Case Track for a specific Case Id.

        Parameters
        ----------
        case_id : str
            The caseId value for which case tracking information is to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_tracking_api.remove_case_track_by_id(
                case_id="CASEak99a698ea5413",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_case_track_by_id(case_id, request_options=request_options)
        return _response.data

    async def get_case_tracks(
        self,
        *,
        last_fetch_date: typing.Optional[dt.datetime] = None,
        last_fetch_date_with_updates: typing.Optional[dt.datetime] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseTrackListResponse:
        """
        Retrieve a list of all tracked cases.

        Parameters
        ----------
        last_fetch_date : typing.Optional[dt.datetime]
            The lastFetchDate value of the tracked case. The date value should be entered in the format YYYY-MM-DDTHH:MM:SS+ZZ:zz.

        last_fetch_date_with_updates : typing.Optional[dt.datetime]
            The date on which changes were last found in the case information.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseTrackListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_tracking_api.get_case_tracks(
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_tracks(
            last_fetch_date=last_fetch_date,
            last_fetch_date_with_updates=last_fetch_date_with_updates,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data
