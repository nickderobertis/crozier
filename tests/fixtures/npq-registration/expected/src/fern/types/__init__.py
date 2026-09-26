



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .application import Application
    from .application_attributes import ApplicationAttributes
    from .application_attributes_course_identifier import ApplicationAttributesCourseIdentifier
    from .application_attributes_funding_choice import ApplicationAttributesFundingChoice
    from .application_attributes_headteacher_status import ApplicationAttributesHeadteacherStatus
    from .application_attributes_ineligible_for_funding_reason import ApplicationAttributesIneligibleForFundingReason
    from .application_attributes_schedule_identifier import ApplicationAttributesScheduleIdentifier
    from .application_attributes_status import ApplicationAttributesStatus
    from .application_response import ApplicationResponse
    from .application_type import ApplicationType
    from .applications_response import ApplicationsResponse
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_errors_item import BadRequestResponseErrorsItem
    from .delivery_partner import DeliveryPartner
    from .delivery_partner_attributes import DeliveryPartnerAttributes
    from .delivery_partner_response import DeliveryPartnerResponse
    from .delivery_partner_type import DeliveryPartnerType
    from .delivery_partners_response import DeliveryPartnersResponse
    from .delivery_partners_sorting_options import DeliveryPartnersSortingOptions
    from .id_attribute import IdAttribute
    from .list_applications_filter import ListApplicationsFilter
    from .list_delivery_partners_filter import ListDeliveryPartnersFilter
    from .list_participant_declarations_filter import ListParticipantDeclarationsFilter
    from .list_participant_outcomes_filter import ListParticipantOutcomesFilter
    from .list_participants_filter import ListParticipantsFilter
    from .list_participants_filter_training_status import ListParticipantsFilterTrainingStatus
    from .list_statements_filter import ListStatementsFilter
    from .not_found_response import NotFoundResponse
    from .pagination_filter import PaginationFilter
    from .participant import Participant
    from .participant_attributes import ParticipantAttributes
    from .participant_attributes_npq_enrolments_item import ParticipantAttributesNpqEnrolmentsItem
    from .participant_attributes_npq_enrolments_item_course_identifier import (
        ParticipantAttributesNpqEnrolmentsItemCourseIdentifier,
    )
    from .participant_attributes_npq_enrolments_item_deferral import ParticipantAttributesNpqEnrolmentsItemDeferral
    from .participant_attributes_npq_enrolments_item_deferral_reason import (
        ParticipantAttributesNpqEnrolmentsItemDeferralReason,
    )
    from .participant_attributes_npq_enrolments_item_schedule_identifier import (
        ParticipantAttributesNpqEnrolmentsItemScheduleIdentifier,
    )
    from .participant_attributes_npq_enrolments_item_training_status import (
        ParticipantAttributesNpqEnrolmentsItemTrainingStatus,
    )
    from .participant_attributes_npq_enrolments_item_withdrawal import ParticipantAttributesNpqEnrolmentsItemWithdrawal
    from .participant_attributes_npq_enrolments_item_withdrawal_reason import (
        ParticipantAttributesNpqEnrolmentsItemWithdrawalReason,
    )
    from .participant_attributes_participant_id_changes_item import ParticipantAttributesParticipantIdChangesItem
    from .participant_declaration import ParticipantDeclaration
    from .participant_declaration_attributes import ParticipantDeclarationAttributes
    from .participant_declaration_attributes_course_identifier import ParticipantDeclarationAttributesCourseIdentifier
    from .participant_declaration_attributes_declaration_type import ParticipantDeclarationAttributesDeclarationType
    from .participant_declaration_attributes_ineligible_for_funding_reason import (
        ParticipantDeclarationAttributesIneligibleForFundingReason,
    )
    from .participant_declaration_attributes_state import ParticipantDeclarationAttributesState
    from .participant_declaration_completed_request import ParticipantDeclarationCompletedRequest
    from .participant_declaration_completed_request_course_identifier import (
        ParticipantDeclarationCompletedRequestCourseIdentifier,
    )
    from .participant_declaration_completed_request_declaration_type import (
        ParticipantDeclarationCompletedRequestDeclarationType,
    )
    from .participant_declaration_response import ParticipantDeclarationResponse
    from .participant_declaration_retained_request import ParticipantDeclarationRetainedRequest
    from .participant_declaration_retained_request_course_identifier import (
        ParticipantDeclarationRetainedRequestCourseIdentifier,
    )
    from .participant_declaration_retained_request_declaration_type import (
        ParticipantDeclarationRetainedRequestDeclarationType,
    )
    from .participant_declaration_started_request import ParticipantDeclarationStartedRequest
    from .participant_declaration_started_request_course_identifier import (
        ParticipantDeclarationStartedRequestCourseIdentifier,
    )
    from .participant_declaration_started_request_declaration_type import (
        ParticipantDeclarationStartedRequestDeclarationType,
    )
    from .participant_declaration_type import ParticipantDeclarationType
    from .participant_declarations_response import ParticipantDeclarationsResponse
    from .participant_outcome import ParticipantOutcome
    from .participant_outcome_attributes import ParticipantOutcomeAttributes
    from .participant_outcome_attributes_course_identifier import ParticipantOutcomeAttributesCourseIdentifier
    from .participant_outcome_attributes_state import ParticipantOutcomeAttributesState
    from .participant_outcome_response import ParticipantOutcomeResponse
    from .participant_outcome_type import ParticipantOutcomeType
    from .participant_outcomes_response import ParticipantOutcomesResponse
    from .participant_response import ParticipantResponse
    from .participant_type import ParticipantType
    from .participants_response import ParticipantsResponse
    from .sorting_options import SortingOptions
    from .statement import Statement
    from .statement_attributes import StatementAttributes
    from .statement_response import StatementResponse
    from .statement_type import StatementType
    from .statements_response import StatementsResponse
    from .unauthorised_response import UnauthorisedResponse
    from .unprocessable_entity_response import UnprocessableEntityResponse
    from .unprocessable_entity_response_errors_item import UnprocessableEntityResponseErrorsItem
_dynamic_imports: typing.Dict[str, str] = {
    "Application": ".application",
    "ApplicationAttributes": ".application_attributes",
    "ApplicationAttributesCourseIdentifier": ".application_attributes_course_identifier",
    "ApplicationAttributesFundingChoice": ".application_attributes_funding_choice",
    "ApplicationAttributesHeadteacherStatus": ".application_attributes_headteacher_status",
    "ApplicationAttributesIneligibleForFundingReason": ".application_attributes_ineligible_for_funding_reason",
    "ApplicationAttributesScheduleIdentifier": ".application_attributes_schedule_identifier",
    "ApplicationAttributesStatus": ".application_attributes_status",
    "ApplicationResponse": ".application_response",
    "ApplicationType": ".application_type",
    "ApplicationsResponse": ".applications_response",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseErrorsItem": ".bad_request_response_errors_item",
    "DeliveryPartner": ".delivery_partner",
    "DeliveryPartnerAttributes": ".delivery_partner_attributes",
    "DeliveryPartnerResponse": ".delivery_partner_response",
    "DeliveryPartnerType": ".delivery_partner_type",
    "DeliveryPartnersResponse": ".delivery_partners_response",
    "DeliveryPartnersSortingOptions": ".delivery_partners_sorting_options",
    "IdAttribute": ".id_attribute",
    "ListApplicationsFilter": ".list_applications_filter",
    "ListDeliveryPartnersFilter": ".list_delivery_partners_filter",
    "ListParticipantDeclarationsFilter": ".list_participant_declarations_filter",
    "ListParticipantOutcomesFilter": ".list_participant_outcomes_filter",
    "ListParticipantsFilter": ".list_participants_filter",
    "ListParticipantsFilterTrainingStatus": ".list_participants_filter_training_status",
    "ListStatementsFilter": ".list_statements_filter",
    "NotFoundResponse": ".not_found_response",
    "PaginationFilter": ".pagination_filter",
    "Participant": ".participant",
    "ParticipantAttributes": ".participant_attributes",
    "ParticipantAttributesNpqEnrolmentsItem": ".participant_attributes_npq_enrolments_item",
    "ParticipantAttributesNpqEnrolmentsItemCourseIdentifier": ".participant_attributes_npq_enrolments_item_course_identifier",
    "ParticipantAttributesNpqEnrolmentsItemDeferral": ".participant_attributes_npq_enrolments_item_deferral",
    "ParticipantAttributesNpqEnrolmentsItemDeferralReason": ".participant_attributes_npq_enrolments_item_deferral_reason",
    "ParticipantAttributesNpqEnrolmentsItemScheduleIdentifier": ".participant_attributes_npq_enrolments_item_schedule_identifier",
    "ParticipantAttributesNpqEnrolmentsItemTrainingStatus": ".participant_attributes_npq_enrolments_item_training_status",
    "ParticipantAttributesNpqEnrolmentsItemWithdrawal": ".participant_attributes_npq_enrolments_item_withdrawal",
    "ParticipantAttributesNpqEnrolmentsItemWithdrawalReason": ".participant_attributes_npq_enrolments_item_withdrawal_reason",
    "ParticipantAttributesParticipantIdChangesItem": ".participant_attributes_participant_id_changes_item",
    "ParticipantDeclaration": ".participant_declaration",
    "ParticipantDeclarationAttributes": ".participant_declaration_attributes",
    "ParticipantDeclarationAttributesCourseIdentifier": ".participant_declaration_attributes_course_identifier",
    "ParticipantDeclarationAttributesDeclarationType": ".participant_declaration_attributes_declaration_type",
    "ParticipantDeclarationAttributesIneligibleForFundingReason": ".participant_declaration_attributes_ineligible_for_funding_reason",
    "ParticipantDeclarationAttributesState": ".participant_declaration_attributes_state",
    "ParticipantDeclarationCompletedRequest": ".participant_declaration_completed_request",
    "ParticipantDeclarationCompletedRequestCourseIdentifier": ".participant_declaration_completed_request_course_identifier",
    "ParticipantDeclarationCompletedRequestDeclarationType": ".participant_declaration_completed_request_declaration_type",
    "ParticipantDeclarationResponse": ".participant_declaration_response",
    "ParticipantDeclarationRetainedRequest": ".participant_declaration_retained_request",
    "ParticipantDeclarationRetainedRequestCourseIdentifier": ".participant_declaration_retained_request_course_identifier",
    "ParticipantDeclarationRetainedRequestDeclarationType": ".participant_declaration_retained_request_declaration_type",
    "ParticipantDeclarationStartedRequest": ".participant_declaration_started_request",
    "ParticipantDeclarationStartedRequestCourseIdentifier": ".participant_declaration_started_request_course_identifier",
    "ParticipantDeclarationStartedRequestDeclarationType": ".participant_declaration_started_request_declaration_type",
    "ParticipantDeclarationType": ".participant_declaration_type",
    "ParticipantDeclarationsResponse": ".participant_declarations_response",
    "ParticipantOutcome": ".participant_outcome",
    "ParticipantOutcomeAttributes": ".participant_outcome_attributes",
    "ParticipantOutcomeAttributesCourseIdentifier": ".participant_outcome_attributes_course_identifier",
    "ParticipantOutcomeAttributesState": ".participant_outcome_attributes_state",
    "ParticipantOutcomeResponse": ".participant_outcome_response",
    "ParticipantOutcomeType": ".participant_outcome_type",
    "ParticipantOutcomesResponse": ".participant_outcomes_response",
    "ParticipantResponse": ".participant_response",
    "ParticipantType": ".participant_type",
    "ParticipantsResponse": ".participants_response",
    "SortingOptions": ".sorting_options",
    "Statement": ".statement",
    "StatementAttributes": ".statement_attributes",
    "StatementResponse": ".statement_response",
    "StatementType": ".statement_type",
    "StatementsResponse": ".statements_response",
    "UnauthorisedResponse": ".unauthorised_response",
    "UnprocessableEntityResponse": ".unprocessable_entity_response",
    "UnprocessableEntityResponseErrorsItem": ".unprocessable_entity_response_errors_item",
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
    "Application",
    "ApplicationAttributes",
    "ApplicationAttributesCourseIdentifier",
    "ApplicationAttributesFundingChoice",
    "ApplicationAttributesHeadteacherStatus",
    "ApplicationAttributesIneligibleForFundingReason",
    "ApplicationAttributesScheduleIdentifier",
    "ApplicationAttributesStatus",
    "ApplicationResponse",
    "ApplicationType",
    "ApplicationsResponse",
    "BadRequestResponse",
    "BadRequestResponseErrorsItem",
    "DeliveryPartner",
    "DeliveryPartnerAttributes",
    "DeliveryPartnerResponse",
    "DeliveryPartnerType",
    "DeliveryPartnersResponse",
    "DeliveryPartnersSortingOptions",
    "IdAttribute",
    "ListApplicationsFilter",
    "ListDeliveryPartnersFilter",
    "ListParticipantDeclarationsFilter",
    "ListParticipantOutcomesFilter",
    "ListParticipantsFilter",
    "ListParticipantsFilterTrainingStatus",
    "ListStatementsFilter",
    "NotFoundResponse",
    "PaginationFilter",
    "Participant",
    "ParticipantAttributes",
    "ParticipantAttributesNpqEnrolmentsItem",
    "ParticipantAttributesNpqEnrolmentsItemCourseIdentifier",
    "ParticipantAttributesNpqEnrolmentsItemDeferral",
    "ParticipantAttributesNpqEnrolmentsItemDeferralReason",
    "ParticipantAttributesNpqEnrolmentsItemScheduleIdentifier",
    "ParticipantAttributesNpqEnrolmentsItemTrainingStatus",
    "ParticipantAttributesNpqEnrolmentsItemWithdrawal",
    "ParticipantAttributesNpqEnrolmentsItemWithdrawalReason",
    "ParticipantAttributesParticipantIdChangesItem",
    "ParticipantDeclaration",
    "ParticipantDeclarationAttributes",
    "ParticipantDeclarationAttributesCourseIdentifier",
    "ParticipantDeclarationAttributesDeclarationType",
    "ParticipantDeclarationAttributesIneligibleForFundingReason",
    "ParticipantDeclarationAttributesState",
    "ParticipantDeclarationCompletedRequest",
    "ParticipantDeclarationCompletedRequestCourseIdentifier",
    "ParticipantDeclarationCompletedRequestDeclarationType",
    "ParticipantDeclarationResponse",
    "ParticipantDeclarationRetainedRequest",
    "ParticipantDeclarationRetainedRequestCourseIdentifier",
    "ParticipantDeclarationRetainedRequestDeclarationType",
    "ParticipantDeclarationStartedRequest",
    "ParticipantDeclarationStartedRequestCourseIdentifier",
    "ParticipantDeclarationStartedRequestDeclarationType",
    "ParticipantDeclarationType",
    "ParticipantDeclarationsResponse",
    "ParticipantOutcome",
    "ParticipantOutcomeAttributes",
    "ParticipantOutcomeAttributesCourseIdentifier",
    "ParticipantOutcomeAttributesState",
    "ParticipantOutcomeResponse",
    "ParticipantOutcomeType",
    "ParticipantOutcomesResponse",
    "ParticipantResponse",
    "ParticipantType",
    "ParticipantsResponse",
    "SortingOptions",
    "Statement",
    "StatementAttributes",
    "StatementResponse",
    "StatementType",
    "StatementsResponse",
    "UnauthorisedResponse",
    "UnprocessableEntityResponse",
    "UnprocessableEntityResponseErrorsItem",
]
