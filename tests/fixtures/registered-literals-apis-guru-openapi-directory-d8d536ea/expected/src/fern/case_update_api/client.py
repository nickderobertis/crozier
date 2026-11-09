

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.case_update import CaseUpdate
from ..types.case_update_list_response import CaseUpdateListResponse
from ..types.case_update_pacer_options import CaseUpdatePacerOptions
from .raw_client import AsyncRawCaseUpdateApiClient, RawCaseUpdateApiClient
from .types.get_case_updates_request_status import GetCaseUpdatesRequestStatus


OMIT = typing.cast(typing.Any, ...)


class CaseUpdateApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCaseUpdateApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCaseUpdateApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCaseUpdateApiClient
        """
        return self._raw_client

    def update_case(
        self,
        *,
        case_id: str,
        pacer_options: typing.Optional[CaseUpdatePacerOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseUpdate:
        """
        Request case updates for the specified case.

        Parameters
        ----------
        case_id : str
            UniCourt's Case Id for update.

        pacer_options : typing.Optional[CaseUpdatePacerOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseUpdate
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_update_api.update_case(
            case_id="CASEak99a698ea5413",
        )
        """
        _response = self._raw_client.update_case(
            case_id=case_id, pacer_options=pacer_options, request_options=request_options
        )
        return _response.data

    def get_case_update_by_case_id(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseUpdate:
        """
        Retrieve case updates for the specified case object.

        Parameters
        ----------
        case_id : str
            The caseId value of the case object for which updates are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseUpdate
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_update_api.get_case_update_by_case_id(
            case_id="CASEeqfb72ba4726f1",
        )
        """
        _response = self._raw_client.get_case_update_by_case_id(case_id, request_options=request_options)
        return _response.data

    def get_case_updates(
        self,
        *,
        case_id: typing.Optional[str] = None,
        requested_date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseUpdatesRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseUpdateListResponse:
        """
        Retrieve case updates for the specified date.

        Parameters
        ----------
        case_id : typing.Optional[str]
            The caseId value of the case for which updates should be retrieved.

        requested_date : typing.Optional[dt.datetime]
            The date for which case updates are to be retrieved.

        status : typing.Optional[GetCaseUpdatesRequestStatus]
            Status of the case updates to be retrieved.

        page_number : typing.Optional[int]
            The page number of the callbacks to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseUpdateListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_update_api.get_case_updates(
            case_id="CASEak99a698ea5413",
            page_number=1,
        )
        """
        _response = self._raw_client.get_case_updates(
            case_id=case_id,
            requested_date=requested_date,
            status=status,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data


class AsyncCaseUpdateApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCaseUpdateApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCaseUpdateApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCaseUpdateApiClient
        """
        return self._raw_client

    async def update_case(
        self,
        *,
        case_id: str,
        pacer_options: typing.Optional[CaseUpdatePacerOptions] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseUpdate:
        """
        Request case updates for the specified case.

        Parameters
        ----------
        case_id : str
            UniCourt's Case Id for update.

        pacer_options : typing.Optional[CaseUpdatePacerOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseUpdate
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_update_api.update_case(
                case_id="CASEak99a698ea5413",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_case(
            case_id=case_id, pacer_options=pacer_options, request_options=request_options
        )
        return _response.data

    async def get_case_update_by_case_id(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseUpdate:
        """
        Retrieve case updates for the specified case object.

        Parameters
        ----------
        case_id : str
            The caseId value of the case object for which updates are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseUpdate
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_update_api.get_case_update_by_case_id(
                case_id="CASEeqfb72ba4726f1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_update_by_case_id(case_id, request_options=request_options)
        return _response.data

    async def get_case_updates(
        self,
        *,
        case_id: typing.Optional[str] = None,
        requested_date: typing.Optional[dt.datetime] = None,
        status: typing.Optional[GetCaseUpdatesRequestStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseUpdateListResponse:
        """
        Retrieve case updates for the specified date.

        Parameters
        ----------
        case_id : typing.Optional[str]
            The caseId value of the case for which updates should be retrieved.

        requested_date : typing.Optional[dt.datetime]
            The date for which case updates are to be retrieved.

        status : typing.Optional[GetCaseUpdatesRequestStatus]
            Status of the case updates to be retrieved.

        page_number : typing.Optional[int]
            The page number of the callbacks to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseUpdateListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_update_api.get_case_updates(
                case_id="CASEak99a698ea5413",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_updates(
            case_id=case_id,
            requested_date=requested_date,
            status=status,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data
