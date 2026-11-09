

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unavailable_for_legal_reasons_error import UnavailableForLegalReasonsError
from ..types.attorney import Attorney
from ..types.attorneys import Attorneys
from ..types.case import Case
from ..types.docket_entries import DocketEntries
from ..types.docket_entry_primary_documents import DocketEntryPrimaryDocuments
from ..types.docket_entry_secondary_documents import DocketEntrySecondaryDocuments
from ..types.exception import Exception
from ..types.hearings import Hearings
from ..types.judge import Judge
from ..types.judges import Judges
from ..types.parties import Parties
from ..types.party import Party
from ..types.party_attorney_associations import PartyAttorneyAssociations
from ..types.related_cases import RelatedCases
from .types.get_case_docket_entries_request_sort_by import GetCaseDocketEntriesRequestSortBy
from .types.get_case_hearings_request_sort_by import GetCaseHearingsRequestSortBy
from .types.get_case_parties_request_party_classification_type import GetCasePartiesRequestPartyClassificationType
from pydantic import ValidationError


class RawCaseDocketApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_attorney_by_id(
        self, attorney_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[Attorney]]:
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
        HttpResponse[typing.Optional[Attorney]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"attorney/{encode_path_param(attorney_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Attorney],
                    parse_obj_as(
                        type_=typing.Optional[Attorney],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_attorney_associated_parties(
        self,
        attorney_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[PartyAttorneyAssociations]]:
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
        HttpResponse[typing.Optional[PartyAttorneyAssociations]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"attorney/{encode_path_param(attorney_id)}/associatedParties",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[PartyAttorneyAssociations],
                    parse_obj_as(
                        type_=typing.Optional[PartyAttorneyAssociations],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_case(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[Case]]:
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
        HttpResponse[typing.Optional[Case]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Case],
                    parse_obj_as(
                        type_=typing.Optional[Case],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_case_attorneys(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[Attorneys]]:
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
        HttpResponse[typing.Optional[Attorneys]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/attorneys",
            method="GET",
            params={
                "isVisible": is_visible,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Attorneys],
                    parse_obj_as(
                        type_=typing.Optional[Attorneys],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_case_docket_entries(
        self,
        case_id: str,
        *,
        docket_number: typing.Optional[int] = None,
        sort_by: typing.Optional[GetCaseDocketEntriesRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[DocketEntries]]:
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
        HttpResponse[typing.Optional[DocketEntries]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/docketEntries",
            method="GET",
            params={
                "docketNumber": docket_number,
                "sortBy": sort_by,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[DocketEntries],
                    parse_obj_as(
                        type_=typing.Optional[DocketEntries],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> HttpResponse[typing.Optional[DocketEntryPrimaryDocuments]]:
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
        HttpResponse[typing.Optional[DocketEntryPrimaryDocuments]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/docketEntries/primaryDocuments",
            method="GET",
            params={
                "docketNumber": docket_number,
                "inLibrary": in_library,
                "afterFirstFetchDate": serialize_datetime(after_first_fetch_date)
                if after_first_fetch_date is not None
                else None,
                "libraryDate": serialize_datetime(library_date) if library_date is not None else None,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[DocketEntryPrimaryDocuments],
                    parse_obj_as(
                        type_=typing.Optional[DocketEntryPrimaryDocuments],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> HttpResponse[typing.Optional[DocketEntrySecondaryDocuments]]:
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
        HttpResponse[typing.Optional[DocketEntrySecondaryDocuments]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/docketEntries/secondaryDocuments",
            method="GET",
            params={
                "docketNumber": docket_number,
                "inLibrary": in_library,
                "afterFirstFetchDate": serialize_datetime(after_first_fetch_date)
                if after_first_fetch_date is not None
                else None,
                "libraryDate": serialize_datetime(library_date) if library_date is not None else None,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[DocketEntrySecondaryDocuments],
                    parse_obj_as(
                        type_=typing.Optional[DocketEntrySecondaryDocuments],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_case_hearings(
        self,
        case_id: str,
        *,
        sort_by: typing.Optional[GetCaseHearingsRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[Hearings]]:
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
        HttpResponse[typing.Optional[Hearings]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/hearings",
            method="GET",
            params={
                "sortBy": sort_by,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Hearings],
                    parse_obj_as(
                        type_=typing.Optional[Hearings],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_case_judges(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[Judges]]:
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
        HttpResponse[typing.Optional[Judges]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/judges",
            method="GET",
            params={
                "isVisible": is_visible,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Judges],
                    parse_obj_as(
                        type_=typing.Optional[Judges],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> HttpResponse[typing.Optional[Parties]]:
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
        HttpResponse[typing.Optional[Parties]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/parties",
            method="GET",
            params={
                "isVisible": is_visible,
                "pageNumber": page_number,
                "partyRoleId": party_role_id,
                "partyRoleGroupId": party_role_group_id,
                "attorneyRepresentationTypeId": attorney_representation_type_id,
                "partyClassificationType": party_classification_type,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Parties],
                    parse_obj_as(
                        type_=typing.Optional[Parties],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_case_related_cases(
        self,
        case_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[RelatedCases]]:
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
        HttpResponse[typing.Optional[RelatedCases]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/relatedCases",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[RelatedCases],
                    parse_obj_as(
                        type_=typing.Optional[RelatedCases],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_judge_by_id(
        self, judge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[Judge]]:
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
        HttpResponse[typing.Optional[Judge]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"judge/{encode_path_param(judge_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Judge],
                    parse_obj_as(
                        type_=typing.Optional[Judge],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_party_by_id(
        self, party_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[Party]]:
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
        HttpResponse[typing.Optional[Party]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"party/{encode_path_param(party_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Party],
                    parse_obj_as(
                        type_=typing.Optional[Party],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_party_associated_attorneys(
        self,
        party_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[PartyAttorneyAssociations]]:
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
        HttpResponse[typing.Optional[PartyAttorneyAssociations]]
            The request is recieved.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"party/{encode_path_param(party_id)}/associatedAttorneys",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[PartyAttorneyAssociations],
                    parse_obj_as(
                        type_=typing.Optional[PartyAttorneyAssociations],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawCaseDocketApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_attorney_by_id(
        self, attorney_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[Attorney]]:
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
        AsyncHttpResponse[typing.Optional[Attorney]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"attorney/{encode_path_param(attorney_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Attorney],
                    parse_obj_as(
                        type_=typing.Optional[Attorney],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_attorney_associated_parties(
        self,
        attorney_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[PartyAttorneyAssociations]]:
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
        AsyncHttpResponse[typing.Optional[PartyAttorneyAssociations]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"attorney/{encode_path_param(attorney_id)}/associatedParties",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[PartyAttorneyAssociations],
                    parse_obj_as(
                        type_=typing.Optional[PartyAttorneyAssociations],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_case(
        self, case_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[Case]]:
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
        AsyncHttpResponse[typing.Optional[Case]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Case],
                    parse_obj_as(
                        type_=typing.Optional[Case],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_case_attorneys(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[Attorneys]]:
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
        AsyncHttpResponse[typing.Optional[Attorneys]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/attorneys",
            method="GET",
            params={
                "isVisible": is_visible,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Attorneys],
                    parse_obj_as(
                        type_=typing.Optional[Attorneys],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_case_docket_entries(
        self,
        case_id: str,
        *,
        docket_number: typing.Optional[int] = None,
        sort_by: typing.Optional[GetCaseDocketEntriesRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[DocketEntries]]:
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
        AsyncHttpResponse[typing.Optional[DocketEntries]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/docketEntries",
            method="GET",
            params={
                "docketNumber": docket_number,
                "sortBy": sort_by,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[DocketEntries],
                    parse_obj_as(
                        type_=typing.Optional[DocketEntries],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> AsyncHttpResponse[typing.Optional[DocketEntryPrimaryDocuments]]:
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
        AsyncHttpResponse[typing.Optional[DocketEntryPrimaryDocuments]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/docketEntries/primaryDocuments",
            method="GET",
            params={
                "docketNumber": docket_number,
                "inLibrary": in_library,
                "afterFirstFetchDate": serialize_datetime(after_first_fetch_date)
                if after_first_fetch_date is not None
                else None,
                "libraryDate": serialize_datetime(library_date) if library_date is not None else None,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[DocketEntryPrimaryDocuments],
                    parse_obj_as(
                        type_=typing.Optional[DocketEntryPrimaryDocuments],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> AsyncHttpResponse[typing.Optional[DocketEntrySecondaryDocuments]]:
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
        AsyncHttpResponse[typing.Optional[DocketEntrySecondaryDocuments]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/docketEntries/secondaryDocuments",
            method="GET",
            params={
                "docketNumber": docket_number,
                "inLibrary": in_library,
                "afterFirstFetchDate": serialize_datetime(after_first_fetch_date)
                if after_first_fetch_date is not None
                else None,
                "libraryDate": serialize_datetime(library_date) if library_date is not None else None,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[DocketEntrySecondaryDocuments],
                    parse_obj_as(
                        type_=typing.Optional[DocketEntrySecondaryDocuments],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_case_hearings(
        self,
        case_id: str,
        *,
        sort_by: typing.Optional[GetCaseHearingsRequestSortBy] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[Hearings]]:
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
        AsyncHttpResponse[typing.Optional[Hearings]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/hearings",
            method="GET",
            params={
                "sortBy": sort_by,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Hearings],
                    parse_obj_as(
                        type_=typing.Optional[Hearings],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_case_judges(
        self,
        case_id: str,
        *,
        is_visible: typing.Optional[bool] = None,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[Judges]]:
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
        AsyncHttpResponse[typing.Optional[Judges]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/judges",
            method="GET",
            params={
                "isVisible": is_visible,
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Judges],
                    parse_obj_as(
                        type_=typing.Optional[Judges],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
    ) -> AsyncHttpResponse[typing.Optional[Parties]]:
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
        AsyncHttpResponse[typing.Optional[Parties]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/parties",
            method="GET",
            params={
                "isVisible": is_visible,
                "pageNumber": page_number,
                "partyRoleId": party_role_id,
                "partyRoleGroupId": party_role_group_id,
                "attorneyRepresentationTypeId": attorney_representation_type_id,
                "partyClassificationType": party_classification_type,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Parties],
                    parse_obj_as(
                        type_=typing.Optional[Parties],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_case_related_cases(
        self,
        case_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[RelatedCases]]:
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
        AsyncHttpResponse[typing.Optional[RelatedCases]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"case/{encode_path_param(case_id)}/relatedCases",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[RelatedCases],
                    parse_obj_as(
                        type_=typing.Optional[RelatedCases],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_judge_by_id(
        self, judge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[Judge]]:
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
        AsyncHttpResponse[typing.Optional[Judge]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"judge/{encode_path_param(judge_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Judge],
                    parse_obj_as(
                        type_=typing.Optional[Judge],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_party_by_id(
        self, party_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[Party]]:
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
        AsyncHttpResponse[typing.Optional[Party]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"party/{encode_path_param(party_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Party],
                    parse_obj_as(
                        type_=typing.Optional[Party],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_party_associated_attorneys(
        self,
        party_id: str,
        *,
        page_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[PartyAttorneyAssociations]]:
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
        AsyncHttpResponse[typing.Optional[PartyAttorneyAssociations]]
            The request is recieved.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"party/{encode_path_param(party_id)}/associatedAttorneys",
            method="GET",
            params={
                "pageNumber": page_number,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[PartyAttorneyAssociations],
                    parse_obj_as(
                        type_=typing.Optional[PartyAttorneyAssociations],
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
            if _response.status_code == 451:
                raise UnavailableForLegalReasonsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
