

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.case_search_response import CaseSearchResponse
from ..types.exception import Exception
from .types.search_cases_request_order import SearchCasesRequestOrder
from .types.search_cases_request_sort import SearchCasesRequestSort
from pydantic import ValidationError


class RawCaseSearchApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_cases(
        self,
        *,
        q: str,
        sort: typing.Optional[SearchCasesRequestSort] = None,
        order: typing.Optional[SearchCasesRequestOrder] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseSearchResponse]:
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
        HttpResponse[CaseSearchResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "caseSearch",
            method="GET",
            params={
                "q": q,
                "sort": sort,
                "order": order,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseSearchResponse,
                    parse_obj_as(
                        type_=CaseSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_cases_by_id(
        self,
        case_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseSearchResponse]:
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
        HttpResponse[CaseSearchResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"caseSearch/{encode_path_param(case_search_id)}",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseSearchResponse,
                    parse_obj_as(
                        type_=CaseSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCaseSearchApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_cases(
        self,
        *,
        q: str,
        sort: typing.Optional[SearchCasesRequestSort] = None,
        order: typing.Optional[SearchCasesRequestOrder] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseSearchResponse]:
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
        AsyncHttpResponse[CaseSearchResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "caseSearch",
            method="GET",
            params={
                "q": q,
                "sort": sort,
                "order": order,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseSearchResponse,
                    parse_obj_as(
                        type_=CaseSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_cases_by_id(
        self,
        case_search_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseSearchResponse]:
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
        AsyncHttpResponse[CaseSearchResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"caseSearch/{encode_path_param(case_search_id)}",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseSearchResponse,
                    parse_obj_as(
                        type_=CaseSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[Exception],
                        parse_obj_as(
                            type_=typing.Optional[Exception],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
