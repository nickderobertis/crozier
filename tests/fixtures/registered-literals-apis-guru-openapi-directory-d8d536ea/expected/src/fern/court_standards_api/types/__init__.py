



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_appeal_courts_for_court_request_order import GetAppealCourtsForCourtRequestOrder
    from .get_appeal_courts_for_court_request_sort import GetAppealCourtsForCourtRequestSort
    from .get_areas_of_law_request_order import GetAreasOfLawRequestOrder
    from .get_areas_of_law_request_sort import GetAreasOfLawRequestSort
    from .get_attorney_representation_types_request_order import GetAttorneyRepresentationTypesRequestOrder
    from .get_attorney_representation_types_request_sort import GetAttorneyRepresentationTypesRequestSort
    from .get_attorney_types_request_order import GetAttorneyTypesRequestOrder
    from .get_attorney_types_request_sort import GetAttorneyTypesRequestSort
    from .get_case_relationship_types_request_order import GetCaseRelationshipTypesRequestOrder
    from .get_case_relationship_types_request_sort import GetCaseRelationshipTypesRequestSort
    from .get_case_status_groups_request_order import GetCaseStatusGroupsRequestOrder
    from .get_case_status_groups_request_sort import GetCaseStatusGroupsRequestSort
    from .get_case_type_groups_request_order import GetCaseTypeGroupsRequestOrder
    from .get_case_type_groups_request_sort import GetCaseTypeGroupsRequestSort
    from .get_case_types_request_order import GetCaseTypesRequestOrder
    from .get_case_types_request_sort import GetCaseTypesRequestSort
    from .get_cases_class_request_order import GetCasesClassRequestOrder
    from .get_cases_class_request_sort import GetCasesClassRequestSort
    from .get_cases_status_request_order import GetCasesStatusRequestOrder
    from .get_cases_status_request_sort import GetCasesStatusRequestSort
    from .get_causes_of_action_additional_data_request_order import GetCausesOfActionAdditionalDataRequestOrder
    from .get_causes_of_action_additional_data_request_sort import GetCausesOfActionAdditionalDataRequestSort
    from .get_causes_of_action_group_request_order import GetCausesOfActionGroupRequestOrder
    from .get_causes_of_action_group_request_sort import GetCausesOfActionGroupRequestSort
    from .get_causes_of_action_request_order import GetCausesOfActionRequestOrder
    from .get_causes_of_action_request_sort import GetCausesOfActionRequestSort
    from .get_charge_groups_request_order import GetChargeGroupsRequestOrder
    from .get_charge_groups_request_sort import GetChargeGroupsRequestSort
    from .get_charges_additional_data_request_order import GetChargesAdditionalDataRequestOrder
    from .get_charges_additional_data_request_sort import GetChargesAdditionalDataRequestSort
    from .get_charges_degree_request_order import GetChargesDegreeRequestOrder
    from .get_charges_degree_request_sort import GetChargesDegreeRequestSort
    from .get_charges_request_order import GetChargesRequestOrder
    from .get_charges_request_sort import GetChargesRequestSort
    from .get_charges_severity_request_order import GetChargesSeverityRequestOrder
    from .get_charges_severity_request_sort import GetChargesSeverityRequestSort
    from .get_court_locations_for_court_request_order import GetCourtLocationsForCourtRequestOrder
    from .get_court_locations_for_court_request_sort import GetCourtLocationsForCourtRequestSort
    from .get_court_locations_request_order import GetCourtLocationsRequestOrder
    from .get_court_locations_request_sort import GetCourtLocationsRequestSort
    from .get_court_systems_request_order import GetCourtSystemsRequestOrder
    from .get_court_systems_request_sort import GetCourtSystemsRequestSort
    from .get_court_types_request_order import GetCourtTypesRequestOrder
    from .get_court_types_request_sort import GetCourtTypesRequestSort
    from .get_courts_for_court_location_request_order import GetCourtsForCourtLocationRequestOrder
    from .get_courts_for_court_location_request_sort import GetCourtsForCourtLocationRequestSort
    from .get_courts_for_jurisdiction_geo_request_order import GetCourtsForJurisdictionGeoRequestOrder
    from .get_courts_for_jurisdiction_geo_request_sort import GetCourtsForJurisdictionGeoRequestSort
    from .get_courts_request_order import GetCourtsRequestOrder
    from .get_courts_request_sort import GetCourtsRequestSort
    from .get_courts_service_status_request_order import GetCourtsServiceStatusRequestOrder
    from .get_courts_service_status_request_sort import GetCourtsServiceStatusRequestSort
    from .get_judge_types_request_order import GetJudgeTypesRequestOrder
    from .get_judge_types_request_sort import GetJudgeTypesRequestSort
    from .get_jurisdiction_geo_for_court_request_order import GetJurisdictionGeoForCourtRequestOrder
    from .get_jurisdiction_geo_for_court_request_sort import GetJurisdictionGeoForCourtRequestSort
    from .get_jurisdictions_geo_request_order import GetJurisdictionsGeoRequestOrder
    from .get_jurisdictions_geo_request_sort import GetJurisdictionsGeoRequestSort
    from .get_party_role_groups_request_order import GetPartyRoleGroupsRequestOrder
    from .get_party_role_groups_request_sort import GetPartyRoleGroupsRequestSort
    from .get_party_roles_request_order import GetPartyRolesRequestOrder
    from .get_party_roles_request_sort import GetPartyRolesRequestSort
_dynamic_imports: typing.Dict[str, str] = {
    "GetAppealCourtsForCourtRequestOrder": ".get_appeal_courts_for_court_request_order",
    "GetAppealCourtsForCourtRequestSort": ".get_appeal_courts_for_court_request_sort",
    "GetAreasOfLawRequestOrder": ".get_areas_of_law_request_order",
    "GetAreasOfLawRequestSort": ".get_areas_of_law_request_sort",
    "GetAttorneyRepresentationTypesRequestOrder": ".get_attorney_representation_types_request_order",
    "GetAttorneyRepresentationTypesRequestSort": ".get_attorney_representation_types_request_sort",
    "GetAttorneyTypesRequestOrder": ".get_attorney_types_request_order",
    "GetAttorneyTypesRequestSort": ".get_attorney_types_request_sort",
    "GetCaseRelationshipTypesRequestOrder": ".get_case_relationship_types_request_order",
    "GetCaseRelationshipTypesRequestSort": ".get_case_relationship_types_request_sort",
    "GetCaseStatusGroupsRequestOrder": ".get_case_status_groups_request_order",
    "GetCaseStatusGroupsRequestSort": ".get_case_status_groups_request_sort",
    "GetCaseTypeGroupsRequestOrder": ".get_case_type_groups_request_order",
    "GetCaseTypeGroupsRequestSort": ".get_case_type_groups_request_sort",
    "GetCaseTypesRequestOrder": ".get_case_types_request_order",
    "GetCaseTypesRequestSort": ".get_case_types_request_sort",
    "GetCasesClassRequestOrder": ".get_cases_class_request_order",
    "GetCasesClassRequestSort": ".get_cases_class_request_sort",
    "GetCasesStatusRequestOrder": ".get_cases_status_request_order",
    "GetCasesStatusRequestSort": ".get_cases_status_request_sort",
    "GetCausesOfActionAdditionalDataRequestOrder": ".get_causes_of_action_additional_data_request_order",
    "GetCausesOfActionAdditionalDataRequestSort": ".get_causes_of_action_additional_data_request_sort",
    "GetCausesOfActionGroupRequestOrder": ".get_causes_of_action_group_request_order",
    "GetCausesOfActionGroupRequestSort": ".get_causes_of_action_group_request_sort",
    "GetCausesOfActionRequestOrder": ".get_causes_of_action_request_order",
    "GetCausesOfActionRequestSort": ".get_causes_of_action_request_sort",
    "GetChargeGroupsRequestOrder": ".get_charge_groups_request_order",
    "GetChargeGroupsRequestSort": ".get_charge_groups_request_sort",
    "GetChargesAdditionalDataRequestOrder": ".get_charges_additional_data_request_order",
    "GetChargesAdditionalDataRequestSort": ".get_charges_additional_data_request_sort",
    "GetChargesDegreeRequestOrder": ".get_charges_degree_request_order",
    "GetChargesDegreeRequestSort": ".get_charges_degree_request_sort",
    "GetChargesRequestOrder": ".get_charges_request_order",
    "GetChargesRequestSort": ".get_charges_request_sort",
    "GetChargesSeverityRequestOrder": ".get_charges_severity_request_order",
    "GetChargesSeverityRequestSort": ".get_charges_severity_request_sort",
    "GetCourtLocationsForCourtRequestOrder": ".get_court_locations_for_court_request_order",
    "GetCourtLocationsForCourtRequestSort": ".get_court_locations_for_court_request_sort",
    "GetCourtLocationsRequestOrder": ".get_court_locations_request_order",
    "GetCourtLocationsRequestSort": ".get_court_locations_request_sort",
    "GetCourtSystemsRequestOrder": ".get_court_systems_request_order",
    "GetCourtSystemsRequestSort": ".get_court_systems_request_sort",
    "GetCourtTypesRequestOrder": ".get_court_types_request_order",
    "GetCourtTypesRequestSort": ".get_court_types_request_sort",
    "GetCourtsForCourtLocationRequestOrder": ".get_courts_for_court_location_request_order",
    "GetCourtsForCourtLocationRequestSort": ".get_courts_for_court_location_request_sort",
    "GetCourtsForJurisdictionGeoRequestOrder": ".get_courts_for_jurisdiction_geo_request_order",
    "GetCourtsForJurisdictionGeoRequestSort": ".get_courts_for_jurisdiction_geo_request_sort",
    "GetCourtsRequestOrder": ".get_courts_request_order",
    "GetCourtsRequestSort": ".get_courts_request_sort",
    "GetCourtsServiceStatusRequestOrder": ".get_courts_service_status_request_order",
    "GetCourtsServiceStatusRequestSort": ".get_courts_service_status_request_sort",
    "GetJudgeTypesRequestOrder": ".get_judge_types_request_order",
    "GetJudgeTypesRequestSort": ".get_judge_types_request_sort",
    "GetJurisdictionGeoForCourtRequestOrder": ".get_jurisdiction_geo_for_court_request_order",
    "GetJurisdictionGeoForCourtRequestSort": ".get_jurisdiction_geo_for_court_request_sort",
    "GetJurisdictionsGeoRequestOrder": ".get_jurisdictions_geo_request_order",
    "GetJurisdictionsGeoRequestSort": ".get_jurisdictions_geo_request_sort",
    "GetPartyRoleGroupsRequestOrder": ".get_party_role_groups_request_order",
    "GetPartyRoleGroupsRequestSort": ".get_party_role_groups_request_sort",
    "GetPartyRolesRequestOrder": ".get_party_roles_request_order",
    "GetPartyRolesRequestSort": ".get_party_roles_request_sort",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "GetAppealCourtsForCourtRequestOrder",
    "GetAppealCourtsForCourtRequestSort",
    "GetAreasOfLawRequestOrder",
    "GetAreasOfLawRequestSort",
    "GetAttorneyRepresentationTypesRequestOrder",
    "GetAttorneyRepresentationTypesRequestSort",
    "GetAttorneyTypesRequestOrder",
    "GetAttorneyTypesRequestSort",
    "GetCaseRelationshipTypesRequestOrder",
    "GetCaseRelationshipTypesRequestSort",
    "GetCaseStatusGroupsRequestOrder",
    "GetCaseStatusGroupsRequestSort",
    "GetCaseTypeGroupsRequestOrder",
    "GetCaseTypeGroupsRequestSort",
    "GetCaseTypesRequestOrder",
    "GetCaseTypesRequestSort",
    "GetCasesClassRequestOrder",
    "GetCasesClassRequestSort",
    "GetCasesStatusRequestOrder",
    "GetCasesStatusRequestSort",
    "GetCausesOfActionAdditionalDataRequestOrder",
    "GetCausesOfActionAdditionalDataRequestSort",
    "GetCausesOfActionGroupRequestOrder",
    "GetCausesOfActionGroupRequestSort",
    "GetCausesOfActionRequestOrder",
    "GetCausesOfActionRequestSort",
    "GetChargeGroupsRequestOrder",
    "GetChargeGroupsRequestSort",
    "GetChargesAdditionalDataRequestOrder",
    "GetChargesAdditionalDataRequestSort",
    "GetChargesDegreeRequestOrder",
    "GetChargesDegreeRequestSort",
    "GetChargesRequestOrder",
    "GetChargesRequestSort",
    "GetChargesSeverityRequestOrder",
    "GetChargesSeverityRequestSort",
    "GetCourtLocationsForCourtRequestOrder",
    "GetCourtLocationsForCourtRequestSort",
    "GetCourtLocationsRequestOrder",
    "GetCourtLocationsRequestSort",
    "GetCourtSystemsRequestOrder",
    "GetCourtSystemsRequestSort",
    "GetCourtTypesRequestOrder",
    "GetCourtTypesRequestSort",
    "GetCourtsForCourtLocationRequestOrder",
    "GetCourtsForCourtLocationRequestSort",
    "GetCourtsForJurisdictionGeoRequestOrder",
    "GetCourtsForJurisdictionGeoRequestSort",
    "GetCourtsRequestOrder",
    "GetCourtsRequestSort",
    "GetCourtsServiceStatusRequestOrder",
    "GetCourtsServiceStatusRequestSort",
    "GetJudgeTypesRequestOrder",
    "GetJudgeTypesRequestSort",
    "GetJurisdictionGeoForCourtRequestOrder",
    "GetJurisdictionGeoForCourtRequestSort",
    "GetJurisdictionsGeoRequestOrder",
    "GetJurisdictionsGeoRequestSort",
    "GetPartyRoleGroupsRequestOrder",
    "GetPartyRoleGroupsRequestSort",
    "GetPartyRolesRequestOrder",
    "GetPartyRolesRequestSort",
]
