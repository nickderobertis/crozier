

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.case_search_response import CaseSearchResponse
from .raw_client import AsyncRawCaseSearchApiClient, RawCaseSearchApiClient
from .types.search_cases_request_order import SearchCasesRequestOrder
from .types.search_cases_request_sort import SearchCasesRequestSort


class CaseSearchApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCaseSearchApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCaseSearchApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCaseSearchApiClient
        """
        return self._raw_client

    def search_cases(
        self,
        *,
        q: str,
        sort: typing.Optional[SearchCasesRequestSort] = None,
        order: typing.Optional[SearchCasesRequestOrder] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseSearchResponse:
        """
        This endpoint retrieves cases according to keyword expressions you provide.
        <br>
        Keyword expressions are constructed according to the rules described below.
        <br><br>
        This API supports multiple use cases:
          - Search for multiple keywords  `Google OR Facebook`.
          - Search within particular attributes.
          - Relational search using terms and connectors.
          - And much more.
        ----

        ## Allowed Connectors in Keyword Expressions
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find cases containing each of the terms joined by AND connectors.|**personal AND injury**|
        | **OR**  |Find cases containing any of the terms joined by OR connectors.|**order OR decision**|
        | **NOT** |Find cases that do not contain the specified term.|**personal AND NOT injury**.  Find cases with the word “personal” and not “injury”.|
        | **“[phrase]”** |Find the exact phrase placed between the quotation marks.|**"personal injury”**|
        | **~**  |Find cases in which the specified words appear near each other. For example, "personal injury" ~ 5 targets cases in which the word "personal" appears within 5 words of the word "injury".|**“personal injury” ~ 5** - Find cases with “personal” within five words of “injury”. |
        | **( … )** |Specifies the order in which connectors are to be appliied in a keyword expression.| **personal AND (injury OR fall)** - Find cases with the word personal injury or personal fall.|

        <br><br>
        ## Fields and Connectors Searching
        | Filed | Description  | Example |
        | ------| ------|------|
        |**caseNumber** |Find cases with the specified case number (i.e., docket number).| **caseNumber:"2020-L-007212"** - Find cases whose case number matches given case number number.|
        |**caseName** |Find cases with the specified case title.| **caseName:"THOMAS P. CARNEY, INC. VS BEHLER JAMES Et Al"** - Find cases whose case name matches given terms.|
        |**Court**|Find cases in the specified court.|**(Court:(name:(New York)))** - Find cases in New York state.<br>|
        |**CaseStatus**|Find cases witih the specified case status.|**(CaseStatus:(name:Disposed))** - All disposed cases.<br>|
        |**CaseType**|Find cases of the specified case type. | **(CaseType:(name:Property))** - Cases with case type “property”.|
        |**Party** | Find cases involving the specified party.| **(Party:(name:Apple))** - Find cases involving Apple. |
        |**partyId**|Find cases involving a party with the specified partyId value.|**(Party:(partyId:"PRTYgu1ffe866484c2"))**|
        |**PartyRole** | Find cases in which at least one party has the specified party role. | **(Party:((PartyRole:(name:"plaintiff"))))** - Find cases with party role “plaintiff”.<br><br> **(Party:((PartyRole:(name:defendant)) AND (AttorneyRepresentationType:(name:(Attorney represented)))))** - Find cases where a party is acting as defendant and represented by an attorney.|
        |**AttorneyRepresentationType**| Find cases in which at least one party has the specified attorney representation type.|**(Party:(AttorneyRepresentationType:(name:"attorney represented")))** - Find cases where a party is represented by an attorney. |
        |**Attorney** | Find cases involving the specified attorney. | **(Attorney:(name:"David Boies"))** - Find cases involving the attorney David Boies. |
        |**AttorneyType**|Find cases involving at least one attorney of the specified attorney type.|**(Attorney:((AttorneyType:(name:"Lead Attorney"))))**|
        |**Judge** |Find cases involving the specified judge. | **(Judge:(name:"Posner"))** - Find cases involving Judge Posner.|
        |**JudgeType**|Find cases involving at least one judge of the specified judge type.|**(Judge:((JudgeType:(name:"Magistrate"))))**|
        |**CaseStats**|Find cases with the specified case statistics.|**(CaseStats:(partyCount:[10 TO 100]))** - Find cases involving 10 to 100 parties.<br>**(CaseStats:(attorneyCount:[2 TO 40]))** - Find cases involving 2 to 40 attorneys.<br>**(CaseStats:(judgeCount:[\\* TO 2]))** - Find cases involving up to 2 judges. <br>**(CaseStats:(docketEntryCount:[10 TO 100]))** - Find cases having 10 to 100 docket_entries. <br>**(CaseStats:(allCaseDocumentCount:[10 TO 100]))** - Find cases having 10 to 100 documents. |
        |**filedDate** | Find cases that were filed on the specified date or within the specified date range. | **filedDate:[2020-03-15 TO 2021-12-01]** - Find the most recently filed cases between March 15, 2020 and December 1, 2021 (inclusive). |
        |**lastFetchDate**| Find cases in which UniCourt last checked for updates on the specified date or within the specified date range. |**(lastFetchDate:[now-60d TO \\*\\])** - Find cases that were updated by UniCourt in the last 60 days. |
        |**lastFetchDateWithUpdates**|Find cases in which UniCourt last detected an update on the specified date or within the specified date range.|**(lastFetchDateWithUpdates:[now-6d TO \\*\\])** - Find cases for the changes found on court site in last 6 days.|
        |**participantsLastFetchDate**|Find cases in which information cocnerning participants was last updated on the specified date or within the specified date range.|**(participantsLastFetchDate:[now-6d TO \\*\\])** - Find cases where the participant's information was updated in last 6 days.|
        |**DocketEntry**|Find cases in which at least one docket entry contains the specified text.|**(DocketEntry:(text:(Motion to Compel Responses) AND docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00]))** - Find cases with docket text “Motion to Compel Responses” and action date between 2020-01-01 and 2020-05-01.|
        |**docketEntryDate**|Find cases in which at least one docket entry was made on the specified date or within the specified date range.|**(DocketEntry:(docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00])) AND (CaseStats:(allCaseDocumentCount:[0 TO 10]))** - Find cases with docket action date between 2020-01-01 and 2020-05-01 having up to 10 documents associated with it.|
        |**HearingDate**| Find cases with at least one hearing scheduled for the specified date or within the specified date range.|**(Hearing:(hearingDate:[now TO now+10d]))** - Find cases where hearing is scheduled in next 10 days.|
        |**HearingDate**| Search for cases where hearing is going to happen in 10 to 20days.|**(Hearing:(hearingDate:[now+10d TO now+20d]))** - Find cases where hearing is scheduled in next 10 to 20 days.|
        |**JurisdictionGeo**|Find cases in which the law of the specified state governs.|**(JurisdictionGeo:(state:"New York"))**- Find cases where Jurisdiction is New York state.|
        |**Party Address Exists**|Find cases with Party addresses.|**(Party:(Contact:(Address:(stateName:\\*))))**- Returns only those cases that have addresses for parties.|
        |**Document**|Find cases with specific document name and preview is available for the document.|**(CaseDocument:(name:"civil case cover sheet" AND isPreviewAvailable:true))**- Returns cases with document civil case cover sheet and preview is available.|

        <br><br>
        ---
        ## Party Sub Filter Examples
        |Example |Explanation |
        |---|---|
        |**(Party:(name:google AND (PartyRole:(name:"plaintiff"))))**|Find cases involving at least one plaintiff whose name contains the term "Google".|
        |**(Party:(name:"OTELIA PEREIDA" AND (AttorneyRepresentationType:(name:"Attorney represented")))) AND (Attorney:(name:"Law Offices of Todd M Friedman"))**|Find cases where the Party is *OTELIA PEREIDA* and is represented by the attorney *Law Offices of Todd M Friedman*.|

        ---
        ### All query parameters supported for this API can be found in below schema section. Schema -->  CaseSearchQueryObject

        Parameters
        ----------
        q : str
            Query parameter for keyword expressions.</a>

        sort : typing.Optional[SearchCasesRequestSort]
            Query parameter specifying how results are to be sorted. Results can be sorted according to filedDate or relevancy.

        order : typing.Optional[SearchCasesRequestOrder]
            Query parameter specifying whether search result are sorted in ascending or descending order.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseSearchResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_search_api.search_cases(
            q='caseNumber:"JP07-22-DC00026818"',
            page_number=1,
        )
        """
        _response = self._raw_client.search_cases(
            q=q, sort=sort, order=order, page_number=page_number, request_options=request_options
        )
        return _response.data

    def search_cases_by_id(
        self,
        case_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseSearchResponse:
        """
        Retrieve the search results corresponding to the specified caseSearchId value.

        Parameters
        ----------
        case_search_id : str
            Case Search information for the given caseSearchId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseSearchResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.case_search_api.search_cases_by_id(
            case_search_id="CSRCU3qFUH8BjLnba5",
            page_number=1,
        )
        """
        _response = self._raw_client.search_cases_by_id(
            case_search_id, page_number=page_number, request_options=request_options
        )
        return _response.data


class AsyncCaseSearchApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCaseSearchApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCaseSearchApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCaseSearchApiClient
        """
        return self._raw_client

    async def search_cases(
        self,
        *,
        q: str,
        sort: typing.Optional[SearchCasesRequestSort] = None,
        order: typing.Optional[SearchCasesRequestOrder] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseSearchResponse:
        """
        This endpoint retrieves cases according to keyword expressions you provide.
        <br>
        Keyword expressions are constructed according to the rules described below.
        <br><br>
        This API supports multiple use cases:
          - Search for multiple keywords  `Google OR Facebook`.
          - Search within particular attributes.
          - Relational search using terms and connectors.
          - And much more.
        ----

        ## Allowed Connectors in Keyword Expressions
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find cases containing each of the terms joined by AND connectors.|**personal AND injury**|
        | **OR**  |Find cases containing any of the terms joined by OR connectors.|**order OR decision**|
        | **NOT** |Find cases that do not contain the specified term.|**personal AND NOT injury**.  Find cases with the word “personal” and not “injury”.|
        | **“[phrase]”** |Find the exact phrase placed between the quotation marks.|**"personal injury”**|
        | **~**  |Find cases in which the specified words appear near each other. For example, "personal injury" ~ 5 targets cases in which the word "personal" appears within 5 words of the word "injury".|**“personal injury” ~ 5** - Find cases with “personal” within five words of “injury”. |
        | **( … )** |Specifies the order in which connectors are to be appliied in a keyword expression.| **personal AND (injury OR fall)** - Find cases with the word personal injury or personal fall.|

        <br><br>
        ## Fields and Connectors Searching
        | Filed | Description  | Example |
        | ------| ------|------|
        |**caseNumber** |Find cases with the specified case number (i.e., docket number).| **caseNumber:"2020-L-007212"** - Find cases whose case number matches given case number number.|
        |**caseName** |Find cases with the specified case title.| **caseName:"THOMAS P. CARNEY, INC. VS BEHLER JAMES Et Al"** - Find cases whose case name matches given terms.|
        |**Court**|Find cases in the specified court.|**(Court:(name:(New York)))** - Find cases in New York state.<br>|
        |**CaseStatus**|Find cases witih the specified case status.|**(CaseStatus:(name:Disposed))** - All disposed cases.<br>|
        |**CaseType**|Find cases of the specified case type. | **(CaseType:(name:Property))** - Cases with case type “property”.|
        |**Party** | Find cases involving the specified party.| **(Party:(name:Apple))** - Find cases involving Apple. |
        |**partyId**|Find cases involving a party with the specified partyId value.|**(Party:(partyId:"PRTYgu1ffe866484c2"))**|
        |**PartyRole** | Find cases in which at least one party has the specified party role. | **(Party:((PartyRole:(name:"plaintiff"))))** - Find cases with party role “plaintiff”.<br><br> **(Party:((PartyRole:(name:defendant)) AND (AttorneyRepresentationType:(name:(Attorney represented)))))** - Find cases where a party is acting as defendant and represented by an attorney.|
        |**AttorneyRepresentationType**| Find cases in which at least one party has the specified attorney representation type.|**(Party:(AttorneyRepresentationType:(name:"attorney represented")))** - Find cases where a party is represented by an attorney. |
        |**Attorney** | Find cases involving the specified attorney. | **(Attorney:(name:"David Boies"))** - Find cases involving the attorney David Boies. |
        |**AttorneyType**|Find cases involving at least one attorney of the specified attorney type.|**(Attorney:((AttorneyType:(name:"Lead Attorney"))))**|
        |**Judge** |Find cases involving the specified judge. | **(Judge:(name:"Posner"))** - Find cases involving Judge Posner.|
        |**JudgeType**|Find cases involving at least one judge of the specified judge type.|**(Judge:((JudgeType:(name:"Magistrate"))))**|
        |**CaseStats**|Find cases with the specified case statistics.|**(CaseStats:(partyCount:[10 TO 100]))** - Find cases involving 10 to 100 parties.<br>**(CaseStats:(attorneyCount:[2 TO 40]))** - Find cases involving 2 to 40 attorneys.<br>**(CaseStats:(judgeCount:[\\* TO 2]))** - Find cases involving up to 2 judges. <br>**(CaseStats:(docketEntryCount:[10 TO 100]))** - Find cases having 10 to 100 docket_entries. <br>**(CaseStats:(allCaseDocumentCount:[10 TO 100]))** - Find cases having 10 to 100 documents. |
        |**filedDate** | Find cases that were filed on the specified date or within the specified date range. | **filedDate:[2020-03-15 TO 2021-12-01]** - Find the most recently filed cases between March 15, 2020 and December 1, 2021 (inclusive). |
        |**lastFetchDate**| Find cases in which UniCourt last checked for updates on the specified date or within the specified date range. |**(lastFetchDate:[now-60d TO \\*\\])** - Find cases that were updated by UniCourt in the last 60 days. |
        |**lastFetchDateWithUpdates**|Find cases in which UniCourt last detected an update on the specified date or within the specified date range.|**(lastFetchDateWithUpdates:[now-6d TO \\*\\])** - Find cases for the changes found on court site in last 6 days.|
        |**participantsLastFetchDate**|Find cases in which information cocnerning participants was last updated on the specified date or within the specified date range.|**(participantsLastFetchDate:[now-6d TO \\*\\])** - Find cases where the participant's information was updated in last 6 days.|
        |**DocketEntry**|Find cases in which at least one docket entry contains the specified text.|**(DocketEntry:(text:(Motion to Compel Responses) AND docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00]))** - Find cases with docket text “Motion to Compel Responses” and action date between 2020-01-01 and 2020-05-01.|
        |**docketEntryDate**|Find cases in which at least one docket entry was made on the specified date or within the specified date range.|**(DocketEntry:(docketEntryDate:[2020-01-01T00:00:00 TO 2020-05-01T00:00:00])) AND (CaseStats:(allCaseDocumentCount:[0 TO 10]))** - Find cases with docket action date between 2020-01-01 and 2020-05-01 having up to 10 documents associated with it.|
        |**HearingDate**| Find cases with at least one hearing scheduled for the specified date or within the specified date range.|**(Hearing:(hearingDate:[now TO now+10d]))** - Find cases where hearing is scheduled in next 10 days.|
        |**HearingDate**| Search for cases where hearing is going to happen in 10 to 20days.|**(Hearing:(hearingDate:[now+10d TO now+20d]))** - Find cases where hearing is scheduled in next 10 to 20 days.|
        |**JurisdictionGeo**|Find cases in which the law of the specified state governs.|**(JurisdictionGeo:(state:"New York"))**- Find cases where Jurisdiction is New York state.|
        |**Party Address Exists**|Find cases with Party addresses.|**(Party:(Contact:(Address:(stateName:\\*))))**- Returns only those cases that have addresses for parties.|
        |**Document**|Find cases with specific document name and preview is available for the document.|**(CaseDocument:(name:"civil case cover sheet" AND isPreviewAvailable:true))**- Returns cases with document civil case cover sheet and preview is available.|

        <br><br>
        ---
        ## Party Sub Filter Examples
        |Example |Explanation |
        |---|---|
        |**(Party:(name:google AND (PartyRole:(name:"plaintiff"))))**|Find cases involving at least one plaintiff whose name contains the term "Google".|
        |**(Party:(name:"OTELIA PEREIDA" AND (AttorneyRepresentationType:(name:"Attorney represented")))) AND (Attorney:(name:"Law Offices of Todd M Friedman"))**|Find cases where the Party is *OTELIA PEREIDA* and is represented by the attorney *Law Offices of Todd M Friedman*.|

        ---
        ### All query parameters supported for this API can be found in below schema section. Schema -->  CaseSearchQueryObject

        Parameters
        ----------
        q : str
            Query parameter for keyword expressions.</a>

        sort : typing.Optional[SearchCasesRequestSort]
            Query parameter specifying how results are to be sorted. Results can be sorted according to filedDate or relevancy.

        order : typing.Optional[SearchCasesRequestOrder]
            Query parameter specifying whether search result are sorted in ascending or descending order.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseSearchResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_search_api.search_cases(
                q='caseNumber:"JP07-22-DC00026818"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_cases(
            q=q, sort=sort, order=order, page_number=page_number, request_options=request_options
        )
        return _response.data

    async def search_cases_by_id(
        self,
        case_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseSearchResponse:
        """
        Retrieve the search results corresponding to the specified caseSearchId value.

        Parameters
        ----------
        case_search_id : str
            Case Search information for the given caseSearchId.

        page_number : typing.Optional[int]
            Query parameter specifying the page number of the search results to be retrieved.
            - Minimum: 1
            - Maximum: 1000

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CaseSearchResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.case_search_api.search_cases_by_id(
                case_search_id="CSRCU3qFUH8BjLnba5",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_cases_by_id(
            case_search_id, page_number=page_number, request_options=request_options
        )
        return _response.data
