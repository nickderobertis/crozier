

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from ..types.judge_type import JudgeType
from ..types.judge_type_response import JudgeTypeResponse
from ..types.jurisdiction_geo import JurisdictionGeo
from ..types.jurisdiction_geo_response import JurisdictionGeoResponse
from ..types.party_role import PartyRole
from ..types.party_role_group import PartyRoleGroup
from ..types.party_role_group_response import PartyRoleGroupResponse
from ..types.party_role_response import PartyRoleResponse
from .raw_client import AsyncRawCourtStandardsApiClient, RawCourtStandardsApiClient
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


class CourtStandardsApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCourtStandardsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCourtStandardsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCourtStandardsApiClient
        """
        return self._raw_client

    def get_areas_of_law(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAreasOfLawRequestSort] = None,
        order: typing.Optional[GetAreasOfLawRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AreaOfLawResponse:
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
        AreaOfLawResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_areas_of_law(
            q='areaOfLawId: "AOFLGAd9Ah5qkTRNw9"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_areas_of_law(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_area_of_law(
        self, area_of_law_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AreaOfLaw:
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
        AreaOfLaw
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_area_of_law(
            area_of_law_id="AOFLGAd9Ah5qkTRNw9",
        )
        """
        _response = self._raw_client.get_area_of_law(area_of_law_id, request_options=request_options)
        return _response.data

    def get_attorney_representation_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAttorneyRepresentationTypesRequestSort] = None,
        order: typing.Optional[GetAttorneyRepresentationTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttorneyRepresentationTypeResponse:
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
        AttorneyRepresentationTypeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_attorney_representation_types(
            q='attorneyRepresentationTypeId: "ATRPYgPMGJufoCsR6Q"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_attorney_representation_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_attorney_representation_type(
        self, attorney_representation_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AttorneyRepresentationType]:
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
        typing.Optional[AttorneyRepresentationType]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_attorney_representation_type(
            attorney_representation_type_id="ATRPYgPMGJufoCsR6Q",
        )
        """
        _response = self._raw_client.get_attorney_representation_type(
            attorney_representation_type_id, request_options=request_options
        )
        return _response.data

    def get_attorney_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAttorneyTypesRequestSort] = None,
        order: typing.Optional[GetAttorneyTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttorneyTypeResponse:
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
        AttorneyTypeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_attorney_types(
            q='attorneyTypeId:"ATYPWXtARwvzu5HLcf"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_attorney_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_attorney_type(
        self, attorney_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AttorneyType]:
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
        typing.Optional[AttorneyType]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_attorney_type(
            attorney_type_id="ATYPWXtARwvzu5HLcf",
        )
        """
        _response = self._raw_client.get_attorney_type(attorney_type_id, request_options=request_options)
        return _response.data

    def get_cases_class(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCasesClassRequestSort] = None,
        order: typing.Optional[GetCasesClassRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseClassResponse:
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
        CaseClassResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_cases_class(
            q='caseClassId:"CSCLNjbKTN7Yfo2wdb"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_cases_class(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_case_class(
        self, case_class_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseClass:
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
        CaseClass
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_class(
            case_class_id="CSCLNjbKTN7Yfo2wdb",
        )
        """
        _response = self._raw_client.get_case_class(case_class_id, request_options=request_options)
        return _response.data

    def get_case_relationship_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseRelationshipTypesRequestSort] = None,
        order: typing.Optional[GetCaseRelationshipTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseRelationshipTypeResponse:
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
        CaseRelationshipTypeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_relationship_types(
            q='caseRelationshipTypeId: "CRTPgkmnzpiBXstT3s"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_case_relationship_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_case_relationship_type(
        self, case_relationship_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CaseRelationshipType]:
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
        typing.Optional[CaseRelationshipType]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_relationship_type(
            case_relationship_type_id="CRTPgkmnzpiBXstT3s",
        )
        """
        _response = self._raw_client.get_case_relationship_type(
            case_relationship_type_id, request_options=request_options
        )
        return _response.data

    def get_cases_status(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCasesStatusRequestSort] = None,
        order: typing.Optional[GetCasesStatusRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseStatusResponse:
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
        CaseStatusResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_cases_status(
            q='caseStatusId: "CSSTBtqf3R2LYFt4j4"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_cases_status(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_case_status(
        self, case_status_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CaseStatus]:
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
        typing.Optional[CaseStatus]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_status(
            case_status_id="CSSTBtqf3R2LYFt4j4",
        )
        """
        _response = self._raw_client.get_case_status(case_status_id, request_options=request_options)
        return _response.data

    def get_case_status_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseStatusGroupsRequestSort] = None,
        order: typing.Optional[GetCaseStatusGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseStatusGroupResponse:
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
        CaseStatusGroupResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_status_groups(
            q='caseStatusGroupId:"CSSG6ERqyFdydo52WK"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_case_status_groups(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_case_status_group(
        self, case_status_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseStatusGroup:
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
        CaseStatusGroup
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_status_group(
            case_status_group_id="CSSG6ERqyFdydo52WK",
        )
        """
        _response = self._raw_client.get_case_status_group(case_status_group_id, request_options=request_options)
        return _response.data

    def get_case_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseTypesRequestSort] = None,
        order: typing.Optional[GetCaseTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseTypeResponse:
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
        CaseTypeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_types(
            q='caseTypeId: "CTYPoLU7sWaGjWtkBx"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_case_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_case_type(
        self, case_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CaseType]:
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
        typing.Optional[CaseType]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_type(
            case_type_id="CTYPoLU7sWaGjWtkBx",
        )
        """
        _response = self._raw_client.get_case_type(case_type_id, request_options=request_options)
        return _response.data

    def get_case_type_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseTypeGroupsRequestSort] = None,
        order: typing.Optional[GetCaseTypeGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseTypeGroupResponse:
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
        CaseTypeGroupResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_type_groups(
            q='caseTypeGroupId: "CTYGSpWaVityBQndsv"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_case_type_groups(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_case_type_group(
        self, case_type_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseTypeGroup:
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
        CaseTypeGroup
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_case_type_group(
            case_type_group_id="CTYGSpWaVityBQndsv",
        )
        """
        _response = self._raw_client.get_case_type_group(case_type_group_id, request_options=request_options)
        return _response.data

    def get_causes_of_action(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionRequestSort] = None,
        order: typing.Optional[GetCausesOfActionRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CauseOfActionResponse:
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
        CauseOfActionResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_causes_of_action(
            q='causeOfActionId:"CATNiHoKn66p3bkcNs"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_causes_of_action(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_cause_of_action(
        self, cause_of_action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CauseOfAction]:
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
        typing.Optional[CauseOfAction]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_cause_of_action(
            cause_of_action_id="CATNoLU7sWaGjWtkBx",
        )
        """
        _response = self._raw_client.get_cause_of_action(cause_of_action_id, request_options=request_options)
        return _response.data

    def get_causes_of_action_additional_data(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionAdditionalDataRequestSort] = None,
        order: typing.Optional[GetCausesOfActionAdditionalDataRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CauseOfActionAdditionalDataResponse:
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
        CauseOfActionAdditionalDataResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_causes_of_action_additional_data(
            q='causeOfActionAdditionalDataId:"CAADiHoKn66p3bkcNs"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_causes_of_action_additional_data(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_cause_of_action_additional_data(
        self, cause_of_action_additional_data_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CauseOfActionAdditionalData:
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
        CauseOfActionAdditionalData
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_cause_of_action_additional_data(
            cause_of_action_additional_data_id="CAADoLU7sWaGjWtkBx",
        )
        """
        _response = self._raw_client.get_cause_of_action_additional_data(
            cause_of_action_additional_data_id, request_options=request_options
        )
        return _response.data

    def get_causes_of_action_group(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionGroupRequestSort] = None,
        order: typing.Optional[GetCausesOfActionGroupRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CauseOfActionGroupResponse:
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
        CauseOfActionGroupResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_causes_of_action_group(
            q='causeOfActionGroupId:"CAGPiHoKn66p3bkcNs"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_causes_of_action_group(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_cause_of_action_group(
        self, cause_of_action_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CauseOfActionGroup:
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
        CauseOfActionGroup
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_cause_of_action_group(
            cause_of_action_group_id="CAGPoLU7sWaGjWtkBx",
        )
        """
        _response = self._raw_client.get_cause_of_action_group(
            cause_of_action_group_id, request_options=request_options
        )
        return _response.data

    def get_charges(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesRequestSort] = None,
        order: typing.Optional[GetChargesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeResponse:
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
        ChargeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charges(
            q='chargeId:"CHRGoLU7sWaGjWtkBx"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_charges(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_charge(
        self, charge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Charge]:
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
        typing.Optional[Charge]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charge(
            charge_id="CHRGiHoKn66p3bkcNs",
        )
        """
        _response = self._raw_client.get_charge(charge_id, request_options=request_options)
        return _response.data

    def get_charges_additional_data(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesAdditionalDataRequestSort] = None,
        order: typing.Optional[GetChargesAdditionalDataRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeAdditionalDataResponse:
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
        ChargeAdditionalDataResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charges_additional_data(
            q='chargeAdditionalDataId:"CHADoLU7sWaGjWtkBx"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_charges_additional_data(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_charge_additional_data(
        self, charge_additional_data_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChargeAdditionalData:
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
        ChargeAdditionalData
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charge_additional_data(
            charge_additional_data_id="CHADiHoKn66p3bkcNs",
        )
        """
        _response = self._raw_client.get_charge_additional_data(
            charge_additional_data_id, request_options=request_options
        )
        return _response.data

    def get_charges_degree(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesDegreeRequestSort] = None,
        order: typing.Optional[GetChargesDegreeRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeDegreeResponse:
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
        ChargeDegreeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charges_degree(
            q='chargeDegreeId:"CHDGiHoKn66p3bkcNs"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_charges_degree(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_charge_degree(
        self, charge_degree_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ChargeDegree]:
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
        typing.Optional[ChargeDegree]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charge_degree(
            charge_degree_id="CHDGiHoKn66p3bkcNs",
        )
        """
        _response = self._raw_client.get_charge_degree(charge_degree_id, request_options=request_options)
        return _response.data

    def get_charge_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargeGroupsRequestSort] = None,
        order: typing.Optional[GetChargeGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeGroupResponse:
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
        ChargeGroupResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charge_groups(
            q='chargeGroupId:"CHRGoLU7sWaGjWtkBx"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_charge_groups(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_charge_group(
        self, charge_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChargeGroup:
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
        ChargeGroup
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charge_group(
            charge_group_id="CHGPiHoKn66p3bkcNs",
        )
        """
        _response = self._raw_client.get_charge_group(charge_group_id, request_options=request_options)
        return _response.data

    def get_charges_severity(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesSeverityRequestSort] = None,
        order: typing.Optional[GetChargesSeverityRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeSeverityResponse:
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
        ChargeSeverityResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charges_severity(
            q='chargeSeverityId:"CHSEiHoKn66p3bkcNs"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_charges_severity(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_charge_severity(
        self, charge_severity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ChargeSeverity]:
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
        typing.Optional[ChargeSeverity]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_charge_severity(
            charge_severity_id="CHSEiHoKn66p3bkcNs",
        )
        """
        _response = self._raw_client.get_charge_severity(charge_severity_id, request_options=request_options)
        return _response.data

    def get_courts(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsRequestSort] = None,
        order: typing.Optional[GetCourtsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtResponse:
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
        CourtResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_courts(
            q='courtId:"CORThSxcef8eGUSkuC"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_courts(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_court(
        self, court_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Court]:
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
        typing.Optional[Court]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_court(
            court_id="CORThSxcef8eGUSkuC",
        )
        """
        _response = self._raw_client.get_court(court_id, request_options=request_options)
        return _response.data

    def get_appeal_courts_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAppealCourtsForCourtRequestSort] = None,
        order: typing.Optional[GetAppealCourtsForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtResponse:
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
        CourtResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_appeal_courts_for_court(
            court_id="CORThSxcef8eGUSkuC",
            page_number=1,
        )
        """
        _response = self._raw_client.get_appeal_courts_for_court(
            court_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_court_locations_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtLocationsForCourtRequestSort] = None,
        order: typing.Optional[GetCourtLocationsForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtLocationResponse:
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
        CourtLocationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_court_locations_for_court(
            court_id="CORThSxcef8eGUSkuC",
            page_number=1,
        )
        """
        _response = self._raw_client.get_court_locations_for_court(
            court_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_jurisdiction_geo_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJurisdictionGeoForCourtRequestSort] = None,
        order: typing.Optional[GetJurisdictionGeoForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JurisdictionGeoResponse:
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
        JurisdictionGeoResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_jurisdiction_geo_for_court(
            court_id="CORThSxcef8eGUSkuC",
            page_number=1,
        )
        """
        _response = self._raw_client.get_jurisdiction_geo_for_court(
            court_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_court_locations(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtLocationsRequestSort] = None,
        order: typing.Optional[GetCourtLocationsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtLocationResponse:
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
        CourtLocationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_court_locations(
            q='courtLocationId:"COLO9g3fhYM4bmxveA"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_court_locations(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_court_location(
        self, court_location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CourtLocation]:
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
        typing.Optional[CourtLocation]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_court_location(
            court_location_id="COLOV75AKgqMqnfVhM",
        )
        """
        _response = self._raw_client.get_court_location(court_location_id, request_options=request_options)
        return _response.data

    def get_courts_for_court_location(
        self,
        court_location_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsForCourtLocationRequestSort] = None,
        order: typing.Optional[GetCourtsForCourtLocationRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtResponse:
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
        CourtResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_courts_for_court_location(
            court_location_id="COLOV75AKgqMqnfVhM",
            page_number=1,
        )
        """
        _response = self._raw_client.get_courts_for_court_location(
            court_location_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_courts_service_status(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsServiceStatusRequestSort] = None,
        order: typing.Optional[GetCourtsServiceStatusRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtServiceStatusResponse:
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
        CourtServiceStatusResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_courts_service_status(
            q='courtServiceStatusId: "CTSSf45fd1bd792e97"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_courts_service_status(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_court_service_status(
        self, court_service_status_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CourtServiceStatus]:
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
        typing.Optional[CourtServiceStatus]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_court_service_status(
            court_service_status_id="CTSSf45fd1bd792e97",
        )
        """
        _response = self._raw_client.get_court_service_status(court_service_status_id, request_options=request_options)
        return _response.data

    def get_court_systems(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtSystemsRequestSort] = None,
        order: typing.Optional[GetCourtSystemsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtSystemResponse:
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
        CourtSystemResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_court_systems(
            q='courtSystemId:"COSY4vuCtGQeAmdDdN"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_court_systems(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_court_system(
        self, court_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourtSystem:
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
        CourtSystem
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_court_system(
            court_system_id="COSY4vuCtGQeAmdDdN",
        )
        """
        _response = self._raw_client.get_court_system(court_system_id, request_options=request_options)
        return _response.data

    def get_court_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtTypesRequestSort] = None,
        order: typing.Optional[GetCourtTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtTypeResponse:
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
        CourtTypeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_court_types(
            q='courtTypeId:"COTPm8jjc2PAydpFhq"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_court_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_court_type(
        self, court_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourtType:
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
        CourtType
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_court_type(
            court_type_id="COTPm8jjc2PAydpFhq",
        )
        """
        _response = self._raw_client.get_court_type(court_type_id, request_options=request_options)
        return _response.data

    def get_judge_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJudgeTypesRequestSort] = None,
        order: typing.Optional[GetJudgeTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JudgeTypeResponse:
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
        JudgeTypeResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_judge_types(
            q='judgeTypeId: "JGTPkwrfzkDJUvxpN9"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_judge_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_judge_type(
        self, judge_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[JudgeType]:
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
        typing.Optional[JudgeType]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_judge_type(
            judge_type_id="JGTPkwrfzkDJUvxpN9",
        )
        """
        _response = self._raw_client.get_judge_type(judge_type_id, request_options=request_options)
        return _response.data

    def get_jurisdictions_geo(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJurisdictionsGeoRequestSort] = None,
        order: typing.Optional[GetJurisdictionsGeoRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JurisdictionGeoResponse:
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
        JurisdictionGeoResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_jurisdictions_geo(
            q='jurisdictionGeoId:"JUGO8s7HvM84dLvVMu"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_jurisdictions_geo(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_jurisdiction_geo(
        self, jurisdiction_geo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JurisdictionGeo:
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
        JurisdictionGeo
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_jurisdiction_geo(
            jurisdiction_geo_id="JUGO8s7HvM84dLvVMu",
        )
        """
        _response = self._raw_client.get_jurisdiction_geo(jurisdiction_geo_id, request_options=request_options)
        return _response.data

    def get_courts_for_jurisdiction_geo(
        self,
        jurisdiction_geo_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsForJurisdictionGeoRequestSort] = None,
        order: typing.Optional[GetCourtsForJurisdictionGeoRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtResponse:
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
        CourtResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_courts_for_jurisdiction_geo(
            jurisdiction_geo_id="JUGO8s7HvM84dLvVMu",
            page_number=1,
        )
        """
        _response = self._raw_client.get_courts_for_jurisdiction_geo(
            jurisdiction_geo_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_party_roles(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetPartyRolesRequestSort] = None,
        order: typing.Optional[GetPartyRolesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartyRoleResponse:
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
        PartyRoleResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_party_roles(
            q='partyRoleId: "PTYRVRgMKueGmhnxRN"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_party_roles(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_party_role(
        self, party_role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[PartyRole]:
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
        typing.Optional[PartyRole]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_party_role(
            party_role_id="PTYRVRgMKueGmhnxRN",
        )
        """
        _response = self._raw_client.get_party_role(party_role_id, request_options=request_options)
        return _response.data

    def get_party_role_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetPartyRoleGroupsRequestSort] = None,
        order: typing.Optional[GetPartyRoleGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartyRoleGroupResponse:
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
        PartyRoleGroupResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_party_role_groups(
            q='partyRoleGroupId: "PTYGBnjxbx6tKNfVEP"',
            page_number=1,
        )
        """
        _response = self._raw_client.get_party_role_groups(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    def get_party_role_group(
        self, party_role_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PartyRoleGroup:
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
        PartyRoleGroup
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.court_standards_api.get_party_role_group(
            party_role_group_id="PTYGBnjxbx6tKNfVEP",
        )
        """
        _response = self._raw_client.get_party_role_group(party_role_group_id, request_options=request_options)
        return _response.data


class AsyncCourtStandardsApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCourtStandardsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCourtStandardsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCourtStandardsApiClient
        """
        return self._raw_client

    async def get_areas_of_law(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAreasOfLawRequestSort] = None,
        order: typing.Optional[GetAreasOfLawRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AreaOfLawResponse:
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
        AreaOfLawResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_areas_of_law(
                q='areaOfLawId: "AOFLGAd9Ah5qkTRNw9"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_areas_of_law(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_area_of_law(
        self, area_of_law_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AreaOfLaw:
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
        AreaOfLaw
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_area_of_law(
                area_of_law_id="AOFLGAd9Ah5qkTRNw9",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_area_of_law(area_of_law_id, request_options=request_options)
        return _response.data

    async def get_attorney_representation_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAttorneyRepresentationTypesRequestSort] = None,
        order: typing.Optional[GetAttorneyRepresentationTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttorneyRepresentationTypeResponse:
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
        AttorneyRepresentationTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_attorney_representation_types(
                q='attorneyRepresentationTypeId: "ATRPYgPMGJufoCsR6Q"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attorney_representation_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_attorney_representation_type(
        self, attorney_representation_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AttorneyRepresentationType]:
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
        typing.Optional[AttorneyRepresentationType]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_attorney_representation_type(
                attorney_representation_type_id="ATRPYgPMGJufoCsR6Q",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attorney_representation_type(
            attorney_representation_type_id, request_options=request_options
        )
        return _response.data

    async def get_attorney_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAttorneyTypesRequestSort] = None,
        order: typing.Optional[GetAttorneyTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AttorneyTypeResponse:
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
        AttorneyTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_attorney_types(
                q='attorneyTypeId:"ATYPWXtARwvzu5HLcf"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attorney_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_attorney_type(
        self, attorney_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AttorneyType]:
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
        typing.Optional[AttorneyType]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_attorney_type(
                attorney_type_id="ATYPWXtARwvzu5HLcf",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_attorney_type(attorney_type_id, request_options=request_options)
        return _response.data

    async def get_cases_class(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCasesClassRequestSort] = None,
        order: typing.Optional[GetCasesClassRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseClassResponse:
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
        CaseClassResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_cases_class(
                q='caseClassId:"CSCLNjbKTN7Yfo2wdb"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cases_class(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_case_class(
        self, case_class_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseClass:
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
        CaseClass
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_class(
                case_class_id="CSCLNjbKTN7Yfo2wdb",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_class(case_class_id, request_options=request_options)
        return _response.data

    async def get_case_relationship_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseRelationshipTypesRequestSort] = None,
        order: typing.Optional[GetCaseRelationshipTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseRelationshipTypeResponse:
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
        CaseRelationshipTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_relationship_types(
                q='caseRelationshipTypeId: "CRTPgkmnzpiBXstT3s"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_relationship_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_case_relationship_type(
        self, case_relationship_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CaseRelationshipType]:
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
        typing.Optional[CaseRelationshipType]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_relationship_type(
                case_relationship_type_id="CRTPgkmnzpiBXstT3s",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_relationship_type(
            case_relationship_type_id, request_options=request_options
        )
        return _response.data

    async def get_cases_status(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCasesStatusRequestSort] = None,
        order: typing.Optional[GetCasesStatusRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseStatusResponse:
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
        CaseStatusResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_cases_status(
                q='caseStatusId: "CSSTBtqf3R2LYFt4j4"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cases_status(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_case_status(
        self, case_status_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CaseStatus]:
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
        typing.Optional[CaseStatus]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_status(
                case_status_id="CSSTBtqf3R2LYFt4j4",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_status(case_status_id, request_options=request_options)
        return _response.data

    async def get_case_status_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseStatusGroupsRequestSort] = None,
        order: typing.Optional[GetCaseStatusGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseStatusGroupResponse:
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
        CaseStatusGroupResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_status_groups(
                q='caseStatusGroupId:"CSSG6ERqyFdydo52WK"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_status_groups(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_case_status_group(
        self, case_status_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseStatusGroup:
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
        CaseStatusGroup
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_status_group(
                case_status_group_id="CSSG6ERqyFdydo52WK",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_status_group(case_status_group_id, request_options=request_options)
        return _response.data

    async def get_case_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseTypesRequestSort] = None,
        order: typing.Optional[GetCaseTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseTypeResponse:
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
        CaseTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_types(
                q='caseTypeId: "CTYPoLU7sWaGjWtkBx"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_case_type(
        self, case_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CaseType]:
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
        typing.Optional[CaseType]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_type(
                case_type_id="CTYPoLU7sWaGjWtkBx",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_type(case_type_id, request_options=request_options)
        return _response.data

    async def get_case_type_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCaseTypeGroupsRequestSort] = None,
        order: typing.Optional[GetCaseTypeGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CaseTypeGroupResponse:
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
        CaseTypeGroupResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_type_groups(
                q='caseTypeGroupId: "CTYGSpWaVityBQndsv"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_type_groups(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_case_type_group(
        self, case_type_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CaseTypeGroup:
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
        CaseTypeGroup
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_case_type_group(
                case_type_group_id="CTYGSpWaVityBQndsv",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_case_type_group(case_type_group_id, request_options=request_options)
        return _response.data

    async def get_causes_of_action(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionRequestSort] = None,
        order: typing.Optional[GetCausesOfActionRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CauseOfActionResponse:
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
        CauseOfActionResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_causes_of_action(
                q='causeOfActionId:"CATNiHoKn66p3bkcNs"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_causes_of_action(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_cause_of_action(
        self, cause_of_action_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CauseOfAction]:
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
        typing.Optional[CauseOfAction]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_cause_of_action(
                cause_of_action_id="CATNoLU7sWaGjWtkBx",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cause_of_action(cause_of_action_id, request_options=request_options)
        return _response.data

    async def get_causes_of_action_additional_data(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionAdditionalDataRequestSort] = None,
        order: typing.Optional[GetCausesOfActionAdditionalDataRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CauseOfActionAdditionalDataResponse:
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
        CauseOfActionAdditionalDataResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_causes_of_action_additional_data(
                q='causeOfActionAdditionalDataId:"CAADiHoKn66p3bkcNs"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_causes_of_action_additional_data(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_cause_of_action_additional_data(
        self, cause_of_action_additional_data_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CauseOfActionAdditionalData:
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
        CauseOfActionAdditionalData
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_cause_of_action_additional_data(
                cause_of_action_additional_data_id="CAADoLU7sWaGjWtkBx",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cause_of_action_additional_data(
            cause_of_action_additional_data_id, request_options=request_options
        )
        return _response.data

    async def get_causes_of_action_group(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCausesOfActionGroupRequestSort] = None,
        order: typing.Optional[GetCausesOfActionGroupRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CauseOfActionGroupResponse:
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
        CauseOfActionGroupResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_causes_of_action_group(
                q='causeOfActionGroupId:"CAGPiHoKn66p3bkcNs"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_causes_of_action_group(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_cause_of_action_group(
        self, cause_of_action_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CauseOfActionGroup:
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
        CauseOfActionGroup
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_cause_of_action_group(
                cause_of_action_group_id="CAGPoLU7sWaGjWtkBx",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cause_of_action_group(
            cause_of_action_group_id, request_options=request_options
        )
        return _response.data

    async def get_charges(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesRequestSort] = None,
        order: typing.Optional[GetChargesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeResponse:
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
        ChargeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charges(
                q='chargeId:"CHRGoLU7sWaGjWtkBx"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charges(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_charge(
        self, charge_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Charge]:
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
        typing.Optional[Charge]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charge(
                charge_id="CHRGiHoKn66p3bkcNs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charge(charge_id, request_options=request_options)
        return _response.data

    async def get_charges_additional_data(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesAdditionalDataRequestSort] = None,
        order: typing.Optional[GetChargesAdditionalDataRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeAdditionalDataResponse:
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
        ChargeAdditionalDataResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charges_additional_data(
                q='chargeAdditionalDataId:"CHADoLU7sWaGjWtkBx"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charges_additional_data(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_charge_additional_data(
        self, charge_additional_data_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChargeAdditionalData:
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
        ChargeAdditionalData
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charge_additional_data(
                charge_additional_data_id="CHADiHoKn66p3bkcNs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charge_additional_data(
            charge_additional_data_id, request_options=request_options
        )
        return _response.data

    async def get_charges_degree(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesDegreeRequestSort] = None,
        order: typing.Optional[GetChargesDegreeRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeDegreeResponse:
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
        ChargeDegreeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charges_degree(
                q='chargeDegreeId:"CHDGiHoKn66p3bkcNs"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charges_degree(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_charge_degree(
        self, charge_degree_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ChargeDegree]:
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
        typing.Optional[ChargeDegree]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charge_degree(
                charge_degree_id="CHDGiHoKn66p3bkcNs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charge_degree(charge_degree_id, request_options=request_options)
        return _response.data

    async def get_charge_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargeGroupsRequestSort] = None,
        order: typing.Optional[GetChargeGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeGroupResponse:
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
        ChargeGroupResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charge_groups(
                q='chargeGroupId:"CHRGoLU7sWaGjWtkBx"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charge_groups(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_charge_group(
        self, charge_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ChargeGroup:
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
        ChargeGroup
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charge_group(
                charge_group_id="CHGPiHoKn66p3bkcNs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charge_group(charge_group_id, request_options=request_options)
        return _response.data

    async def get_charges_severity(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetChargesSeverityRequestSort] = None,
        order: typing.Optional[GetChargesSeverityRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChargeSeverityResponse:
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
        ChargeSeverityResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charges_severity(
                q='chargeSeverityId:"CHSEiHoKn66p3bkcNs"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charges_severity(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_charge_severity(
        self, charge_severity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[ChargeSeverity]:
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
        typing.Optional[ChargeSeverity]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_charge_severity(
                charge_severity_id="CHSEiHoKn66p3bkcNs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charge_severity(charge_severity_id, request_options=request_options)
        return _response.data

    async def get_courts(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsRequestSort] = None,
        order: typing.Optional[GetCourtsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtResponse:
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
        CourtResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_courts(
                q='courtId:"CORThSxcef8eGUSkuC"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_courts(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_court(
        self, court_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Court]:
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
        typing.Optional[Court]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_court(
                court_id="CORThSxcef8eGUSkuC",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court(court_id, request_options=request_options)
        return _response.data

    async def get_appeal_courts_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetAppealCourtsForCourtRequestSort] = None,
        order: typing.Optional[GetAppealCourtsForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtResponse:
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
        CourtResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_appeal_courts_for_court(
                court_id="CORThSxcef8eGUSkuC",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_appeal_courts_for_court(
            court_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_court_locations_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtLocationsForCourtRequestSort] = None,
        order: typing.Optional[GetCourtLocationsForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtLocationResponse:
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
        CourtLocationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_court_locations_for_court(
                court_id="CORThSxcef8eGUSkuC",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court_locations_for_court(
            court_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_jurisdiction_geo_for_court(
        self,
        court_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJurisdictionGeoForCourtRequestSort] = None,
        order: typing.Optional[GetJurisdictionGeoForCourtRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JurisdictionGeoResponse:
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
        JurisdictionGeoResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_jurisdiction_geo_for_court(
                court_id="CORThSxcef8eGUSkuC",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jurisdiction_geo_for_court(
            court_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_court_locations(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtLocationsRequestSort] = None,
        order: typing.Optional[GetCourtLocationsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtLocationResponse:
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
        CourtLocationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_court_locations(
                q='courtLocationId:"COLO9g3fhYM4bmxveA"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court_locations(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_court_location(
        self, court_location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CourtLocation]:
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
        typing.Optional[CourtLocation]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_court_location(
                court_location_id="COLOV75AKgqMqnfVhM",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court_location(court_location_id, request_options=request_options)
        return _response.data

    async def get_courts_for_court_location(
        self,
        court_location_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsForCourtLocationRequestSort] = None,
        order: typing.Optional[GetCourtsForCourtLocationRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtResponse:
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
        CourtResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_courts_for_court_location(
                court_location_id="COLOV75AKgqMqnfVhM",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_courts_for_court_location(
            court_location_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_courts_service_status(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsServiceStatusRequestSort] = None,
        order: typing.Optional[GetCourtsServiceStatusRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtServiceStatusResponse:
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
        CourtServiceStatusResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_courts_service_status(
                q='courtServiceStatusId: "CTSSf45fd1bd792e97"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_courts_service_status(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_court_service_status(
        self, court_service_status_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[CourtServiceStatus]:
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
        typing.Optional[CourtServiceStatus]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_court_service_status(
                court_service_status_id="CTSSf45fd1bd792e97",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court_service_status(
            court_service_status_id, request_options=request_options
        )
        return _response.data

    async def get_court_systems(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtSystemsRequestSort] = None,
        order: typing.Optional[GetCourtSystemsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtSystemResponse:
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
        CourtSystemResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_court_systems(
                q='courtSystemId:"COSY4vuCtGQeAmdDdN"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court_systems(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_court_system(
        self, court_system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourtSystem:
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
        CourtSystem
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_court_system(
                court_system_id="COSY4vuCtGQeAmdDdN",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court_system(court_system_id, request_options=request_options)
        return _response.data

    async def get_court_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtTypesRequestSort] = None,
        order: typing.Optional[GetCourtTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtTypeResponse:
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
        CourtTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_court_types(
                q='courtTypeId:"COTPm8jjc2PAydpFhq"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_court_type(
        self, court_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CourtType:
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
        CourtType
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_court_type(
                court_type_id="COTPm8jjc2PAydpFhq",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_court_type(court_type_id, request_options=request_options)
        return _response.data

    async def get_judge_types(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJudgeTypesRequestSort] = None,
        order: typing.Optional[GetJudgeTypesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JudgeTypeResponse:
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
        JudgeTypeResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_judge_types(
                q='judgeTypeId: "JGTPkwrfzkDJUvxpN9"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_judge_types(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_judge_type(
        self, judge_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[JudgeType]:
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
        typing.Optional[JudgeType]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_judge_type(
                judge_type_id="JGTPkwrfzkDJUvxpN9",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_judge_type(judge_type_id, request_options=request_options)
        return _response.data

    async def get_jurisdictions_geo(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetJurisdictionsGeoRequestSort] = None,
        order: typing.Optional[GetJurisdictionsGeoRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JurisdictionGeoResponse:
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
        JurisdictionGeoResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_jurisdictions_geo(
                q='jurisdictionGeoId:"JUGO8s7HvM84dLvVMu"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jurisdictions_geo(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_jurisdiction_geo(
        self, jurisdiction_geo_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JurisdictionGeo:
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
        JurisdictionGeo
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_jurisdiction_geo(
                jurisdiction_geo_id="JUGO8s7HvM84dLvVMu",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jurisdiction_geo(jurisdiction_geo_id, request_options=request_options)
        return _response.data

    async def get_courts_for_jurisdiction_geo(
        self,
        jurisdiction_geo_id: str,
        *,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetCourtsForJurisdictionGeoRequestSort] = None,
        order: typing.Optional[GetCourtsForJurisdictionGeoRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CourtResponse:
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
        CourtResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_courts_for_jurisdiction_geo(
                jurisdiction_geo_id="JUGO8s7HvM84dLvVMu",
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_courts_for_jurisdiction_geo(
            jurisdiction_geo_id, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_party_roles(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetPartyRolesRequestSort] = None,
        order: typing.Optional[GetPartyRolesRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartyRoleResponse:
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
        PartyRoleResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_party_roles(
                q='partyRoleId: "PTYRVRgMKueGmhnxRN"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_party_roles(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_party_role(
        self, party_role_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[PartyRole]:
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
        typing.Optional[PartyRole]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_party_role(
                party_role_id="PTYRVRgMKueGmhnxRN",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_party_role(party_role_id, request_options=request_options)
        return _response.data

    async def get_party_role_groups(
        self,
        *,
        q: typing.Optional[str] = None,
        page_number: typing.Optional[int] = None,
        sort: typing.Optional[GetPartyRoleGroupsRequestSort] = None,
        order: typing.Optional[GetPartyRoleGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PartyRoleGroupResponse:
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
        PartyRoleGroupResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_party_role_groups(
                q='partyRoleGroupId: "PTYGBnjxbx6tKNfVEP"',
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_party_role_groups(
            q=q, page_number=page_number, sort=sort, order=order, request_options=request_options
        )
        return _response.data

    async def get_party_role_group(
        self, party_role_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PartyRoleGroup:
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
        PartyRoleGroup
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.court_standards_api.get_party_role_group(
                party_role_group_id="PTYGBnjxbx6tKNfVEP",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_party_role_group(party_role_group_id, request_options=request_options)
        return _response.data
