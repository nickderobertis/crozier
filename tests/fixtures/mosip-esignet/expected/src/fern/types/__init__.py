



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .auth_challenge import AuthChallenge
    from .auth_challenge_auth_factor_type import AuthChallengeAuthFactorType
    from .auth_challenge_format import AuthChallengeFormat
    from .auth_factor import AuthFactor
    from .auth_factor_type import AuthFactorType
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_error import BadRequestErrorBodyError
    from .claim import Claim
    from .claim_detail import ClaimDetail
    from .claim_id_token import ClaimIdToken
    from .claim_status import ClaimStatus
    from .claim_userinfo import ClaimUserinfo
    from .electronic_record import ElectronicRecord
    from .electronic_record_created_at import ElectronicRecordCreatedAt
    from .electronic_record_date_of_expiry import ElectronicRecordDateOfExpiry
    from .evidence_check_detail import EvidenceCheckDetail
    from .evidence_check_detail_time import EvidenceCheckDetailTime
    from .evidence_issuer import EvidenceIssuer
    from .filter_criteria import FilterCriteria
    from .method_not_allowed_error_body import MethodNotAllowedErrorBody
    from .method_not_allowed_error_body_error import MethodNotAllowedErrorBodyError
    from .purpose import Purpose
    from .purpose_type import PurposeType
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .verified_claim_detail import VerifiedClaimDetail
    from .verified_claim_detail_claims import VerifiedClaimDetailClaims
    from .verified_claim_detail_verification import VerifiedClaimDetailVerification
    from .verified_claim_detail_verification_evidence_item import VerifiedClaimDetailVerificationEvidenceItem
    from .verified_claim_detail_verification_evidence_item_created_at import (
        VerifiedClaimDetailVerificationEvidenceItemCreatedAt,
    )
    from .verified_claim_detail_verification_evidence_item_document_details import (
        VerifiedClaimDetailVerificationEvidenceItemDocumentDetails,
    )
    from .verified_claim_detail_verification_evidence_item_document_details_date_of_expiry import (
        VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfExpiry,
    )
    from .verified_claim_detail_verification_evidence_item_document_details_date_of_issuance import (
        VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfIssuance,
    )
    from .verified_claim_detail_verification_evidence_item_time import VerifiedClaimDetailVerificationEvidenceItemTime
    from .verified_claim_detail_verification_evidence_item_type import VerifiedClaimDetailVerificationEvidenceItemType
    from .verified_claim_detail_verification_evidence_item_type_value import (
        VerifiedClaimDetailVerificationEvidenceItemTypeValue,
    )
    from .verified_claim_detail_verification_evidence_item_verification_method import (
        VerifiedClaimDetailVerificationEvidenceItemVerificationMethod,
    )
    from .verified_claim_detail_verification_time import VerifiedClaimDetailVerificationTime
_dynamic_imports: typing.Dict[str, str] = {
    "AuthChallenge": ".auth_challenge",
    "AuthChallengeAuthFactorType": ".auth_challenge_auth_factor_type",
    "AuthChallengeFormat": ".auth_challenge_format",
    "AuthFactor": ".auth_factor",
    "AuthFactorType": ".auth_factor_type",
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyError": ".bad_request_error_body_error",
    "Claim": ".claim",
    "ClaimDetail": ".claim_detail",
    "ClaimIdToken": ".claim_id_token",
    "ClaimStatus": ".claim_status",
    "ClaimUserinfo": ".claim_userinfo",
    "ElectronicRecord": ".electronic_record",
    "ElectronicRecordCreatedAt": ".electronic_record_created_at",
    "ElectronicRecordDateOfExpiry": ".electronic_record_date_of_expiry",
    "EvidenceCheckDetail": ".evidence_check_detail",
    "EvidenceCheckDetailTime": ".evidence_check_detail_time",
    "EvidenceIssuer": ".evidence_issuer",
    "FilterCriteria": ".filter_criteria",
    "MethodNotAllowedErrorBody": ".method_not_allowed_error_body",
    "MethodNotAllowedErrorBodyError": ".method_not_allowed_error_body_error",
    "Purpose": ".purpose",
    "PurposeType": ".purpose_type",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "VerifiedClaimDetail": ".verified_claim_detail",
    "VerifiedClaimDetailClaims": ".verified_claim_detail_claims",
    "VerifiedClaimDetailVerification": ".verified_claim_detail_verification",
    "VerifiedClaimDetailVerificationEvidenceItem": ".verified_claim_detail_verification_evidence_item",
    "VerifiedClaimDetailVerificationEvidenceItemCreatedAt": ".verified_claim_detail_verification_evidence_item_created_at",
    "VerifiedClaimDetailVerificationEvidenceItemDocumentDetails": ".verified_claim_detail_verification_evidence_item_document_details",
    "VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfExpiry": ".verified_claim_detail_verification_evidence_item_document_details_date_of_expiry",
    "VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfIssuance": ".verified_claim_detail_verification_evidence_item_document_details_date_of_issuance",
    "VerifiedClaimDetailVerificationEvidenceItemTime": ".verified_claim_detail_verification_evidence_item_time",
    "VerifiedClaimDetailVerificationEvidenceItemType": ".verified_claim_detail_verification_evidence_item_type",
    "VerifiedClaimDetailVerificationEvidenceItemTypeValue": ".verified_claim_detail_verification_evidence_item_type_value",
    "VerifiedClaimDetailVerificationEvidenceItemVerificationMethod": ".verified_claim_detail_verification_evidence_item_verification_method",
    "VerifiedClaimDetailVerificationTime": ".verified_claim_detail_verification_time",
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
    "AuthChallenge",
    "AuthChallengeAuthFactorType",
    "AuthChallengeFormat",
    "AuthFactor",
    "AuthFactorType",
    "BadRequestErrorBody",
    "BadRequestErrorBodyError",
    "Claim",
    "ClaimDetail",
    "ClaimIdToken",
    "ClaimStatus",
    "ClaimUserinfo",
    "ElectronicRecord",
    "ElectronicRecordCreatedAt",
    "ElectronicRecordDateOfExpiry",
    "EvidenceCheckDetail",
    "EvidenceCheckDetailTime",
    "EvidenceIssuer",
    "FilterCriteria",
    "MethodNotAllowedErrorBody",
    "MethodNotAllowedErrorBodyError",
    "Purpose",
    "PurposeType",
    "UnauthorizedErrorBody",
    "VerifiedClaimDetail",
    "VerifiedClaimDetailClaims",
    "VerifiedClaimDetailVerification",
    "VerifiedClaimDetailVerificationEvidenceItem",
    "VerifiedClaimDetailVerificationEvidenceItemCreatedAt",
    "VerifiedClaimDetailVerificationEvidenceItemDocumentDetails",
    "VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfExpiry",
    "VerifiedClaimDetailVerificationEvidenceItemDocumentDetailsDateOfIssuance",
    "VerifiedClaimDetailVerificationEvidenceItemTime",
    "VerifiedClaimDetailVerificationEvidenceItemType",
    "VerifiedClaimDetailVerificationEvidenceItemTypeValue",
    "VerifiedClaimDetailVerificationEvidenceItemVerificationMethod",
    "VerifiedClaimDetailVerificationTime",
]
