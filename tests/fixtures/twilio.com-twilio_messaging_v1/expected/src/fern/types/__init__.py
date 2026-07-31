



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .brand_registrations_enum_brand_feedback import BrandRegistrationsEnumBrandFeedback
    from .brand_registrations_enum_identity_status import BrandRegistrationsEnumIdentityStatus
    from .brand_registrations_enum_status import BrandRegistrationsEnumStatus
    from .brand_vetting_enum_vetting_provider import BrandVettingEnumVettingProvider
    from .create_service_request_fallback_method import CreateServiceRequestFallbackMethod
    from .create_service_request_inbound_method import CreateServiceRequestInboundMethod
    from .list_alpha_sender_response import ListAlphaSenderResponse
    from .list_alpha_sender_response_meta import ListAlphaSenderResponseMeta
    from .list_brand_registrations_response import ListBrandRegistrationsResponse
    from .list_brand_registrations_response_meta import ListBrandRegistrationsResponseMeta
    from .list_brand_vetting_response import ListBrandVettingResponse
    from .list_brand_vetting_response_meta import ListBrandVettingResponseMeta
    from .list_phone_number_response import ListPhoneNumberResponse
    from .list_phone_number_response_meta import ListPhoneNumberResponseMeta
    from .list_service_response import ListServiceResponse
    from .list_service_response_meta import ListServiceResponseMeta
    from .list_short_code_response import ListShortCodeResponse
    from .list_short_code_response_meta import ListShortCodeResponseMeta
    from .list_tollfree_verification_response import ListTollfreeVerificationResponse
    from .list_tollfree_verification_response_meta import ListTollfreeVerificationResponseMeta
    from .list_us_app_to_person_response import ListUsAppToPersonResponse
    from .list_us_app_to_person_response_meta import ListUsAppToPersonResponseMeta
    from .messaging_v1brand_registrations import MessagingV1BrandRegistrations
    from .messaging_v1brand_registrations_brand_registration_otp import (
        MessagingV1BrandRegistrationsBrandRegistrationOtp,
    )
    from .messaging_v1brand_registrations_brand_vetting import MessagingV1BrandRegistrationsBrandVetting
    from .messaging_v1deactivation import MessagingV1Deactivation
    from .messaging_v1domain_cert_v4 import MessagingV1DomainCertV4
    from .messaging_v1domain_config import MessagingV1DomainConfig
    from .messaging_v1domain_config_messaging_service import MessagingV1DomainConfigMessagingService
    from .messaging_v1external_campaign import MessagingV1ExternalCampaign
    from .messaging_v1linkshortening_messaging_service import MessagingV1LinkshorteningMessagingService
    from .messaging_v1service import MessagingV1Service
    from .messaging_v1service_alpha_sender import MessagingV1ServiceAlphaSender
    from .messaging_v1service_fallback_method import MessagingV1ServiceFallbackMethod
    from .messaging_v1service_inbound_method import MessagingV1ServiceInboundMethod
    from .messaging_v1service_phone_number import MessagingV1ServicePhoneNumber
    from .messaging_v1service_short_code import MessagingV1ServiceShortCode
    from .messaging_v1service_us_app_to_person import MessagingV1ServiceUsAppToPerson
    from .messaging_v1service_us_app_to_person_usecase import MessagingV1ServiceUsAppToPersonUsecase
    from .messaging_v1tollfree_verification import MessagingV1TollfreeVerification
    from .messaging_v1usecase import MessagingV1Usecase
    from .service_enum_scan_message_content import ServiceEnumScanMessageContent
    from .tollfree_verification_enum_opt_in_type import TollfreeVerificationEnumOptInType
    from .tollfree_verification_enum_status import TollfreeVerificationEnumStatus
    from .update_service_request_fallback_method import UpdateServiceRequestFallbackMethod
    from .update_service_request_inbound_method import UpdateServiceRequestInboundMethod
_dynamic_imports: typing.Dict[str, str] = {
    "BrandRegistrationsEnumBrandFeedback": ".brand_registrations_enum_brand_feedback",
    "BrandRegistrationsEnumIdentityStatus": ".brand_registrations_enum_identity_status",
    "BrandRegistrationsEnumStatus": ".brand_registrations_enum_status",
    "BrandVettingEnumVettingProvider": ".brand_vetting_enum_vetting_provider",
    "CreateServiceRequestFallbackMethod": ".create_service_request_fallback_method",
    "CreateServiceRequestInboundMethod": ".create_service_request_inbound_method",
    "ListAlphaSenderResponse": ".list_alpha_sender_response",
    "ListAlphaSenderResponseMeta": ".list_alpha_sender_response_meta",
    "ListBrandRegistrationsResponse": ".list_brand_registrations_response",
    "ListBrandRegistrationsResponseMeta": ".list_brand_registrations_response_meta",
    "ListBrandVettingResponse": ".list_brand_vetting_response",
    "ListBrandVettingResponseMeta": ".list_brand_vetting_response_meta",
    "ListPhoneNumberResponse": ".list_phone_number_response",
    "ListPhoneNumberResponseMeta": ".list_phone_number_response_meta",
    "ListServiceResponse": ".list_service_response",
    "ListServiceResponseMeta": ".list_service_response_meta",
    "ListShortCodeResponse": ".list_short_code_response",
    "ListShortCodeResponseMeta": ".list_short_code_response_meta",
    "ListTollfreeVerificationResponse": ".list_tollfree_verification_response",
    "ListTollfreeVerificationResponseMeta": ".list_tollfree_verification_response_meta",
    "ListUsAppToPersonResponse": ".list_us_app_to_person_response",
    "ListUsAppToPersonResponseMeta": ".list_us_app_to_person_response_meta",
    "MessagingV1BrandRegistrations": ".messaging_v1brand_registrations",
    "MessagingV1BrandRegistrationsBrandRegistrationOtp": ".messaging_v1brand_registrations_brand_registration_otp",
    "MessagingV1BrandRegistrationsBrandVetting": ".messaging_v1brand_registrations_brand_vetting",
    "MessagingV1Deactivation": ".messaging_v1deactivation",
    "MessagingV1DomainCertV4": ".messaging_v1domain_cert_v4",
    "MessagingV1DomainConfig": ".messaging_v1domain_config",
    "MessagingV1DomainConfigMessagingService": ".messaging_v1domain_config_messaging_service",
    "MessagingV1ExternalCampaign": ".messaging_v1external_campaign",
    "MessagingV1LinkshorteningMessagingService": ".messaging_v1linkshortening_messaging_service",
    "MessagingV1Service": ".messaging_v1service",
    "MessagingV1ServiceAlphaSender": ".messaging_v1service_alpha_sender",
    "MessagingV1ServiceFallbackMethod": ".messaging_v1service_fallback_method",
    "MessagingV1ServiceInboundMethod": ".messaging_v1service_inbound_method",
    "MessagingV1ServicePhoneNumber": ".messaging_v1service_phone_number",
    "MessagingV1ServiceShortCode": ".messaging_v1service_short_code",
    "MessagingV1ServiceUsAppToPerson": ".messaging_v1service_us_app_to_person",
    "MessagingV1ServiceUsAppToPersonUsecase": ".messaging_v1service_us_app_to_person_usecase",
    "MessagingV1TollfreeVerification": ".messaging_v1tollfree_verification",
    "MessagingV1Usecase": ".messaging_v1usecase",
    "ServiceEnumScanMessageContent": ".service_enum_scan_message_content",
    "TollfreeVerificationEnumOptInType": ".tollfree_verification_enum_opt_in_type",
    "TollfreeVerificationEnumStatus": ".tollfree_verification_enum_status",
    "UpdateServiceRequestFallbackMethod": ".update_service_request_fallback_method",
    "UpdateServiceRequestInboundMethod": ".update_service_request_inbound_method",
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
    "BrandRegistrationsEnumBrandFeedback",
    "BrandRegistrationsEnumIdentityStatus",
    "BrandRegistrationsEnumStatus",
    "BrandVettingEnumVettingProvider",
    "CreateServiceRequestFallbackMethod",
    "CreateServiceRequestInboundMethod",
    "ListAlphaSenderResponse",
    "ListAlphaSenderResponseMeta",
    "ListBrandRegistrationsResponse",
    "ListBrandRegistrationsResponseMeta",
    "ListBrandVettingResponse",
    "ListBrandVettingResponseMeta",
    "ListPhoneNumberResponse",
    "ListPhoneNumberResponseMeta",
    "ListServiceResponse",
    "ListServiceResponseMeta",
    "ListShortCodeResponse",
    "ListShortCodeResponseMeta",
    "ListTollfreeVerificationResponse",
    "ListTollfreeVerificationResponseMeta",
    "ListUsAppToPersonResponse",
    "ListUsAppToPersonResponseMeta",
    "MessagingV1BrandRegistrations",
    "MessagingV1BrandRegistrationsBrandRegistrationOtp",
    "MessagingV1BrandRegistrationsBrandVetting",
    "MessagingV1Deactivation",
    "MessagingV1DomainCertV4",
    "MessagingV1DomainConfig",
    "MessagingV1DomainConfigMessagingService",
    "MessagingV1ExternalCampaign",
    "MessagingV1LinkshorteningMessagingService",
    "MessagingV1Service",
    "MessagingV1ServiceAlphaSender",
    "MessagingV1ServiceFallbackMethod",
    "MessagingV1ServiceInboundMethod",
    "MessagingV1ServicePhoneNumber",
    "MessagingV1ServiceShortCode",
    "MessagingV1ServiceUsAppToPerson",
    "MessagingV1ServiceUsAppToPersonUsecase",
    "MessagingV1TollfreeVerification",
    "MessagingV1Usecase",
    "ServiceEnumScanMessageContent",
    "TollfreeVerificationEnumOptInType",
    "TollfreeVerificationEnumStatus",
    "UpdateServiceRequestFallbackMethod",
    "UpdateServiceRequestInboundMethod",
]
