



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .algorithm_advisory import AlgorithmAdvisory
    from .algorithm_advisory_action import AlgorithmAdvisoryAction
    from .algorithm_advisory_type import AlgorithmAdvisoryType
    from .anchor_receipt import AnchorReceipt
    from .bundle_manifest import BundleManifest
    from .citizenship_bundle_v1 import CitizenshipBundleV1
    from .citizenship_bundle_v2 import CitizenshipBundleV2
    from .citizenship_bundle_v2dcp_bundle_version import CitizenshipBundleV2DcpBundleVersion
    from .composite_signature import CompositeSignature
    from .composite_signature_binding import CompositeSignatureBinding
    from .composite_signature_classical import CompositeSignatureClassical
    from .composite_signature_pq import CompositeSignaturePq
    from .dcp_capabilities import DcpCapabilities
    from .dcp_capabilities_supported_algs import DcpCapabilitiesSupportedAlgs
    from .error_response import ErrorResponse
    from .governance_key_set import GovernanceKeySet
    from .inclusion_proof import InclusionProof
    from .inclusion_proof_proof_item import InclusionProofProofItem
    from .inclusion_proof_proof_item_direction import InclusionProofProofItemDirection
    from .key_entry_v2 import KeyEntryV2
    from .key_entry_v2alg import KeyEntryV2Alg
    from .key_entry_v2status import KeyEntryV2Status
    from .not_found_error_body import NotFoundErrorBody
    from .policy_decision_v2 import PolicyDecisionV2
    from .policy_decision_v2decision import PolicyDecisionV2Decision
    from .policy_decision_v2resolved_tier import PolicyDecisionV2ResolvedTier
    from .revocation_record import RevocationRecord
    from .signed_bundle_v1 import SignedBundleV1
    from .signed_bundle_v1signature import SignedBundleV1Signature
    from .signed_bundle_v1signature_alg import SignedBundleV1SignatureAlg
    from .signed_bundle_v1signature_signer import SignedBundleV1SignatureSigner
    from .signed_bundle_v1signature_signer_type import SignedBundleV1SignatureSignerType
    from .signed_bundle_v2 import SignedBundleV2
    from .signed_bundle_v2signature import SignedBundleV2Signature
    from .signed_bundle_v2signature_hash_alg import SignedBundleV2SignatureHashAlg
    from .signed_bundle_v2signature_signer import SignedBundleV2SignatureSigner
    from .signed_payload import SignedPayload
    from .signed_tree_head import SignedTreeHead
    from .split_view_alert import SplitViewAlert
    from .split_view_alert_type import SplitViewAlertType
    from .verification_result import VerificationResult
    from .verifier_policy import VerifierPolicy
    from .verifier_policy_default_mode import VerifierPolicyDefaultMode
_dynamic_imports: typing.Dict[str, str] = {
    "AlgorithmAdvisory": ".algorithm_advisory",
    "AlgorithmAdvisoryAction": ".algorithm_advisory_action",
    "AlgorithmAdvisoryType": ".algorithm_advisory_type",
    "AnchorReceipt": ".anchor_receipt",
    "BundleManifest": ".bundle_manifest",
    "CitizenshipBundleV1": ".citizenship_bundle_v1",
    "CitizenshipBundleV2": ".citizenship_bundle_v2",
    "CitizenshipBundleV2DcpBundleVersion": ".citizenship_bundle_v2dcp_bundle_version",
    "CompositeSignature": ".composite_signature",
    "CompositeSignatureBinding": ".composite_signature_binding",
    "CompositeSignatureClassical": ".composite_signature_classical",
    "CompositeSignaturePq": ".composite_signature_pq",
    "DcpCapabilities": ".dcp_capabilities",
    "DcpCapabilitiesSupportedAlgs": ".dcp_capabilities_supported_algs",
    "ErrorResponse": ".error_response",
    "GovernanceKeySet": ".governance_key_set",
    "InclusionProof": ".inclusion_proof",
    "InclusionProofProofItem": ".inclusion_proof_proof_item",
    "InclusionProofProofItemDirection": ".inclusion_proof_proof_item_direction",
    "KeyEntryV2": ".key_entry_v2",
    "KeyEntryV2Alg": ".key_entry_v2alg",
    "KeyEntryV2Status": ".key_entry_v2status",
    "NotFoundErrorBody": ".not_found_error_body",
    "PolicyDecisionV2": ".policy_decision_v2",
    "PolicyDecisionV2Decision": ".policy_decision_v2decision",
    "PolicyDecisionV2ResolvedTier": ".policy_decision_v2resolved_tier",
    "RevocationRecord": ".revocation_record",
    "SignedBundleV1": ".signed_bundle_v1",
    "SignedBundleV1Signature": ".signed_bundle_v1signature",
    "SignedBundleV1SignatureAlg": ".signed_bundle_v1signature_alg",
    "SignedBundleV1SignatureSigner": ".signed_bundle_v1signature_signer",
    "SignedBundleV1SignatureSignerType": ".signed_bundle_v1signature_signer_type",
    "SignedBundleV2": ".signed_bundle_v2",
    "SignedBundleV2Signature": ".signed_bundle_v2signature",
    "SignedBundleV2SignatureHashAlg": ".signed_bundle_v2signature_hash_alg",
    "SignedBundleV2SignatureSigner": ".signed_bundle_v2signature_signer",
    "SignedPayload": ".signed_payload",
    "SignedTreeHead": ".signed_tree_head",
    "SplitViewAlert": ".split_view_alert",
    "SplitViewAlertType": ".split_view_alert_type",
    "VerificationResult": ".verification_result",
    "VerifierPolicy": ".verifier_policy",
    "VerifierPolicyDefaultMode": ".verifier_policy_default_mode",
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
    "AlgorithmAdvisory",
    "AlgorithmAdvisoryAction",
    "AlgorithmAdvisoryType",
    "AnchorReceipt",
    "BundleManifest",
    "CitizenshipBundleV1",
    "CitizenshipBundleV2",
    "CitizenshipBundleV2DcpBundleVersion",
    "CompositeSignature",
    "CompositeSignatureBinding",
    "CompositeSignatureClassical",
    "CompositeSignaturePq",
    "DcpCapabilities",
    "DcpCapabilitiesSupportedAlgs",
    "ErrorResponse",
    "GovernanceKeySet",
    "InclusionProof",
    "InclusionProofProofItem",
    "InclusionProofProofItemDirection",
    "KeyEntryV2",
    "KeyEntryV2Alg",
    "KeyEntryV2Status",
    "NotFoundErrorBody",
    "PolicyDecisionV2",
    "PolicyDecisionV2Decision",
    "PolicyDecisionV2ResolvedTier",
    "RevocationRecord",
    "SignedBundleV1",
    "SignedBundleV1Signature",
    "SignedBundleV1SignatureAlg",
    "SignedBundleV1SignatureSigner",
    "SignedBundleV1SignatureSignerType",
    "SignedBundleV2",
    "SignedBundleV2Signature",
    "SignedBundleV2SignatureHashAlg",
    "SignedBundleV2SignatureSigner",
    "SignedPayload",
    "SignedTreeHead",
    "SplitViewAlert",
    "SplitViewAlertType",
    "VerificationResult",
    "VerifierPolicy",
    "VerifierPolicyDefaultMode",
]
