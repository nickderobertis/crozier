



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .address_address_type import AddressAddressType
    from .address_data import AddressData
    from .address_data_previous_addresses_item import AddressDataPreviousAddressesItem
    from .age_verification_response import AgeVerificationResponse
    from .age_verification_response_assurance_level import AgeVerificationResponseAssuranceLevel
    from .age_verification_response_attribute_value import AgeVerificationResponseAttributeValue
    from .age_verification_response_privacy_compliance import AgeVerificationResponsePrivacyCompliance
    from .background_checks_response import BackgroundChecksResponse
    from .background_checks_response_overall_risk import BackgroundChecksResponseOverallRisk
    from .basic_customer_data import BasicCustomerData
    from .basic_customer_data_gender import BasicCustomerDataGender
    from .basic_customer_data_marital_status import BasicCustomerDataMaritalStatus
    from .beneficial_owner import BeneficialOwner
    from .biometric_data import BiometricData
    from .check_result import CheckResult
    from .check_result_status import CheckResultStatus
    from .client_configuration import ClientConfiguration
    from .client_configuration_status import ClientConfigurationStatus
    from .client_registration_response import ClientRegistrationResponse
    from .client_registration_response_fapi_compliance_level import ClientRegistrationResponseFapiComplianceLevel
    from .client_registration_response_swiss_standards_support import ClientRegistrationResponseSwissStandardsSupport
    from .compliance_data import ComplianceData
    from .compliance_data_aml_risk_rating import ComplianceDataAmlRiskRating
    from .compliance_data_fatca_status import ComplianceDataFatcaStatus
    from .comprehensive_check_response import ComprehensiveCheckResponse
    from .comprehensive_check_response_overall_risk import ComprehensiveCheckResponseOverallRisk
    from .consent_response import ConsentResponse
    from .consent_response_status import ConsentResponseStatus
    from .consent_status import ConsentStatus
    from .consent_status_status import ConsentStatusStatus
    from .contact_information import ContactInformation
    from .contact_information_preferred_contact_method import ContactInformationPreferredContactMethod
    from .customer_check_response import CustomerCheckResponse
    from .customer_check_response_level_of_assurance import CustomerCheckResponseLevelOfAssurance
    from .customer_data_response import CustomerDataResponse
    from .data_category import DataCategory
    from .data_metadata import DataMetadata
    from .data_metadata_data_classification import DataMetadataDataClassification
    from .data_metadata_verification_status import DataMetadataVerificationStatus
    from .document_data import DocumentData
    from .document_data_document_type import DocumentDataDocumentType
    from .document_to_sign import DocumentToSign
    from .error_response import ErrorResponse
    from .fapi_configuration import FapiConfiguration
    from .fapi_configuration_fapi_compliance_level import FapiConfigurationFapiComplianceLevel
    from .fapi_configuration_fapi_profile import FapiConfigurationFapiProfile
    from .fapi_configuration_fapi_security_profile import FapiConfigurationFapiSecurityProfile
    from .full_customer_dataset import FullCustomerDataset
    from .health_status import HealthStatus
    from .health_status_services import HealthStatusServices
    from .health_status_services_database import HealthStatusServicesDatabase
    from .health_status_services_external_apis import HealthStatusServicesExternalApis
    from .health_status_status import HealthStatusStatus
    from .identification_data import IdentificationData
    from .identification_data_biometric_data import IdentificationDataBiometricData
    from .identification_data_document_type import IdentificationDataDocumentType
    from .identification_data_identification_method import IdentificationDataIdentificationMethod
    from .identification_data_level_of_assurance import IdentificationDataLevelOfAssurance
    from .identification_data_nfc_data import IdentificationDataNfcData
    from .identification_response import IdentificationResponse
    from .identification_response_level_of_assurance import IdentificationResponseLevelOfAssurance
    from .identification_response_status import IdentificationResponseStatus
    from .identification_status_response import IdentificationStatusResponse
    from .identification_status_response_assurance_level import IdentificationStatusResponseAssuranceLevel
    from .identification_status_response_status import IdentificationStatusResponseStatus
    from .introspection_response import IntrospectionResponse
    from .introspection_response_token_type import IntrospectionResponseTokenType
    from .jwk import Jwk
    from .jwk_alg import JwkAlg
    from .jwk_crv import JwkCrv
    from .jwk_kty import JwkKty
    from .jwk_set import JwkSet
    from .jwk_use import JwkUse
    from .kyc_data import KycData
    from .kyc_data_employment_type import KycDataEmploymentType
    from .kyc_data_source_of_funds import KycDataSourceOfFunds
    from .mi_fid_assessment_response import MiFidAssessmentResponse
    from .mi_fid_assessment_response_risk_profile import MiFidAssessmentResponseRiskProfile
    from .mi_fid_assessment_response_suitability_rating import MiFidAssessmentResponseSuitabilityRating
    from .monetary_amount import MonetaryAmount
    from .o_auth_error import OAuthError
    from .o_auth_error_error import OAuthErrorError
    from .oidc_discovery import OidcDiscovery
    from .par_request import ParRequest
    from .par_request_code_challenge_method import ParRequestCodeChallengeMethod
    from .par_request_response_type import ParRequestResponseType
    from .par_response import ParResponse
    from .participant import Participant
    from .participant_endpoints import ParticipantEndpoints
    from .participant_industry import ParticipantIndustry
    from .participant_list import ParticipantList
    from .participant_status import ParticipantStatus
    from .portfolio_sync_response import PortfolioSyncResponse
    from .portfolio_sync_response_status import PortfolioSyncResponseStatus
    from .process_initialization_response import ProcessInitializationResponse
    from .process_status import ProcessStatus
    from .process_status_status import ProcessStatusStatus
    from .process_step_response import ProcessStepResponse
    from .process_step_response_status import ProcessStepResponseStatus
    from .provider_relationship import ProviderRelationship
    from .provider_relationship_relationship_type import ProviderRelationshipRelationshipType
    from .risk_profile import RiskProfile
    from .risk_profile_esg_preferences import RiskProfileEsgPreferences
    from .risk_profile_esg_preferences_esg_importance import RiskProfileEsgPreferencesEsgImportance
    from .risk_profile_investment_experience import RiskProfileInvestmentExperience
    from .risk_profile_investment_horizon import RiskProfileInvestmentHorizon
    from .risk_profile_investment_knowledge import RiskProfileInvestmentKnowledge
    from .risk_profile_investment_objectives_item import RiskProfileInvestmentObjectivesItem
    from .risk_profile_risk_tolerance import RiskProfileRiskTolerance
    from .screening_result import ScreeningResult
    from .screening_result_adverse_media import ScreeningResultAdverseMedia
    from .screening_result_pep_check import ScreeningResultPepCheck
    from .screening_result_sanctions_list import ScreeningResultSanctionsList
    from .signature_response import SignatureResponse
    from .signature_status import SignatureStatus
    from .signature_status_certificate_info import SignatureStatusCertificateInfo
    from .signature_status_status import SignatureStatusStatus
    from .swiss_banking_metadata import SwissBankingMetadata
    from .swiss_banking_metadata_support import SwissBankingMetadataSupport
    from .swiss_banking_metadata_supported_banking_use_cases_item import (
        SwissBankingMetadataSupportedBankingUseCasesItem,
    )
    from .tax_residency import TaxResidency
    from .tin_number import TinNumber
    from .token_response import TokenResponse
    from .token_response_token_type import TokenResponseTokenType
    from .user_info import UserInfo
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AddressAddressType": ".address_address_type",
    "AddressData": ".address_data",
    "AddressDataPreviousAddressesItem": ".address_data_previous_addresses_item",
    "AgeVerificationResponse": ".age_verification_response",
    "AgeVerificationResponseAssuranceLevel": ".age_verification_response_assurance_level",
    "AgeVerificationResponseAttributeValue": ".age_verification_response_attribute_value",
    "AgeVerificationResponsePrivacyCompliance": ".age_verification_response_privacy_compliance",
    "BackgroundChecksResponse": ".background_checks_response",
    "BackgroundChecksResponseOverallRisk": ".background_checks_response_overall_risk",
    "BasicCustomerData": ".basic_customer_data",
    "BasicCustomerDataGender": ".basic_customer_data_gender",
    "BasicCustomerDataMaritalStatus": ".basic_customer_data_marital_status",
    "BeneficialOwner": ".beneficial_owner",
    "BiometricData": ".biometric_data",
    "CheckResult": ".check_result",
    "CheckResultStatus": ".check_result_status",
    "ClientConfiguration": ".client_configuration",
    "ClientConfigurationStatus": ".client_configuration_status",
    "ClientRegistrationResponse": ".client_registration_response",
    "ClientRegistrationResponseFapiComplianceLevel": ".client_registration_response_fapi_compliance_level",
    "ClientRegistrationResponseSwissStandardsSupport": ".client_registration_response_swiss_standards_support",
    "ComplianceData": ".compliance_data",
    "ComplianceDataAmlRiskRating": ".compliance_data_aml_risk_rating",
    "ComplianceDataFatcaStatus": ".compliance_data_fatca_status",
    "ComprehensiveCheckResponse": ".comprehensive_check_response",
    "ComprehensiveCheckResponseOverallRisk": ".comprehensive_check_response_overall_risk",
    "ConsentResponse": ".consent_response",
    "ConsentResponseStatus": ".consent_response_status",
    "ConsentStatus": ".consent_status",
    "ConsentStatusStatus": ".consent_status_status",
    "ContactInformation": ".contact_information",
    "ContactInformationPreferredContactMethod": ".contact_information_preferred_contact_method",
    "CustomerCheckResponse": ".customer_check_response",
    "CustomerCheckResponseLevelOfAssurance": ".customer_check_response_level_of_assurance",
    "CustomerDataResponse": ".customer_data_response",
    "DataCategory": ".data_category",
    "DataMetadata": ".data_metadata",
    "DataMetadataDataClassification": ".data_metadata_data_classification",
    "DataMetadataVerificationStatus": ".data_metadata_verification_status",
    "DocumentData": ".document_data",
    "DocumentDataDocumentType": ".document_data_document_type",
    "DocumentToSign": ".document_to_sign",
    "ErrorResponse": ".error_response",
    "FapiConfiguration": ".fapi_configuration",
    "FapiConfigurationFapiComplianceLevel": ".fapi_configuration_fapi_compliance_level",
    "FapiConfigurationFapiProfile": ".fapi_configuration_fapi_profile",
    "FapiConfigurationFapiSecurityProfile": ".fapi_configuration_fapi_security_profile",
    "FullCustomerDataset": ".full_customer_dataset",
    "HealthStatus": ".health_status",
    "HealthStatusServices": ".health_status_services",
    "HealthStatusServicesDatabase": ".health_status_services_database",
    "HealthStatusServicesExternalApis": ".health_status_services_external_apis",
    "HealthStatusStatus": ".health_status_status",
    "IdentificationData": ".identification_data",
    "IdentificationDataBiometricData": ".identification_data_biometric_data",
    "IdentificationDataDocumentType": ".identification_data_document_type",
    "IdentificationDataIdentificationMethod": ".identification_data_identification_method",
    "IdentificationDataLevelOfAssurance": ".identification_data_level_of_assurance",
    "IdentificationDataNfcData": ".identification_data_nfc_data",
    "IdentificationResponse": ".identification_response",
    "IdentificationResponseLevelOfAssurance": ".identification_response_level_of_assurance",
    "IdentificationResponseStatus": ".identification_response_status",
    "IdentificationStatusResponse": ".identification_status_response",
    "IdentificationStatusResponseAssuranceLevel": ".identification_status_response_assurance_level",
    "IdentificationStatusResponseStatus": ".identification_status_response_status",
    "IntrospectionResponse": ".introspection_response",
    "IntrospectionResponseTokenType": ".introspection_response_token_type",
    "Jwk": ".jwk",
    "JwkAlg": ".jwk_alg",
    "JwkCrv": ".jwk_crv",
    "JwkKty": ".jwk_kty",
    "JwkSet": ".jwk_set",
    "JwkUse": ".jwk_use",
    "KycData": ".kyc_data",
    "KycDataEmploymentType": ".kyc_data_employment_type",
    "KycDataSourceOfFunds": ".kyc_data_source_of_funds",
    "MiFidAssessmentResponse": ".mi_fid_assessment_response",
    "MiFidAssessmentResponseRiskProfile": ".mi_fid_assessment_response_risk_profile",
    "MiFidAssessmentResponseSuitabilityRating": ".mi_fid_assessment_response_suitability_rating",
    "MonetaryAmount": ".monetary_amount",
    "OAuthError": ".o_auth_error",
    "OAuthErrorError": ".o_auth_error_error",
    "OidcDiscovery": ".oidc_discovery",
    "ParRequest": ".par_request",
    "ParRequestCodeChallengeMethod": ".par_request_code_challenge_method",
    "ParRequestResponseType": ".par_request_response_type",
    "ParResponse": ".par_response",
    "Participant": ".participant",
    "ParticipantEndpoints": ".participant_endpoints",
    "ParticipantIndustry": ".participant_industry",
    "ParticipantList": ".participant_list",
    "ParticipantStatus": ".participant_status",
    "PortfolioSyncResponse": ".portfolio_sync_response",
    "PortfolioSyncResponseStatus": ".portfolio_sync_response_status",
    "ProcessInitializationResponse": ".process_initialization_response",
    "ProcessStatus": ".process_status",
    "ProcessStatusStatus": ".process_status_status",
    "ProcessStepResponse": ".process_step_response",
    "ProcessStepResponseStatus": ".process_step_response_status",
    "ProviderRelationship": ".provider_relationship",
    "ProviderRelationshipRelationshipType": ".provider_relationship_relationship_type",
    "RiskProfile": ".risk_profile",
    "RiskProfileEsgPreferences": ".risk_profile_esg_preferences",
    "RiskProfileEsgPreferencesEsgImportance": ".risk_profile_esg_preferences_esg_importance",
    "RiskProfileInvestmentExperience": ".risk_profile_investment_experience",
    "RiskProfileInvestmentHorizon": ".risk_profile_investment_horizon",
    "RiskProfileInvestmentKnowledge": ".risk_profile_investment_knowledge",
    "RiskProfileInvestmentObjectivesItem": ".risk_profile_investment_objectives_item",
    "RiskProfileRiskTolerance": ".risk_profile_risk_tolerance",
    "ScreeningResult": ".screening_result",
    "ScreeningResultAdverseMedia": ".screening_result_adverse_media",
    "ScreeningResultPepCheck": ".screening_result_pep_check",
    "ScreeningResultSanctionsList": ".screening_result_sanctions_list",
    "SignatureResponse": ".signature_response",
    "SignatureStatus": ".signature_status",
    "SignatureStatusCertificateInfo": ".signature_status_certificate_info",
    "SignatureStatusStatus": ".signature_status_status",
    "SwissBankingMetadata": ".swiss_banking_metadata",
    "SwissBankingMetadataSupport": ".swiss_banking_metadata_support",
    "SwissBankingMetadataSupportedBankingUseCasesItem": ".swiss_banking_metadata_supported_banking_use_cases_item",
    "TaxResidency": ".tax_residency",
    "TinNumber": ".tin_number",
    "TokenResponse": ".token_response",
    "TokenResponseTokenType": ".token_response_token_type",
    "UserInfo": ".user_info",
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
    "Address",
    "AddressAddressType",
    "AddressData",
    "AddressDataPreviousAddressesItem",
    "AgeVerificationResponse",
    "AgeVerificationResponseAssuranceLevel",
    "AgeVerificationResponseAttributeValue",
    "AgeVerificationResponsePrivacyCompliance",
    "BackgroundChecksResponse",
    "BackgroundChecksResponseOverallRisk",
    "BasicCustomerData",
    "BasicCustomerDataGender",
    "BasicCustomerDataMaritalStatus",
    "BeneficialOwner",
    "BiometricData",
    "CheckResult",
    "CheckResultStatus",
    "ClientConfiguration",
    "ClientConfigurationStatus",
    "ClientRegistrationResponse",
    "ClientRegistrationResponseFapiComplianceLevel",
    "ClientRegistrationResponseSwissStandardsSupport",
    "ComplianceData",
    "ComplianceDataAmlRiskRating",
    "ComplianceDataFatcaStatus",
    "ComprehensiveCheckResponse",
    "ComprehensiveCheckResponseOverallRisk",
    "ConsentResponse",
    "ConsentResponseStatus",
    "ConsentStatus",
    "ConsentStatusStatus",
    "ContactInformation",
    "ContactInformationPreferredContactMethod",
    "CustomerCheckResponse",
    "CustomerCheckResponseLevelOfAssurance",
    "CustomerDataResponse",
    "DataCategory",
    "DataMetadata",
    "DataMetadataDataClassification",
    "DataMetadataVerificationStatus",
    "DocumentData",
    "DocumentDataDocumentType",
    "DocumentToSign",
    "ErrorResponse",
    "FapiConfiguration",
    "FapiConfigurationFapiComplianceLevel",
    "FapiConfigurationFapiProfile",
    "FapiConfigurationFapiSecurityProfile",
    "FullCustomerDataset",
    "HealthStatus",
    "HealthStatusServices",
    "HealthStatusServicesDatabase",
    "HealthStatusServicesExternalApis",
    "HealthStatusStatus",
    "IdentificationData",
    "IdentificationDataBiometricData",
    "IdentificationDataDocumentType",
    "IdentificationDataIdentificationMethod",
    "IdentificationDataLevelOfAssurance",
    "IdentificationDataNfcData",
    "IdentificationResponse",
    "IdentificationResponseLevelOfAssurance",
    "IdentificationResponseStatus",
    "IdentificationStatusResponse",
    "IdentificationStatusResponseAssuranceLevel",
    "IdentificationStatusResponseStatus",
    "IntrospectionResponse",
    "IntrospectionResponseTokenType",
    "Jwk",
    "JwkAlg",
    "JwkCrv",
    "JwkKty",
    "JwkSet",
    "JwkUse",
    "KycData",
    "KycDataEmploymentType",
    "KycDataSourceOfFunds",
    "MiFidAssessmentResponse",
    "MiFidAssessmentResponseRiskProfile",
    "MiFidAssessmentResponseSuitabilityRating",
    "MonetaryAmount",
    "OAuthError",
    "OAuthErrorError",
    "OidcDiscovery",
    "ParRequest",
    "ParRequestCodeChallengeMethod",
    "ParRequestResponseType",
    "ParResponse",
    "Participant",
    "ParticipantEndpoints",
    "ParticipantIndustry",
    "ParticipantList",
    "ParticipantStatus",
    "PortfolioSyncResponse",
    "PortfolioSyncResponseStatus",
    "ProcessInitializationResponse",
    "ProcessStatus",
    "ProcessStatusStatus",
    "ProcessStepResponse",
    "ProcessStepResponseStatus",
    "ProviderRelationship",
    "ProviderRelationshipRelationshipType",
    "RiskProfile",
    "RiskProfileEsgPreferences",
    "RiskProfileEsgPreferencesEsgImportance",
    "RiskProfileInvestmentExperience",
    "RiskProfileInvestmentHorizon",
    "RiskProfileInvestmentKnowledge",
    "RiskProfileInvestmentObjectivesItem",
    "RiskProfileRiskTolerance",
    "ScreeningResult",
    "ScreeningResultAdverseMedia",
    "ScreeningResultPepCheck",
    "ScreeningResultSanctionsList",
    "SignatureResponse",
    "SignatureStatus",
    "SignatureStatusCertificateInfo",
    "SignatureStatusStatus",
    "SwissBankingMetadata",
    "SwissBankingMetadataSupport",
    "SwissBankingMetadataSupportedBankingUseCasesItem",
    "TaxResidency",
    "TinNumber",
    "TokenResponse",
    "TokenResponseTokenType",
    "UserInfo",
]
