



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BadRequestErrorBody,
        BillingVerificationError,
        BillingVerificationErrorCode,
        Error,
        ExcludedBlocMember,
        FieldViolation,
        FiveFactorBlocScorecard,
        FiveFactorBlocScorecardMethodologyVersion,
        FiveFactorCountryScorecard,
        FiveFactorCountryScorecardMethodologyVersion,
        FiveFactorCountryScorecardSummary,
        FiveFactorPillar,
        FiveFactorPillarSummary,
        ForbiddenErrorBody,
        ForbiddenErrorBodyCode,
        GatewayError,
        GatewayErrorError,
        GetBlocScorecardRequest,
        GetBlocScorecardResponse,
        GetBlocScorecardResponseOne,
        GetBlocScorecardResponseOneUnavailableReason,
        GetBlocScorecardResponseZero,
        GetBlocScorecardResponseZeroUnavailableReason,
        GetFiveFactorScorecardRequest,
        GetFiveFactorScorecardResponse,
        GetFiveFactorScorecardResponseOne,
        GetFiveFactorScorecardResponseOneUnavailableReason,
        GetFiveFactorScorecardResponseZero,
        GetFiveFactorScorecardResponseZeroUnavailableReason,
        InvalidRequestBodyError,
        JmespathProjectionError,
        ListFiveFactorScorecardsRequest,
        ListFiveFactorScorecardsResponse,
        ListFiveFactorScorecardsResponseComputedAt,
        ListFiveFactorScorecardsResponseComputedAtComputedAt,
        ListFiveFactorScorecardsResponseComputedAtMethodologyVersion,
        ListFiveFactorScorecardsResponseComputedAtUnavailableReason,
        ListFiveFactorScorecardsResponseZero,
        ListFiveFactorScorecardsResponseZeroMethodologyVersion,
        ListFiveFactorScorecardsResponseZeroUnavailableReason,
        RateLimitError,
        ScorecardEvidence,
        ScorecardMemberWeight,
        ScorecardObservation,
        ServiceUnavailableErrorBody,
        TooManyRequestsErrorBody,
        UnauthorizedErrorBody,
        ValidationError,
    )
    from .errors import (
        BadRequestError,
        ForbiddenError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    )
    from . import scorecard_service
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "BillingVerificationError": ".types",
    "BillingVerificationErrorCode": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "ExcludedBlocMember": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FieldViolation": ".types",
    "FiveFactorBlocScorecard": ".types",
    "FiveFactorBlocScorecardMethodologyVersion": ".types",
    "FiveFactorCountryScorecard": ".types",
    "FiveFactorCountryScorecardMethodologyVersion": ".types",
    "FiveFactorCountryScorecardSummary": ".types",
    "FiveFactorPillar": ".types",
    "FiveFactorPillarSummary": ".types",
    "ForbiddenError": ".errors",
    "ForbiddenErrorBody": ".types",
    "ForbiddenErrorBodyCode": ".types",
    "GatewayError": ".types",
    "GatewayErrorError": ".types",
    "GetBlocScorecardRequest": ".types",
    "GetBlocScorecardResponse": ".types",
    "GetBlocScorecardResponseOne": ".types",
    "GetBlocScorecardResponseOneUnavailableReason": ".types",
    "GetBlocScorecardResponseZero": ".types",
    "GetBlocScorecardResponseZeroUnavailableReason": ".types",
    "GetFiveFactorScorecardRequest": ".types",
    "GetFiveFactorScorecardResponse": ".types",
    "GetFiveFactorScorecardResponseOne": ".types",
    "GetFiveFactorScorecardResponseOneUnavailableReason": ".types",
    "GetFiveFactorScorecardResponseZero": ".types",
    "GetFiveFactorScorecardResponseZeroUnavailableReason": ".types",
    "InvalidRequestBodyError": ".types",
    "JmespathProjectionError": ".types",
    "ListFiveFactorScorecardsRequest": ".types",
    "ListFiveFactorScorecardsResponse": ".types",
    "ListFiveFactorScorecardsResponseComputedAt": ".types",
    "ListFiveFactorScorecardsResponseComputedAtComputedAt": ".types",
    "ListFiveFactorScorecardsResponseComputedAtMethodologyVersion": ".types",
    "ListFiveFactorScorecardsResponseComputedAtUnavailableReason": ".types",
    "ListFiveFactorScorecardsResponseZero": ".types",
    "ListFiveFactorScorecardsResponseZeroMethodologyVersion": ".types",
    "ListFiveFactorScorecardsResponseZeroUnavailableReason": ".types",
    "RateLimitError": ".types",
    "ScorecardEvidence": ".types",
    "ScorecardMemberWeight": ".types",
    "ScorecardObservation": ".types",
    "ServiceUnavailableError": ".errors",
    "ServiceUnavailableErrorBody": ".types",
    "TooManyRequestsError": ".errors",
    "TooManyRequestsErrorBody": ".types",
    "UnauthorizedError": ".errors",
    "UnauthorizedErrorBody": ".types",
    "ValidationError": ".types",
    "__version__": ".version",
    "scorecard_service": ".scorecard_service",
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
    "BadRequestError",
    "BadRequestErrorBody",
    "BillingVerificationError",
    "BillingVerificationErrorCode",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "ExcludedBlocMember",
    "FernApi",
    "FernApiEnvironment",
    "FieldViolation",
    "FiveFactorBlocScorecard",
    "FiveFactorBlocScorecardMethodologyVersion",
    "FiveFactorCountryScorecard",
    "FiveFactorCountryScorecardMethodologyVersion",
    "FiveFactorCountryScorecardSummary",
    "FiveFactorPillar",
    "FiveFactorPillarSummary",
    "ForbiddenError",
    "ForbiddenErrorBody",
    "ForbiddenErrorBodyCode",
    "GatewayError",
    "GatewayErrorError",
    "GetBlocScorecardRequest",
    "GetBlocScorecardResponse",
    "GetBlocScorecardResponseOne",
    "GetBlocScorecardResponseOneUnavailableReason",
    "GetBlocScorecardResponseZero",
    "GetBlocScorecardResponseZeroUnavailableReason",
    "GetFiveFactorScorecardRequest",
    "GetFiveFactorScorecardResponse",
    "GetFiveFactorScorecardResponseOne",
    "GetFiveFactorScorecardResponseOneUnavailableReason",
    "GetFiveFactorScorecardResponseZero",
    "GetFiveFactorScorecardResponseZeroUnavailableReason",
    "InvalidRequestBodyError",
    "JmespathProjectionError",
    "ListFiveFactorScorecardsRequest",
    "ListFiveFactorScorecardsResponse",
    "ListFiveFactorScorecardsResponseComputedAt",
    "ListFiveFactorScorecardsResponseComputedAtComputedAt",
    "ListFiveFactorScorecardsResponseComputedAtMethodologyVersion",
    "ListFiveFactorScorecardsResponseComputedAtUnavailableReason",
    "ListFiveFactorScorecardsResponseZero",
    "ListFiveFactorScorecardsResponseZeroMethodologyVersion",
    "ListFiveFactorScorecardsResponseZeroUnavailableReason",
    "RateLimitError",
    "ScorecardEvidence",
    "ScorecardMemberWeight",
    "ScorecardObservation",
    "ServiceUnavailableError",
    "ServiceUnavailableErrorBody",
    "TooManyRequestsError",
    "TooManyRequestsErrorBody",
    "UnauthorizedError",
    "UnauthorizedErrorBody",
    "ValidationError",
    "__version__",
    "scorecard_service",
]
