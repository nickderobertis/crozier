

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
from ..types.area_of_law import AreaOfLaw
from ..types.area_of_law_response import AreaOfLawResponse
from ..types.attorney_representation_type import AttorneyRepresentationType
from ..types.attorney_representation_type_response import AttorneyRepresentationTypeResponse
from ..types.attorney_type import AttorneyType
from ..types.attorney_type_response import AttorneyTypeResponse
from ..types.case_class import CaseClass
from ..types.case_class_response import CaseClassResponse
from ..types.case_relationship_type import CaseRelationshipType
from ..types.case_relationship_type_response import CaseRelationshipTypeResponse
from ..types.case_status import CaseStatus
from ..types.case_status_group import CaseStatusGroup
from ..types.case_status_group_response import CaseStatusGroupResponse
from ..types.case_status_response import CaseStatusResponse
from ..types.case_type import CaseType
from ..types.case_type_group import CaseTypeGroup
from ..types.case_type_group_response import CaseTypeGroupResponse
from ..types.case_type_response import CaseTypeResponse
from ..types.cause_of_action import CauseOfAction
from ..types.cause_of_action_additional_data import CauseOfActionAdditionalData
from ..types.cause_of_action_additional_data_response import CauseOfActionAdditionalDataResponse
from ..types.cause_of_action_group import CauseOfActionGroup
from ..types.cause_of_action_group_response import CauseOfActionGroupResponse
from ..types.cause_of_action_response import CauseOfActionResponse
from ..types.charge import Charge
from ..types.charge_additional_data import ChargeAdditionalData
from ..types.charge_additional_data_response import ChargeAdditionalDataResponse
from ..types.charge_degree import ChargeDegree
from ..types.charge_degree_response import ChargeDegreeResponse
from ..types.charge_group import ChargeGroup
from ..types.charge_group_response import ChargeGroupResponse
from ..types.charge_response import ChargeResponse
from ..types.charge_severity import ChargeSeverity
from ..types.charge_severity_response import ChargeSeverityResponse
from ..types.court import Court
from ..types.court_location import CourtLocation
from ..types.court_location_response import CourtLocationResponse
from ..types.court_response import CourtResponse
from ..types.court_service_status import CourtServiceStatus
from ..types.court_service_status_response import CourtServiceStatusResponse
from ..types.court_system import CourtSystem
from ..types.court_system_response import CourtSystemResponse
from ..types.court_type import CourtType
from ..types.court_type_response import CourtTypeResponse
from ..types.exception import Exception
from ..types.judge_type import JudgeType
from ..types.judge_type_response import JudgeTypeResponse
from ..types.jurisdiction_geo import JurisdictionGeo
from ..types.jurisdiction_geo_response import JurisdictionGeoResponse
from ..types.party_role import PartyRole
from ..types.party_role_group import PartyRoleGroup
from ..types.party_role_group_response import PartyRoleGroupResponse
from ..types.party_role_response import PartyRoleResponse
from .types.get_appeal_courts_for_court_request_order import GetAppealCourtsForCourtRequestOrder
from .types.get_appeal_courts_for_court_request_sort import GetAppealCourtsForCourtRequestSort
from .types.get_areas_of_law_request_order import GetAreasOfLawRequestOrder
from .types.get_areas_of_law_request_sort import GetAreasOfLawRequestSort
from .types.get_attorney_representation_types_request_order import GetAttorneyRepresentationTypesRequestOrder
from .types.get_attorney_representation_types_request_sort import GetAttorneyRepresentationTypesRequestSort
from .types.get_attorney_types_request_order import GetAttorneyTypesRequestOrder
from .types.get_attorney_types_request_sort import GetAttorneyTypesRequestSort
from .types.get_case_relationship_types_request_order import GetCaseRelationshipTypesRequestOrder
from .types.get_case_relationship_types_request_sort import GetCaseRelationshipTypesRequestSort
from .types.get_case_status_groups_request_order import GetCaseStatusGroupsRequestOrder
from .types.get_case_status_groups_request_sort import GetCaseStatusGroupsRequestSort
from .types.get_case_type_groups_request_order import GetCaseTypeGroupsRequestOrder
from .types.get_case_type_groups_request_sort import GetCaseTypeGroupsRequestSort
from .types.get_case_types_request_order import GetCaseTypesRequestOrder
from .types.get_case_types_request_sort import GetCaseTypesRequestSort
from .types.get_cases_class_request_order import GetCasesClassRequestOrder
from .types.get_cases_class_request_sort import GetCasesClassRequestSort
from .types.get_cases_status_request_order import GetCasesStatusRequestOrder
from .types.get_cases_status_request_sort import GetCasesStatusRequestSort
from .types.get_causes_of_action_additional_data_request_order import GetCausesOfActionAdditionalDataRequestOrder
from .types.get_causes_of_action_additional_data_request_sort import GetCausesOfActionAdditionalDataRequestSort
from .types.get_causes_of_action_group_request_order import GetCausesOfActionGroupRequestOrder
from .types.get_causes_of_action_group_request_sort import GetCausesOfActionGroupRequestSort
from .types.get_causes_of_action_request_order import GetCausesOfActionRequestOrder
from .types.get_causes_of_action_request_sort import GetCausesOfActionRequestSort
from .types.get_charge_groups_request_order import GetChargeGroupsRequestOrder
from .types.get_charge_groups_request_sort import GetChargeGroupsRequestSort
from .types.get_charges_additional_data_request_order import GetChargesAdditionalDataRequestOrder
from .types.get_charges_additional_data_request_sort import GetChargesAdditionalDataRequestSort
from .types.get_charges_degree_request_order import GetChargesDegreeRequestOrder
from .types.get_charges_degree_request_sort import GetChargesDegreeRequestSort
from .types.get_charges_request_order import GetChargesRequestOrder
from .types.get_charges_request_sort import GetChargesRequestSort
from .types.get_charges_severity_request_order import GetChargesSeverityRequestOrder
from .types.get_charges_severity_request_sort import GetChargesSeverityRequestSort
from .types.get_court_locations_for_court_request_order import GetCourtLocationsForCourtRequestOrder
from .types.get_court_locations_for_court_request_sort import GetCourtLocationsForCourtRequestSort
from .types.get_court_locations_request_order import GetCourtLocationsRequestOrder
from .types.get_court_locations_request_sort import GetCourtLocationsRequestSort
from .types.get_court_systems_request_order import GetCourtSystemsRequestOrder
from .types.get_court_systems_request_sort import GetCourtSystemsRequestSort
from .types.get_court_types_request_order import GetCourtTypesRequestOrder
from .types.get_court_types_request_sort import GetCourtTypesRequestSort
from .types.get_courts_for_court_location_request_order import GetCourtsForCourtLocationRequestOrder
from .types.get_courts_for_court_location_request_sort import GetCourtsForCourtLocationRequestSort
from .types.get_courts_for_jurisdiction_geo_request_order import GetCourtsForJurisdictionGeoRequestOrder
from .types.get_courts_for_jurisdiction_geo_request_sort import GetCourtsForJurisdictionGeoRequestSort
from .types.get_courts_request_order import GetCourtsRequestOrder
from .types.get_courts_request_sort import GetCourtsRequestSort
from .types.get_courts_service_status_request_order import GetCourtsServiceStatusRequestOrder
from .types.get_courts_service_status_request_sort import GetCourtsServiceStatusRequestSort
from .types.get_judge_types_request_order import GetJudgeTypesRequestOrder
from .types.get_judge_types_request_sort import GetJudgeTypesRequestSort
from .types.get_jurisdiction_geo_for_court_request_order import GetJurisdictionGeoForCourtRequestOrder
from .types.get_jurisdiction_geo_for_court_request_sort import GetJurisdictionGeoForCourtRequestSort
from .types.get_jurisdictions_geo_request_order import GetJurisdictionsGeoRequestOrder
from .types.get_jurisdictions_geo_request_sort import GetJurisdictionsGeoRequestSort
from .types.get_party_role_groups_request_order import GetPartyRoleGroupsRequestOrder
from .types.get_party_role_groups_request_sort import GetPartyRoleGroupsRequestSort
from .types.get_party_roles_request_order import GetPartyRolesRequestOrder
from .types.get_party_roles_request_sort import GetPartyRolesRequestSort
from pydantic import ValidationError


class RawCourtStandardsApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_areas_of_law(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAreasOfLawRequestSort] = None,
        order: typing.Optional[GetAreasOfLawRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AreaOfLawResponse]:
        """
        The keyword expression targeting the desired area of law.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetAreasOfLawRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetAreasOfLawRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AreaOfLawResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/areaOfLaw",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AreaOfLawResponse,
                    parse_obj_as(
                        type_=AreaOfLawResponse,
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

    def get_area_of_law(
        self, area_of_law_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AreaOfLaw]:
        """
        Retrieve the specified area of law.

        Parameters
        ----------
        area_of_law_id : str
            The areaOfLawId value of the desired area of law.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AreaOfLaw]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/areaOfLaw/{encode_path_param(area_of_law_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AreaOfLaw,
                    parse_obj_as(
                        type_=AreaOfLaw,
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

    def get_attorney_representation_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAttorneyRepresentationTypesRequestSort] = None,
        order: typing.Optional[GetAttorneyRepresentationTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AttorneyRepresentationTypeResponse]:
        """
        Retrieve an attorney representation type using a keyword expression. Keyword expressions should be constructed according to the rules given above.
        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the attorney representation type.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetAttorneyRepresentationTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetAttorneyRepresentationTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AttorneyRepresentationTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/attorneyRepresentationType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AttorneyRepresentationTypeResponse,
                    parse_obj_as(
                        type_=AttorneyRepresentationTypeResponse,
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

    def get_attorney_representation_type(
        self, attorney_representation_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AttorneyRepresentationType]]:
        """
        Retrieve the specified attorney representation type.

        Parameters
        ----------
        attorney_representation_type_id : str
            The attorneyRepresentationTypeId value of the desired attorney representation type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AttorneyRepresentationType]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/attorneyRepresentationType/{encode_path_param(attorney_representation_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AttorneyRepresentationType],
                    parse_obj_as(
                        type_=typing.Optional[AttorneyRepresentationType],
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

    def get_attorney_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAttorneyTypesRequestSort] = None,
        order: typing.Optional[GetAttorneyTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AttorneyTypeResponse]:
        """
        Retrieve an attorney type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the attorney type.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetAttorneyTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetAttorneyTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AttorneyTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/attorneyType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AttorneyTypeResponse,
                    parse_obj_as(
                        type_=AttorneyTypeResponse,
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

    def get_attorney_type(
        self, attorney_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[AttorneyType]]:
        """
        Retrieve a specified attorney type object.

        Parameters
        ----------
        attorney_type_id : str
            The attorneyTypeId value of the desired attorney type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[AttorneyType]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/attorneyType/{encode_path_param(attorney_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AttorneyType],
                    parse_obj_as(
                        type_=typing.Optional[AttorneyType],
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

    def get_cases_class(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCasesClassRequestSort] = None,
        order: typing.Optional[GetCasesClassRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseClassResponse]:
        """
        Retrieve one or more case classes using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired case class.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCasesClassRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCasesClassRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseClassResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/caseClass",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseClassResponse,
                    parse_obj_as(
                        type_=CaseClassResponse,
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

    def get_case_class(
        self, case_class_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CaseClass]:
        """
        Retrieve the specified case class.

        Parameters
        ----------
        case_class_id : str
            The caseClassId value of the desired case class.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseClass]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/caseClass/{encode_path_param(case_class_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseClass,
                    parse_obj_as(
                        type_=CaseClass,
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

    def get_case_relationship_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseRelationshipTypesRequestSort] = None,
        order: typing.Optional[GetCaseRelationshipTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseRelationshipTypeResponse]:
        """
        Retrieve an case relationship type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the case relationship type.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCaseRelationshipTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCaseRelationshipTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseRelationshipTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/caseRelationshipType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseRelationshipTypeResponse,
                    parse_obj_as(
                        type_=CaseRelationshipTypeResponse,
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

    def get_case_relationship_type(
        self, case_relationship_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[CaseRelationshipType]]:
        """
        Retrieve the specified case relationship type.

        Parameters
        ----------
        case_relationship_type_id : str
            The caseRelationshipTypeId value of the desired case relationship type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[CaseRelationshipType]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/caseRelationshipType/{encode_path_param(case_relationship_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseRelationshipType],
                    parse_obj_as(
                        type_=typing.Optional[CaseRelationshipType],
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

    def get_cases_status(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCasesStatusRequestSort] = None,
        order: typing.Optional[GetCasesStatusRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseStatusResponse]:
        """
        Retrieve a case status using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired case status.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCasesStatusRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCasesStatusRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseStatusResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/caseStatus",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseStatusResponse,
                    parse_obj_as(
                        type_=CaseStatusResponse,
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

    def get_case_status(
        self, case_status_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[CaseStatus]]:
        """
        Retrieve the specified case status.

        Parameters
        ----------
        case_status_id : str
            The caseStatusId value of the desired case status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[CaseStatus]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/caseStatus/{encode_path_param(case_status_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseStatus],
                    parse_obj_as(
                        type_=typing.Optional[CaseStatus],
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

    def get_case_status_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseStatusGroupsRequestSort] = None,
        order: typing.Optional[GetCaseStatusGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseStatusGroupResponse]:
        """
        Retrieve a case status group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired case status group.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCaseStatusGroupsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCaseStatusGroupsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseStatusGroupResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/caseStatusGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseStatusGroupResponse,
                    parse_obj_as(
                        type_=CaseStatusGroupResponse,
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

    def get_case_status_group(
        self, case_status_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CaseStatusGroup]:
        """
        Retrieve the specified case status group.

        Parameters
        ----------
        case_status_group_id : str
            The caseStatusGroupId value of the desired case status group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseStatusGroup]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/caseStatusGroup/{encode_path_param(case_status_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseStatusGroup,
                    parse_obj_as(
                        type_=CaseStatusGroup,
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

    def get_case_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseTypesRequestSort] = None,
        order: typing.Optional[GetCaseTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseTypeResponse]:
        """
        Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCaseTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCaseTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/caseType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseTypeResponse,
                    parse_obj_as(
                        type_=CaseTypeResponse,
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

    def get_case_type(
        self, case_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[CaseType]]:
        """
        Retrieve the specified case type.

        Parameters
        ----------
        case_type_id : str
            The caseTypeId value of the desired case type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[CaseType]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/caseType/{encode_path_param(case_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseType],
                    parse_obj_as(
                        type_=typing.Optional[CaseType],
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

    def get_case_type_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseTypeGroupsRequestSort] = None,
        order: typing.Optional[GetCaseTypeGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CaseTypeGroupResponse]:
        """
        Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCaseTypeGroupsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCaseTypeGroupsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseTypeGroupResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/caseTypeGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseTypeGroupResponse,
                    parse_obj_as(
                        type_=CaseTypeGroupResponse,
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

    def get_case_type_group(
        self, case_type_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CaseTypeGroup]:
        """
        Retrieve the specified case type group.

        Parameters
        ----------
        case_type_group_id : str
            caseTypeGroupId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CaseTypeGroup]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/caseTypeGroup/{encode_path_param(case_type_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseTypeGroup,
                    parse_obj_as(
                        type_=CaseTypeGroup,
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

    def get_causes_of_action(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionRequestSort] = None,
        order: typing.Optional[GetCausesOfActionRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CauseOfActionResponse]:
        """
        Retrieve a cause of action using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired cause of action.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCausesOfActionRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCausesOfActionRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CauseOfActionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/causeOfAction",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionResponse,
                    parse_obj_as(
                        type_=CauseOfActionResponse,
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

    def get_cause_of_action(
        self, cause_of_action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[CauseOfAction]]:
        """
        Retrieve the specified cause of action.

        Parameters
        ----------
        cause_of_action_id : str
            The causeOfActionId value of the desired cause of action.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[CauseOfAction]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/causeOfAction/{encode_path_param(cause_of_action_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CauseOfAction],
                    parse_obj_as(
                        type_=typing.Optional[CauseOfAction],
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

    def get_causes_of_action_additional_data(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionAdditionalDataRequestSort] = None,
        order: typing.Optional[GetCausesOfActionAdditionalDataRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CauseOfActionAdditionalDataResponse]:
        """
        Retrieve a cause of action additional data using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired cause of action additional data.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCausesOfActionAdditionalDataRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCausesOfActionAdditionalDataRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CauseOfActionAdditionalDataResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/causeOfActionAdditionalData",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionAdditionalDataResponse,
                    parse_obj_as(
                        type_=CauseOfActionAdditionalDataResponse,
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

    def get_cause_of_action_additional_data(
        self, cause_of_action_additional_data_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CauseOfActionAdditionalData]:
        """
        Retrieve the specified cause of action additional data.

        Parameters
        ----------
        cause_of_action_additional_data_id : str
            The causeOfActionAdditionalDataId value of the desired cause of action additional data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CauseOfActionAdditionalData]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/causeOfActionAdditionalData/{encode_path_param(cause_of_action_additional_data_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionAdditionalData,
                    parse_obj_as(
                        type_=CauseOfActionAdditionalData,
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

    def get_causes_of_action_group(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionGroupRequestSort] = None,
        order: typing.Optional[GetCausesOfActionGroupRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CauseOfActionGroupResponse]:
        """
        Retrieve a cause of action group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired cause of action group.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCausesOfActionGroupRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCausesOfActionGroupRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CauseOfActionGroupResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/causeOfActionGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionGroupResponse,
                    parse_obj_as(
                        type_=CauseOfActionGroupResponse,
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

    def get_cause_of_action_group(
        self, cause_of_action_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CauseOfActionGroup]:
        """
        Retrieve the specified cause of action group.

        Parameters
        ----------
        cause_of_action_group_id : str
            causeOfActionGroupId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CauseOfActionGroup]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/causeOfActionGroup/{encode_path_param(cause_of_action_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionGroup,
                    parse_obj_as(
                        type_=CauseOfActionGroup,
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

    def get_charges(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesRequestSort] = None,
        order: typing.Optional[GetChargesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChargeResponse]:
        """
        Retrieve one or more charges using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChargeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/charge",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeResponse,
                    parse_obj_as(
                        type_=ChargeResponse,
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

    def get_charge(
        self, charge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[Charge]]:
        """
        Retrieve the specified charge.

        Parameters
        ----------
        charge_id : str
            The chargeId value of the desired charge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[Charge]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/charge/{encode_path_param(charge_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Charge],
                    parse_obj_as(
                        type_=typing.Optional[Charge],
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

    def get_charges_additional_data(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesAdditionalDataRequestSort] = None,
        order: typing.Optional[GetChargesAdditionalDataRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChargeAdditionalDataResponse]:
        """
        Retrieve additional information on a charge using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge additional data.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargesAdditionalDataRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargesAdditionalDataRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChargeAdditionalDataResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/chargeAdditionalData",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeAdditionalDataResponse,
                    parse_obj_as(
                        type_=ChargeAdditionalDataResponse,
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

    def get_charge_additional_data(
        self, charge_additional_data_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ChargeAdditionalData]:
        """
        Retrieve the specified charge additional data.

        Parameters
        ----------
        charge_additional_data_id : str
            The chargeAdditionalDataId value of the desired charge additional data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChargeAdditionalData]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/chargeAdditionalData/{encode_path_param(charge_additional_data_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeAdditionalData,
                    parse_obj_as(
                        type_=ChargeAdditionalData,
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

    def get_charges_degree(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesDegreeRequestSort] = None,
        order: typing.Optional[GetChargesDegreeRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChargeDegreeResponse]:
        """
        Retrieve a charge degree using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge degree.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargesDegreeRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargesDegreeRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChargeDegreeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/chargeDegree",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeDegreeResponse,
                    parse_obj_as(
                        type_=ChargeDegreeResponse,
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

    def get_charge_degree(
        self, charge_degree_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[ChargeDegree]]:
        """
        Retrieve the specified charge degree.

        Parameters
        ----------
        charge_degree_id : str
            The chargeDegreeId value of the desired charge degree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[ChargeDegree]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/chargeDegree/{encode_path_param(charge_degree_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ChargeDegree],
                    parse_obj_as(
                        type_=typing.Optional[ChargeDegree],
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

    def get_charge_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargeGroupsRequestSort] = None,
        order: typing.Optional[GetChargeGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChargeGroupResponse]:
        """
        Retrieve one or more charge groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge group.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargeGroupsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargeGroupsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChargeGroupResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/chargeGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeGroupResponse,
                    parse_obj_as(
                        type_=ChargeGroupResponse,
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

    def get_charge_group(
        self, charge_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ChargeGroup]:
        """
        Retrieve the specified charge group.

        Parameters
        ----------
        charge_group_id : str
            The chargeGroupId value of the desired charge group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChargeGroup]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/chargeGroup/{encode_path_param(charge_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeGroup,
                    parse_obj_as(
                        type_=ChargeGroup,
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

    def get_charges_severity(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesSeverityRequestSort] = None,
        order: typing.Optional[GetChargesSeverityRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChargeSeverityResponse]:
        """
        Retrieve a charge severity using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge severity.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargesSeverityRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargesSeverityRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChargeSeverityResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/chargeSeverity",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeSeverityResponse,
                    parse_obj_as(
                        type_=ChargeSeverityResponse,
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

    def get_charge_severity(
        self, charge_severity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[ChargeSeverity]]:
        """
        Retrieve the specified charge severity.

        Parameters
        ----------
        charge_severity_id : str
            The chargeSeverityId value of the desired charge severity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[ChargeSeverity]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/chargeSeverity/{encode_path_param(charge_severity_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ChargeSeverity],
                    parse_obj_as(
                        type_=typing.Optional[ChargeSeverity],
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

    def get_courts(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsRequestSort] = None,
        order: typing.Optional[GetCourtsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CourtResponse]:
        """
        Retrieve information about a specified court or courts.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
                | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/court",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtResponse,
                    parse_obj_as(
                        type_=CourtResponse,
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

    def get_court(
        self, court_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[Court]]:
        """
        Retrieve information about a specified court.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[Court]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/court/{encode_path_param(court_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Court],
                    parse_obj_as(
                        type_=typing.Optional[Court],
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

    def get_appeal_courts_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAppealCourtsForCourtRequestSort] = None,
        order: typing.Optional[GetAppealCourtsForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CourtResponse]:
        """
        Retrieve the appeals courts associated with the specified court.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetAppealCourtsForCourtRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetAppealCourtsForCourtRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/court/{encode_path_param(court_id)}/appealCourts",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtResponse,
                    parse_obj_as(
                        type_=CourtResponse,
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

    def get_court_locations_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtLocationsForCourtRequestSort] = None,
        order: typing.Optional[GetCourtLocationsForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CourtLocationResponse]:
        """
        Retrieve the court locations associated with the specified court.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtLocationsForCourtRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtLocationsForCourtRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtLocationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/court/{encode_path_param(court_id)}/courtLocations",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtLocationResponse,
                    parse_obj_as(
                        type_=CourtLocationResponse,
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

    def get_jurisdiction_geo_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJurisdictionGeoForCourtRequestSort] = None,
        order: typing.Optional[GetJurisdictionGeoForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JurisdictionGeoResponse]:
        """
        Retrieve the jurisdiction geography object for the specified court.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetJurisdictionGeoForCourtRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetJurisdictionGeoForCourtRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JurisdictionGeoResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/court/{encode_path_param(court_id)}/jurisdictionGeo",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JurisdictionGeoResponse,
                    parse_obj_as(
                        type_=JurisdictionGeoResponse,
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

    def get_court_locations(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtLocationsRequestSort] = None,
        order: typing.Optional[GetCourtLocationsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CourtLocationResponse]:
        """
        Retrieve the specified court location or court locations.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtLocationsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtLocationsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtLocationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/courtLocation",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtLocationResponse,
                    parse_obj_as(
                        type_=CourtLocationResponse,
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

    def get_court_location(
        self, court_location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[CourtLocation]]:
        """
        Contains the Court Location Object.

        Parameters
        ----------
        court_location_id : str
            courtLocationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[CourtLocation]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/courtLocation/{encode_path_param(court_location_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CourtLocation],
                    parse_obj_as(
                        type_=typing.Optional[CourtLocation],
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

    def get_courts_for_court_location(
        self,
        court_location_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsForCourtLocationRequestSort] = None,
        order: typing.Optional[GetCourtsForCourtLocationRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CourtResponse]:
        """
        Retrieve the courts associated with the specified court location.

        Parameters
        ----------
        court_location_id : str
            The courtLocationId value of the court location for which courts are to be retrieved.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtsForCourtLocationRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtsForCourtLocationRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/courtLocation/{encode_path_param(court_location_id)}/courts",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtResponse,
                    parse_obj_as(
                        type_=CourtResponse,
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

    def get_courts_service_status(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsServiceStatusRequestSort] = None,
        order: typing.Optional[GetCourtsServiceStatusRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CourtServiceStatusResponse]:
        """
        Retrieve the status of one or more courts using a keyword expression.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtsServiceStatusRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtsServiceStatusRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtServiceStatusResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/courtServiceStatus",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtServiceStatusResponse,
                    parse_obj_as(
                        type_=CourtServiceStatusResponse,
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

    def get_court_service_status(
        self, court_service_status_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[CourtServiceStatus]]:
        """
        Retrieve the court status of the specified court.

        Parameters
        ----------
        court_service_status_id : str
            The courtServiceStatusId value of the desired court.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[CourtServiceStatus]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/courtServiceStatus/{encode_path_param(court_service_status_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CourtServiceStatus],
                    parse_obj_as(
                        type_=typing.Optional[CourtServiceStatus],
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

    def get_court_systems(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtSystemsRequestSort] = None,
        order: typing.Optional[GetCourtSystemsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CourtSystemResponse]:
        """
        Retrieve information about the specified court system or court systems.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
                | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtSystemsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtSystemsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtSystemResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/courtSystem",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtSystemResponse,
                    parse_obj_as(
                        type_=CourtSystemResponse,
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

    def get_court_system(
        self, court_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CourtSystem]:
        """
        Retrieve the specified court system.

        Parameters
        ----------
        court_system_id : str
            The courtSystemId value of the court system to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtSystem]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/courtSystem/{encode_path_param(court_system_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtSystem,
                    parse_obj_as(
                        type_=CourtSystem,
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

    def get_court_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtTypesRequestSort] = None,
        order: typing.Optional[GetCourtTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CourtTypeResponse]:
        """
        Retrieve court types recognized by UniCourt.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
                | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/courtType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtTypeResponse,
                    parse_obj_as(
                        type_=CourtTypeResponse,
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

    def get_court_type(
        self, court_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CourtType]:
        """
        Retrieve the information concerning the specific court type.

        Parameters
        ----------
        court_type_id : str
            The courtTypeId value of the court type to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtType]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/courtType/{encode_path_param(court_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtType,
                    parse_obj_as(
                        type_=CourtType,
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

    def get_judge_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJudgeTypesRequestSort] = None,
        order: typing.Optional[GetJudgeTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JudgeTypeResponse]:
        """
        Retrieve a judge type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the judge type.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetJudgeTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetJudgeTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JudgeTypeResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/judgeType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JudgeTypeResponse,
                    parse_obj_as(
                        type_=JudgeTypeResponse,
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

    def get_judge_type(
        self, judge_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[JudgeType]]:
        """
        Retrieve the specified judge type.

        Parameters
        ----------
        judge_type_id : str
            The judgeTypeId of the desired judge type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[JudgeType]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/judgeType/{encode_path_param(judge_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[JudgeType],
                    parse_obj_as(
                        type_=typing.Optional[JudgeType],
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

    def get_jurisdictions_geo(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJurisdictionsGeoRequestSort] = None,
        order: typing.Optional[GetJurisdictionsGeoRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JurisdictionGeoResponse]:
        """
        Retrieve one or more jurisdiction geographies using a keyword expression.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetJurisdictionsGeoRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetJurisdictionsGeoRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JurisdictionGeoResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/jurisdictionGeo",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JurisdictionGeoResponse,
                    parse_obj_as(
                        type_=JurisdictionGeoResponse,
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

    def get_jurisdiction_geo(
        self, jurisdiction_geo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JurisdictionGeo]:
        """
        Retrieve the specified jurisdiction geography.

        Parameters
        ----------
        jurisdiction_geo_id : str
            The jurisdictionGeoId value of the desired jurisdiction geography.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JurisdictionGeo]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/jurisdictionGeo/{encode_path_param(jurisdiction_geo_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JurisdictionGeo,
                    parse_obj_as(
                        type_=JurisdictionGeo,
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

    def get_courts_for_jurisdiction_geo(
        self,
        jurisdiction_geo_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsForJurisdictionGeoRequestSort] = None,
        order: typing.Optional[GetCourtsForJurisdictionGeoRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CourtResponse]:
        """
        Returns Associated Court for given Jurisdiction Geo.

        Parameters
        ----------
        jurisdiction_geo_id : str
            jurisdictionGeoId

        page_number : typing.Optional[int]
            Page number.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtsForJurisdictionGeoRequestSort]
            Sort field.

        order : typing.Optional[GetCourtsForJurisdictionGeoRequestOrder]
            Sort order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CourtResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/jurisdictionGeo/{encode_path_param(jurisdiction_geo_id)}/courts",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtResponse,
                    parse_obj_as(
                        type_=CourtResponse,
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

    def get_party_roles(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetPartyRolesRequestSort] = None,
        order: typing.Optional[GetPartyRolesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PartyRoleResponse]:
        """
        Retrieve a party role using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired party role.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetPartyRolesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetPartyRolesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PartyRoleResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/partyRole",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PartyRoleResponse,
                    parse_obj_as(
                        type_=PartyRoleResponse,
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

    def get_party_role(
        self, party_role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[PartyRole]]:
        """
        Retrieve the specified party role.

        Parameters
        ----------
        party_role_id : str
            The partyRoleId value of the desired party role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[PartyRole]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/partyRole/{encode_path_param(party_role_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[PartyRole],
                    parse_obj_as(
                        type_=typing.Optional[PartyRole],
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

    def get_party_role_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetPartyRoleGroupsRequestSort] = None,
        order: typing.Optional[GetPartyRoleGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PartyRoleGroupResponse]:
        """
        Retrieve a party role group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired party role group.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetPartyRoleGroupsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetPartyRoleGroupsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PartyRoleGroupResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "masterData/partyRoleGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PartyRoleGroupResponse,
                    parse_obj_as(
                        type_=PartyRoleGroupResponse,
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

    def get_party_role_group(
        self, party_role_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PartyRoleGroup]:
        """
        Retrieve the specified party role group.

        Parameters
        ----------
        party_role_group_id : str
            The partyRoleGroupId value of the desired party role group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PartyRoleGroup]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"masterData/partyRoleGroup/{encode_path_param(party_role_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PartyRoleGroup,
                    parse_obj_as(
                        type_=PartyRoleGroup,
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


class AsyncRawCourtStandardsApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_areas_of_law(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAreasOfLawRequestSort] = None,
        order: typing.Optional[GetAreasOfLawRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AreaOfLawResponse]:
        """
        The keyword expression targeting the desired area of law.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            Retrieve one or more areas of law using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetAreasOfLawRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetAreasOfLawRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AreaOfLawResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/areaOfLaw",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AreaOfLawResponse,
                    parse_obj_as(
                        type_=AreaOfLawResponse,
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

    async def get_area_of_law(
        self, area_of_law_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AreaOfLaw]:
        """
        Retrieve the specified area of law.

        Parameters
        ----------
        area_of_law_id : str
            The areaOfLawId value of the desired area of law.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AreaOfLaw]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/areaOfLaw/{encode_path_param(area_of_law_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AreaOfLaw,
                    parse_obj_as(
                        type_=AreaOfLaw,
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

    async def get_attorney_representation_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAttorneyRepresentationTypesRequestSort] = None,
        order: typing.Optional[GetAttorneyRepresentationTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AttorneyRepresentationTypeResponse]:
        """
        Retrieve an attorney representation type using a keyword expression. Keyword expressions should be constructed according to the rules given above.
        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the attorney representation type.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetAttorneyRepresentationTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetAttorneyRepresentationTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AttorneyRepresentationTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/attorneyRepresentationType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AttorneyRepresentationTypeResponse,
                    parse_obj_as(
                        type_=AttorneyRepresentationTypeResponse,
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

    async def get_attorney_representation_type(
        self, attorney_representation_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AttorneyRepresentationType]]:
        """
        Retrieve the specified attorney representation type.

        Parameters
        ----------
        attorney_representation_type_id : str
            The attorneyRepresentationTypeId value of the desired attorney representation type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AttorneyRepresentationType]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/attorneyRepresentationType/{encode_path_param(attorney_representation_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AttorneyRepresentationType],
                    parse_obj_as(
                        type_=typing.Optional[AttorneyRepresentationType],
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

    async def get_attorney_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAttorneyTypesRequestSort] = None,
        order: typing.Optional[GetAttorneyTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AttorneyTypeResponse]:
        """
        Retrieve an attorney type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the attorney type.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetAttorneyTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetAttorneyTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AttorneyTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/attorneyType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AttorneyTypeResponse,
                    parse_obj_as(
                        type_=AttorneyTypeResponse,
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

    async def get_attorney_type(
        self, attorney_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[AttorneyType]]:
        """
        Retrieve a specified attorney type object.

        Parameters
        ----------
        attorney_type_id : str
            The attorneyTypeId value of the desired attorney type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[AttorneyType]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/attorneyType/{encode_path_param(attorney_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AttorneyType],
                    parse_obj_as(
                        type_=typing.Optional[AttorneyType],
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

    async def get_cases_class(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCasesClassRequestSort] = None,
        order: typing.Optional[GetCasesClassRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseClassResponse]:
        """
        Retrieve one or more case classes using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired case class.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCasesClassRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCasesClassRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseClassResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/caseClass",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseClassResponse,
                    parse_obj_as(
                        type_=CaseClassResponse,
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

    async def get_case_class(
        self, case_class_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CaseClass]:
        """
        Retrieve the specified case class.

        Parameters
        ----------
        case_class_id : str
            The caseClassId value of the desired case class.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseClass]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/caseClass/{encode_path_param(case_class_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseClass,
                    parse_obj_as(
                        type_=CaseClass,
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

    async def get_case_relationship_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseRelationshipTypesRequestSort] = None,
        order: typing.Optional[GetCaseRelationshipTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseRelationshipTypeResponse]:
        """
        Retrieve an case relationship type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the case relationship type.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCaseRelationshipTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCaseRelationshipTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseRelationshipTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/caseRelationshipType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseRelationshipTypeResponse,
                    parse_obj_as(
                        type_=CaseRelationshipTypeResponse,
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

    async def get_case_relationship_type(
        self, case_relationship_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[CaseRelationshipType]]:
        """
        Retrieve the specified case relationship type.

        Parameters
        ----------
        case_relationship_type_id : str
            The caseRelationshipTypeId value of the desired case relationship type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[CaseRelationshipType]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/caseRelationshipType/{encode_path_param(case_relationship_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseRelationshipType],
                    parse_obj_as(
                        type_=typing.Optional[CaseRelationshipType],
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

    async def get_cases_status(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCasesStatusRequestSort] = None,
        order: typing.Optional[GetCasesStatusRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseStatusResponse]:
        """
        Retrieve a case status using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired case status.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCasesStatusRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCasesStatusRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseStatusResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/caseStatus",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseStatusResponse,
                    parse_obj_as(
                        type_=CaseStatusResponse,
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

    async def get_case_status(
        self, case_status_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[CaseStatus]]:
        """
        Retrieve the specified case status.

        Parameters
        ----------
        case_status_id : str
            The caseStatusId value of the desired case status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[CaseStatus]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/caseStatus/{encode_path_param(case_status_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseStatus],
                    parse_obj_as(
                        type_=typing.Optional[CaseStatus],
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

    async def get_case_status_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseStatusGroupsRequestSort] = None,
        order: typing.Optional[GetCaseStatusGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseStatusGroupResponse]:
        """
        Retrieve a case status group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired case status group.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCaseStatusGroupsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCaseStatusGroupsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseStatusGroupResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/caseStatusGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseStatusGroupResponse,
                    parse_obj_as(
                        type_=CaseStatusGroupResponse,
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

    async def get_case_status_group(
        self, case_status_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CaseStatusGroup]:
        """
        Retrieve the specified case status group.

        Parameters
        ----------
        case_status_group_id : str
            The caseStatusGroupId value of the desired case status group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseStatusGroup]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/caseStatusGroup/{encode_path_param(case_status_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseStatusGroup,
                    parse_obj_as(
                        type_=CaseStatusGroup,
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

    async def get_case_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseTypesRequestSort] = None,
        order: typing.Optional[GetCaseTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseTypeResponse]:
        """
        Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCaseTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCaseTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/caseType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseTypeResponse,
                    parse_obj_as(
                        type_=CaseTypeResponse,
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

    async def get_case_type(
        self, case_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[CaseType]]:
        """
        Retrieve the specified case type.

        Parameters
        ----------
        case_type_id : str
            The caseTypeId value of the desired case type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[CaseType]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/caseType/{encode_path_param(case_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CaseType],
                    parse_obj_as(
                        type_=typing.Optional[CaseType],
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

    async def get_case_type_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseTypeGroupsRequestSort] = None,
        order: typing.Optional[GetCaseTypeGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CaseTypeGroupResponse]:
        """
        Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCaseTypeGroupsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCaseTypeGroupsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseTypeGroupResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/caseTypeGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseTypeGroupResponse,
                    parse_obj_as(
                        type_=CaseTypeGroupResponse,
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

    async def get_case_type_group(
        self, case_type_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CaseTypeGroup]:
        """
        Retrieve the specified case type group.

        Parameters
        ----------
        case_type_group_id : str
            caseTypeGroupId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CaseTypeGroup]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/caseTypeGroup/{encode_path_param(case_type_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CaseTypeGroup,
                    parse_obj_as(
                        type_=CaseTypeGroup,
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

    async def get_causes_of_action(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionRequestSort] = None,
        order: typing.Optional[GetCausesOfActionRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CauseOfActionResponse]:
        """
        Retrieve a cause of action using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired cause of action.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCausesOfActionRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCausesOfActionRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CauseOfActionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/causeOfAction",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionResponse,
                    parse_obj_as(
                        type_=CauseOfActionResponse,
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

    async def get_cause_of_action(
        self, cause_of_action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[CauseOfAction]]:
        """
        Retrieve the specified cause of action.

        Parameters
        ----------
        cause_of_action_id : str
            The causeOfActionId value of the desired cause of action.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[CauseOfAction]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/causeOfAction/{encode_path_param(cause_of_action_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CauseOfAction],
                    parse_obj_as(
                        type_=typing.Optional[CauseOfAction],
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

    async def get_causes_of_action_additional_data(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionAdditionalDataRequestSort] = None,
        order: typing.Optional[GetCausesOfActionAdditionalDataRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CauseOfActionAdditionalDataResponse]:
        """
        Retrieve a cause of action additional data using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired cause of action additional data.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCausesOfActionAdditionalDataRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCausesOfActionAdditionalDataRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CauseOfActionAdditionalDataResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/causeOfActionAdditionalData",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionAdditionalDataResponse,
                    parse_obj_as(
                        type_=CauseOfActionAdditionalDataResponse,
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

    async def get_cause_of_action_additional_data(
        self, cause_of_action_additional_data_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CauseOfActionAdditionalData]:
        """
        Retrieve the specified cause of action additional data.

        Parameters
        ----------
        cause_of_action_additional_data_id : str
            The causeOfActionAdditionalDataId value of the desired cause of action additional data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CauseOfActionAdditionalData]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/causeOfActionAdditionalData/{encode_path_param(cause_of_action_additional_data_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionAdditionalData,
                    parse_obj_as(
                        type_=CauseOfActionAdditionalData,
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

    async def get_causes_of_action_group(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionGroupRequestSort] = None,
        order: typing.Optional[GetCausesOfActionGroupRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CauseOfActionGroupResponse]:
        """
        Retrieve a cause of action group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired cause of action group.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCausesOfActionGroupRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCausesOfActionGroupRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CauseOfActionGroupResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/causeOfActionGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionGroupResponse,
                    parse_obj_as(
                        type_=CauseOfActionGroupResponse,
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

    async def get_cause_of_action_group(
        self, cause_of_action_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CauseOfActionGroup]:
        """
        Retrieve the specified cause of action group.

        Parameters
        ----------
        cause_of_action_group_id : str
            causeOfActionGroupId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CauseOfActionGroup]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/causeOfActionGroup/{encode_path_param(cause_of_action_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CauseOfActionGroup,
                    parse_obj_as(
                        type_=CauseOfActionGroup,
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

    async def get_charges(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesRequestSort] = None,
        order: typing.Optional[GetChargesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChargeResponse]:
        """
        Retrieve one or more charges using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChargeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/charge",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeResponse,
                    parse_obj_as(
                        type_=ChargeResponse,
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

    async def get_charge(
        self, charge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[Charge]]:
        """
        Retrieve the specified charge.

        Parameters
        ----------
        charge_id : str
            The chargeId value of the desired charge.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[Charge]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/charge/{encode_path_param(charge_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Charge],
                    parse_obj_as(
                        type_=typing.Optional[Charge],
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

    async def get_charges_additional_data(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesAdditionalDataRequestSort] = None,
        order: typing.Optional[GetChargesAdditionalDataRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChargeAdditionalDataResponse]:
        """
        Retrieve additional information on a charge using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge additional data.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargesAdditionalDataRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargesAdditionalDataRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChargeAdditionalDataResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/chargeAdditionalData",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeAdditionalDataResponse,
                    parse_obj_as(
                        type_=ChargeAdditionalDataResponse,
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

    async def get_charge_additional_data(
        self, charge_additional_data_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChargeAdditionalData]:
        """
        Retrieve the specified charge additional data.

        Parameters
        ----------
        charge_additional_data_id : str
            The chargeAdditionalDataId value of the desired charge additional data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChargeAdditionalData]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/chargeAdditionalData/{encode_path_param(charge_additional_data_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeAdditionalData,
                    parse_obj_as(
                        type_=ChargeAdditionalData,
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

    async def get_charges_degree(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesDegreeRequestSort] = None,
        order: typing.Optional[GetChargesDegreeRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChargeDegreeResponse]:
        """
        Retrieve a charge degree using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge degree.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargesDegreeRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargesDegreeRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChargeDegreeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/chargeDegree",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeDegreeResponse,
                    parse_obj_as(
                        type_=ChargeDegreeResponse,
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

    async def get_charge_degree(
        self, charge_degree_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[ChargeDegree]]:
        """
        Retrieve the specified charge degree.

        Parameters
        ----------
        charge_degree_id : str
            The chargeDegreeId value of the desired charge degree.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[ChargeDegree]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/chargeDegree/{encode_path_param(charge_degree_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ChargeDegree],
                    parse_obj_as(
                        type_=typing.Optional[ChargeDegree],
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

    async def get_charge_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargeGroupsRequestSort] = None,
        order: typing.Optional[GetChargeGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChargeGroupResponse]:
        """
        Retrieve one or more charge groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge group.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargeGroupsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargeGroupsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChargeGroupResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/chargeGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeGroupResponse,
                    parse_obj_as(
                        type_=ChargeGroupResponse,
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

    async def get_charge_group(
        self, charge_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChargeGroup]:
        """
        Retrieve the specified charge group.

        Parameters
        ----------
        charge_group_id : str
            The chargeGroupId value of the desired charge group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChargeGroup]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/chargeGroup/{encode_path_param(charge_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeGroup,
                    parse_obj_as(
                        type_=ChargeGroup,
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

    async def get_charges_severity(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesSeverityRequestSort] = None,
        order: typing.Optional[GetChargesSeverityRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChargeSeverityResponse]:
        """
        Retrieve a charge severity using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired charge severity.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetChargesSeverityRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetChargesSeverityRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChargeSeverityResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/chargeSeverity",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChargeSeverityResponse,
                    parse_obj_as(
                        type_=ChargeSeverityResponse,
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

    async def get_charge_severity(
        self, charge_severity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[ChargeSeverity]]:
        """
        Retrieve the specified charge severity.

        Parameters
        ----------
        charge_severity_id : str
            The chargeSeverityId value of the desired charge severity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[ChargeSeverity]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/chargeSeverity/{encode_path_param(charge_severity_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ChargeSeverity],
                    parse_obj_as(
                        type_=typing.Optional[ChargeSeverity],
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

    async def get_courts(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsRequestSort] = None,
        order: typing.Optional[GetCourtsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CourtResponse]:
        """
        Retrieve information about a specified court or courts.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
                | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression that sets forth the criteria concerning the court or courts to be retrieved. Keyword expressions should be constructed according to the rules shown above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/court",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtResponse,
                    parse_obj_as(
                        type_=CourtResponse,
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

    async def get_court(
        self, court_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[Court]]:
        """
        Retrieve information about a specified court.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[Court]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/court/{encode_path_param(court_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[Court],
                    parse_obj_as(
                        type_=typing.Optional[Court],
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

    async def get_appeal_courts_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAppealCourtsForCourtRequestSort] = None,
        order: typing.Optional[GetAppealCourtsForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CourtResponse]:
        """
        Retrieve the appeals courts associated with the specified court.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetAppealCourtsForCourtRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetAppealCourtsForCourtRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/court/{encode_path_param(court_id)}/appealCourts",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtResponse,
                    parse_obj_as(
                        type_=CourtResponse,
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

    async def get_court_locations_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtLocationsForCourtRequestSort] = None,
        order: typing.Optional[GetCourtLocationsForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CourtLocationResponse]:
        """
        Retrieve the court locations associated with the specified court.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtLocationsForCourtRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtLocationsForCourtRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtLocationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/court/{encode_path_param(court_id)}/courtLocations",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtLocationResponse,
                    parse_obj_as(
                        type_=CourtLocationResponse,
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

    async def get_jurisdiction_geo_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJurisdictionGeoForCourtRequestSort] = None,
        order: typing.Optional[GetJurisdictionGeoForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JurisdictionGeoResponse]:
        """
        Retrieve the jurisdiction geography object for the specified court.

        Parameters
        ----------
        court_id : str
            The courtId value of the target court.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetJurisdictionGeoForCourtRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetJurisdictionGeoForCourtRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JurisdictionGeoResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/court/{encode_path_param(court_id)}/jurisdictionGeo",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JurisdictionGeoResponse,
                    parse_obj_as(
                        type_=JurisdictionGeoResponse,
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

    async def get_court_locations(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtLocationsRequestSort] = None,
        order: typing.Optional[GetCourtLocationsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CourtLocationResponse]:
        """
        Retrieve the specified court location or court locations.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression that sets forth the criteria concerning the court location or court locations to target. Keyword expressions should be constructed according to the rules shown above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtLocationsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtLocationsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtLocationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/courtLocation",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtLocationResponse,
                    parse_obj_as(
                        type_=CourtLocationResponse,
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

    async def get_court_location(
        self, court_location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[CourtLocation]]:
        """
        Contains the Court Location Object.

        Parameters
        ----------
        court_location_id : str
            courtLocationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[CourtLocation]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/courtLocation/{encode_path_param(court_location_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CourtLocation],
                    parse_obj_as(
                        type_=typing.Optional[CourtLocation],
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

    async def get_courts_for_court_location(
        self,
        court_location_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsForCourtLocationRequestSort] = None,
        order: typing.Optional[GetCourtsForCourtLocationRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CourtResponse]:
        """
        Retrieve the courts associated with the specified court location.

        Parameters
        ----------
        court_location_id : str
            The courtLocationId value of the court location for which courts are to be retrieved.

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtsForCourtLocationRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtsForCourtLocationRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/courtLocation/{encode_path_param(court_location_id)}/courts",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtResponse,
                    parse_obj_as(
                        type_=CourtResponse,
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

    async def get_courts_service_status(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsServiceStatusRequestSort] = None,
        order: typing.Optional[GetCourtsServiceStatusRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CourtServiceStatusResponse]:
        """
        Retrieve the status of one or more courts using a keyword expression.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired court. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtsServiceStatusRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtsServiceStatusRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtServiceStatusResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/courtServiceStatus",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtServiceStatusResponse,
                    parse_obj_as(
                        type_=CourtServiceStatusResponse,
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

    async def get_court_service_status(
        self, court_service_status_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[CourtServiceStatus]]:
        """
        Retrieve the court status of the specified court.

        Parameters
        ----------
        court_service_status_id : str
            The courtServiceStatusId value of the desired court.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[CourtServiceStatus]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/courtServiceStatus/{encode_path_param(court_service_status_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CourtServiceStatus],
                    parse_obj_as(
                        type_=typing.Optional[CourtServiceStatus],
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

    async def get_court_systems(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtSystemsRequestSort] = None,
        order: typing.Optional[GetCourtSystemsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CourtSystemResponse]:
        """
        Retrieve information about the specified court system or court systems.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
                | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression that sets forth the criteria concerning the court system or court systems. Keyword expressions should be constructed according to the rules shown above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtSystemsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtSystemsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtSystemResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/courtSystem",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtSystemResponse,
                    parse_obj_as(
                        type_=CourtSystemResponse,
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

    async def get_court_system(
        self, court_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CourtSystem]:
        """
        Retrieve the specified court system.

        Parameters
        ----------
        court_system_id : str
            The courtSystemId value of the court system to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtSystem]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/courtSystem/{encode_path_param(court_system_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtSystem,
                    parse_obj_as(
                        type_=CourtSystem,
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

    async def get_court_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtTypesRequestSort] = None,
        order: typing.Optional[GetCourtTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CourtTypeResponse]:
        """
        Retrieve court types recognized by UniCourt.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
                | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression that sets forth the criteria concerning the court type or court types. Keyword expressions should be constructed according to the rules shown above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetCourtTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/courtType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtTypeResponse,
                    parse_obj_as(
                        type_=CourtTypeResponse,
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

    async def get_court_type(
        self, court_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CourtType]:
        """
        Retrieve the information concerning the specific court type.

        Parameters
        ----------
        court_type_id : str
            The courtTypeId value of the court type to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtType]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/courtType/{encode_path_param(court_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtType,
                    parse_obj_as(
                        type_=CourtType,
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

    async def get_judge_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJudgeTypesRequestSort] = None,
        order: typing.Optional[GetJudgeTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JudgeTypeResponse]:
        """
        Retrieve a judge type using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the judge type.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetJudgeTypesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetJudgeTypesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JudgeTypeResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/judgeType",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JudgeTypeResponse,
                    parse_obj_as(
                        type_=JudgeTypeResponse,
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

    async def get_judge_type(
        self, judge_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[JudgeType]]:
        """
        Retrieve the specified judge type.

        Parameters
        ----------
        judge_type_id : str
            The judgeTypeId of the desired judge type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[JudgeType]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/judgeType/{encode_path_param(judge_type_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[JudgeType],
                    parse_obj_as(
                        type_=typing.Optional[JudgeType],
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

    async def get_jurisdictions_geo(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJurisdictionsGeoRequestSort] = None,
        order: typing.Optional[GetJurisdictionsGeoRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JurisdictionGeoResponse]:
        """
        Retrieve one or more jurisdiction geographies using a keyword expression.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired jurisdiction geography. Keyword expressions should be constructed according to the rules given above.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetJurisdictionsGeoRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetJurisdictionsGeoRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JurisdictionGeoResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/jurisdictionGeo",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JurisdictionGeoResponse,
                    parse_obj_as(
                        type_=JurisdictionGeoResponse,
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

    async def get_jurisdiction_geo(
        self, jurisdiction_geo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JurisdictionGeo]:
        """
        Retrieve the specified jurisdiction geography.

        Parameters
        ----------
        jurisdiction_geo_id : str
            The jurisdictionGeoId value of the desired jurisdiction geography.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JurisdictionGeo]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/jurisdictionGeo/{encode_path_param(jurisdiction_geo_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JurisdictionGeo,
                    parse_obj_as(
                        type_=JurisdictionGeo,
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

    async def get_courts_for_jurisdiction_geo(
        self,
        jurisdiction_geo_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsForJurisdictionGeoRequestSort] = None,
        order: typing.Optional[GetCourtsForJurisdictionGeoRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CourtResponse]:
        """
        Returns Associated Court for given Jurisdiction Geo.

        Parameters
        ----------
        jurisdiction_geo_id : str
            jurisdictionGeoId

        page_number : typing.Optional[int]
            Page number.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetCourtsForJurisdictionGeoRequestSort]
            Sort field.

        order : typing.Optional[GetCourtsForJurisdictionGeoRequestOrder]
            Sort order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CourtResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/jurisdictionGeo/{encode_path_param(jurisdiction_geo_id)}/courts",
            method="GET",
            params={
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CourtResponse,
                    parse_obj_as(
                        type_=CourtResponse,
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

    async def get_party_roles(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetPartyRolesRequestSort] = None,
        order: typing.Optional[GetPartyRolesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PartyRoleResponse]:
        """
        Retrieve a party role using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired party role.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetPartyRolesRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetPartyRolesRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PartyRoleResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/partyRole",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PartyRoleResponse,
                    parse_obj_as(
                        type_=PartyRoleResponse,
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

    async def get_party_role(
        self, party_role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[PartyRole]]:
        """
        Retrieve the specified party role.

        Parameters
        ----------
        party_role_id : str
            The partyRoleId value of the desired party role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[PartyRole]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/partyRole/{encode_path_param(party_role_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[PartyRole],
                    parse_obj_as(
                        type_=typing.Optional[PartyRole],
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

    async def get_party_role_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetPartyRoleGroupsRequestSort] = None,
        order: typing.Optional[GetPartyRoleGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PartyRoleGroupResponse]:
        """
        Retrieve a party role group using a keyword expression. Keyword expressions should be constructed according to the rules given above.

        ## Logical Operators
        | Connector | Description  | Example |
        | ------| ------|------|
        | **AND** |Find data containing all connected terms.|**google AND facebook**|
        | **OR**  |Find data containing any connected term.| **order OR decision**|
        | **NOT** |Exclude data.| **google NOT apple**.|
        | **“[phrase]”** |Find an exact phrase.| **"Google Inc”** |
        | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|

        ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject

        Parameters
        ----------
        q : typing.Optional[str]
            The keyword expression targeting the desired party role group.</a>

        page_number : typing.Optional[int]
            The page number of the results to be retrieved.
            - minimum: 1
            - maximum: 100

        sort : typing.Optional[GetPartyRoleGroupsRequestSort]
            The field according to which search results are to be sorted.

        order : typing.Optional[GetPartyRoleGroupsRequestOrder]
            Whether search results are to be shown in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PartyRoleGroupResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "masterData/partyRoleGroup",
            method="GET",
            params={
                "q": q,
                "pageNumber": page_number,
                "sort": sort,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PartyRoleGroupResponse,
                    parse_obj_as(
                        type_=PartyRoleGroupResponse,
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

    async def get_party_role_group(
        self, party_role_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PartyRoleGroup]:
        """
        Retrieve the specified party role group.

        Parameters
        ----------
        party_role_group_id : str
            The partyRoleGroupId value of the desired party role group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PartyRoleGroup]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"masterData/partyRoleGroup/{encode_path_param(party_role_group_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PartyRoleGroup,
                    parse_obj_as(
                        type_=PartyRoleGroup,
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
