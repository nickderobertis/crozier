



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_token_request import AccessTokenRequest
    from .access_token_request_client_assertion_type import AccessTokenRequestClientAssertionType
    from .access_token_request_grant_type import AccessTokenRequestGrantType
    from .access_token_response import AccessTokenResponse
    from .access_token_revocation_request import AccessTokenRevocationRequest
    from .access_token_revocation_request_token_type_hint import AccessTokenRevocationRequestTokenTypeHint
    from .api_certification_uri import ApiCertificationUri
    from .api_discovery_endpoint import ApiDiscoveryEndpoint
    from .api_discovery_endpoint_family_response import ApiDiscoveryEndpointFamilyResponse
    from .api_discovery_endpoint_request import ApiDiscoveryEndpointRequest
    from .api_discovery_endpoints import ApiDiscoveryEndpoints
    from .api_endpoint import ApiEndpoint
    from .api_endpoint_id import ApiEndpointId
    from .api_family_type import ApiFamilyType
    from .api_resource import ApiResource
    from .api_resource_certification_status import ApiResourceCertificationStatus
    from .api_resource_id import ApiResourceId
    from .api_resource_request import ApiResourceRequest
    from .api_resource_request_certification_status import ApiResourceRequestCertificationStatus
    from .api_resources import ApiResources
    from .auth_deprecated_date import AuthDeprecatedDate
    from .auth_retirement_date import AuthRetirementDate
    from .auth_superseded_by_id import AuthSupersededById
    from .authorisation_domain import AuthorisationDomain
    from .authorisation_domain_name import AuthorisationDomainName
    from .authorisation_domain_request import AuthorisationDomainRequest
    from .authorisation_domain_role import AuthorisationDomainRole
    from .authorisation_domain_role_name import AuthorisationDomainRoleName
    from .authorisation_domain_role_request import AuthorisationDomainRoleRequest
    from .authorisation_domain_roles_page import AuthorisationDomainRolesPage
    from .authorisation_domain_user import AuthorisationDomainUser
    from .authorisation_domain_user_create_request import AuthorisationDomainUserCreateRequest
    from .authorisation_domain_user_id import AuthorisationDomainUserId
    from .authorisation_domain_user_update_request import AuthorisationDomainUserUpdateRequest
    from .authorisation_domain_users_page import AuthorisationDomainUsersPage
    from .authorisation_domains_page import AuthorisationDomainsPage
    from .authorisation_server import AuthorisationServer
    from .authorisation_server_certification import AuthorisationServerCertification
    from .authorisation_server_certification_id import AuthorisationServerCertificationId
    from .authorisation_server_certification_request import AuthorisationServerCertificationRequest
    from .authorisation_server_certification_request_status import AuthorisationServerCertificationRequestStatus
    from .authorisation_server_certification_status import AuthorisationServerCertificationStatus
    from .authorisation_server_certifications import AuthorisationServerCertifications
    from .authorisation_server_id import AuthorisationServerId
    from .authorisation_server_request import AuthorisationServerRequest
    from .authorisation_servers import AuthorisationServers
    from .authorities import Authorities
    from .authority import Authority
    from .authority_authorisation_domain import AuthorityAuthorisationDomain
    from .authority_authorisation_domain_id import AuthorityAuthorisationDomainId
    from .authority_authorisation_domain_request import AuthorityAuthorisationDomainRequest
    from .authority_authorisation_domains_page import AuthorityAuthorisationDomainsPage
    from .authority_id import AuthorityId
    from .authority_request import AuthorityRequest
    from .certificate_or_key import CertificateOrKey
    from .certificate_or_key_id import CertificateOrKeyId
    from .certificate_or_key_or_jwt import CertificateOrKeyOrJwt
    from .certificates_or_keys import CertificatesOrKeys
    from .certification_expiration_date import CertificationExpirationDate
    from .certification_manager import CertificationManager
    from .certification_manager_creation_request import CertificationManagerCreationRequest
    from .certification_managers import CertificationManagers
    from .certification_start_date import CertificationStartDate
    from .client_creation_request import ClientCreationRequest
    from .client_creation_request_id_token_signed_response_alg import ClientCreationRequestIdTokenSignedResponseAlg
    from .client_creation_request_token_endpoint_auth_method import ClientCreationRequestTokenEndpointAuthMethod
    from .client_creation_response import ClientCreationResponse
    from .client_creation_response_application_type import ClientCreationResponseApplicationType
    from .client_update_request import ClientUpdateRequest
    from .client_update_request_id_token_signed_response_alg import ClientUpdateRequestIdTokenSignedResponseAlg
    from .client_update_request_token_endpoint_auth_method import ClientUpdateRequestTokenEndpointAuthMethod
    from .contact import Contact
    from .contact_contact_type import ContactContactType
    from .contact_id import ContactId
    from .contact_request import ContactRequest
    from .contact_request_contact_type import ContactRequestContactType
    from .contact_role_enum import ContactRoleEnum
    from .contacts import Contacts
    from .contacts_page import ContactsPage
    from .docusign_org_request import DocusignOrgRequest
    from .docusign_post import DocusignPost
    from .docusign_post_data import DocusignPostData
    from .domain_role_detail import DomainRoleDetail
    from .envelope_summary import EnvelopeSummary
    from .ess_poll_response import EssPollResponse
    from .ess_poll_responses import EssPollResponses
    from .ess_sign_request import EssSignRequest
    from .external_signing_service import ExternalSigningService
    from .external_signing_service_envelope_id import ExternalSigningServiceEnvelopeId
    from .external_signing_service_envelope_status import ExternalSigningServiceEnvelopeStatus
    from .external_signing_service_name import ExternalSigningServiceName
    from .external_signing_service_signer_template_config import ExternalSigningServiceSignerTemplateConfig
    from .http_response_body import HttpResponseBody
    from .introspection import Introspection
    from .introspection_request import IntrospectionRequest
    from .metadata_id import MetadataId
    from .metadata_list_response import MetadataListResponse
    from .metadata_request import MetadataRequest
    from .metadata_response import MetadataResponse
    from .notification_webhook_status_enum import NotificationWebhookStatusEnum
    from .oauth_scope import OauthScope
    from .org_access_detail import OrgAccessDetail
    from .org_admin_user_create_request import OrgAdminUserCreateRequest
    from .org_terms_and_conditions_detail import OrgTermsAndConditionsDetail
    from .org_terms_and_conditions_page import OrgTermsAndConditionsPage
    from .organisation import Organisation
    from .organisation_admin_user import OrganisationAdminUser
    from .organisation_admin_users import OrganisationAdminUsers
    from .organisation_authorisation_id import OrganisationAuthorisationId
    from .organisation_authority_claim import OrganisationAuthorityClaim
    from .organisation_authority_claim_authorisation import OrganisationAuthorityClaimAuthorisation
    from .organisation_authority_claim_authorisation_request import OrganisationAuthorityClaimAuthorisationRequest
    from .organisation_authority_claim_authorisations import OrganisationAuthorityClaimAuthorisations
    from .organisation_authority_claim_authorisations_item import OrganisationAuthorityClaimAuthorisationsItem
    from .organisation_authority_claim_id import OrganisationAuthorityClaimId
    from .organisation_authority_claim_request import OrganisationAuthorityClaimRequest
    from .organisation_authority_claims import OrganisationAuthorityClaims
    from .organisation_authority_domain_claim import OrganisationAuthorityDomainClaim
    from .organisation_authority_domain_claim_id import OrganisationAuthorityDomainClaimId
    from .organisation_authority_domain_claim_request import OrganisationAuthorityDomainClaimRequest
    from .organisation_authority_domain_claim_update_request import OrganisationAuthorityDomainClaimUpdateRequest
    from .organisation_authority_domain_claims import OrganisationAuthorityDomainClaims
    from .organisation_authority_domain_claims_page import OrganisationAuthorityDomainClaimsPage
    from .organisation_certificate_type import OrganisationCertificateType
    from .organisation_conformance_test import OrganisationConformanceTest
    from .organisation_conformance_test_result import OrganisationConformanceTestResult
    from .organisation_enrol import OrganisationEnrol
    from .organisation_enrolments import OrganisationEnrolments
    from .organisation_enrolments_item import OrganisationEnrolmentsItem
    from .organisation_export_open_data import OrganisationExportOpenData
    from .organisation_export_open_data_status import OrganisationExportOpenDataStatus
    from .organisation_id import OrganisationId
    from .organisation_request import OrganisationRequest
    from .organisation_request_status import OrganisationRequestStatus
    from .organisation_roles import OrganisationRoles
    from .organisation_roles_org_domain_claims_item import OrganisationRolesOrgDomainClaimsItem
    from .organisation_roles_org_domain_role_claims_item import OrganisationRolesOrgDomainRoleClaimsItem
    from .organisation_roles_status import OrganisationRolesStatus
    from .organisation_snapshot import OrganisationSnapshot
    from .organisation_snapshot_page import OrganisationSnapshotPage
    from .organisation_snapshot_software_statements_value import OrganisationSnapshotSoftwareStatementsValue
    from .organisation_status import OrganisationStatus
    from .organisation_update_request import OrganisationUpdateRequest
    from .organisation_update_request_status import OrganisationUpdateRequestStatus
    from .organisation_with_tnc import OrganisationWithTnc
    from .organisation_with_tnc_tnc_details import OrganisationWithTncTncDetails
    from .organisations_export_open_data import OrganisationsExportOpenData
    from .organisations_page import OrganisationsPage
    from .organisations_roles import OrganisationsRoles
    from .organisations_snapshot import OrganisationsSnapshot
    from .pageable import Pageable
    from .pageable_request import PageableRequest
    from .pagination_properties import PaginationProperties
    from .profile_type import ProfileType
    from .profile_variant import ProfileVariant
    from .sns_notification_webhook_uri import SnsNotificationWebhookUri
    from .software_authority_claim import SoftwareAuthorityClaim
    from .software_authority_claim_id import SoftwareAuthorityClaimId
    from .software_authority_claim_request import SoftwareAuthorityClaimRequest
    from .software_authority_claim_update_request import SoftwareAuthorityClaimUpdateRequest
    from .software_authority_claims import SoftwareAuthorityClaims
    from .software_statement import SoftwareStatement
    from .software_statement_assertion import SoftwareStatementAssertion
    from .software_statement_certificate_or_key_type import SoftwareStatementCertificateOrKeyType
    from .software_statement_certification import SoftwareStatementCertification
    from .software_statement_certification_id import SoftwareStatementCertificationId
    from .software_statement_certification_request import SoftwareStatementCertificationRequest
    from .software_statement_certification_request_status import SoftwareStatementCertificationRequestStatus
    from .software_statement_certification_status import SoftwareStatementCertificationStatus
    from .software_statement_certifications import SoftwareStatementCertifications
    from .software_statement_id import SoftwareStatementId
    from .software_statement_mode import SoftwareStatementMode
    from .software_statement_request import SoftwareStatementRequest
    from .software_statement_request_mode import SoftwareStatementRequestMode
    from .software_statement_status import SoftwareStatementStatus
    from .software_statements import SoftwareStatements
    from .sort import Sort
    from .sort_order_by_item import SortOrderByItem
    from .sort_order_by_item_direction import SortOrderByItemDirection
    from .status_enum import StatusEnum
    from .super_user import SuperUser
    from .super_user_creation_request import SuperUserCreationRequest
    from .super_users import SuperUsers
    from .system_enum import SystemEnum
    from .terms_and_conditions_detail import TermsAndConditionsDetail
    from .terms_and_conditions_details import TermsAndConditionsDetails
    from .terms_and_conditions_item import TermsAndConditionsItem
    from .terms_and_conditions_item_type import TermsAndConditionsItemType
    from .terms_and_conditions_page import TermsAndConditionsPage
    from .terms_and_conditions_update_request import TermsAndConditionsUpdateRequest
    from .tn_c_id import TnCId
    from .tn_cs_to_be_signed import TnCsToBeSigned
    from .user_create_request import UserCreateRequest
    from .user_detail import UserDetail
    from .user_detail_basic_information import UserDetailBasicInformation
    from .user_email_id import UserEmailId
    from .user_op_info import UserOpInfo
    from .user_terms_and_conditions_page import UserTermsAndConditionsPage
    from .user_update_request import UserUpdateRequest
    from .webhook_status_response import WebhookStatusResponse
    from .webhook_status_responses import WebhookStatusResponses
    from .well_known import WellKnown
    from .x_fapi_interaction_id import XFapiInteractionId
_dynamic_imports: typing.Dict[str, str] = {
    "AccessTokenRequest": ".access_token_request",
    "AccessTokenRequestClientAssertionType": ".access_token_request_client_assertion_type",
    "AccessTokenRequestGrantType": ".access_token_request_grant_type",
    "AccessTokenResponse": ".access_token_response",
    "AccessTokenRevocationRequest": ".access_token_revocation_request",
    "AccessTokenRevocationRequestTokenTypeHint": ".access_token_revocation_request_token_type_hint",
    "ApiCertificationUri": ".api_certification_uri",
    "ApiDiscoveryEndpoint": ".api_discovery_endpoint",
    "ApiDiscoveryEndpointFamilyResponse": ".api_discovery_endpoint_family_response",
    "ApiDiscoveryEndpointRequest": ".api_discovery_endpoint_request",
    "ApiDiscoveryEndpoints": ".api_discovery_endpoints",
    "ApiEndpoint": ".api_endpoint",
    "ApiEndpointId": ".api_endpoint_id",
    "ApiFamilyType": ".api_family_type",
    "ApiResource": ".api_resource",
    "ApiResourceCertificationStatus": ".api_resource_certification_status",
    "ApiResourceId": ".api_resource_id",
    "ApiResourceRequest": ".api_resource_request",
    "ApiResourceRequestCertificationStatus": ".api_resource_request_certification_status",
    "ApiResources": ".api_resources",
    "AuthDeprecatedDate": ".auth_deprecated_date",
    "AuthRetirementDate": ".auth_retirement_date",
    "AuthSupersededById": ".auth_superseded_by_id",
    "AuthorisationDomain": ".authorisation_domain",
    "AuthorisationDomainName": ".authorisation_domain_name",
    "AuthorisationDomainRequest": ".authorisation_domain_request",
    "AuthorisationDomainRole": ".authorisation_domain_role",
    "AuthorisationDomainRoleName": ".authorisation_domain_role_name",
    "AuthorisationDomainRoleRequest": ".authorisation_domain_role_request",
    "AuthorisationDomainRolesPage": ".authorisation_domain_roles_page",
    "AuthorisationDomainUser": ".authorisation_domain_user",
    "AuthorisationDomainUserCreateRequest": ".authorisation_domain_user_create_request",
    "AuthorisationDomainUserId": ".authorisation_domain_user_id",
    "AuthorisationDomainUserUpdateRequest": ".authorisation_domain_user_update_request",
    "AuthorisationDomainUsersPage": ".authorisation_domain_users_page",
    "AuthorisationDomainsPage": ".authorisation_domains_page",
    "AuthorisationServer": ".authorisation_server",
    "AuthorisationServerCertification": ".authorisation_server_certification",
    "AuthorisationServerCertificationId": ".authorisation_server_certification_id",
    "AuthorisationServerCertificationRequest": ".authorisation_server_certification_request",
    "AuthorisationServerCertificationRequestStatus": ".authorisation_server_certification_request_status",
    "AuthorisationServerCertificationStatus": ".authorisation_server_certification_status",
    "AuthorisationServerCertifications": ".authorisation_server_certifications",
    "AuthorisationServerId": ".authorisation_server_id",
    "AuthorisationServerRequest": ".authorisation_server_request",
    "AuthorisationServers": ".authorisation_servers",
    "Authorities": ".authorities",
    "Authority": ".authority",
    "AuthorityAuthorisationDomain": ".authority_authorisation_domain",
    "AuthorityAuthorisationDomainId": ".authority_authorisation_domain_id",
    "AuthorityAuthorisationDomainRequest": ".authority_authorisation_domain_request",
    "AuthorityAuthorisationDomainsPage": ".authority_authorisation_domains_page",
    "AuthorityId": ".authority_id",
    "AuthorityRequest": ".authority_request",
    "CertificateOrKey": ".certificate_or_key",
    "CertificateOrKeyId": ".certificate_or_key_id",
    "CertificateOrKeyOrJwt": ".certificate_or_key_or_jwt",
    "CertificatesOrKeys": ".certificates_or_keys",
    "CertificationExpirationDate": ".certification_expiration_date",
    "CertificationManager": ".certification_manager",
    "CertificationManagerCreationRequest": ".certification_manager_creation_request",
    "CertificationManagers": ".certification_managers",
    "CertificationStartDate": ".certification_start_date",
    "ClientCreationRequest": ".client_creation_request",
    "ClientCreationRequestIdTokenSignedResponseAlg": ".client_creation_request_id_token_signed_response_alg",
    "ClientCreationRequestTokenEndpointAuthMethod": ".client_creation_request_token_endpoint_auth_method",
    "ClientCreationResponse": ".client_creation_response",
    "ClientCreationResponseApplicationType": ".client_creation_response_application_type",
    "ClientUpdateRequest": ".client_update_request",
    "ClientUpdateRequestIdTokenSignedResponseAlg": ".client_update_request_id_token_signed_response_alg",
    "ClientUpdateRequestTokenEndpointAuthMethod": ".client_update_request_token_endpoint_auth_method",
    "Contact": ".contact",
    "ContactContactType": ".contact_contact_type",
    "ContactId": ".contact_id",
    "ContactRequest": ".contact_request",
    "ContactRequestContactType": ".contact_request_contact_type",
    "ContactRoleEnum": ".contact_role_enum",
    "Contacts": ".contacts",
    "ContactsPage": ".contacts_page",
    "DocusignOrgRequest": ".docusign_org_request",
    "DocusignPost": ".docusign_post",
    "DocusignPostData": ".docusign_post_data",
    "DomainRoleDetail": ".domain_role_detail",
    "EnvelopeSummary": ".envelope_summary",
    "EssPollResponse": ".ess_poll_response",
    "EssPollResponses": ".ess_poll_responses",
    "EssSignRequest": ".ess_sign_request",
    "ExternalSigningService": ".external_signing_service",
    "ExternalSigningServiceEnvelopeId": ".external_signing_service_envelope_id",
    "ExternalSigningServiceEnvelopeStatus": ".external_signing_service_envelope_status",
    "ExternalSigningServiceName": ".external_signing_service_name",
    "ExternalSigningServiceSignerTemplateConfig": ".external_signing_service_signer_template_config",
    "HttpResponseBody": ".http_response_body",
    "Introspection": ".introspection",
    "IntrospectionRequest": ".introspection_request",
    "MetadataId": ".metadata_id",
    "MetadataListResponse": ".metadata_list_response",
    "MetadataRequest": ".metadata_request",
    "MetadataResponse": ".metadata_response",
    "NotificationWebhookStatusEnum": ".notification_webhook_status_enum",
    "OauthScope": ".oauth_scope",
    "OrgAccessDetail": ".org_access_detail",
    "OrgAdminUserCreateRequest": ".org_admin_user_create_request",
    "OrgTermsAndConditionsDetail": ".org_terms_and_conditions_detail",
    "OrgTermsAndConditionsPage": ".org_terms_and_conditions_page",
    "Organisation": ".organisation",
    "OrganisationAdminUser": ".organisation_admin_user",
    "OrganisationAdminUsers": ".organisation_admin_users",
    "OrganisationAuthorisationId": ".organisation_authorisation_id",
    "OrganisationAuthorityClaim": ".organisation_authority_claim",
    "OrganisationAuthorityClaimAuthorisation": ".organisation_authority_claim_authorisation",
    "OrganisationAuthorityClaimAuthorisationRequest": ".organisation_authority_claim_authorisation_request",
    "OrganisationAuthorityClaimAuthorisations": ".organisation_authority_claim_authorisations",
    "OrganisationAuthorityClaimAuthorisationsItem": ".organisation_authority_claim_authorisations_item",
    "OrganisationAuthorityClaimId": ".organisation_authority_claim_id",
    "OrganisationAuthorityClaimRequest": ".organisation_authority_claim_request",
    "OrganisationAuthorityClaims": ".organisation_authority_claims",
    "OrganisationAuthorityDomainClaim": ".organisation_authority_domain_claim",
    "OrganisationAuthorityDomainClaimId": ".organisation_authority_domain_claim_id",
    "OrganisationAuthorityDomainClaimRequest": ".organisation_authority_domain_claim_request",
    "OrganisationAuthorityDomainClaimUpdateRequest": ".organisation_authority_domain_claim_update_request",
    "OrganisationAuthorityDomainClaims": ".organisation_authority_domain_claims",
    "OrganisationAuthorityDomainClaimsPage": ".organisation_authority_domain_claims_page",
    "OrganisationCertificateType": ".organisation_certificate_type",
    "OrganisationConformanceTest": ".organisation_conformance_test",
    "OrganisationConformanceTestResult": ".organisation_conformance_test_result",
    "OrganisationEnrol": ".organisation_enrol",
    "OrganisationEnrolments": ".organisation_enrolments",
    "OrganisationEnrolmentsItem": ".organisation_enrolments_item",
    "OrganisationExportOpenData": ".organisation_export_open_data",
    "OrganisationExportOpenDataStatus": ".organisation_export_open_data_status",
    "OrganisationId": ".organisation_id",
    "OrganisationRequest": ".organisation_request",
    "OrganisationRequestStatus": ".organisation_request_status",
    "OrganisationRoles": ".organisation_roles",
    "OrganisationRolesOrgDomainClaimsItem": ".organisation_roles_org_domain_claims_item",
    "OrganisationRolesOrgDomainRoleClaimsItem": ".organisation_roles_org_domain_role_claims_item",
    "OrganisationRolesStatus": ".organisation_roles_status",
    "OrganisationSnapshot": ".organisation_snapshot",
    "OrganisationSnapshotPage": ".organisation_snapshot_page",
    "OrganisationSnapshotSoftwareStatementsValue": ".organisation_snapshot_software_statements_value",
    "OrganisationStatus": ".organisation_status",
    "OrganisationUpdateRequest": ".organisation_update_request",
    "OrganisationUpdateRequestStatus": ".organisation_update_request_status",
    "OrganisationWithTnc": ".organisation_with_tnc",
    "OrganisationWithTncTncDetails": ".organisation_with_tnc_tnc_details",
    "OrganisationsExportOpenData": ".organisations_export_open_data",
    "OrganisationsPage": ".organisations_page",
    "OrganisationsRoles": ".organisations_roles",
    "OrganisationsSnapshot": ".organisations_snapshot",
    "Pageable": ".pageable",
    "PageableRequest": ".pageable_request",
    "PaginationProperties": ".pagination_properties",
    "ProfileType": ".profile_type",
    "ProfileVariant": ".profile_variant",
    "SnsNotificationWebhookUri": ".sns_notification_webhook_uri",
    "SoftwareAuthorityClaim": ".software_authority_claim",
    "SoftwareAuthorityClaimId": ".software_authority_claim_id",
    "SoftwareAuthorityClaimRequest": ".software_authority_claim_request",
    "SoftwareAuthorityClaimUpdateRequest": ".software_authority_claim_update_request",
    "SoftwareAuthorityClaims": ".software_authority_claims",
    "SoftwareStatement": ".software_statement",
    "SoftwareStatementAssertion": ".software_statement_assertion",
    "SoftwareStatementCertificateOrKeyType": ".software_statement_certificate_or_key_type",
    "SoftwareStatementCertification": ".software_statement_certification",
    "SoftwareStatementCertificationId": ".software_statement_certification_id",
    "SoftwareStatementCertificationRequest": ".software_statement_certification_request",
    "SoftwareStatementCertificationRequestStatus": ".software_statement_certification_request_status",
    "SoftwareStatementCertificationStatus": ".software_statement_certification_status",
    "SoftwareStatementCertifications": ".software_statement_certifications",
    "SoftwareStatementId": ".software_statement_id",
    "SoftwareStatementMode": ".software_statement_mode",
    "SoftwareStatementRequest": ".software_statement_request",
    "SoftwareStatementRequestMode": ".software_statement_request_mode",
    "SoftwareStatementStatus": ".software_statement_status",
    "SoftwareStatements": ".software_statements",
    "Sort": ".sort",
    "SortOrderByItem": ".sort_order_by_item",
    "SortOrderByItemDirection": ".sort_order_by_item_direction",
    "StatusEnum": ".status_enum",
    "SuperUser": ".super_user",
    "SuperUserCreationRequest": ".super_user_creation_request",
    "SuperUsers": ".super_users",
    "SystemEnum": ".system_enum",
    "TermsAndConditionsDetail": ".terms_and_conditions_detail",
    "TermsAndConditionsDetails": ".terms_and_conditions_details",
    "TermsAndConditionsItem": ".terms_and_conditions_item",
    "TermsAndConditionsItemType": ".terms_and_conditions_item_type",
    "TermsAndConditionsPage": ".terms_and_conditions_page",
    "TermsAndConditionsUpdateRequest": ".terms_and_conditions_update_request",
    "TnCId": ".tn_c_id",
    "TnCsToBeSigned": ".tn_cs_to_be_signed",
    "UserCreateRequest": ".user_create_request",
    "UserDetail": ".user_detail",
    "UserDetailBasicInformation": ".user_detail_basic_information",
    "UserEmailId": ".user_email_id",
    "UserOpInfo": ".user_op_info",
    "UserTermsAndConditionsPage": ".user_terms_and_conditions_page",
    "UserUpdateRequest": ".user_update_request",
    "WebhookStatusResponse": ".webhook_status_response",
    "WebhookStatusResponses": ".webhook_status_responses",
    "WellKnown": ".well_known",
    "XFapiInteractionId": ".x_fapi_interaction_id",
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
    "AccessTokenRequest",
    "AccessTokenRequestClientAssertionType",
    "AccessTokenRequestGrantType",
    "AccessTokenResponse",
    "AccessTokenRevocationRequest",
    "AccessTokenRevocationRequestTokenTypeHint",
    "ApiCertificationUri",
    "ApiDiscoveryEndpoint",
    "ApiDiscoveryEndpointFamilyResponse",
    "ApiDiscoveryEndpointRequest",
    "ApiDiscoveryEndpoints",
    "ApiEndpoint",
    "ApiEndpointId",
    "ApiFamilyType",
    "ApiResource",
    "ApiResourceCertificationStatus",
    "ApiResourceId",
    "ApiResourceRequest",
    "ApiResourceRequestCertificationStatus",
    "ApiResources",
    "AuthDeprecatedDate",
    "AuthRetirementDate",
    "AuthSupersededById",
    "AuthorisationDomain",
    "AuthorisationDomainName",
    "AuthorisationDomainRequest",
    "AuthorisationDomainRole",
    "AuthorisationDomainRoleName",
    "AuthorisationDomainRoleRequest",
    "AuthorisationDomainRolesPage",
    "AuthorisationDomainUser",
    "AuthorisationDomainUserCreateRequest",
    "AuthorisationDomainUserId",
    "AuthorisationDomainUserUpdateRequest",
    "AuthorisationDomainUsersPage",
    "AuthorisationDomainsPage",
    "AuthorisationServer",
    "AuthorisationServerCertification",
    "AuthorisationServerCertificationId",
    "AuthorisationServerCertificationRequest",
    "AuthorisationServerCertificationRequestStatus",
    "AuthorisationServerCertificationStatus",
    "AuthorisationServerCertifications",
    "AuthorisationServerId",
    "AuthorisationServerRequest",
    "AuthorisationServers",
    "Authorities",
    "Authority",
    "AuthorityAuthorisationDomain",
    "AuthorityAuthorisationDomainId",
    "AuthorityAuthorisationDomainRequest",
    "AuthorityAuthorisationDomainsPage",
    "AuthorityId",
    "AuthorityRequest",
    "CertificateOrKey",
    "CertificateOrKeyId",
    "CertificateOrKeyOrJwt",
    "CertificatesOrKeys",
    "CertificationExpirationDate",
    "CertificationManager",
    "CertificationManagerCreationRequest",
    "CertificationManagers",
    "CertificationStartDate",
    "ClientCreationRequest",
    "ClientCreationRequestIdTokenSignedResponseAlg",
    "ClientCreationRequestTokenEndpointAuthMethod",
    "ClientCreationResponse",
    "ClientCreationResponseApplicationType",
    "ClientUpdateRequest",
    "ClientUpdateRequestIdTokenSignedResponseAlg",
    "ClientUpdateRequestTokenEndpointAuthMethod",
    "Contact",
    "ContactContactType",
    "ContactId",
    "ContactRequest",
    "ContactRequestContactType",
    "ContactRoleEnum",
    "Contacts",
    "ContactsPage",
    "DocusignOrgRequest",
    "DocusignPost",
    "DocusignPostData",
    "DomainRoleDetail",
    "EnvelopeSummary",
    "EssPollResponse",
    "EssPollResponses",
    "EssSignRequest",
    "ExternalSigningService",
    "ExternalSigningServiceEnvelopeId",
    "ExternalSigningServiceEnvelopeStatus",
    "ExternalSigningServiceName",
    "ExternalSigningServiceSignerTemplateConfig",
    "HttpResponseBody",
    "Introspection",
    "IntrospectionRequest",
    "MetadataId",
    "MetadataListResponse",
    "MetadataRequest",
    "MetadataResponse",
    "NotificationWebhookStatusEnum",
    "OauthScope",
    "OrgAccessDetail",
    "OrgAdminUserCreateRequest",
    "OrgTermsAndConditionsDetail",
    "OrgTermsAndConditionsPage",
    "Organisation",
    "OrganisationAdminUser",
    "OrganisationAdminUsers",
    "OrganisationAuthorisationId",
    "OrganisationAuthorityClaim",
    "OrganisationAuthorityClaimAuthorisation",
    "OrganisationAuthorityClaimAuthorisationRequest",
    "OrganisationAuthorityClaimAuthorisations",
    "OrganisationAuthorityClaimAuthorisationsItem",
    "OrganisationAuthorityClaimId",
    "OrganisationAuthorityClaimRequest",
    "OrganisationAuthorityClaims",
    "OrganisationAuthorityDomainClaim",
    "OrganisationAuthorityDomainClaimId",
    "OrganisationAuthorityDomainClaimRequest",
    "OrganisationAuthorityDomainClaimUpdateRequest",
    "OrganisationAuthorityDomainClaims",
    "OrganisationAuthorityDomainClaimsPage",
    "OrganisationCertificateType",
    "OrganisationConformanceTest",
    "OrganisationConformanceTestResult",
    "OrganisationEnrol",
    "OrganisationEnrolments",
    "OrganisationEnrolmentsItem",
    "OrganisationExportOpenData",
    "OrganisationExportOpenDataStatus",
    "OrganisationId",
    "OrganisationRequest",
    "OrganisationRequestStatus",
    "OrganisationRoles",
    "OrganisationRolesOrgDomainClaimsItem",
    "OrganisationRolesOrgDomainRoleClaimsItem",
    "OrganisationRolesStatus",
    "OrganisationSnapshot",
    "OrganisationSnapshotPage",
    "OrganisationSnapshotSoftwareStatementsValue",
    "OrganisationStatus",
    "OrganisationUpdateRequest",
    "OrganisationUpdateRequestStatus",
    "OrganisationWithTnc",
    "OrganisationWithTncTncDetails",
    "OrganisationsExportOpenData",
    "OrganisationsPage",
    "OrganisationsRoles",
    "OrganisationsSnapshot",
    "Pageable",
    "PageableRequest",
    "PaginationProperties",
    "ProfileType",
    "ProfileVariant",
    "SnsNotificationWebhookUri",
    "SoftwareAuthorityClaim",
    "SoftwareAuthorityClaimId",
    "SoftwareAuthorityClaimRequest",
    "SoftwareAuthorityClaimUpdateRequest",
    "SoftwareAuthorityClaims",
    "SoftwareStatement",
    "SoftwareStatementAssertion",
    "SoftwareStatementCertificateOrKeyType",
    "SoftwareStatementCertification",
    "SoftwareStatementCertificationId",
    "SoftwareStatementCertificationRequest",
    "SoftwareStatementCertificationRequestStatus",
    "SoftwareStatementCertificationStatus",
    "SoftwareStatementCertifications",
    "SoftwareStatementId",
    "SoftwareStatementMode",
    "SoftwareStatementRequest",
    "SoftwareStatementRequestMode",
    "SoftwareStatementStatus",
    "SoftwareStatements",
    "Sort",
    "SortOrderByItem",
    "SortOrderByItemDirection",
    "StatusEnum",
    "SuperUser",
    "SuperUserCreationRequest",
    "SuperUsers",
    "SystemEnum",
    "TermsAndConditionsDetail",
    "TermsAndConditionsDetails",
    "TermsAndConditionsItem",
    "TermsAndConditionsItemType",
    "TermsAndConditionsPage",
    "TermsAndConditionsUpdateRequest",
    "TnCId",
    "TnCsToBeSigned",
    "UserCreateRequest",
    "UserDetail",
    "UserDetailBasicInformation",
    "UserEmailId",
    "UserOpInfo",
    "UserTermsAndConditionsPage",
    "UserUpdateRequest",
    "WebhookStatusResponse",
    "WebhookStatusResponses",
    "WellKnown",
    "XFapiInteractionId",
]
