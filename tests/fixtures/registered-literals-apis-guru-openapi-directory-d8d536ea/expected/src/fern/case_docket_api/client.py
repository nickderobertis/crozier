

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attorney import Attorney
from ..types.attorneys import Attorneys
from ..types.case import Case
from ..types.docket_entries import DocketEntries
from ..types.docket_entry_primary_documents import DocketEntryPrimaryDocuments
from ..types.docket_entry_secondary_documents import DocketEntrySecondaryDocuments
from ..types.hearings import Hearings
from ..types.judge import Judge
from ..types.judges import Judges
from ..types.parties import Parties
from ..types.party import Party
from ..types.party_attorney_associations import PartyAttorneyAssociations
from ..types.related_cases import RelatedCases
from .raw_client import AsyncRawCaseDocketApiClient, RawCaseDocketApiClient
from .types.get_case_docket_entries_request_sort_by import GetCaseDocketEntriesRequestSortBy
from .types.get_case_hearings_request_sort_by import GetCaseHearingsRequestSortBy
from .types.get_case_parties_request_party_classification_type import GetCasePartiesRequestPartyClassificationType


class CaseDocketApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCaseDocketApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCaseDocketApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCaseDocketApiClient
        """
        return self._raw_client

    def get_attorney_by_id(
        self, attorney_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Attorney]:
        """
        Retrieve the attorney with the specified attorneyId value.

        Parameters
        ----------
        attorney_id : str
            Retrieve the attorney with the specified attorneyId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Attorney]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_attorney_by_id(
            attorney_id="ATTYgu01be2e4de654",
        )
        """
        _response = self._raw_client.get_attorney_by_id(attorney_id, request_options=request_options)
        return _response.data

    def get_attorney_associated_parties(
        self,
        attorney_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[PartyAttorneyAssociations]:
        """
        Retrieve the parties represented by the attorney with the specified attorneyId value.

        Parameters
        ----------
        attorney_id : str
            Retrieve the parties represented by the attorney with the specified attorneyId value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[PartyAttorneyAssociations]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_attorney_associated_parties(
            attorney_id="ATTYgu01be2e4de654",
        )
        """
        _response = self._raw_client.get_attorney_associated_parties(
            attorney_id, page_number=page_number, request_options=request_options
        )
        return _response.data

    def get_case(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Case]:
        """
        Retrieve the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Case]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_case(
            case_id="CASEgr45196c84f3ff",
        )
        """
        _response = self._raw_client.get_case(case_id, request_options=request_options)
        return _response.data

    def get_case_attorneys(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Attorneys]:
        """
        Retrieve the attorneys in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        is_visible : typing.Optional[bool]
            Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Attorneys]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_case_attorneys(
            case_id="CASEgq5943bd47a6d2",
        )
        """
        _response = self._raw_client.get_case_attorneys(
            case_id, is_visible=is_visible, page_number=page_number, request_options=request_options
        )
        return _response.data

    def get_case_docket_entries(
        self,
        case_id: str,
        *,
        docket_number: typing.Optional[int] = None,
        sort_by: typing.Optional[GetCaseDocketEntriesRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[DocketEntries]:
        """
        Retrieve the docket entries in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        docket_number : typing.Optional[int]
            Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.

        sort_by : typing.Optional[GetCaseDocketEntriesRequestSortBy]
            Sort the retrieved docket entries in ascending order or descending order of date.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DocketEntries]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_case_docket_entries(
            case_id="CASEgle0bf14b74a96",
        )
        """
        _response = self._raw_client.get_case_docket_entries(
            case_id,
            docket_number=docket_number,
            sort_by=sort_by,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data

    def get_primary_documents_for_docket_entries(
        self,
        case_id: str,
        *,
        docket_number: int,
        in_library: typing.Optional[bool] = None,
        after_first_fetch_date: typing.Optional[dt.datetime] = None,
        library_date: typing.Optional[dt.datetime] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[DocketEntryPrimaryDocuments]:
        """
        Retrieve the primary documents in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        docket_number : int
            Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value.

        in_library : typing.Optional[bool]
            Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.

        after_first_fetch_date : typing.Optional[dt.datetime]
            Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.

        library_date : typing.Optional[dt.datetime]
            Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DocketEntryPrimaryDocuments]
            The request is recieved.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_primary_documents_for_docket_entries(
            case_id="CASEgued96d541f794",
            docket_number=1,
            after_first_fetch_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            library_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.get_primary_documents_for_docket_entries(
            case_id,
            docket_number=docket_number,
            in_library=in_library,
            after_first_fetch_date=after_first_fetch_date,
            library_date=library_date,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data

    def get_secondary_documents_for_docket_entries(
        self,
        case_id: str,
        *,
        docket_number: int,
        in_library: typing.Optional[bool] = None,
        after_first_fetch_date: typing.Optional[dt.datetime] = None,
        library_date: typing.Optional[dt.datetime] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[DocketEntrySecondaryDocuments]:
        """
        Retrieve the secondary documents in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        docket_number : int
            Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value.

        in_library : typing.Optional[bool]
            Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.

        after_first_fetch_date : typing.Optional[dt.datetime]
            Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.

        library_date : typing.Optional[dt.datetime]
            Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DocketEntrySecondaryDocuments]
            The request is recieved.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_secondary_documents_for_docket_entries(
            case_id="CASEgq5da86597e9a4",
            docket_number=1,
            after_first_fetch_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            library_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.get_secondary_documents_for_docket_entries(
            case_id,
            docket_number=docket_number,
            in_library=in_library,
            after_first_fetch_date=after_first_fetch_date,
            library_date=library_date,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data

    def get_case_hearings(
        self,
        case_id: str,
        *,
        sort_by: typing.Optional[GetCaseHearingsRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Hearings]:
        """
        Gets Hearings for a requested Case ID.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        sort_by : typing.Optional[GetCaseHearingsRequestSortBy]
            Specify the sort order of hearings in the case with the specified caseId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Hearings]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_case_hearings(
            case_id="CASEar3c45901ef267",
            page_number=1,
        )
        """
        _response = self._raw_client.get_case_hearings(
            case_id, sort_by=sort_by, page_number=page_number, request_options=request_options
        )
        return _response.data

    def get_case_judges(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Judges]:
        """
        Retrieve the judges involved in the specified case.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        is_visible : typing.Optional[bool]
            Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Judges]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_case_judges(
            case_id="CASEgq6e6ea66cd91d",
        )
        """
        _response = self._raw_client.get_case_judges(
            case_id, is_visible=is_visible, page_number=page_number, request_options=request_options
        )
        return _response.data

    def get_case_parties(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        party_role_id: typing.Optional[str] = None,
        party_role_group_id: typing.Optional[str] = None,
        attorney_representation_type_id: typing.Optional[str] = None,
        party_classification_type: typing.Optional[GetCasePartiesRequestPartyClassificationType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Parties]:
        """
        Retrieve the parties involved in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        is_visible : typing.Optional[bool]
            Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        party_role_id : typing.Optional[str]
            Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.

        party_role_group_id : typing.Optional[str]
            Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.

        attorney_representation_type_id : typing.Optional[str]
            Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.

        party_classification_type : typing.Optional[GetCasePartiesRequestPartyClassificationType]
            Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Parties]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_case_parties(
            case_id="CASEgq8f4cea2d8e1a",
            party_role_id="PTYRiMsyk7znqq5684",
            party_role_group_id="PTYGUZYzpfQ8eCm895",
            attorney_representation_type_id="ATRP2jCCwDRNaP9695",
        )
        """
        _response = self._raw_client.get_case_parties(
            case_id,
            is_visible=is_visible,
            page_number=page_number,
            party_role_id=party_role_id,
            party_role_group_id=party_role_group_id,
            attorney_representation_type_id=attorney_representation_type_id,
            party_classification_type=party_classification_type,
            request_options=request_options,
        )
        return _response.data

    def get_case_related_cases(
        self,
        case_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[RelatedCases]:
        """
        Retrieve cases that UniCourt has identified as related to the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[RelatedCases]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_case_related_cases(
            case_id="CASEba328623913f9f",
        )
        """
        _response = self._raw_client.get_case_related_cases(
            case_id, page_number=page_number, request_options=request_options
        )
        return _response.data

    def get_judge_by_id(
        self, judge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Judge]:
        """
        Retrieve the judge with the specified judgeId value.

        Parameters
        ----------
        judge_id : str
            Retrieve the judge with the specified judgeId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Judge]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_judge_by_id(
            judge_id="JUDGgue04d2894de7a",
        )
        """
        _response = self._raw_client.get_judge_by_id(judge_id, request_options=request_options)
        return _response.data

    def get_party_by_id(
        self, party_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Party]:
        """
        Retrieve the party with the specified partyId value.

        Parameters
        ----------
        party_id : str
            Retrieve the party with the specified partyId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Party]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_party_by_id(
            party_id="PRTYgla171a8952aed",
        )
        """
        _response = self._raw_client.get_party_by_id(party_id, request_options=request_options)
        return _response.data

    def get_party_associated_attorneys(
        self,
        party_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[PartyAttorneyAssociations]:
        """
        Retrieve the attorneys in the case with the specified partyId value.

        Parameters
        ----------
        party_id : str
            Retrieve the party with the specified partyId value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[PartyAttorneyAssociations]
            The request is recieved.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_docket_api.get_party_associated_attorneys(
            party_id="PRTYgu537f3901f406",
        )
        """
        _response = self._raw_client.get_party_associated_attorneys(
            party_id, page_number=page_number, request_options=request_options
        )
        return _response.data


class AsyncCaseDocketApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCaseDocketApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCaseDocketApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCaseDocketApiClient
        """
        return self._raw_client

    async def get_attorney_by_id(
        self, attorney_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Attorney]:
        """
        Retrieve the attorney with the specified attorneyId value.

        Parameters
        ----------
        attorney_id : str
            Retrieve the attorney with the specified attorneyId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Attorney]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_attorney_by_id(
                attorney_id="ATTYgu01be2e4de654",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attorney_by_id(attorney_id, request_options=request_options)
        return _response.data

    async def get_attorney_associated_parties(
        self,
        attorney_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[PartyAttorneyAssociations]:
        """
        Retrieve the parties represented by the attorney with the specified attorneyId value.

        Parameters
        ----------
        attorney_id : str
            Retrieve the parties represented by the attorney with the specified attorneyId value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[PartyAttorneyAssociations]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_attorney_associated_parties(
                attorney_id="ATTYgu01be2e4de654",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attorney_associated_parties(
            attorney_id, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def get_case(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Case]:
        """
        Retrieve the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Case]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_case(
                case_id="CASEgr45196c84f3ff",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case(case_id, request_options=request_options)
        return _response.data

    async def get_case_attorneys(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Attorneys]:
        """
        Retrieve the attorneys in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        is_visible : typing.Optional[bool]
            Retrieve attorneys in the case with the specified caseId value whose isVisible flag is set to the specified value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Attorneys]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_case_attorneys(
                case_id="CASEgq5943bd47a6d2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_attorneys(
            case_id, is_visible=is_visible, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def get_case_docket_entries(
        self,
        case_id: str,
        *,
        docket_number: typing.Optional[int] = None,
        sort_by: typing.Optional[GetCaseDocketEntriesRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[DocketEntries]:
        """
        Retrieve the docket entries in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        docket_number : typing.Optional[int]
            Retrieve the docket entry witih the specified docket number in the case with the specified caseId value.

        sort_by : typing.Optional[GetCaseDocketEntriesRequestSortBy]
            Sort the retrieved docket entries in ascending order or descending order of date.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DocketEntries]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_case_docket_entries(
                case_id="CASEgle0bf14b74a96",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_docket_entries(
            case_id,
            docket_number=docket_number,
            sort_by=sort_by,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data

    async def get_primary_documents_for_docket_entries(
        self,
        case_id: str,
        *,
        docket_number: int,
        in_library: typing.Optional[bool] = None,
        after_first_fetch_date: typing.Optional[dt.datetime] = None,
        library_date: typing.Optional[dt.datetime] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[DocketEntryPrimaryDocuments]:
        """
        Retrieve the primary documents in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        docket_number : int
            Retrieve the primary documents associated with the specified docket number in the case with the specified caseId value.

        in_library : typing.Optional[bool]
            Retrieve the primary documents in the with the specified inLibrary flag in the case with the specified caseId value.

        after_first_fetch_date : typing.Optional[dt.datetime]
            Retrieve all primary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.

        library_date : typing.Optional[dt.datetime]
            Retrieve all primary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DocketEntryPrimaryDocuments]
            The request is recieved.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_primary_documents_for_docket_entries(
                case_id="CASEgued96d541f794",
                docket_number=1,
                after_first_fetch_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                library_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_primary_documents_for_docket_entries(
            case_id,
            docket_number=docket_number,
            in_library=in_library,
            after_first_fetch_date=after_first_fetch_date,
            library_date=library_date,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data

    async def get_secondary_documents_for_docket_entries(
        self,
        case_id: str,
        *,
        docket_number: int,
        in_library: typing.Optional[bool] = None,
        after_first_fetch_date: typing.Optional[dt.datetime] = None,
        library_date: typing.Optional[dt.datetime] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[DocketEntrySecondaryDocuments]:
        """
        Retrieve the secondary documents in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        docket_number : int
            Retrieve the secondary documents associated with the specified docket number in the case with the specified caseId value.

        in_library : typing.Optional[bool]
            Retrieve the secondary documents in the with the specified inLibrary flag in the case with the specified caseId value.

        after_first_fetch_date : typing.Optional[dt.datetime]
            Retrieve all secondary documents in the case with the specified caseId value that were first fetched by UniCourt on the specified date or within the specified date.

        library_date : typing.Optional[dt.datetime]
            Retrieve all secondary documents in the case with the specified caseId value that were added to the Crowdsourced Library on the specified date or within the specified date.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DocketEntrySecondaryDocuments]
            The request is recieved.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_secondary_documents_for_docket_entries(
                case_id="CASEgq5da86597e9a4",
                docket_number=1,
                after_first_fetch_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                library_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_secondary_documents_for_docket_entries(
            case_id,
            docket_number=docket_number,
            in_library=in_library,
            after_first_fetch_date=after_first_fetch_date,
            library_date=library_date,
            page_number=page_number,
            request_options=request_options,
        )
        return _response.data

    async def get_case_hearings(
        self,
        case_id: str,
        *,
        sort_by: typing.Optional[GetCaseHearingsRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Hearings]:
        """
        Gets Hearings for a requested Case ID.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        sort_by : typing.Optional[GetCaseHearingsRequestSortBy]
            Specify the sort order of hearings in the case with the specified caseId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Hearings]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_case_hearings(
                case_id="CASEar3c45901ef267",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_hearings(
            case_id, sort_by=sort_by, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def get_case_judges(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Judges]:
        """
        Retrieve the judges involved in the specified case.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        is_visible : typing.Optional[bool]
            Retrieve attorneys judges in the case with the specified caseId value whose isVisible flag is set to the specified value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Judges]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_case_judges(
                case_id="CASEgq6e6ea66cd91d",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_judges(
            case_id, is_visible=is_visible, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def get_case_parties(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        party_role_id: typing.Optional[str] = None,
        party_role_group_id: typing.Optional[str] = None,
        attorney_representation_type_id: typing.Optional[str] = None,
        party_classification_type: typing.Optional[GetCasePartiesRequestPartyClassificationType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[Parties]:
        """
        Retrieve the parties involved in the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        is_visible : typing.Optional[bool]
            Retrieve parties in the case with the specified caseId value whose isVisible flag is set to the specified value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        party_role_id : typing.Optional[str]
            Retrieve all parties with the specified partyRoleId value in the case with the specified caseId value.

        party_role_group_id : typing.Optional[str]
            Retrieve all parties with the specified partyRoleGroupId value in the case with the specified caseId value.

        attorney_representation_type_id : typing.Optional[str]
            Retrieve all parties with the specified attorneyRepresentationTypeId value in the case with the specified caseId value.

        party_classification_type : typing.Optional[GetCasePartiesRequestPartyClassificationType]
            Retrieve all parties with the specified partyClassificationType value in the case with the specified caseId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Parties]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_case_parties(
                case_id="CASEgq8f4cea2d8e1a",
                party_role_id="PTYRiMsyk7znqq5684",
                party_role_group_id="PTYGUZYzpfQ8eCm895",
                attorney_representation_type_id="ATRP2jCCwDRNaP9695",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_parties(
            case_id,
            is_visible=is_visible,
            page_number=page_number,
            party_role_id=party_role_id,
            party_role_group_id=party_role_group_id,
            attorney_representation_type_id=attorney_representation_type_id,
            party_classification_type=party_classification_type,
            request_options=request_options,
        )
        return _response.data

    async def get_case_related_cases(
        self,
        case_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[RelatedCases]:
        """
        Retrieve cases that UniCourt has identified as related to the case with the specified caseId value.

        Parameters
        ----------
        case_id : str
            Retrieve the case with the specified caseId value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[RelatedCases]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_case_related_cases(
                case_id="CASEba328623913f9f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_related_cases(
            case_id, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def get_judge_by_id(
        self, judge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Judge]:
        """
        Retrieve the judge with the specified judgeId value.

        Parameters
        ----------
        judge_id : str
            Retrieve the judge with the specified judgeId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Judge]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_judge_by_id(
                judge_id="JUDGgue04d2894de7a",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_judge_by_id(judge_id, request_options=request_options)
        return _response.data

    async def get_party_by_id(
        self, party_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Party]:
        """
        Retrieve the party with the specified partyId value.

        Parameters
        ----------
        party_id : str
            Retrieve the party with the specified partyId value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Party]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_party_by_id(
                party_id="PRTYgla171a8952aed",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_party_by_id(party_id, request_options=request_options)
        return _response.data

    async def get_party_associated_attorneys(
        self,
        party_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[PartyAttorneyAssociations]:
        """
        Retrieve the attorneys in the case with the specified partyId value.

        Parameters
        ----------
        party_id : str
            Retrieve the party with the specified partyId value.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[PartyAttorneyAssociations]
            The request is recieved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_docket_api.get_party_associated_attorneys(
                party_id="PRTYgu537f3901f406",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_party_associated_attorneys(
            party_id, page_number=page_number, request_options=request_options
        )
        return _response.data
