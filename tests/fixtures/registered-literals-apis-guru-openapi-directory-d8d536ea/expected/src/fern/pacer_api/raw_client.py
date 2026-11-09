

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..types.exception import Exception
from ..types.pacer_import_case import PacerImportCase
from ..types.pcl_case import PclCase
from ..types.pcl_party import PclParty
from .types.all_courts_pacer_case_locator_case_search_request_case_status import (
    AllCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
)
from .types.all_courts_pacer_case_locator_party_search_request_case_status import (
    AllCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
)
from .types.appeal_courts_pacer_case_locator_case_search_request_case_status import (
    AppealCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
)
from .types.appeal_courts_pacer_case_locator_party_search_request_case_status import (
    AppealCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
)
from .types.bankruptcy_courts_pacer_case_locator_case_search_request_case_status import (
    BankruptcyCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
)
from .types.bankruptcy_courts_pacer_case_locator_party_search_request_case_status import (
    BankruptcyCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
)
from .types.civil_courts_pacer_case_locator_case_search_request_case_status import (
    CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
)
from .types.civil_courts_pacer_case_locator_party_search_request_case_status import (
    CivilCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
)
from .types.criminal_courts_pacer_case_locator_case_search_request_case_status import (
    CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
)
from .types.criminal_courts_pacer_case_locator_party_search_request_case_status import (
    CriminalCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
)
from .types.multi_district_courts_pacer_case_locator_case_search_request_case_status import (
    MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus,
)
from .types.multi_district_courts_pacer_case_locator_party_search_request_case_status import (
    MultiDistrictCourtsPacerCaseLocatorPartySearchRequestCaseStatus,
)
from pydantic import ValidationError


class RawPacerApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def import_pacer_case_by_court_using_case_number(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: str,
        court_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PacerImportCase]:
        """
        Import the specified case from PACER.

            Workflow:

                1.This API will return the Find Case results from the court site in a form of array of UniCourt Case Objects. These case objects will consists only Meta information of the case if not already present in the UniCourt Database.

                2.To get the full updated case information one will have to request the caseUpdate API by passing the caseId.

            Note:

                1.Charges for Find Case in District, Bankruptcy and National Courts is free. Find case for Appeal Courts will be charged at minimum rate of $0.1. The fee charged by the court for find case can be found in the response of this API in the field courtFee.

                2.The results of the search has less Meta information in case objects compared to the Meta information of cases found using the PCL search APIs.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username of the PACER account under which the case should be imported.

        pacer_client_code : str
            The PACER client code under which the case should be imported.

        case_number : str
            The case number of the case to be imported.

        court_id : str
            The courtId value of the court from which the case is to be imported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PacerImportCase]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacer/importCaseByCourtUsingCaseNumber",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "courtId": court_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PacerImportCase,
                    parse_obj_as(
                        type_=PacerImportCase,
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

    def all_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[AllCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclCase]:
        """
        Search all courts within the PACER system for a particular case.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[AllCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclCase]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/allCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    def appeal_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        nature_of_suits_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[AppealCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclCase]:
        """
        Search for PACER cases filed in U.S. Courts of Appeals.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        nature_of_suits_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned nature of suit classification of the target case. Please see Appendix E for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.

                Scenario: When mulitple nature of suits needs to be requested.

                Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.

                Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[AppealCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclCase]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/appealCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "natureOfSuitsArray": nature_of_suits_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    def bankruptcy_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        federal_bankruptcy_chapter_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        case_discharged_start_date: typing.Optional[dt.datetime] = None,
        case_discharged_end_date: typing.Optional[dt.datetime] = None,
        case_dismissed_start_date: typing.Optional[dt.datetime] = None,
        case_dismissed_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[BankruptcyCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclCase]:
        """
        Search for PACER cases filed in U.S. Bankruptcy Courts.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        federal_bankruptcy_chapter_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please see Appendix D for a list of valid chapter numbers.

                Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.

                Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.

                Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_discharged_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_discharged_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_dismissed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_dismissed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[BankruptcyCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclCase]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/bankruptcyCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "federalBankruptcyChapterArray": federal_bankruptcy_chapter_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "caseDischargedStartDate": serialize_datetime(case_discharged_start_date)
                if case_discharged_start_date is not None
                else None,
                "caseDischargedEndDate": serialize_datetime(case_discharged_end_date)
                if case_discharged_end_date is not None
                else None,
                "caseDismissedStartDate": serialize_datetime(case_dismissed_start_date)
                if case_dismissed_start_date is not None
                else None,
                "caseDismissedEndDate": serialize_datetime(case_dismissed_end_date)
                if case_dismissed_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    def civil_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        nature_of_suits_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclCase]:
        """
        Search for civil cases filed in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case.

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        nature_of_suits_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned nature of suit classification of the target case. Please see Appendix E for valid nature-of-suit classifications for cases.

                Scenario: When mulitple nature of suits needs to be requested.

                Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.

                Example: natureOfSuitsArray=110&natureOfSuitsArray=140

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclCase]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/civilCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "natureOfSuitsArray": nature_of_suits_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    def criminal_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclCase]:
        """
        Search for criminal cases in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclCase]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/criminalCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    def multi_district_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        jpml_number: typing.Optional[int] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclCase]:
        """
        Search for multidistrict litigation in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        jpml_number : typing.Optional[int]
            Master JPML Case Number.

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclCase]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/multiDistrictCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "jpmlNumber": jpml_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    def all_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[AllCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclParty]:
        """
        Search for the specified party across all PACER case filings.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case.

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[AllCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclParty]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/allCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    def appeal_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[AppealCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclParty]:
        """
        Search for the specified party across all PACER appeals cases.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[AppealCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclParty]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/appealCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    def bankruptcy_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        ssn_or_ein: typing.Optional[str] = None,
        four_digit_ssn: typing.Optional[str] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        case_discharged_start_date: typing.Optional[dt.datetime] = None,
        case_discharged_end_date: typing.Optional[dt.datetime] = None,
        case_dismissed_start_date: typing.Optional[dt.datetime] = None,
        case_dismissed_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[BankruptcyCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclParty]:
        """
        Search for the specified party in PACER bankruptcy filings.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        ssn_or_ein : typing.Optional[str]
            The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.

        four_digit_ssn : typing.Optional[str]
            The last four digits of the Social Security number of the target party.

                Note: When specified, a last name/entity name must also be specified.

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_discharged_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_discharged_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_dismissed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_dismissed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[BankruptcyCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclParty]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/bankruptcyCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "ssnOrEin": ssn_or_ein,
                "fourDigitSsn": four_digit_ssn,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "caseDischargedStartDate": serialize_datetime(case_discharged_start_date)
                if case_discharged_start_date is not None
                else None,
                "caseDischargedEndDate": serialize_datetime(case_discharged_end_date)
                if case_discharged_end_date is not None
                else None,
                "caseDismissedStartDate": serialize_datetime(case_dismissed_start_date)
                if case_dismissed_start_date is not None
                else None,
                "caseDismissedEndDate": serialize_datetime(case_dismissed_end_date)
                if case_dismissed_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    def civil_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[CivilCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclParty]:
        """
        Search for the specified party in civil cases filed in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The name suffix (e.g., III, MD).

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[CivilCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclParty]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/civilCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    def criminal_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[CriminalCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclParty]:
        """
        Search for the specified party in PACER criminal cases.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[CriminalCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclParty]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/criminalCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    def multi_district_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        jpml_number: typing.Optional[int] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[MultiDistrictCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PclParty]:
        """
        Search for the specified party in multidistrict litigation in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        jpml_number : typing.Optional[int]
            Master JPML Case Number.

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[MultiDistrictCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PclParty]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/multiDistrictCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "jpmlNumber": jpml_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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


class AsyncRawPacerApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def import_pacer_case_by_court_using_case_number(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: str,
        court_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PacerImportCase]:
        """
        Import the specified case from PACER.

            Workflow:

                1.This API will return the Find Case results from the court site in a form of array of UniCourt Case Objects. These case objects will consists only Meta information of the case if not already present in the UniCourt Database.

                2.To get the full updated case information one will have to request the caseUpdate API by passing the caseId.

            Note:

                1.Charges for Find Case in District, Bankruptcy and National Courts is free. Find case for Appeal Courts will be charged at minimum rate of $0.1. The fee charged by the court for find case can be found in the response of this API in the field courtFee.

                2.The results of the search has less Meta information in case objects compared to the Meta information of cases found using the PCL search APIs.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username of the PACER account under which the case should be imported.

        pacer_client_code : str
            The PACER client code under which the case should be imported.

        case_number : str
            The case number of the case to be imported.

        court_id : str
            The courtId value of the court from which the case is to be imported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PacerImportCase]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacer/importCaseByCourtUsingCaseNumber",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "courtId": court_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PacerImportCase,
                    parse_obj_as(
                        type_=PacerImportCase,
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

    async def all_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[AllCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclCase]:
        """
        Search all courts within the PACER system for a particular case.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[AllCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclCase]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/allCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    async def appeal_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        nature_of_suits_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[AppealCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclCase]:
        """
        Search for PACER cases filed in U.S. Courts of Appeals.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        nature_of_suits_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned nature of suit classification of the target case. Please see Appendix E for valid nature-of-suit classifications for cases in U.S. Courts of Appeals.

                Scenario: When mulitple nature of suits needs to be requested.

                Imagine for a given case number 12-1234 I would like to search with the nature of suit 1110 (Insurance) and 1150 (Overpayments & Enforc. of Judgments), My query in the request will look like the example mentioned below.

                Example: natureOfSuitsArray=1110&natureOfSuitsArray=1150

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[AppealCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclCase]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/appealCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "natureOfSuitsArray": nature_of_suits_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    async def bankruptcy_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        federal_bankruptcy_chapter_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        case_discharged_start_date: typing.Optional[dt.datetime] = None,
        case_discharged_end_date: typing.Optional[dt.datetime] = None,
        case_dismissed_start_date: typing.Optional[dt.datetime] = None,
        case_dismissed_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[BankruptcyCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclCase]:
        """
        Search for PACER cases filed in U.S. Bankruptcy Courts.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        federal_bankruptcy_chapter_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The chapter of the U.S. Bankruptcy Code under which the target case was filed. Please see Appendix D for a list of valid chapter numbers.

                Scenario: When mulitple Federal Bankruptcy Chapters needs to be requested.

                Imagine for a given case number 12-1234 I would like to search with the Federal Bankruptcy Chapters 7 (Chapter 7) and 11 (Chapter 11), My query in the request will look like the example mentioned below.

                Example: federalBankruptcyChapterArray=7&federalBankruptcyChapterArray=11

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_discharged_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_discharged_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_dismissed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_dismissed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[BankruptcyCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclCase]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/bankruptcyCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "federalBankruptcyChapterArray": federal_bankruptcy_chapter_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "caseDischargedStartDate": serialize_datetime(case_discharged_start_date)
                if case_discharged_start_date is not None
                else None,
                "caseDischargedEndDate": serialize_datetime(case_discharged_end_date)
                if case_discharged_end_date is not None
                else None,
                "caseDismissedStartDate": serialize_datetime(case_dismissed_start_date)
                if case_dismissed_start_date is not None
                else None,
                "caseDismissedEndDate": serialize_datetime(case_dismissed_end_date)
                if case_dismissed_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    async def civil_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        nature_of_suits_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclCase]:
        """
        Search for civil cases filed in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case.

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        nature_of_suits_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned nature of suit classification of the target case. Please see Appendix E for valid nature-of-suit classifications for cases.

                Scenario: When mulitple nature of suits needs to be requested.

                Imagine for a given case number 12-1234 I would like to search with the nature of suit 110 (Insurance) and 140 (Negotiable Instrument), My query in the request will look like the example mentioned below.

                Example: natureOfSuitsArray=110&natureOfSuitsArray=140

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[CivilCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclCase]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/civilCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "natureOfSuitsArray": nature_of_suits_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    async def criminal_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclCase]:
        """
        Search for criminal cases in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[CriminalCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclCase]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/criminalCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    async def multi_district_courts_pacer_case_locator_case_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        jpml_number: typing.Optional[int] = None,
        pacer_case_id: typing.Optional[int] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclCase]:
        """
        Search for multidistrict litigation in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        jpml_number : typing.Optional[int]
            Master JPML Case Number.

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

        case_status : typing.Optional[MultiDistrictCourtsPacerCaseLocatorCaseSearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclCase]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/caseSearch/multiDistrictCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "jpmlNumber": jpml_number,
                "pacerCaseId": pacer_case_id,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclCase,
                    parse_obj_as(
                        type_=PclCase,
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

    async def all_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[AllCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclParty]:
        """
        Search for the specified party across all PACER case filings.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case.

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[AllCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclParty]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/allCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    async def appeal_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[AppealCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclParty]:
        """
        Search for the specified party across all PACER appeals cases.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[AppealCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclParty]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/appealCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    async def bankruptcy_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        ssn_or_ein: typing.Optional[str] = None,
        four_digit_ssn: typing.Optional[str] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        case_discharged_start_date: typing.Optional[dt.datetime] = None,
        case_discharged_end_date: typing.Optional[dt.datetime] = None,
        case_dismissed_start_date: typing.Optional[dt.datetime] = None,
        case_dismissed_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[BankruptcyCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclParty]:
        """
        Search for the specified party in PACER bankruptcy filings.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        ssn_or_ein : typing.Optional[str]
            The Social Security number or the federal Employer Identification Number of the target party. Either number can be entered with or without dashes.

        four_digit_ssn : typing.Optional[str]
            The last four digits of the Social Security number of the target party.

                Note: When specified, a last name/entity name must also be specified.

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_discharged_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_discharged_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as discharged within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_dismissed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

                Note: This parameter is applicable since we only perform this search for Bankruptcy Court type.

        case_dismissed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as dismissed within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[BankruptcyCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclParty]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/bankruptcyCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "ssnOrEin": ssn_or_ein,
                "fourDigitSsn": four_digit_ssn,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "caseDischargedStartDate": serialize_datetime(case_discharged_start_date)
                if case_discharged_start_date is not None
                else None,
                "caseDischargedEndDate": serialize_datetime(case_discharged_end_date)
                if case_discharged_end_date is not None
                else None,
                "caseDismissedStartDate": serialize_datetime(case_dismissed_start_date)
                if case_dismissed_start_date is not None
                else None,
                "caseDismissedEndDate": serialize_datetime(case_dismissed_end_date)
                if case_dismissed_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    async def civil_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[CivilCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclParty]:
        """
        Search for the specified party in civil cases filed in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The name suffix (e.g., III, MD).

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[CivilCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclParty]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/civilCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    async def criminal_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[CriminalCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclParty]:
        """
        Search for the specified party in PACER criminal cases.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[CriminalCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclParty]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/criminalCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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

    async def multi_district_courts_pacer_case_locator_party_search(
        self,
        *,
        pacer_user_id: str,
        pacer_client_code: str,
        case_number: typing.Optional[str] = None,
        jpml_number: typing.Optional[int] = None,
        pacer_case_id: typing.Optional[int] = None,
        last_name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        generation: typing.Optional[str] = None,
        party_type: typing.Optional[str] = None,
        party_exact_name_match: typing.Optional[bool] = None,
        party_role_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_title: typing.Optional[str] = None,
        case_office: typing.Optional[int] = None,
        case_sequence_number: typing.Optional[int] = None,
        case_year: typing.Optional[int] = None,
        case_type_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        court_region_id_array: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        case_year_from: typing.Optional[int] = None,
        case_year_to: typing.Optional[int] = None,
        case_filed_start_date: typing.Optional[dt.datetime] = None,
        case_filed_end_date: typing.Optional[dt.datetime] = None,
        case_terminated_start_date: typing.Optional[dt.datetime] = None,
        case_terminated_end_date: typing.Optional[dt.datetime] = None,
        sort_parameter_query: typing.Optional[str] = None,
        case_status: typing.Optional[MultiDistrictCourtsPacerCaseLocatorPartySearchRequestCaseStatus] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PclParty]:
        """
        Search for the specified party in multidistrict litigation in PACER.

        Parameters
        ----------
        pacer_user_id : str
            The username of the PACER account under which the search is to be performed.

        pacer_client_code : str
            The PACER client code under which the search is to be performed.

        case_number : typing.Optional[str]
            The case number of the target case. You may use the following case-number formats:

                yy-nnnnn

                yy-tp-nnnnn

                yy tp nnnnn

                yytpnnnnn

                o:yy-nnnnn

                o:yy-tp-nnnnn

                o:yy tp nnnnn

                o:yytpnnnnn

            where:

            yy  case year (may be 2 or 4 digits)

            nnnnn  case number (up to 5 digits)

            tp  case type (up to 2 characters)

            o  office where the case was filed (1 digit).

        jpml_number : typing.Optional[int]
            Master JPML Case Number.

        pacer_case_id : typing.Optional[int]
            The PACER-assigned identifier of the target case.

        last_name : typing.Optional[str]
            The last name (for an individual) or the entity name (for a business entity) of the target party.

        first_name : typing.Optional[str]
            The first name of the target party.

        middle_name : typing.Optional[str]
            The middle name of the target party.

        generation : typing.Optional[str]
            The suffix (e.g., Jr., III) of the target party's name.

        party_type : typing.Optional[str]
            The court-assigned party type for a party involved in a case. Party type codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        party_exact_name_match : typing.Optional[bool]
            Specify whether the search string must match the name of the target party exactly.

        party_role_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The court-assigned role for a party to a case. Party role codes are created and assigned by individual courts, and as such, their meanings can vary from court to court.

        case_title : typing.Optional[str]
            The title of the target case.

                Examples:

                A search for case title john doe v will result in all cases with the case title John Doe v.

                A search for case title Acme, Inc. will result in all case titles starting with Acme, Inc.

        case_office : typing.Optional[int]
            The divisional office in which the case was filed.

        case_sequence_number : typing.Optional[int]
            The PACER-assigned sequence number of the target case. Ex 12345

        case_year : typing.Optional[int]
            The two- or four-digit year in which the target case was filed.

        case_type_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned case type of the target case. Please see Appendix A for valid case-type values.

                Scenario: When mulitple case types needs to be requested.

                Imagine for a given case number 12-1234 I would like to search only with the case type civil(cv) and criminal(cr), My query in the request will look like the example mentioned below.

                Example: caseTypeArray=cv&caseTypeArray=cr

        court_region_id_array : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The PACER-assigned court region in which the target case was filed. Please see Appendix B for valid court-region values.

                Scenario: When mulitple court region ids needs to be requested.

                Imagine for a given case number 12-1234 I would like to search in the court regions California Central (cac) and California Eastern (cae), My query in the request will look like the example mentioned below.

                Example: courtRegionIdArray=cac&courtRegionIdArray=cae

        case_year_from : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or later

        case_year_to : typing.Optional[int]
            Limit the results of the search to those cases from the year specified or earlier

        case_filed_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_filed_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was filed. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_start_date : typing.Optional[dt.datetime]
            The date on which or after which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        case_terminated_end_date : typing.Optional[dt.datetime]
            The date on which or before which the target case was marked as terminated within PACER. The date format must be YYYY-MM-DDTHH:MM:SS+ZZ:zz, (e.g., 2017-12-20T12:54:24+00:00).

        sort_parameter_query : typing.Optional[str]
            How search results from PACER are to be sorted. Please see Appendix C for valid sort-related settings.

                Scenario 1: When mulitple sort paramters needs to be requested.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of courtId and caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtId,ASC&caseId,ASC

                Scenario 2: When you want to sort the response using the case parameters in the party search.

                Imagine for a given case number 12-1234 I would like to sort the results in the Ascending order of caseOffice and descending order of caseId, My query in the request will look like the example mentioned below.

                Example: sortParameterQuery=courtCase.caseOffice,ASC&caseid,DESC

        case_status : typing.Optional[MultiDistrictCourtsPacerCaseLocatorPartySearchRequestCaseStatus]
            Whether the target case is marked as 'open' or 'closed' within PACER.

        page_number : typing.Optional[int]
            The page number of the search results to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PclParty]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pacerCaseLocator/partySearch/multiDistrictCourts",
            method="GET",
            params={
                "pacerUserId": pacer_user_id,
                "pacerClientCode": pacer_client_code,
                "caseNumber": case_number,
                "jpmlNumber": jpml_number,
                "pacerCaseId": pacer_case_id,
                "lastName": last_name,
                "firstName": first_name,
                "middleName": middle_name,
                "generation": generation,
                "partyType": party_type,
                "partyExactNameMatch": party_exact_name_match,
                "partyRoleArray": party_role_array,
                "caseTitle": case_title,
                "caseOffice": case_office,
                "caseSequenceNumber": case_sequence_number,
                "caseYear": case_year,
                "caseTypeArray": case_type_array,
                "courtRegionIdArray": court_region_id_array,
                "caseYearFrom": case_year_from,
                "caseYearTo": case_year_to,
                "caseFiledStartDate": serialize_datetime(case_filed_start_date)
                if case_filed_start_date is not None
                else None,
                "caseFiledEndDate": serialize_datetime(case_filed_end_date)
                if case_filed_end_date is not None
                else None,
                "caseTerminatedStartDate": serialize_datetime(case_terminated_start_date)
                if case_terminated_start_date is not None
                else None,
                "caseTerminatedEndDate": serialize_datetime(case_terminated_end_date)
                if case_terminated_end_date is not None
                else None,
                "sortParameterQuery": sort_parameter_query,
                "caseStatus": case_status,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PclParty,
                    parse_obj_as(
                        type_=PclParty,
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
