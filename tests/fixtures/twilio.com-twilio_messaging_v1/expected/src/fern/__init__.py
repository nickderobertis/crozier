



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BrandRegistrationsEnumBrandFeedback,
        BrandRegistrationsEnumIdentityStatus,
        BrandRegistrationsEnumStatus,
        BrandVettingEnumVettingProvider,
        CreateServiceRequestFallbackMethod,
        CreateServiceRequestInboundMethod,
        ListAlphaSenderResponse,
        ListAlphaSenderResponseMeta,
        ListBrandRegistrationsResponse,
        ListBrandRegistrationsResponseMeta,
        ListBrandVettingResponse,
        ListBrandVettingResponseMeta,
        ListPhoneNumberResponse,
        ListPhoneNumberResponseMeta,
        ListServiceResponse,
        ListServiceResponseMeta,
        ListShortCodeResponse,
        ListShortCodeResponseMeta,
        ListTollfreeVerificationResponse,
        ListTollfreeVerificationResponseMeta,
        ListUsAppToPersonResponse,
        ListUsAppToPersonResponseMeta,
        MessagingV1BrandRegistrations,
        MessagingV1BrandRegistrationsBrandRegistrationOtp,
        MessagingV1BrandRegistrationsBrandVetting,
        MessagingV1Deactivation,
        MessagingV1DomainCertV4,
        MessagingV1DomainConfig,
        MessagingV1DomainConfigMessagingService,
        MessagingV1ExternalCampaign,
        MessagingV1LinkshorteningMessagingService,
        MessagingV1Service,
        MessagingV1ServiceAlphaSender,
        MessagingV1ServiceFallbackMethod,
        MessagingV1ServiceInboundMethod,
        MessagingV1ServicePhoneNumber,
        MessagingV1ServiceShortCode,
        MessagingV1ServiceUsAppToPerson,
        MessagingV1ServiceUsAppToPersonUsecase,
        MessagingV1TollfreeVerification,
        MessagingV1Usecase,
        ServiceEnumScanMessageContent,
        TollfreeVerificationEnumOptInType,
        TollfreeVerificationEnumStatus,
        UpdateServiceRequestFallbackMethod,
        UpdateServiceRequestInboundMethod,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BrandRegistrationsEnumBrandFeedback": ".types",
    "BrandRegistrationsEnumIdentityStatus": ".types",
    "BrandRegistrationsEnumStatus": ".types",
    "BrandVettingEnumVettingProvider": ".types",
    "CreateServiceRequestFallbackMethod": ".types",
    "CreateServiceRequestInboundMethod": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ListAlphaSenderResponse": ".types",
    "ListAlphaSenderResponseMeta": ".types",
    "ListBrandRegistrationsResponse": ".types",
    "ListBrandRegistrationsResponseMeta": ".types",
    "ListBrandVettingResponse": ".types",
    "ListBrandVettingResponseMeta": ".types",
    "ListPhoneNumberResponse": ".types",
    "ListPhoneNumberResponseMeta": ".types",
    "ListServiceResponse": ".types",
    "ListServiceResponseMeta": ".types",
    "ListShortCodeResponse": ".types",
    "ListShortCodeResponseMeta": ".types",
    "ListTollfreeVerificationResponse": ".types",
    "ListTollfreeVerificationResponseMeta": ".types",
    "ListUsAppToPersonResponse": ".types",
    "ListUsAppToPersonResponseMeta": ".types",
    "MessagingV1BrandRegistrations": ".types",
    "MessagingV1BrandRegistrationsBrandRegistrationOtp": ".types",
    "MessagingV1BrandRegistrationsBrandVetting": ".types",
    "MessagingV1Deactivation": ".types",
    "MessagingV1DomainCertV4": ".types",
    "MessagingV1DomainConfig": ".types",
    "MessagingV1DomainConfigMessagingService": ".types",
    "MessagingV1ExternalCampaign": ".types",
    "MessagingV1LinkshorteningMessagingService": ".types",
    "MessagingV1Service": ".types",
    "MessagingV1ServiceAlphaSender": ".types",
    "MessagingV1ServiceFallbackMethod": ".types",
    "MessagingV1ServiceInboundMethod": ".types",
    "MessagingV1ServicePhoneNumber": ".types",
    "MessagingV1ServiceShortCode": ".types",
    "MessagingV1ServiceUsAppToPerson": ".types",
    "MessagingV1ServiceUsAppToPersonUsecase": ".types",
    "MessagingV1TollfreeVerification": ".types",
    "MessagingV1Usecase": ".types",
    "ServiceEnumScanMessageContent": ".types",
    "TollfreeVerificationEnumOptInType": ".types",
    "TollfreeVerificationEnumStatus": ".types",
    "UpdateServiceRequestFallbackMethod": ".types",
    "UpdateServiceRequestInboundMethod": ".types",
    "__version__": ".version",
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
    "AsyncFernApi",
    "BrandRegistrationsEnumBrandFeedback",
    "BrandRegistrationsEnumIdentityStatus",
    "BrandRegistrationsEnumStatus",
    "BrandVettingEnumVettingProvider",
    "CreateServiceRequestFallbackMethod",
    "CreateServiceRequestInboundMethod",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
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
    "__version__",
]
