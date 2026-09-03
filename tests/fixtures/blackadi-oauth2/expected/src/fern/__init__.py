



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ForbiddenErrorBody,
        GetAuthorizationRequestCodeChallengeMethod,
        GetAuthorizationRequestPrompt,
        GetAuthorizationRequestResponseType,
        GetFapiConfigResponse,
        GetFapiConfigResponseMode,
        GetFapiConfigResponseSpecs,
        GetFapiStatusResponse,
        GetHealthAllResponse,
        GetHealthAllResponseChecks,
        GetHealthAllResponseChecksAuthlete,
        GetHealthAllResponseChecksRedis,
        GetHealthAuthleteRequestExtended,
        GetHealthResponse,
        GetLogoutRequestBackchannel,
        GetTokenListResponse,
        PostCibaCompleteRequestResult,
        PostDeviceAuthorizationResponse,
        PostDeviceCompleteRequestResult,
        PostIntrospectionStandardResponse,
        PostLogoutRequestBackchannel,
        PostParResponse,
        PostSessionConsentRequestDecision,
        PostTokenRequestGrantType,
        PostTokenResponse,
        PostTokenResponseTokenType,
        PostVciDeferredIssueRequestOrder,
    )
    from .errors import (
        BadGatewayError,
        BadRequestError,
        ForbiddenError,
        InternalServerError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadGatewayError": ".errors",
    "BadRequestError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "ForbiddenErrorBody": ".types",
    "GetAuthorizationRequestCodeChallengeMethod": ".types",
    "GetAuthorizationRequestPrompt": ".types",
    "GetAuthorizationRequestResponseType": ".types",
    "GetFapiConfigResponse": ".types",
    "GetFapiConfigResponseMode": ".types",
    "GetFapiConfigResponseSpecs": ".types",
    "GetFapiStatusResponse": ".types",
    "GetHealthAllResponse": ".types",
    "GetHealthAllResponseChecks": ".types",
    "GetHealthAllResponseChecksAuthlete": ".types",
    "GetHealthAllResponseChecksRedis": ".types",
    "GetHealthAuthleteRequestExtended": ".types",
    "GetHealthResponse": ".types",
    "GetLogoutRequestBackchannel": ".types",
    "GetTokenListResponse": ".types",
    "InternalServerError": ".errors",
    "NotFoundError": ".errors",
    "PostCibaCompleteRequestResult": ".types",
    "PostDeviceAuthorizationResponse": ".types",
    "PostDeviceCompleteRequestResult": ".types",
    "PostIntrospectionStandardResponse": ".types",
    "PostLogoutRequestBackchannel": ".types",
    "PostParResponse": ".types",
    "PostSessionConsentRequestDecision": ".types",
    "PostTokenRequestGrantType": ".types",
    "PostTokenResponse": ".types",
    "PostTokenResponseTokenType": ".types",
    "PostVciDeferredIssueRequestOrder": ".types",
    "ServiceUnavailableError": ".errors",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
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
    "BadGatewayError",
    "BadRequestError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "ForbiddenErrorBody",
    "GetAuthorizationRequestCodeChallengeMethod",
    "GetAuthorizationRequestPrompt",
    "GetAuthorizationRequestResponseType",
    "GetFapiConfigResponse",
    "GetFapiConfigResponseMode",
    "GetFapiConfigResponseSpecs",
    "GetFapiStatusResponse",
    "GetHealthAllResponse",
    "GetHealthAllResponseChecks",
    "GetHealthAllResponseChecksAuthlete",
    "GetHealthAllResponseChecksRedis",
    "GetHealthAuthleteRequestExtended",
    "GetHealthResponse",
    "GetLogoutRequestBackchannel",
    "GetTokenListResponse",
    "InternalServerError",
    "NotFoundError",
    "PostCibaCompleteRequestResult",
    "PostDeviceAuthorizationResponse",
    "PostDeviceCompleteRequestResult",
    "PostIntrospectionStandardResponse",
    "PostLogoutRequestBackchannel",
    "PostParResponse",
    "PostSessionConsentRequestDecision",
    "PostTokenRequestGrantType",
    "PostTokenResponse",
    "PostTokenResponseTokenType",
    "PostVciDeferredIssueRequestOrder",
    "ServiceUnavailableError",
    "TooManyRequestsError",
    "UnauthorizedError",
    "__version__",
]
