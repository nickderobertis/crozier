



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .billing_verification_error import BillingVerificationError
    from .billing_verification_error_code import BillingVerificationErrorCode
    from .error import Error
    from .excluded_bloc_member import ExcludedBlocMember
    from .field_violation import FieldViolation
    from .five_factor_bloc_scorecard import FiveFactorBlocScorecard
    from .five_factor_bloc_scorecard_methodology_version import FiveFactorBlocScorecardMethodologyVersion
    from .five_factor_country_scorecard import FiveFactorCountryScorecard
    from .five_factor_country_scorecard_methodology_version import FiveFactorCountryScorecardMethodologyVersion
    from .five_factor_country_scorecard_summary import FiveFactorCountryScorecardSummary
    from .five_factor_pillar import FiveFactorPillar
    from .five_factor_pillar_summary import FiveFactorPillarSummary
    from .forbidden_error_body import ForbiddenErrorBody
    from .forbidden_error_body_code import ForbiddenErrorBodyCode
    from .gateway_error import GatewayError
    from .gateway_error_error import GatewayErrorError
    from .get_bloc_scorecard_request import GetBlocScorecardRequest
    from .get_bloc_scorecard_response import GetBlocScorecardResponse
    from .get_bloc_scorecard_response_one import GetBlocScorecardResponseOne
    from .get_bloc_scorecard_response_one_unavailable_reason import GetBlocScorecardResponseOneUnavailableReason
    from .get_bloc_scorecard_response_zero import GetBlocScorecardResponseZero
    from .get_bloc_scorecard_response_zero_unavailable_reason import GetBlocScorecardResponseZeroUnavailableReason
    from .get_five_factor_scorecard_request import GetFiveFactorScorecardRequest
    from .get_five_factor_scorecard_response import GetFiveFactorScorecardResponse
    from .get_five_factor_scorecard_response_one import GetFiveFactorScorecardResponseOne
    from .get_five_factor_scorecard_response_one_unavailable_reason import (
        GetFiveFactorScorecardResponseOneUnavailableReason,
    )
    from .get_five_factor_scorecard_response_zero import GetFiveFactorScorecardResponseZero
    from .get_five_factor_scorecard_response_zero_unavailable_reason import (
        GetFiveFactorScorecardResponseZeroUnavailableReason,
    )
    from .invalid_request_body_error import InvalidRequestBodyError
    from .jmespath_projection_error import JmespathProjectionError
    from .list_five_factor_scorecards_request import ListFiveFactorScorecardsRequest
    from .list_five_factor_scorecards_response import ListFiveFactorScorecardsResponse
    from .list_five_factor_scorecards_response_computed_at import ListFiveFactorScorecardsResponseComputedAt
    from .list_five_factor_scorecards_response_computed_at_computed_at import (
        ListFiveFactorScorecardsResponseComputedAtComputedAt,
    )
    from .list_five_factor_scorecards_response_computed_at_methodology_version import (
        ListFiveFactorScorecardsResponseComputedAtMethodologyVersion,
    )
    from .list_five_factor_scorecards_response_computed_at_unavailable_reason import (
        ListFiveFactorScorecardsResponseComputedAtUnavailableReason,
    )
    from .list_five_factor_scorecards_response_zero import ListFiveFactorScorecardsResponseZero
    from .list_five_factor_scorecards_response_zero_methodology_version import (
        ListFiveFactorScorecardsResponseZeroMethodologyVersion,
    )
    from .list_five_factor_scorecards_response_zero_unavailable_reason import (
        ListFiveFactorScorecardsResponseZeroUnavailableReason,
    )
    from .rate_limit_error import RateLimitError
    from .scorecard_evidence import ScorecardEvidence
    from .scorecard_member_weight import ScorecardMemberWeight
    from .scorecard_observation import ScorecardObservation
    from .service_unavailable_error_body import ServiceUnavailableErrorBody
    from .too_many_requests_error_body import TooManyRequestsErrorBody
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .validation_error import ValidationError
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "BillingVerificationError": ".billing_verification_error",
    "BillingVerificationErrorCode": ".billing_verification_error_code",
    "Error": ".error",
    "ExcludedBlocMember": ".excluded_bloc_member",
    "FieldViolation": ".field_violation",
    "FiveFactorBlocScorecard": ".five_factor_bloc_scorecard",
    "FiveFactorBlocScorecardMethodologyVersion": ".five_factor_bloc_scorecard_methodology_version",
    "FiveFactorCountryScorecard": ".five_factor_country_scorecard",
    "FiveFactorCountryScorecardMethodologyVersion": ".five_factor_country_scorecard_methodology_version",
    "FiveFactorCountryScorecardSummary": ".five_factor_country_scorecard_summary",
    "FiveFactorPillar": ".five_factor_pillar",
    "FiveFactorPillarSummary": ".five_factor_pillar_summary",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "ForbiddenErrorBodyCode": ".forbidden_error_body_code",
    "GatewayError": ".gateway_error",
    "GatewayErrorError": ".gateway_error_error",
    "GetBlocScorecardRequest": ".get_bloc_scorecard_request",
    "GetBlocScorecardResponse": ".get_bloc_scorecard_response",
    "GetBlocScorecardResponseOne": ".get_bloc_scorecard_response_one",
    "GetBlocScorecardResponseOneUnavailableReason": ".get_bloc_scorecard_response_one_unavailable_reason",
    "GetBlocScorecardResponseZero": ".get_bloc_scorecard_response_zero",
    "GetBlocScorecardResponseZeroUnavailableReason": ".get_bloc_scorecard_response_zero_unavailable_reason",
    "GetFiveFactorScorecardRequest": ".get_five_factor_scorecard_request",
    "GetFiveFactorScorecardResponse": ".get_five_factor_scorecard_response",
    "GetFiveFactorScorecardResponseOne": ".get_five_factor_scorecard_response_one",
    "GetFiveFactorScorecardResponseOneUnavailableReason": ".get_five_factor_scorecard_response_one_unavailable_reason",
    "GetFiveFactorScorecardResponseZero": ".get_five_factor_scorecard_response_zero",
    "GetFiveFactorScorecardResponseZeroUnavailableReason": ".get_five_factor_scorecard_response_zero_unavailable_reason",
    "InvalidRequestBodyError": ".invalid_request_body_error",
    "JmespathProjectionError": ".jmespath_projection_error",
    "ListFiveFactorScorecardsRequest": ".list_five_factor_scorecards_request",
    "ListFiveFactorScorecardsResponse": ".list_five_factor_scorecards_response",
    "ListFiveFactorScorecardsResponseComputedAt": ".list_five_factor_scorecards_response_computed_at",
    "ListFiveFactorScorecardsResponseComputedAtComputedAt": ".list_five_factor_scorecards_response_computed_at_computed_at",
    "ListFiveFactorScorecardsResponseComputedAtMethodologyVersion": ".list_five_factor_scorecards_response_computed_at_methodology_version",
    "ListFiveFactorScorecardsResponseComputedAtUnavailableReason": ".list_five_factor_scorecards_response_computed_at_unavailable_reason",
    "ListFiveFactorScorecardsResponseZero": ".list_five_factor_scorecards_response_zero",
    "ListFiveFactorScorecardsResponseZeroMethodologyVersion": ".list_five_factor_scorecards_response_zero_methodology_version",
    "ListFiveFactorScorecardsResponseZeroUnavailableReason": ".list_five_factor_scorecards_response_zero_unavailable_reason",
    "RateLimitError": ".rate_limit_error",
    "ScorecardEvidence": ".scorecard_evidence",
    "ScorecardMemberWeight": ".scorecard_member_weight",
    "ScorecardObservation": ".scorecard_observation",
    "ServiceUnavailableErrorBody": ".service_unavailable_error_body",
    "TooManyRequestsErrorBody": ".too_many_requests_error_body",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "ValidationError": ".validation_error",
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
    "BadRequestErrorBody",
    "BillingVerificationError",
    "BillingVerificationErrorCode",
    "Error",
    "ExcludedBlocMember",
    "FieldViolation",
    "FiveFactorBlocScorecard",
    "FiveFactorBlocScorecardMethodologyVersion",
    "FiveFactorCountryScorecard",
    "FiveFactorCountryScorecardMethodologyVersion",
    "FiveFactorCountryScorecardSummary",
    "FiveFactorPillar",
    "FiveFactorPillarSummary",
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
    "ServiceUnavailableErrorBody",
    "TooManyRequestsErrorBody",
    "UnauthorizedErrorBody",
    "ValidationError",
]
